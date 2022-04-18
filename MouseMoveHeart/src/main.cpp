#include <Arduino.h>

int RXLED = 17; // The RX LED has a defined Arduino pin
int TXLED = 30; // The TX LED has a defined Arduino pin

// the setup function runs once when you press reset or power the board
void setup() {
  
  pinMode(RXLED, OUTPUT); // Set RX LED as an output
  pinMode(TXLED, OUTPUT); // Set TX LED as an output
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(RXLED, HIGH); // set the LED off
  digitalWrite(TXLED, LOW); // set the LED off
  delay(300);                       // wait for a second
  digitalWrite(RXLED, LOW); // set the LED on
  digitalWrite(TXLED, HIGH); // set the LED on
  delay(300);                       // wait for a second
}
