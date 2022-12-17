import datetime
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
        self.value = False
        self.operator = operator
        self.compare_value = compare_value
        self.identifier = identifier
        self.real_value = real_value
        self.set_value()

    def set_value(self):
        if self.operator == 'eq':
            self.value = self.real_value == self.compare_value
        elif self.operator == 'low':
            self.value = self.real_value < self.compare_value
        elif self.operator == 'up':
            self.value = self.real_value > self.compare_value
        elif self.operator == 'eqlow':
            self.value = self.real_value <= self.compare_value
        elif self.operator == 'equp':
            self.value = self.real_value >= self.compare_value

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
        self.value = False
        self.operator = operator
        self.compare_value = compare_value
        self.identifier = identifier
        self.real_value = real_value

    def set_value(self):
        if self.operator == 'eq':
            self.value = self.real_value == self.compare_value
        elif self.operator == 'low':
            self.value = self.real_value < self.compare_value
        elif self.operator == 'up':
            self.value = self.real_value > self.compare_value
        elif self.operator == 'eqlow':
            
            self.value = self.real_value <= self.compare_value
        elif self.operator == 'equp':
            self.value = self.real_value >= self.compare_value

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
        self.value = False
        self.operator = operator
        self.compare_value = compare_value
        self.identifier = identifier
        self.real_value = real_value
        self.set_value()

    def set_value(self):
        compare_hour = str(self.compare_value).split(':')[0]
        compare_minutes = str(self.compare_value).split(':')[1]
        self.compare_value = datetime.time(int(compare_hour), int(compare_minutes))

        print(self.real_value)
        real_hour = str(self.real_value).split(':')[0]
        real_minutes = str(self.real_value).split(':')[1]
        self.real_value = datetime.time(int(real_hour), int(real_minutes)).strftime('%H:%M')

        if self.operator == 'eq':
            self.value = self.real_value == self.compare_value
        elif self.operator == 'low':
            self.value = self.real_value < self.compare_value
        elif self.operator == 'up':
            self.value = self.real_value > self.compare_value
        elif self.operator == 'eqlow':
            self.value = self.real_value <= self.compare_value
        elif self.operator == 'equp':
            self.value = self.real_value >= self.compare_value

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
        self.value = False
        self.operator = operator
        self.compare_value = compare_value
        self.identifier = identifier
        self.real_value = real_value
        self.set_value()

    def set_value(self):
        if self.operator == 'eq':
            self.value = self.real_value == self.compare_value
        elif self.operator == 'low':
            self.value = self.real_value < self.compare_value
        elif self.operator == 'up':
            self.value = self.real_value > self.compare_value
        elif self.operator == 'eqlow':
            self.value = self.real_value <= self.compare_value
        elif self.operator == 'equp':
            self.value = self.real_value >= self.compare_value

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
