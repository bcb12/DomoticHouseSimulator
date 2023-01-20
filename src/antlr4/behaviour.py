from State import State
from Transition import Transition

class Behaviour:
    def __init__(self, states_list, initial_state, transitions):
        self.states_list = states_list
        self.initial_state = initial_state
        self.transitions = transitions