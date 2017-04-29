from django.db import models
import datetime


class Compartment(models.Model):
    compartment_name = models.CharField(max_length=500)
    compartment_security_class = models.IntegerField(default=1)  # 1 = BALMAS , 2 = SODY

    def __str__(self):
        return self.compartment_name


class Department(models.Model):
    officer = models.CharField(max_length=250)
    department_name = models.CharField(max_length=500)
    department_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.department_name + ' - ' + self.officer


class Soldier(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    tag = models.CharField(max_length=250, default="0x00 0x00 0x00 0x00")
    soldier_name = models.CharField(max_length=250)
    last_seen_pre_defined_max_time = models.IntegerField(default=240)
    lack_of_movement_pre_defined_max_time = models.IntegerField(default=360)
    current_compartment = models.CharField(max_length=250, default='CIC')
    last_time_stamp = models.CharField(max_length=250, default='2000-01-01 12:34:56')
    battle_stations_compartment = models.CharField(max_length=250, default='CIC')
    soldier_security_class = models.IntegerField(default=1)  # 1 = BALMAS , 2 = SODY

    def __str__(self):
        return self.soldier_name


class RecordManager(models.Manager):
    def create_singlerecord(self, compartment, tag_string, signal):
        time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            soldier = Soldier.objects.get(tag=tag_string)
            singlerecord = self.create(compartment=compartment, soldier=soldier, soldier_name=soldier.soldier_name, tag_string=tag_string
                                       , time_stamp=time_tag, signal_strength=signal)
            return singlerecord
        except Soldier.DoesNotExist:
            print("soldier not found %s " % tag_string)


class SingleRecord(models.Model):
    soldier = models.ForeignKey(Soldier, on_delete=models.CASCADE, related_name='records', null=True)
    time_stamp = models.CharField(max_length=250)
    soldier_name = models.CharField(max_length=250, default='ah sheli')
    tag_string = models.CharField(max_length=250, default='0x00 0x00 0x00 0x00')
    signal_strength = models.CharField(max_length=250, default='0x00')
    compartment = models.CharField(max_length=250, default='CIC')
    objects = RecordManager()
