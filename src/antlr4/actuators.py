''' THIS MODULE IS AIMED AT DESCRIBING THE ACTUATORS OF THE DOMOTIC HOUSE '''

class Actuator:
    ''' THIS CLASS REPRESENTS A GENERIC ACTUATOR '''
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value


class ActuatorDoor(Actuator):
    ''' THIS CLASS REPRESENTS A DOOR ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Puerta {self.identifier}: on'
        else:
            return f'Puerta {self.identifier}: off'


class ActuatorHeat(Actuator):
    ''' THIS CLASS REPRESENTS A HEAT ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Calefacción {self.identifier}: on'
        else:
            return f'Calefacción {self.identifier}: off'


class ActuatorWindowBlind(Actuator):
    ''' THIS CLASS REPRESENTS A WINDOW BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Persiana {self.identifier}: on'
        else:
            return f'Persiana {self.identifier}: off'


class ActuatorLight(Actuator):
    ''' THIS CLASS REPRESENTS A LIGHT BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Luz {self.identifier}: on'
        else:
            return f'Luz {self.identifier}: off'


class ActuatorWindow(Actuator):
    ''' THIS CLASS REPRESENTS A WINDOW ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Ventana {self.identifier}: on'
        else:
            return f'Ventana {self.identifier}: off'


class ActuatorCold(Actuator):
    ''' THIS CLASS REPRESENTS A COOLING ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Aire acondicionado {self.identifier}: on'
        else:
            return f'Aire acondicionado {self.identifier}: off'


class ActuatorGas(Actuator):
    ''' THIS CLASS REPRESENTS A GAS ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Gas {self.identifier}: on'
        else:
            return f'Gas {self.identifier}: off'


class ActuatorSunBlind(Actuator):
    ''' THIS CLASS REPRESENTS A SUN BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Toldo {self.identifier}: on'
        else:
            return f'Toldo {self.identifier}: off'


class ActuatorAlarm(Actuator):
    ''' THIS CLASS REPRESENTS AN ALARM ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Alarma {self.identifier}: on'
        else:
            return f'Alarma {self.identifier}: off'


class ActuatorEmergency(Actuator):
    ''' THIS CLASS REPRESENTS AN EMERGENCY CALL ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''

        if self.value:
            return f'Llamada de emergencia {self.identifier}: on'
        else:
            return f'Llamada de emergencia {self.identifier}: off'
