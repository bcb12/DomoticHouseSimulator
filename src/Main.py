"""
PYTHON MODULE TO IMPLEMENT THE AUTOMATON AND ITS FUNCTIONALITY
"""

from datetime import datetime
import logging

import Room
import Automaton
import Transition
import State
import Action

logging.basicConfig(
format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
level = logging.INFO
)
  
def main():
    """
    MAIN METHOD DECLARATION
    """

    # AUTOMATON GENERATION READ METHOD


    # OUTPUT AUTOMATON GENERATION



    COMBINACION_PRUEBA = "001"

    # TEST AUTOMATON
    # Actions
    action_01 = Action.Action("act_window_01",True)
    action_02 = Action.Action("act_window_01",False)
    action_03 = Action.Action("act_light_01",True)
    action_04 = Action.Action("act_light_01",False)
    action_05 = Action.Action("act_wblind_01",True)
    action_06 = Action.Action("act_wblind_01",False)
    action_07 = Action.Action("act_cold_01",True)
    action_08 = Action.Action("act_cold_01",False)

    # States
    state_01 = State.State("estate_01", [action_02, action_04, action_05, action_08])
    state_02 = State.State("estate_02", [action_01, action_04, action_05, action_08])
    state_03 = State.State("estate_03", [action_02, action_03, action_06, action_07])
    state_04 = State.State("estate_04", [action_01, action_04, action_05, action_07])

    # Transitions
    transition_01 = Transition.Transition("001", state_01, state_02)
    transition_02 = Transition.Transition("101", state_02, state_01)
    transition_03 = Transition.Transition("110", state_01, state_02)
    transition_04 = Transition.Transition("010", state_02, state_01)

    # Automatons
    automaton_01 = Automaton.Automaton("autom_01", state_01, [transition_01, transition_02])

    # Rooms
    room_01 = Room.Room("room_01", automaton_01, False, False, 3.0, str(datetime.now().month),
        22.1, False, 12.0, False, False, False)
    # END OF TEST AUTOMATON

    print("Current state: " + room_01.automaton.current_state.id)
    prueba = make_transition(automaton_01, COMBINACION_PRUEBA)
    print("Current state: " + room_01.automaton.current_state.id)


def make_transition(automaton, combination):
    """
    TRANSITION METHOD DECLARATION
    """
    result = automaton.current_state

    transition_index = transition_exists(automaton.transitions, combination)
    if transition_index != -1:
        transition = automaton.transitions[transition_index]
        if transition.source_state.id == automaton.current_state.id:
            # Realiza el cambio de estado
            automaton.current_state = transition.target_state

            # Ejecutar acciones
            target_state = transition.target_state
            result = target_state
            actions = target_state.actions
            
            # Mostrar acciones ejecutadas
            for action in actions:
                print("Executing action: Setting " + action.id + " to " + str(action.value))
        else:
            print("Error, the current state does not match the source state of the transition.")
    else:
        # Output error
        print("Error, the given combination does not exist.")
    
    return result


def transition_exists(transitions, combination):
    found = -1
    for index in range(len(transitions)):
        if transitions[index].combination == combination:
            found = index
            break
    return found


if __name__ == '__main__':
    main()