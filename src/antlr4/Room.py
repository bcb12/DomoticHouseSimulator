import sensors


class Room:
    def __init__(self, id, room_type, states, automaton, presence, rain, light_intensity,
    time, temperature, smoke, wind, gas, intruders, flood, sensors, actuators, connection_list = []):
        self.id = id
        self.type = room_type
        self.states = states
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

        self.connection_list = connection_list

        self.reset_variables()


    def reset_variables(self):
        '''Reset variable values to 0'''

        self.rain = False
        self.light_intensity = 0.0
        self.time = '00:00'
        self.temperature = 0.0
        self.smoke = False
        self.wind = 0.0
        self.gas = False
        self.intruders = False
        self.flood = False

    def update_sensors(self):
        '''Updates the values in the sensors acording to the variables'''

        for sensor in self.sensors:
            if isinstance(sensor, sensors.SensorPresence):
                sensor.value = self.presence
            elif isinstance(sensor, sensors.SensorRain):
                sensor.value = self.rain
            elif isinstance(sensor, sensors.SensorLight):
                sensor.real_value = float(self.light_intensity)
                sensor.set_value()
            elif isinstance(sensor, sensors.SensorTime):
                sensor.real_value = self.time
                sensor.set_value()
            elif isinstance(sensor, sensors.SensorTemperature):
                sensor.real_value = float(self.temperature)
                sensor.set_value()
            elif isinstance(sensor, sensors.SensorSmoke):
                sensor.value = self.smoke
            elif isinstance(sensor, sensors.SensorWind):
                sensor.real_value = float(self.wind)
                sensor.set_value()
            elif isinstance(sensor, sensors.SensorGas):
                sensor.value = self.gas
            elif isinstance(sensor, sensors.SensorIntruders):
                sensor.value = self.intruders
            elif isinstance(sensor, sensors.SensorFlood):
                sensor.value = self.flood

    def call_automaton(self, global_combination):
        '''Calls the automaton to change state if possible'''

        self.update_sensors()
        self.make_transition(self.automaton, global_combination+self.get_combination(self.sensors))


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
            if transition.source_state == automaton.current_state:
                print("\nExecuting transition from state " + transition.source_state + " to state " + transition.target_state + " in room " + self.id + ".")
                target_state = transition.target_state

                # Realiza el cambio de estado
                automaton.current_state = target_state

                # Find state
                state = self.get_state(target_state)

                # Ejecutar acciones
                result = target_state
                actions = state.actions
                
                # Mostrar acciones ejecutadas
                for action in actions:
                    action.actuator.value = action.value
        
        return result


    def get_combination(self, sensors):
        combination = ""
        for sensor in sensors:
            if(sensor.value):
                combination += "1"
            else:
                combination += "0"
        return(combination)


    def get_state(self, id):
        found_state = False
        for state in self.states:
            if(state.id == id):
                found_state = state
                break

        return found_state

    def __str__(self):
        '''To_string method for class Room'''
        sensor_list_str = []
        actuator_list_str = []
        if self.sensors: sensor_list_str = '\n\t'.join([str(sensor) for sensor in self.sensors])
        if self.actuators: actuator_list_str = '\n\t'.join([str(act) for act in self.actuators])
        if self.type == 'H':
            return f'Room {self.id} with the following: \n\t - Local sensors: {sensor_list_str} \n\t - Local actuators: {actuator_list_str}'
        elif self.type == 'P':
            return f'Corridor {self.id} with the following: \n\t - Local sensors: {sensor_list_str} \n\t - Local actuators: {actuator_list_str}\n\t - Connexions with: {self.connection_list}'
