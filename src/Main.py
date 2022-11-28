from simulation import Simulation
from House import House
from ExampleRooms import ROOMS, GLOBAL_SENSORS, GLOBAL_ACTUATORS


def simulate_house(house):
    ''' Given a house, runs it in the simulation '''

    start_simulation(house.room_list, house.global_sensors, house.global_actuators)


def start_simulation(room_list, global_sensors, global_actuators):
    ''' Starts the simulation given the necessary parameters '''
    num_vert = len(room_list)

    edge_list = {}
    edges = []

    for i in range(num_vert):
        edge_list.update({room_list[i].id:i})

    for room in room_list:
        if len(room.connection_list) != 0:
            for i in range(len(room.connection_list)):
                edges.append([edge_list[room.id], edge_list[room.connection_list[i]]])

    types_used = [room.type for room in room_list]
    names_used = [room.id for room in room_list]

    sim = Simulation(num_vert, edges, types_used, names_used, room_list, global_sensors,\
        global_actuators)
    sim.run()


if __name__ == "__main__":
    house = House('house1', ROOMS, GLOBAL_SENSORS, GLOBAL_ACTUATORS)
    simulate_house(house)
