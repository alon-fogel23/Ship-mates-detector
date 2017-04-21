from django.shortcuts import render, get_object_or_404
from .models import Department, Soldier, SingleRecord


def index(request):
    all_departments = Department.objects.all()
    all_records = SingleRecord.objects.all()
    all_soldiers = Soldier.objects.all()

    compartment_to_name = {532: 'cic', 522: 'engine'}  # TODO: should be saved in the db

    counters = {}
    present_soldiers = {}
    for soldier in all_soldiers:
        last_read = soldier.records.last()
        compartment = compartment_to_name[last_read.compartment]
        present_soldier = last_read.soldier_name
        if compartment not in counters:
            counters[compartment] = 1
            present_soldiers[compartment] = ' ' + present_soldier
        else:
            counters[compartment] += 1
            present_soldiers[compartment] += ' ' + present_soldier

    return render(request, 'ship/index.html',
                  {'all_departments': all_departments, 'all_records': all_records,
                   'counters': counters, 'present_soldiers': present_soldiers
                   })


def departments(request):
    all_departments = Department.objects.all()
    return render(request, 'ship/departments.html', {'all_departments': all_departments})


def details(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'ship/detail.html', {'department': department, })


def records(request):
    all_records = SingleRecord.objects.all()
    return render(request, 'ship/records.html', {'all_records': all_records})




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

