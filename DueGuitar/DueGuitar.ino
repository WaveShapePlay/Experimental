
int in_ADC0, in_ADC1;  



void setup()
{
  //ADC Configuration
  ADC->ADC_MR |= 0x80;   // ADC in free running mode.
  ADC->ADC_CR=2;         // Starts ADC conversion.
  ADC->ADC_CHER=0x80;  // Enable ADC channel 0

  //DAC Configuration
  analogWrite(DAC0,0);  // Enables DAC0

}

void loop()
{
  //Read the ADCs
  while((ADC->ADC_ISR & 0x80) != 0x80);   // Single statment - wait for ADC conversion of ADC0
  in_ADC0=ADC->ADC_CDR[7];               // read data from ADC0

  
  //Write the DACs
  dacc_set_channel_selection(DACC_INTERFACE, 0);       //select DAC channel 0
  dacc_write_conversion_data(DACC_INTERFACE, in_ADC0);//write on DAC

}
