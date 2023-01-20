class Automaton:
    def __init__(self, id, current_state, transitions):
        self.id = id
        self.current_state = current_state
        self.transitions = transitions