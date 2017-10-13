int in_ADC0;


void setup()
{
  
  ADC->ADC_MR |= 0x80;        // Mode Register - Select free running mode for ADC.
  ADC->ADC_CR = 0x02;         // Control Register - Begin conversions
  ADC->ADC_CHER = 0x80;       // Channel Enable Register - Selects the correstponding ADC channels 
                              // A0 = CH7, A1 = CH6, A2 = CH5, A3 = CH4
                              // For example A0 on the Arduino Due board uses the internal CH7 of ADC
  
  analogWrite(DAC0,0);        // Enables Digital to Analog Converter 
  
}

void loop()
{
                                          
  while((ADC->ADC_ISR & 0x80) != 0x80);   // Single statment - Wait for ADC CH7 End of Conversion
  in_ADC0=ADC->ADC_CDR[7];                // Read CH7 ADC and store in in_ADC0

  dacc_set_channel_selection(DACC_INTERFACE, 0);        // Select channel D0 for DAC
  dacc_write_conversion_data(DACC_INTERFACE, in_ADC0);  // Write in_ADC0 to DAC
}
