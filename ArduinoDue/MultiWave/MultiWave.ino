

#include "Waveforms.h"

int wave0 = 0;
int i = 0;
int sample;
char userInput;
unsigned long uSec = 500;


void setup() {
  analogWriteResolution(12);  // set the analog output resolution to 12 bit (4096 levels)
  analogReadResolution(12);   // set the analog input resolution to 12 bit 
  Serial.begin(9600);
}

void loop() {

  if(Serial.available()>0){

        userInput = Serial.read();

        if(userInput == 'u'){

          uSec += 5;
          
        }

        if(userInput == 'd'){

          uSec -= 5;
          
         }

        if (userInput == 't'){
          wave0 = 1;
        }

        if(userInput == 's'){
          wave0 = 0;
        }
    
  } // Serial.available

  
  
  analogWrite(DAC0, waveformsTable[wave0][i]);  // write the selected waveform on DAC0
  i++;
  
  if(i == maxSamplesNum){  // Reset the counter to repeat the wave
    i = 0;
  }

  
  delayMicroseconds(uSec);
}
