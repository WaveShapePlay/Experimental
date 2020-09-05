
int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial
  pinMode(LED_BUILTIN, OUTPUT);
}

// for getDelayTime - PySerial will nee to send both 'b' followed by the time.
int getDelayTime(){
  Serial.print("In the delay time fuction");
  String blinkTimeString;
  int blinkTimeInt = 0;
  
  delay(3000); // Need to wait for pyserial send time 
  
  blinkTimeString = Serial.readString();
  Serial.println(blinkTimeString);
  blinkTimeInt = blinkTimeString.toInt();
  return blinkTimeInt;

} // Get Delay Time Loop


void loop(){
  
if(Serial.available()> 0){ 
    
    userInput = Serial.read();               // read user input
      
      if(userInput == 'o'){                
        digitalWrite(LED_BUILTIN, HIGH); 
      }
      if(userInput == 'x'){
       digitalWrite(LED_BUILTIN, LOW);         
      }
      if(userInput == 'b'){
        
        int delayTime = getDelayTime();
        String delayTimePrint = String(delayTime);
        Serial.println("The time recived was: ");
        Serial.println(delayTimePrint);
        for(int i =0;i<10;i++){
          digitalWrite(LED_BUILTIN,LOW);
          delay(delayTime);
          digitalWrite(LED_BUILTIN,HIGH);
          delay(delayTime);
          
        } // User delay blink for loop
        digitalWrite(LED_BUILTIN,LOW);
      } // if userinput == 'b'
  } // Serial.available
} // Void Loop

  

