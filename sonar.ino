
#include <Servo.h>
#include <Ultrasonic.h>

Servo myservo;
Ultrasonic ultrasonic(5);

// Initialize variables
int pos = 0;  
long dist;

void setup() {
  Serial.begin(9600);
  myservo.attach(6);

  // setup
  myservo.write(0);
  delay(3000);
}

void loop() {

  // Scan from 0 to 180 degrees
  for (pos = 0; pos <= 180; pos += 1) { 

    myservo.write(pos);              
    delay(30);                      

    dist = ultrasonic.read();

    Serial.print(pos);
    Serial.print(","); 
    Serial.println(dist);
  }

    // Scan back from 180 to 0 degrees
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);              
    delay(30);           

    dist = ultrasonic.read();

    Serial.print(pos);
    Serial.print(","); 
    Serial.println(dist);            
  }
}
