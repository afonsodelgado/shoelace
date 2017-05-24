fall_samples_number = 10
fall_samples_delay = 1
fall_channel = 2
GAIN = 1

def FallSensor():
    fall_sum = 0.0
    for i in range(fall_samples_number):
        fall_adc_read = Adafruit_ADS1x15.ADS1115()
        fall_value = fall_adc_read.read_adc(fall_channel, gain = GAIN)
        fall_sum += fall_value
        time.sleep(fall_samples_delay)

    fall_avg = fall_sum/fall_samples_number
    if fall_avg <= 50:
        return 1 #Alert patient fall!
    else:
        return 0 #Normal status
