import Action
import State
import Transition
import Automaton
import Room
import sensors
import actuators
import datetime

action_1_01 = Action.Action("act_window_01",True)
action_1_02 = Action.Action("act_window_01",False)
action_1_03 = Action.Action("act_light_01",True)
action_1_04 = Action.Action("act_light_01",False)
action_1_05 = Action.Action("act_wblind_01",True)
action_1_06 = Action.Action("act_wblind_01",False)
action_1_07 = Action.Action("act_cold_01",True)
action_1_08 = Action.Action("act_cold_01",False)

state_1_01 = State.State("estate_01", [action_1_02, action_1_04, action_1_05, action_1_08])
state_1_02 = State.State("estate_02", [action_1_01, action_1_04, action_1_05, action_1_08])

transition_1_01 = Transition.Transition("001", state_1_01, state_1_02)
transition_1_02 = Transition.Transition("101", state_1_02, state_1_01)

automaton_1 = Automaton.Automaton("autom_01", state_1_01, [transition_1_01, transition_1_02])

sensor_1_01 = sensors.SensorPresence("spres1", True)
sensor_1_02 = sensors.SensorLight("slight1", 25.0, 25.0, 'eq')
sensor_1_03 = sensors.SensorSmoke("ssmoke1", False)

actuator_1_01 = actuators.ActuatorDoor("adoor1")
actuator_1_02 = actuators.ActuatorCold("acold1")

room_1 = Room.Room("room1", automaton_1, False, False, 3.0, "12:43",
    22.1, False, 12.0, False, False, False, [sensor_1_01, sensor_1_02, sensor_1_03],
    [actuator_1_01, actuator_1_02])


ROOMS = [room_1, room_1, room_1, room_1, room_1, room_1, room_1, room_1]

NAMES = []
for i in range(len(ROOMS)):
    NAMES.append(ROOMS[i].id + '_' + str(i))