#include "Waveforms.h"

int wave0 = 0;
int i = 0;
int sample;
unsigned long uSec = 500;

String inString = "";    // string to hold input
int temp;

// ser.write("%01#RDD0010000107**\r".encode()) See if this works on python
void setup() {
  
  analogWriteResolution(12);  // set the analog output resolution to 12 bit (4096 levels)
  analogReadResolution(12);   // set the analog input resolution to 12 bit 
  Serial.begin(9600);
  
}

void loop() {
  
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      temp = inString.toInt();
      Serial.println(temp);      
      Serial.print("String: ");
      Serial.println(inString);
      // clear the string for new input:
      inString = "";
    }
  }


  analogWrite(DAC0, waveformsTable[wave0][i]);  // write the selected waveform on DAC0
  i++;
  
  if(i == maxSamplesNum){  // Reset the counter to repeat the wave
    i = 0;
  }
  delayMicroseconds(uSec);
}
