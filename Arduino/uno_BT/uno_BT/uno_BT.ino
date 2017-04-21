#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX | TX
unsigned long lastTime;
unsigned long interval = 2000;
char texto[105];
char *test;
char *id;
 int h;
void setup()
{
 //pinMode(9, OUTPUT);  // this pin will pull the HC-05 pin 34 (key pin) HIGH to switch module to AT mode
  //digitalWrite(9, HIGH);
  Serial.begin(9600);

  //Serial.println("enter hc-05 to AT mode");
  delay(10000);
  
  BTSerial.begin(38400);  // HC-05 default speed in AT command more

 
  BTSerial.print("\r");
  //Serial.println("press and hold HC-05 button");
  delay(5000);
  BTSerial.print("AT+INIT\r\n");
  delay(100);
  //BTSerial.print("AT+IAC=9e8b33\r\n");
  //delay(100);
  //BTSerial.print("AT+CLASS=0\r\n");
  //delay(100);
  BTSerial.print("AT+ROLE=1\r\n");
  delay(100);
  BTSerial.print("AT+INQM=1,9,48\r\n");
  delay(100);
  BTSerial.print("AT+INQ\r\n");
  delay(1000);

}

void loop()
{
  BTSerial.print("AT+INQ\r\n");
  delay(1000);
  
    h=BTSerial.available(); 
    if(h>=0)
    { 
      id = readSerial(h);
      Serial.write(id);
      Serial.println();
      
      
    }
 /*  test=strstr(id,"ERROR");
   if(test)
   {
 
  BTSerial.print("\r");
  delay(100);
  BTSerial.print("AT+INIT\r\n");
  delay(100);
  //BTSerial.print("AT+IAC=9e8b33\r\n");
  //delay(100);
  //BTSerial.print("AT+CLASS=0\r\n");
  //delay(100);
  BTSerial.print("AT+ROLE=1\r\n");
  delay(100);
  BTSerial.print("AT+INQM=1,9,48\r\n");
  delay(100);
  BTSerial.print("AT+INQ\r\n");
  delay(100);
  }
 */   
    //test=strstr(id,":DC:OB:34:71:A1:B5");  //alon's phone - not working
    test=strstr(id,":FO5B:7B:2D34A0"); // Shiran's phone - kinda working - can read the inq massage, doesnt get the test positive
    if(test)
    {
     //Serial.println("Device connected LGG4!");
     Serial.println("Device connected GALAXY5!");
      delay(1500);
    }    

}

void clearAll() 
{
    for(int i = 0; i < BTSerial.available(); i++)
    {
        BTSerial.read();
    }
}

char* readSerial (int h)
{
    char input;
    int j=0;
    int flag=0;
    
    char buffer [27];
    if (BTSerial.available ()> 0) 
    {

        for (int i = 0; i <h; i ++)
        {
            input = (char) BTSerial.read ();
            if (input == ':')                    // the id's start after the first ":"
              flag = 1;
            if (flag==1)
            {
              if (j<=25)
              {
                buffer [j] = input;
                buffer [j + 1] = '\0';
                j++;
              }
            }
        }
        return buffer;
    } 
 /*   else
      {
        return "No Data";
      }
 */
}


