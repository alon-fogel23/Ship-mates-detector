from django.shortcuts import render, get_object_or_404
from ship.models import Compartment, Department, Soldier, SingleRecord, ViewMode
from django.utils.dateparse import parse_datetime
from datetime import timedelta
from django.http import JsonResponse
import datetime
import csv


def index(request):
    all_departments = Department.objects.all()
    all_records = SingleRecord.objects.all()
    all_soldiers = Soldier.objects.all()
    all_compartment = Compartment.objects.all()
    viewmode = ViewMode.objects.all()[0].view_mode
    counters = {}
    missing_counters = {}
    battle_station_counter = 0

    present_soldiers = {}
    missing_soldiers = {}
    unauthorized_soldiers = {}
    lack_of_movement_soldiers = {}

    if viewmode == '1':
        all_soldiers = all_soldiers.exclude(officer=1)
    if viewmode == '2':
        all_soldiers = all_soldiers.exclude(baknaz_team=0)
    for soldier in all_soldiers:

        # soldier.refresh_from_db()

        # filtering the best read for each soldier of the past 10 seconds read-outs
        last_read = soldier.records.latest('time_stamp')
        last_record_time_1 = parse_datetime(last_read.time_stamp)
        best_match_record = soldier.records.filter(time_stamp__gte=(last_record_time_1 + timedelta(seconds=-10)).strftime('%Y-%m-%d %H:%M:%S')).order_by("-signal_strength")[0]
        soldier.current_compartment = best_match_record.compartment
        soldier.last_time_stamp = best_match_record.time_stamp
        soldier.save()

        #  implementing the man over board feature - can set different times for different soldiers
        present_time = datetime.datetime.now()
        last_seen = parse_datetime(best_match_record.time_stamp)
        elapsedtime_missing_person = present_time - last_seen
        time_difference_missing_person_in_minutes = elapsedtime_missing_person / timedelta(minutes=1)
        if time_difference_missing_person_in_minutes > soldier.last_seen_pre_defined_max_time:
            if soldier not in missing_counters:
                missing_counters[soldier.soldier_name] = 1
                missing_soldiers[soldier.soldier_name] = {soldier.soldier_name}
            else:
                missing_counters[soldier.soldier_name] += 1
                missing_soldiers[soldier.soldier_name].add(soldier.soldier_name)
        # end of man over board

        # lack of movement
        current_compartment = best_match_record.compartment.lower()
        records_from_other_compartment = soldier.records.exclude(compartment=current_compartment.upper())
        if records_from_other_compartment:
            before_current_compartment_record = records_from_other_compartment.latest('time_stamp')
            before_current_compartment_record_time_stamp = parse_datetime(before_current_compartment_record.time_stamp)
            elapsedtime_sleeping_person = last_seen - before_current_compartment_record_time_stamp
            time_difference_sleeping_person_in_minutes = elapsedtime_sleeping_person / timedelta(minutes=1)
            if time_difference_sleeping_person_in_minutes > soldier.lack_of_movement_pre_defined_max_time:
                if soldier.soldier_name not in lack_of_movement_soldiers:
                    lack_of_movement_soldiers[soldier.soldier_name] = {soldier.soldier_name.lower()}
                else:
                    lack_of_movement_soldiers[soldier.soldier_name].add(soldier.soldier_name.lower())
        else:
            earliest_reading = soldier.records.earliest('time_stamp')
            earliest_reading_time_stamp = parse_datetime(earliest_reading.time_stamp)
            if (last_seen - earliest_reading_time_stamp)/timedelta(minutes=1) > soldier.lack_of_movement_pre_defined_max_time:
                if soldier.soldier_name not in lack_of_movement_soldiers:
                    lack_of_movement_soldiers[soldier.soldier_name] = {soldier.soldier_name.lower()}
                else:
                    lack_of_movement_soldiers[soldier.soldier_name].add(soldier.soldier_name.lower())
        # end of lack of movement

        # battle stations
        if best_match_record.compartment == soldier.battle_stations_compartment:
            battle_station_counter += 1
        if battle_station_counter == all_soldiers.count():
            ship_in_battle_stations = 'SHIP IN BATTLE STATIONS !'
        else:
            ship_in_battle_stations = 'SHIP NOT IN BATTLE STATIONS '
        # end of battle stations

        # unauthorized personnel
        current_compartment_for_security_class_check = all_compartment.filter(compartment_name=best_match_record.compartment)[0]
        if soldier.soldier_security_class < current_compartment_for_security_class_check.compartment_security_class:
            if soldier.soldier_name not in unauthorized_soldiers:
                unauthorized_soldiers[soldier.soldier_name] = {soldier.soldier_name}
        # end of unauthorized personnel

        # home page counters presentation
        present_soldier = best_match_record.soldier_name
        if current_compartment not in counters:
            counters[current_compartment] = 1
            present_soldiers[current_compartment] = {present_soldier}
        else:
            counters[current_compartment] += 1
            present_soldiers[current_compartment].add(present_soldier)

    return render(request, 'ship/index.html',
                  {'all_departments': all_departments, 'all_records': all_records,
                   'counters': counters, 'present_soldiers': present_soldiers, 'all_soldiers': all_soldiers,
                   'ship_in_battle_stations': ship_in_battle_stations, 'missing_soldiers': missing_soldiers,
                   'missing_counters': missing_counters, 'unauthorized_soldiers': unauthorized_soldiers,
                   'lack_of_movement_soldiers': lack_of_movement_soldiers, 'viewmode': viewmode
                   })


def search_soldier(request):
    name = request.GET.get('username', None)
    compartment_to_return = Soldier.objects.all().filter(soldier_name=name)[0].current_compartment
    time_stamp_to_return = Soldier.objects.all().filter(soldier_name=name)[0].last_time_stamp
    data = {
            'name': name, 'compartment': compartment_to_return, 'last_time_stamp': time_stamp_to_return
            }
    return JsonResponse(data)


def departments(request):
    all_departments = Department.objects.all()
    return render(request, 'ship/departments.html', {'all_departments': all_departments})


def details(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'ship/detail.html', {'department': department, })


def records(request):
    all_records = SingleRecord.objects.all()
    # ship_records_backup = open(r'C:\Users\Alon Fogel\Desktop\website\ship_records.txt', 'w')
    # writes to the manage.py folder
    with open(r'ship_records.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for record in all_records:
            spamwriter.writerow(record.soldier_name + ' ' + record.time_stamp + ' ' + record.compartment + ' ' + record.signal_strength)


    # ship_records_backup.close()
    # doc_request = get_csv(request)
    return render(request, 'ship/records.html', {'all_records': all_records})


# #  22-4-2017
    # null_compartment = 0
    # null_signal = 0
    #
    # counters = {}
    # present_soldiers = {}
    # for soldier in all_soldiers:
    #     before_last_read = SingleRecord.objects.create_singlerecord(null_compartment, soldier.tag, null_signal)
    #     print("before_last_compartment %d" % before_last_read.compartment)
    #     last_read = soldier.records.last()
    #     if last_read.compartment != 0:
    #         before_last_read = last_read  # saving the earlier reading for comparison with the new one
    #         last_read = soldier.records.last()
    #         compartment = compartment_to_name[last_read.compartment]
    #
    #         if last_read.compartment == before_last_read.compartment:  # different compartments
    #             if last_read.time_stamp == before_last_read.time_stamp:  # same day
    #                     print("2 compromised records")
    #             else:
    #                     print("no problem")
    #
    #
    #     else:
    #         last_read = soldier.records.last()
    #         compartment = compartment_to_name[last_read.compartment]
    #         present_soldier = last_read.soldier_name
    #         if compartment not in counters:
    #             counters[compartment] = 1
    #             present_soldiers[compartment] = ' ' + present_soldier
    #         else:
    #             counters[compartment] += 1
    #             present_soldiers[compartment] += ' ' + present_soldier
    #
    # return render(request, 'ship/index.html',
    #               {'all_departments': all_departments, 'all_records': all_records,
    #                'counters': counters, 'present_soldiers': present_soldiers
    #                })

    # end of 22-4-2017

# from django.views import generic
# from .models import Department, SingleRecord
#
#
# class IndexView(generic.ListView):
#         template_name = 'ship/index.html'
#         context_object_name = 'all_records'
#
#         def get_queryset(self):
#                 return SingleRecord.objects.all()
#
#
# class DepartmentView(generic.ListView):
#         template_name = 'ship/departments.html'
#         context_object_name = 'all_departments'
#
#         def get_queryset(self):
#                 return Department.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Department
#     template_name = 'ship/detail.html'
#
#
# class RecordsView(generic.ListView):
#     template_name = 'ship/records.html'
#     context_object_name='all_records'
#     def get_queryset(self):
#         return SingleRecord.objects.all()



# def baknaz_team(request, department_id):
#     department = get_object_or_404(Department, pk=department_id)
#     try:
#         selected_soldier = department.soldier_set.get(pk=request.POST['soldier'])
#     except(KeyError, Soldier.DoesNotExist):
#         return render(request, 'ship/detail.html',
#                       {'department': department, 'error_message': "You did not select a valid soldier"})
#     else:
#         selected_soldier.is_baknaz_team = True
#         selected_soldier.save()
#         return render(request, 'ship/detail.html', {'department': department, })

