''' THIS MODULE IS AIMED AT DESCRIBING THE ACTUATORS OF THE DOMOTIC HOUSE '''

class Actuator:
    ''' THIS CLASS REPRESENTS A GENERIC ACTUATOR '''
    def __init__(self, identifier):
        self.identifier = identifier


class ActuatorDoor(Actuator):
    ''' THIS CLASS REPRESENTS A DOOR ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'APUERTA {self.identifier}'


class ActuatorHeat(Actuator):
    ''' THIS CLASS REPRESENTS A HEAT ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'ACALEFACCION {self.identifier}'


class ActuatorWindowBlind(Actuator):
    ''' THIS CLASS REPRESENTS A WINDOW BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'APERSIANA {self.identifier}'


class ActuatorLight(Actuator):
    ''' THIS CLASS REPRESENTS A LIGHT BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'ALUZ {self.identifier}'


class ActuatorWINDOW(Actuator):
    ''' THIS CLASS REPRESENTS A WINDOW ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'AVENTANA {self.identifier}'


class ActuatorCold(Actuator):
    ''' THIS CLASS REPRESENTS A COOLING ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'AFRIO {self.identifier}'


class ActuatorGas(Actuator):
    ''' THIS CLASS REPRESENTS A GAS ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'AGAS {self.identifier}'


class ActuatorSunBlind(Actuator):
    ''' THIS CLASS REPRESENTS A SUN BLIND ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'ATOLDO {self.identifier}'


class ActuatorAlarm(Actuator):
    ''' THIS CLASS REPRESENTS AN ALARM ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'AALARM {self.identifier}'


class ActuatorEmergency(Actuator):
    ''' THIS CLASS REPRESENTS AN EMERGENCY CALL ACTUATOR '''

    def __str__(self):
        ''' TO STRING METHOD '''
        return f'AEMERGENCIA {self.identifier}'
