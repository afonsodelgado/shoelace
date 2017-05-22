temperature_samples = 100
temperature_delay = 0.02
GAIN = 1
lm35_adc_sum = 0.0

def TemperatureSensor():
    for i in range(0, temperature_samples):
        adc = Adafruit_ADS1x15.ADS1115()
        lm35_adc = adc.read_adc(0, gain=GAIN)
        lm35_adc_sum += lm35_adc
        time.sleep(temperature_delay)
    lm35_adc_avg = lm35_adc_sum/temperature_samples
    lm35_adc_sum = 0.0

    temp_celsius = (float(lm35_adc_avg)*5.0/(65535))/0.01
    #print("TEMPERATURA => ", "%.2f" %temp_celsius)
    return temp_celsius
