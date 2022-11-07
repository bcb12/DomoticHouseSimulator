import sensors

class Room:
    def __init__(self, id, automaton, presence, rain, light_intensity, time, temperature,
        smoke, wind, gas, intruders, flood, sensors, actuators):
        self.id = id
        self.automaton = automaton

        self.presence = presence
        self.rain = rain
        self.light_intensity = light_intensity
        self.time = time
        self.temperature = temperature
        self.smoke = smoke
        self.wind = wind
        self.gas = gas
        self.intruders = intruders
        self.flood = flood

        self.sensors = sensors
        self.actuators = actuators


    def update_sensors(self):
        '''Updates the values in the sensors acording to the variables'''

        for sensor in self.sensors:
            if sensor is sensors.SensorPresence:
                sensor.value = self.presence
            elif sensor is sensors.SensorRain:
                sensor.value = self.rain
            elif sensor is sensors.SensorLight:
                sensor.real_value = self.light_intensity
            elif sensor is sensors.SensorTime:
                sensor.real_value = self.time
            elif sensor is sensors.SensorTemperature:
                sensor.real_value = self.temperature
            elif sensor is sensors.SensorSmoke:
                sensor.value = self.smoke
            elif sensor is sensors.SensorWind:
                sensor.real_value = self.wind
            elif sensor is sensors.SensorGas:
                sensor.value = self.gas
            elif sensor is sensors.SensorIntruders:
                sensor.value = self.intruders
            elif sensor is sensors.SensorFlood:
                sensor.value = self.flood
