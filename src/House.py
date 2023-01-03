class House:
    def __init__(self, id, room_list, global_sensors, global_actuators):
        self.id = id
        self.room_list = room_list
        self.global_sensors = global_sensors
        self.global_actuators = global_actuators

    def __str__(self):
        '''To_string method for class House'''
        room_list_str = '\n\t'.join([str(room) for room in self.room_list])
        gsensor_list_str = '\n\t'.join([str(sensor) for sensor in self.global_sensors])
        gactuator_list_str = '\n\t'.join([str(act) for act in self.global_actuators])
        return f'House with id {self.id} has the following:\n - Rooms: \n\t{room_list_str}\n - Global sensors: \n\t{gsensor_list_str}\n - Global actuators: \n\t{gactuator_list_str}'
