
int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial
  pinMode(LED_BUILTIN, OUTPUT);
}

int getDelayTime(){
  int flag = 0;
  int blinkTimeInt = 0;
  String blinkTimeString;
  
  
  while(flag == 0){
    
    if(Serial.available()>0){
      Serial.readString()
    } // Serial available

    
  } // While Flag loop
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
        
        digitalWrite(LED_BUILTIN,LOW)
      }
       
  } // Serial.available
} // Void Loop

  

