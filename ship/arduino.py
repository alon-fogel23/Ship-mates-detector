import serial
from django.db import models
from ship.models import Department, Soldier, SingleRecord, RecordManager
import datetime
import time
#  import numpy

#  arduinoData = serial.Serial('/dev/ttyUSB1', 115200)  #not working
arduinoData = serial.Serial('com5', 115200)    # working
# arduinoDataMega = serial.Serial('com7', 9600)
# compartment = models.IntegerField(532)
# time_tag = "1999-12-31 14:30:59"  ---- working !
# time_tag = models.DateTimeField(auto_now_add=True, blank=True)  ---- not working

# time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # '2006-10-25 14:30:59'
compartment = 532
# compartmentMega = 522

while True:
    while arduinoData.inWaiting() == 0:
        pass  # do nothing
    soldier_tag = arduinoData.readline().decode('utf-8').strip('\r\n')
    # soldier_tag_Mega = arduinoDataMega.readline().decode('utf-8').strip('\r\n')
    print(soldier_tag)
    # print(soldier_tag_Mega)
    record_for_db = SingleRecord.objects.create_singlerecord(compartment, soldier_tag)  # , time_tag
    # record_for_db_Mega = SingleRecord.objects.create_singlerecord(compartmentMega, soldier_tag_Mega)  # , time_tag
    # record_for_db.save()

