
int analogPin = 3;     
int data = 0;           
char userInput;

void setup(){

  Serial.begin(9600);                        //  setup serial
  pinMode(LED_BUILTIN, OUTPUT);
}

int getDelayTime(){
  String blinkTimeString;
  int blinkTimeInt = 0;
  String toClearbuffer;
  Serial.print("In the delay time fuction");
  
  while(1){
    //toClearbuffer = Serial.readString();
    delay(1);
    if(Serial.available()> 0){
      blinkTimeString = Serial.readString();
      Serial.println(blinkTimeString);
      blinkTimeInt = blinkTimeString.toInt();
      return blinkTimeInt;
      //flag = 1; // Do I need this flag, if I return the value of the function
      // https://stackoverflow.com/questions/6620949/difference-between-return-and-break-statements#:~:text=break%20is%20used%20when%20you,or%20to%20stop%20further%20execution.
    } // Serial available
  } // While loop
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
      }
       
  } // Serial.available
} // Void Loop

  

