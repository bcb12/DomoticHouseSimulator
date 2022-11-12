"""
PYTHON MODULE TO IMPLEMENT THE AUTOMATON AND ITS FUNCTIONALITY
"""

from datetime import datetime
import logging

from Room import Room
from Automaton import Automaton
from Transition import Transition
from State import State
from Action import Action
from sensors import *
from actuators import *


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
    # Sensors
    sen_presence_01 = SensorPresence("sen_presence_01", False)
    sen_light_01 = SensorLight("sen_light_01", 11.0, 10.0, "equp")
    # Sensors list
    sensors_list = [sen_presence_01, sen_light_01]

    # Actuators
    act_window_01 = ActuatorWindow("act_window_01", False)
    act_light_01 = ActuatorLight("act_light_01", False)
    act_wblind_01 = ActuatorWindowBlind("act_wblind_01", False)
    act_cold_01 = ActuatorCold("act_cold_01", False)
    # Actuator list
    actuators_list = [act_window_01, act_light_01, act_wblind_01, act_cold_01]

    # Actions
    action_01 = Action("action_01", act_window_01, True)
    action_02 = Action("action_02", act_window_01, False)
    action_03 = Action("action_03", act_light_01, True)
    action_04 = Action("action_04", act_light_01, False)
    action_05 = Action("action_05", act_wblind_01, True)
    action_06 = Action("action_06", act_wblind_01, False)
    action_07 = Action("action_07", act_cold_01, True)
    action_08 = Action("action_08", act_cold_01, False)

    # States
    state_01 = State("estate_01", [action_02, action_04, action_05, action_08])
    state_02 = State("estate_02", [action_01, action_04, action_05, action_08])
    state_03 = State("estate_03", [action_02, action_03, action_06, action_07])
    state_04 = State("estate_04", [action_01, action_04, action_05, action_07])

    # Transitions
    transition_01 = Transition("001", state_01, state_02)
    transition_02 = Transition("101", state_02, state_01)
    transition_03 = Transition("110", state_01, state_02)
    transition_04 = Transition("010", state_02, state_01)

    # Automatons
    automaton_01 = Automaton("autom_01", state_01, [transition_01, transition_02])

    # Rooms
    room_01 = Room("room_01", automaton_01, False, False, 3.0, str(datetime.now().month),
        22.1, False, 12.0, False, False, False, sensors_list, actuators_list)
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
            target_state = transition.target_state

            # Realiza el cambio de estado
            automaton.current_state = target_state

            # Ejecutar acciones
            result = target_state
            actions = target_state.actions
            
            # Mostrar acciones ejecutadas
            for action in actions:
                print("Previous actuator value: " + str(action.actuator.value))
                action.actuator.value = action.value
                print("Executing action: Setting " + action.id + " to " + str(action.value) + ". New actuator value: " + str(action.actuator.value))
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