#include <Arduino.h>
#include <Mouse.h>

#define xStep 10
#define mapSize 80

bool right = true;
int tab[] = {44, 16, 11, 9, 7, 5, 3, 3, 1, 1, -1, -1, -3, -3, -5, -7, -9, -11, -16, -44, 44, 16, 11, 9, 7, 5, 3, 3, 1, 1, -1, -1, -3, -3, -5, -7, -9, -11, -16, -44, 45, 19, 16, 13, 12, 11, 11, 10, 10, 10, 10, 10, 11, 10, 11, 12, 14, 15, 19, 45, -45, -19, -15, -14, -12, -11, -10, -11, -10, -10, -10, -10, -10, -11, -11, -12, -13, -16, -19, -45};

void setup() {
  delay(5000);
}

void loop() {
  for(int i = 0; i < mapSize; i++) {
    if(i == mapSize / 2)
      right = false;
    
    else if (i == 0)
      right = true;
    
    if(right)
      Mouse.move(xStep, tab[i], 0);
    
    else
      Mouse.move(-xStep, tab[i], 0);

    delay(100);
  }
}
