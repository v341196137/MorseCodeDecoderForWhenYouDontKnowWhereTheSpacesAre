/*
 * UltrasonicCandyDispenser
 * 
 * Detects when an object is within a certain distance of the ultrasonic 
 * sensor and spins the stepper motor a certain amount to drop a candy.
 * 
 * The circuit:
 * - Ultrasonic sensor with trigger to D6 and echo to D5
 * - Stepper motor driver with IN1-IN4 connected to D11-D8
 * 
 * created 15 Oct 2021
 * by Vivian Dai
 * modified 15 Oct 2021
 * by Vivian Dai
 */

#include <Stepper.h>

#define gnd 4
#define echo 5
#define trig 6
#define vcc 7
#define in4 8
#define in3 9
#define in2 10
#define in1 11

const float SPEED_OF_SOUND = 0.034; // sound travels at 343m/s at 20°C which is roughly 0.034 in centimeters
const int STEPS_PER_REVOLUTION = 2038; // number of steps it will take to form one full circle
const int STEPS[] = {340, 340, 399};

Stepper stepperMotor(STEPS_PER_REVOLUTION, in1, in2, in3, in4);

float distance; // variable storing the distance between the ultrasonic sensor and nearest object
int pulseLength; // length of the pulse measured by the ultrasonic sensor
int pointer = 0;
bool dispensed = false; // checks if a candy has already been dispensed 

void setup() {
  // put your setup code here, to run once:
  stepperMotor.setSpeed(5);
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(gnd, OUTPUT);
  pinMode(vcc, OUTPUT);
  digitalWrite(gnd, LOW);
  digitalWrite(vcc, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  distance = getDistance();

  if (distance > 20) {
    dispensed = false;
  } else {
    if (!dispensed) {
      dispenseCandy();
    }
    dispensed = true;
  }

  delay(100);
}

float getDistance() {
  // get the distance between the object and the ultrasonic sensor
  digitalWrite(trig, LOW);
  delayMicroseconds(20);
  digitalWrite(trig, HIGH);
  delayMicroseconds(100);
  digitalWrite(trig, LOW);

  pulseLength = pulseIn(echo, HIGH);

  return pulseLength*SPEED_OF_SOUND/2;
}

void dispenseCandy() {
  // moves the stepper motor by a precalculated amount to get a candy out
  stepperMotor.step(STEPS[pointer]);
  pointer++;
  pointer %= sizeof(STEPS);
}
