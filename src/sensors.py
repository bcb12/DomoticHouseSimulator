''' THIS MODULE IS AIMED AT DESCRIBING THE SENSORS OF THE DOMOTIC HOUSE '''

class SensorPresence:
    ''' This class represents a presence sensor '''

    def __init__(self, identifier, is_person):
        ''' CONSTRUCTOR METHOD '''
        self.value = is_person
        self.identifier = identifier

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de presencia {self.identifier}: 1'
        else:
            return f'Sensor de presencia {self.identifier}: 0'


class SensorRain:
    ''' This class represents a rain sensor '''

    def __init__(self, identifier, is_raining):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.value = is_raining

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de lluvia {self.identifier}: 1'
        else:
            return f'Sensor de lluvia {self.identifier}: 0'


class SensorLight:
    ''' This class represents a light sensor '''

    def __init__(self, identifier, compare_value, real_value, operator):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.real_value = real_value

        if operator == 'eq':
            self.value = real_value == compare_value
        elif operator == 'low':
            self.value = real_value < compare_value
        elif operator == 'up':
            self.value = real_value > compare_value
        elif operator == 'eqlow':
            self.value = real_value <= compare_value
        elif operator == 'equp':
            self.value = real_value >= compare_value

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de int. luminosa {self.identifier}: 1'
        else:
            return f'Sensor de int. luminosa {self.identifier}: 0'


class SensorTemperature:
    ''' This class represents a temperature sensor '''

    def __init__(self, identifier, compare_value, real_value, operator):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.real_value = real_value

        if operator == 'eq':
            self.value = real_value == compare_value
        elif operator == 'low':
            self.value = real_value < compare_value
        elif operator == 'up':
            self.value = real_value > compare_value
        elif operator == 'eqlow':
            self.value = real_value <= compare_value
        elif operator == 'equp':
            self.value = real_value >= compare_value

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de temperatura {self.identifier}: 1'
        else:
            return f'Sensor de temperatura {self.identifier}: 0'


class SensorTime:
    ''' This class represents a time sensor '''

    def __init__(self, identifier, compare_value, real_value, operator):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier

        if operator == 'eq':
            self.value = real_value == compare_value
        elif operator == 'low':
            self.value = real_value < compare_value
        elif operator == 'up':
            self.value = real_value > compare_value
        elif operator == 'eqlow':
            self.value = real_value <= compare_value
        elif operator == 'equp':
            self.value = real_value >= compare_value

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de hora {self.identifier}: 1'
        else:
            return f'Sensor de hora {self.identifier}: 0'


class SensorSmoke:
    ''' This class represents a smoke sensor '''

    def __init__(self, identifier, is_smoke):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.value = is_smoke

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de humo {self.identifier}: 1'
        else:
            return f'Sensor de humo {self.identifier}: 0'


class SensorWind:
    ''' This class represents a wind sensor '''

    def __init__(self, identifier, compare_value, real_value, operator):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier

        if operator == 'eq':
            self.value = real_value == compare_value
        elif operator == 'low':
            self.value = real_value < compare_value
        elif operator == 'up':
            self.value = real_value > compare_value
        elif operator == 'eqlow':
            self.value = real_value <= compare_value
        elif operator == 'equp':
            self.value = real_value >= compare_value

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de viento {self.identifier}: 1'
        else:
            return f'Sensor de viento {self.identifier}: 0'


class SensorIntruders:
    ''' This class represents an intruders sensor '''

    def __init__(self, identifier, is_intruder):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.value = is_intruder

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de intrusos {self.identifier}: 1'
        else:
            return f'Sensor de intrusos {self.identifier}: 0'


class SensorFlood:
    ''' This class represents a flood sensor '''

    def __init__(self, identifier, is_flood):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.value = is_flood

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de inundación {self.identifier}: 1'
        else:
            return f'Sensor de inundación {self.identifier}: 0'


class SensorGas:
    ''' This class represents a gas sensor '''

    def __init__(self, identifier, is_gas):
        ''' CONSTRUCTOR METHOD '''
        self.identifier = identifier
        self.value = is_gas

    def __str__(self):
        ''' TO STRING METHOD '''
        if self.value:
            return f'Sensor de gas {self.identifier}: 1'
        else:
            return f'Sensor de gas {self.identifier}: 0'
