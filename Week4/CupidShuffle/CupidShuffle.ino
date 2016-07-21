#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void setup() {
  // put your setup code here, to run once:
  servoRight.attach(11);
  servoLeft.attach(12);
}

void forward(){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
}

void backward(){
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
}

void left(){  
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1300);
}

void right(){ 
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1700);
}

void stopmove(){
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=0; i< 3; i++){
    right();
    delay(1000);
    stopmove();
    delay(50);
  }
  for (int i=0; i< 3; i++){
    left();
    delay(1000);
    stopmove();
    delay(50);
  }
  for (int i=0; i< 4; i++){
    forward();
    delay(1000);
  }
  for (int i=0; i< 4; i++){
    backward();
    delay(1000); 
  }

}

