import Action
import State
import Transition
import Automaton
import Room
import sensors
import actuators
import copy

GLOBAL_SENSORS = []
GLOBAL_ACTUATORS = []

sensor_1_01 = sensors.SensorPresence("spres1", True)
sensor_1_02 = sensors.SensorTime("stime1", "13:00", "14:00", 'up')
sensor_1_03 = sensors.SensorSmoke("ssmoke1", False)

actuator_1_01 = actuators.ActuatorDoor("adoor1", False)
actuator_1_02 = actuators.ActuatorCold("acold1", False)

action_1_01 = Action.Action(actuator_1_01,True)
action_1_02 = Action.Action(actuator_1_01,False)

state_1_01 = State.State("state_01", [action_1_01])
state_1_02 = State.State("state_02", [action_1_02])

transition_1_01 = Transition.Transition("100", state_1_01, state_1_02)
transition_1_02 = Transition.Transition("110", state_1_02, state_1_01)
transition_1_03 = Transition.Transition("111", state_1_01, state_1_02)

automaton_1 = Automaton.Automaton("autom_01", state_1_01, [transition_1_01, transition_1_02, transition_1_03])

room_1 = Room.Room("room", "H", automaton_1, False, False, 3.0, "12:43",
    22.1, False, 12.0, False, False, False, [sensor_1_01, sensor_1_02, sensor_1_03],
    [actuator_1_01, actuator_1_02])


room_2 = copy.deepcopy(room_1)
room_2.temperature = 19.7
room_2.id = 'alt'


ROOMS = [room_1, copy.deepcopy(room_1), copy.deepcopy(room_1), copy.deepcopy(room_1),
    copy.deepcopy(room_1), copy.deepcopy(room_1), copy.deepcopy(room_1), room_2]

NAMES = []

for i in range(len(ROOMS)):
    ROOMS[i].id += '_' + str(i)
    NAMES.append(ROOMS[i].id)

ROOMS[0].connection_list = ['room_1', 'room_3']
ROOMS[1].connection_list = ['room_2']
ROOMS[4].connection_list = ['room_1', 'room_5', 'room_3', 'room_2']
ROOMS[5].connection_list = ['alt_7']
ROOMS[7].connection_list = ['room_6']