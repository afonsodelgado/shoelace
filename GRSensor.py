gsr_samples_number = 10 #Wait 10 samples of GSR to filter average
gsr_samples_delay = 0.02 #Time between samples equals to 20ms
gsr_channel = 1
GAIN = 1

def GRSensor():
    gsr_sum = 0.0
    for i in range(0, gsr_samples_number):
        gsr_adc_read = Adafruit_ADS1x15.ADS1115()
        gsr_value = gsr_adc_read.read_adc(gsr_channel, gain=GAIN)/100
        gsr_sum += gsr_value
        time.sleep(gsr_samples_delay) #delay

    gsr_avg = gsr_sum/gsr_samples_number #Filter average from gsr samples
    if gsr_avg <= 20:
        return 0 #Disconnected
    elif gsr_avg >= 20 and gsr_avg<=200:
        return 1 #Normal status
    else:
        return 2 #Alert status
    #print("GSR AVERAGE => ", gsr_avg)
