from django.db import models
from datetime import datetime


class Department(models.Model):
    officer = models.CharField(max_length=250)
    department_name = models.CharField(max_length=500)
    # genre = models.CharField(max_length=100)
    department_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.department_name + ' - ' + self.officer


class Soldier(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    tag = models.IntegerField()
    soldier_name = models.CharField(max_length=250)
    is_baknaz_team = models.BooleanField(default=False)

    def __str__(self):
        return self.soldier_name


class SingleRecord(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)
    tag_string = models.CharField(max_length=250, default="0x00 0x00 0x00 0x00")
    compartment = models.IntegerField(default=532)
    # soldier_tag_field_0 = models.IntegerField(default=0)
    # soldier_tag_field_1 = models.IntegerField(default=0)
    # soldier_tag_field_2 = models.IntegerField(default=0)
    # soldier_tag_field_3 = models.IntegerField(default=0)
