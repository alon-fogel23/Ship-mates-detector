
char foo;



#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // CONNECT BT RX PIN TO ARDUINO 11 PIN | CONNECT BT TX PIN TO ARDUINO 10 PIN


void setup() 
{
  //pinMode(12, OUTPUT);  // this pin will pull the HC-05 pin 34 (key pin) HIGH to switch module to AT mode
  //digitalWrite(12, HIGH); 
  Serial.begin(9600);
  Serial.println("Enter AT commands:");
  BTSerial.begin(38400);  // HC-05 default speed in AT command more

 

  
}

void loop()
{

  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if 
    (BTSerial.available())
    Serial.write(BTSerial.read());
  


/*
     test=strstr(id,"DC:0B:34:71:A1:B5"); // c'est l'adresse BT de mon telephone Nokia
      if(test)
      {
      Serial.println("Device connected LGG4!");
      delay(1500);
      }    

    }     
    */  

  // Keep reading from Arduino Serial Monitor and send to HC-05
  if (Serial.available())
    BTSerial.write(Serial.read());
}


