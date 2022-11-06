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
