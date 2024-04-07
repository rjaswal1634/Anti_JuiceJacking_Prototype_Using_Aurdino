#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

const int SPK_PIN = 2;

void setup() {
  Serial.begin(9600);
  pinMode(SPK_PIN, OUTPUT);
  
  lcd.begin(16, 2);
  lcd.setRGB(0, 255, 0); // Green backlight
  lcd.setCursor(0, 0);
  lcd.print("Ready to Check");
}

void loop() {
  if (Serial.available() > 0) {
    lcd.setRGB(255, 0, 0);
    lcd.setCursor(0, 0);
    lcd.print("  Unsafe USB   ");
    digitalWrite(SPK_PIN, HIGH); // Activate sound
  } 
  else {
    digitalWrite(SPK_PIN, LOW); // Deactivate sound
    lcd.setRGB(0, 255, 0); // Green backlight
    lcd.setCursor(0, 0);
    lcd.print("Ready to Check");
  }
}
