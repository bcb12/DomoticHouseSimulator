from simulation import Simulation
from House import House

import LALR
import sys
import logging


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

def main():
    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return
    house = LALR.main(sys.argv[1])
    simulate_house(house)

if __name__ == '__main__':
    main()


