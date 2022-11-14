import sensors


class Room:
    def __init__(self, id, automaton, presence, rain, light_intensity, time, temperature,
        smoke, wind, gas, intruders, flood, sensors, actuators):
        self.id = id
        self.automaton = automaton

        self.presence = presence
        self.rain = rain
        self.light_intensity = str(light_intensity)
        self.time = str(time)
        self.temperature = str(temperature)
        self.smoke = smoke
        self.wind = str(wind)
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
                sensor.real_value = float(self.light_intensity)
                sensor.set_value()
            elif sensor is sensors.SensorTime:
                sensor.real_value = self.time
                sensor.set_value()
            elif sensor is sensors.SensorTemperature:
                sensor.real_value = float(self.temperature)
                sensor.set_value()
            elif sensor is sensors.SensorSmoke:
                sensor.value = self.smoke
            elif sensor is sensors.SensorWind:
                sensor.real_value = float(self.wind)
                sensor.set_value()
            elif sensor is sensors.SensorGas:
                sensor.value = self.gas
            elif sensor is sensors.SensorIntruders:
                sensor.value = self.intruders
            elif sensor is sensors.SensorFlood:
                sensor.value = self.flood


    def call_automaton(self):
        '''Calls the automaton to change state if possible'''

        self.make_transition(self.automaton, self.get_combination(self.sensors))


    def transition_exists(self, transitions, combination):
        found = -1
        for index in range(len(transitions)):
            if transitions[index].combination == combination:
                found = index
                break
        return found


    def make_transition(self, automaton, combination):
        """
        TRANSITION METHOD DECLARATION
        """
        result = automaton.current_state

        transition_index = self.transition_exists(automaton.transitions, combination)
        if transition_index != -1:
            transition = automaton.transitions[transition_index]
            if transition.source_state.id == automaton.current_state.id:
                target_state = transition.target_state

                # Realiza el cambio de estado
                automaton.current_state = target_state

                # Ejecutar acciones
                result = target_state
                actions = target_state.actions
                
                # Mostrar acciones ejecutadas
                for action in actions:
                    print("Previous actuator value: " + str(action.actuator.value))
                    action.actuator.value = action.value
                    print("Executing action: Setting " + action.id + " to " + str(action.value) + ". New actuator value: " + str(action.actuator.value))
            else:
                print("Error, the current state does not match the source state of the transition.")
        else:
            # Output error
            print("Error, the given combination does not exist.")
        
        return result


    def get_combination(self, sensors):
        combination = ""
        for sensor in sensors:
            if(sensor.value):
                combination += "1"
            else:
                combination += "0"
        return(combination)
