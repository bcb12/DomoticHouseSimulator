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


sensor_G_01 = sensors.SensorPresence("globalpres1", True)
GLOBAL_SENSORS.append(sensor_G_01)

actuator_G_01 = actuators.ActuatorAlarm("GlobalAlarm", False)
GLOBAL_ACTUATORS.append(actuator_G_01)

action_1_01 = Action.Action(actuator_G_01,True)
action_1_02 = Action.Action(actuator_G_01,False)
action_1_03 = Action.Action(actuator_G_01,True)
action_1_04 = Action.Action(actuator_G_01,False)
action_1_05 = Action.Action(actuator_G_01,True)
action_1_06 = Action.Action(actuator_G_01,False)
action_1_07 = Action.Action(actuator_G_01,True)
action_1_08 = Action.Action(actuator_G_01,False)

state_1_01 = State.State("estate_01", [action_1_02, action_1_04, action_1_05, action_1_08])
state_1_02 = State.State("estate_02", [action_1_01, action_1_04, action_1_05, action_1_08])

transition_1_01 = Transition.Transition("001", state_1_01, state_1_02)
transition_1_02 = Transition.Transition("101", state_1_02, state_1_01)

automaton_1 = Automaton.Automaton("autom_01", state_1_01, [transition_1_01, transition_1_02])

sensor_1_01 = sensors.SensorPresence("spres1", True)
sensor_1_02 = sensors.SensorLight("slight1", 25.0, 25.0, 'eq')
sensor_1_03 = sensors.SensorSmoke("ssmoke1", False)

actuator_1_01 = actuators.ActuatorDoor("adoor1", False)
actuator_1_02 = actuators.ActuatorCold("acold1", False)

room_1 = Room.Room("room", automaton_1, False, False, 3.0, "12:43",
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