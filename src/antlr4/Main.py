from simulation import Simulation
from House import House

import LALR
import sys
import logging
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from antlr4 import InputStream
from DHSemanticGrammarLexer import DHSemanticGrammarLexer
from DHSemanticGrammarListener import DHSemanticGrammarListener
from DHSemanticGrammarParser import DHSemanticGrammarParser


def simulate_house(house):
    ''' Given a house, runs it in the simulation '''

    start_simulation(house.room_list, house.global_sensors, house.global_actuators)


def start_simulation(room_list, global_sensors, global_actuators):
    ''' Starts the simulation given the necessary parameters '''
    room_list = check_repeated_rooms(room_list)
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


def check_repeated_rooms(room_list):
    '''Checks if there are repeated rooms'''
    final_rooms = []

    for room in room_list:
        if room not in final_rooms:
            final_rooms.append(room)

    return final_rooms


def main():
    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return

    with open(sys.argv[1], 'r+', encoding = 'utf-8') as file:
        # lexer
        lexer = DHSemanticGrammarLexer(InputStream(file.read()))
        stream = CommonTokenStream(lexer)
        # parser
        parser = DHSemanticGrammarParser(stream)
        tree = parser.casa()
        house = tree.data
        simulate_house(house)


if __name__ == '__main__':
    main()
