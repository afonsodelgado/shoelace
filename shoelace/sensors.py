from shoelace.core import Sensor
import requests
from shoelace.config import env
import math

class TemperatureSensor(Sensor):
    """Temperature Sensor class
    Usage:
        >>> temp_sens = TemperatureSensor()
        >>> temp_sens.push(111)
    """
    @classmethod
    def limiar(cls):
        return 10

    def steinhart_hart(self, temp):
        print("TEMP AKI => ", temp)
        series_resistance = 10000. #Series resistance from the circuit
        ads_resolution = 65536. # ADC 16 bits resolution (2**16)
        coeff_a = 0.001129148 #STEINHART-HART A coefficient
        coeff_b = 0.000234125 #STEINHART-HART B coefficient
        coeff_c = 0.0000000876741 #STEINHART-HART C coefficient
        therm_resistance = abs(((ads_resolution/temp) - series_resistance))
        ln_temp = math.log1p(therm_resistance)
        # print("LN_TEMP => ", ln_temp)
        return (1. / (coeff_a + (coeff_b * ln_temp) + (coeff_c * ln_temp**3 ))) - 273.15

    def push_callback(self, item):
        #item = self.steinhart_hart(item)
        url = env["server_address"]+"/api/skin_temperatures"
        if (self.diff(item, self.last_sended) > TemperatureSensor.limiar()):
            print("SAIDA ANTES =>", item)
            item = int(item)
            #item += 10
            print("ITEM =>", item)
            self.last_sended = item
            data = {
                'temperature': item
            }
            r = requests.post(url, headers={'Authorization': 'Token '+self.token}, data=data)
            print(r.json())
        else:
            print("skip...")

class GRSensor(Sensor):
    """Galvanic Resistance Sensor class
    Usage:
        >>> grs = GRSensor()
        >>> grs.push(150)
    """
    @classmethod
    def limiar(cls):
        return 5

    def push_callback(self, item):
        url = env["server_address"]+"/api/galvanic_resistances"
        if (self.diff(item, self.last_sended) > GRSensor.limiar()):
            print("sending...")
            self.last_sended = item
            data = {
                'resistance': item
            }
            r = requests.post(url, headers={'Authorization': 'Token '+self.token}, data=data)
        else:
            print("skip...")

class HBSensor(Sensor):
    """HeartBeats Sensor class
    Usage:
        >>> hbs = HBSensor()
        >>> hbs.push(150)
    """
    @classmethod
    def limiar(cls):
        return 5

    def push_callback(self, item):
        url = env["server_address"]+"/api/heart_beats"
        if (self.diff(item, self.last_sended) > HBSensor.limiar()):
            print("sending...")
            self.last_sended = item
            data = {
                'beats': item
            }
            r = requests.post(url, headers={'Authorization': 'Token '+self.token}, data=data)
        else:
            print("skip...")
