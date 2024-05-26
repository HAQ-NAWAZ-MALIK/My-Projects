#include <Servo.h>

#include <Servo.h>

Servo servoX;  // create servo object for the X axis
Servo servoY;  // create servo object for the Y axis

void setup() {
  Serial.begin(9600);  // initialize serial communication
  servoX.attach(9);    // attaches the servo on pin 9 to the servo object
  servoY.attach(10);   // attaches the servo on pin 10 to the servo object
  servoX.write(90);    // initial position
  servoY.write(90);    // initial position
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int delimiterIndex = data.indexOf(',');
    if (delimiterIndex != -1) {
      String xString = data.substring(0, delimiterIndex);
      String yString = data.substring(delimiterIndex + 1);
      int xPos = xString.toInt();
      int yPos = yString.toInt();
      servoX.write(xPos);
      servoY.write(yPos);
    }
  }
}
