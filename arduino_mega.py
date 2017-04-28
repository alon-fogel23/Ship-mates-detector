import serial
from django.db import models
from ship.models import Department, Soldier, SingleRecord, RecordManager
import datetime
import time
#  import numpy


# self_test_compartment = 0
# self_test_signal = 0
# self_test_soldier_tag = 0
# before_last_read = SingleRecord.objects.create_singlerecord(self_test_compartment, self_test_soldier_tag, self_test_signal)

#  arduinoData = serial.Serial('/dev/ttyUSB1', 115200)  #not working
# arduinoData = serial.Serial('com3', 115200)    # working for uno rfid
# arduinoDataMega = serial.Serial('com7', 9600)
arduinoData = serial.Serial('com4', 9600)  # mega hc-05
# compartment = models.IntegerField(532)
# time_tag = "1999-12-31 14:30:59"  ---- working !
# time_tag = models.DateTimeField(auto_now_add=True, blank=True)  ---- not working

# time_tag = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # '2006-10-25 14:30:59'
compartmentUno = 'CIC'
compartmentMega = 'ENGINE ROOM'

while True:
    while arduinoData.inWaiting() == 0:
        pass  # do nothing
    try:
        arduinoData.readline().decode('ascii')
    except UnicodeDecodeError:
        print("it was not a ascii-encoded unicode string")
        continue
    else:
        soldier_tag = arduinoData.readline().decode('utf-8').strip('\r\n')
        tag_data = soldier_tag.split(",")
        print(tag_data)

        if tag_data[0] and tag_data[2]:  # tag_data[0] is the soldier ID and [2] is signal strength
            record_for_db_Mega = SingleRecord.objects.create_singlerecord(compartmentMega, tag_data[0], int(tag_data[2], 16))





        # print(soldier_tag_Mega)
        # record_for_db = SingleRecord.objects.create_singlerecord(compartment, soldier_tag)  # , time_tag - last one that worked for uno rfid
        # record_for_db_Mega = SingleRecord.objects.create_singlerecord(compartmentMega, soldier_tag_Mega)  # , time_tag
        # record_for_db.save()

