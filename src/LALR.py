# -----------------------------------------------------------------------------
# example.py
#
# Example of using PLY To parse the following simple grammar.
#
#   expression : term PLUS term
#              | term MINUS term
#              | term
#
#   term       : factor TIMES factor
#              | factor DIVIDE factor
#              | factor
#
#   factor     : NUMBER
#              | NAME
#              | PLUS factor
#              | MINUS factor
#              | LPAREN expression RPAREN
#
# -----------------------------------------------------------------------------
import sys
import logging

from House import House
from Room import Room
from Automaton import Automaton
from Transition import Transition
from State import State
from Action import Action
from sensors import *
from actuators import *
from behaviour import Behaviour

from ply.lex import lex
from ply.yacc import yacc

# --- Tokenizer

# All tokens must be named in advance.
tokens = ( 'SPRESENCIA', 'SLLUVIA', 'SILUMINACION', 'STEMPERATURA', 'SRELOJ', 'SHUMO',
           'SGAS', 'SVIENTO', 'SINTRUSOS', 'SINUNDACION', 'APUERTA', 'ACALEFACCION', 'APERSIANA', 'ALUZ', 'AVENTANA', 'AFRIO', 'AGAS', 'ATOLDO', 'AALARMA', 'AEMERGENCIA', 'ROOM', 'HOUSE', 'CORRIDOR', 'GLOBAL', 'STATE', 'INIT', 'OPL', 'BOOL', 'ID', 'DOUBLE', 'TIME', 'COMBINATION', 'SEQ', 'SEMICOLON', 'LBRACKET', 'RBRACKET', 'COMMA' )

# Ignored characters
t_ignore = ' '

# Token matching rules are written as regexs


# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_COMMENT(token):
    r'\\\*.*?\*/'
    pass
    # No return value. Token discarded

def t_IGNORE(token):
    r'(\t|\n|\r)+'
    pass
    # No return value. Token discarded

def t_SPRESENCIA(token):
    r'sensor_presence'
    return token

def t_SLLUVIA(token):
    r'sensor_rain'
    return token

def t_SILUMINACION(token):
    r'sensor_light'
    return token

def t_STEMPERATURA(token):
    r'sensor_temperature'
    return token

def t_SRELOJ(token):
    r'sensor_time'
    return token

def t_SHUMO(token):
    r'sensor_smoke'
    return token

def t_SGAS(token):
    r'sensor_gas'
    return token

def t_SVIENTO(token):
    r'sensor_wind'
    return token

def t_SINTRUSOS(token):
    r'sensor_intruder'
    return token

def t_SINUNDACION(token):
    r'sensor_flood'
    return token

def t_APUERTA(token):
    r'actuator_door'
    return token

def t_ACALEFACCION(token):
    r'actuator_heat'
    return token

def t_APERSIANA(token):
    r'actuator_wblind'
    return token

def t_ALUZ(token):
    r'actuator_light'
    return token

def t_AVENTANA(token):
    r'actuator_window'
    return token

def t_AFRIO(token):
    r'actuator_cold'
    return token

def t_AGAS(token):
    r'actuator_gas'
    return token

def t_ATOLDO(token):
    r'actuator_wind'
    return token

def t_AALARMA(token):
    r'actuator_alarm'
    return token

def t_AEMERGENCIA(token):
    r'actuator_emergency'
    return token

def t_ROOM(token):
    r'room'
    return token

def t_HOUSE(token):
    r'house'
    return token

def t_CORRIDOR(token):
    r'corridor'
    return token

def t_GLOBAL(token):
    r'global'
    return token

def t_STATE(token):
    r'state'
    return token

def t_INIT(token):
    r'init'
    return token

def t_OPL(token):
    r'eqlow|equp|eq|up|low'
    return token

def t_BOOL(token):
    r'true|false'
    return token

def t_ID(token):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return token

def t_DOUBLE(token):
    r'-?[0-9]([0-9]*)\.([0-9]+)'
    return token

def t_TIME(token):
    r'((0|1)[0-9]|2[0-3]):[0-5][0-9]'
    return token

def t_COMBINATION(token):
    r'(0|1)+'
    return token

def t_SEQ(token):
    r':='
    return token

def t_SEMICOLON(token):
    r';'
    return token

def t_LBRACKET(token):
    r'{'
    return token

def t_RBRACKET(token):
    r'}'
    return token

def t_COMMA(token):
    r','
    return token

# Ignored token with an action associated with it
def t_ignore_newline(token):
    r'\n+'
    token.lexer.lineno += token.value.count('\n')

# Error handler for illegal characters
def t_error(token):
    print(f'Illegal character {token.value[0]!r}')
    token.lexer.skip(1)

# Build the lexer object
lexer = lex()

# Productions
def p_casa1(token):
    '''
	casa : HOUSE ID LBRACKET lh RBRACKET SEMICOLON
	'''
    token[0] = House(token[2], token[4], [], [])

def p_casa2(token):
    '''
	casa : HOUSE ID LBRACKET lh lp RBRACKET SEMICOLON
	'''
    token[4].extend(token[5])
    token[0] = House(token[2], token[4], [], [])

def p_casa3(token):
    '''
	casa : HOUSE ID LBRACKET lh lsg RBRACKET SEMICOLON
	'''
    token[0] = House(token[2], token[4], token[6], [])

def p_casa4(token):
    '''
	casa : HOUSE ID LBRACKET lh lag RBRACKET SEMICOLON
	'''
    token[0] = House(token[2], token[4], [], token[6])

def p_casa5(token):
    '''
	casa : HOUSE ID LBRACKET lh lp lsg RBRACKET SEMICOLON
	'''
    token[4].extend(token[5])
    token[0] = House(token[2], token[4], token[6], [])

def p_casa6(token):
    '''
	casa : HOUSE ID LBRACKET lh lp lag RBRACKET SEMICOLON
	'''
    token[4].extend(token[5])
    token[0] = House(token[2], token[4], [], token[6])

def p_casa7(token):
    '''
	casa : HOUSE ID LBRACKET lh lsg lag RBRACKET SEMICOLON
	'''
    token[0] = House(token[2], token[4], token[5], token[6])

def p_casa8(token):
    '''
	casa : HOUSE ID LBRACKET lh lp lsg lag RBRACKET SEMICOLON
	'''
    token[4].extend(token[5])
    token[0] = House(token[2], token[4], token[6], token[7])

def p_lh1(token):
    '''
	lh : h COMMA lh
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lh2(token):
    '''
	lh : h SEMICOLON
	'''
    room_list = []
    room_list.append(token[1])
    token[0] = room_list

def p_lp1(token):
    '''
	lp : p COMMA lp
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lp2(token):
    '''
	lp : p SEMICOLON
	'''
    corridor_list = []
    corridor_list.append(token[1])
    token[0] = corridor_list

def p_h1(token):
    '''
	h : ROOM ID LBRACKET lsl RBRACKET
	'''
    presence, rain, smoke, gas, intruders, flood = False
    light_intensity, temperature, wind = 0.0
    time = "00:00"
    sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders, flood]
    for sensor in token[4]:
        check_sensor_type(sensor, sensors)
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "H", [], automaton, sensor[0], sensor[1], sensor[2], sensor[3], sensor[4], sensor[5], sensor[6], sensor[7], sensor[8], sensor[9], [], token[4], [])

def p_h2(token):
    '''
	h : ROOM ID LBRACKET lal RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "H", [], automaton, False, False, 0.0, "00:00", 0.0, False, 0.0, False, False, False, [], token[5], [])

def p_h3(token):
    '''
	h : ROOM ID LBRACKET c RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], token[4].initial_state, token[4].transitions)
    token[0] = Room(token[2], "H", token[5].states_list, automaton, False, False, 0.0, "00:00", 0.0, False, 0.0, False, False, False, [], [], [])

def p_h4(token):
    '''
	h : ROOM ID LBRACKET lsl lal RBRACKET
	'''
    presence, rain, smoke, gas, intruders, flood = False
    light_intensity, temperature, wind = 0.0
    time = "00:00"
    sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders, flood]
    for sensor in token[4]:
        check_sensor_type(sensor, sensors)
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "H", [], automaton, sensor[0], sensor[1], sensor[2], sensor[3], sensor[4], sensor[5], sensor[6], sensor[7], sensor[8], sensor[9], token[4], token[5], [])

def p_h5(token):
    '''
	h : ROOM ID LBRACKET lsl c RBRACKET
	'''
    presence, rain, smoke, gas, intruders, flood = False
    light_intensity, temperature, wind = 0.0
    time = "00:00"
    sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders, flood]
    for sensor in token[4]:
        check_sensor_type(sensor, sensors)
    automaton = Automaton('autom_'+token[2], token[5].initial_state, token[5].transitions)
    token[0] = Room(token[2], "H", token[5].states_list, automaton, sensor[0], sensor[1], sensor[2], sensor[3], sensor[4], sensor[5], sensor[6], sensor[7], sensor[8], sensor[9], token[4], [], [])

def p_h6(token):
    '''
	h : ROOM ID LBRACKET lal c RBRACKET
	'''
    for state in token[5].states_list:
        for action in state.actions:
            for actuator in token[4]:
                if(action.actuator == actuator.identifier):
                    action.actuator = actuator
    
    initial_state = ""
    for state in token[5].states_list:
        if(state.id == token[5].initial_state):
            initial_state = state
    
    for actuator in token[5]:
        for action in initial_state.actions:
            if(action.actuator == actuator):
                actuator.value = action.value

    automaton = Automaton('autom_'+token[2], token[5].initial_state, token[5].transitions)
    token[0] = Room(token[2], "H", token[5].states_list, automaton, False, False, 0.0, "00:00", 0.0, False, False, False, False, [], [], token[4])

def p_h7(token):
    '''
	h : ROOM ID LBRACKET lsl lal c RBRACKET
	'''
    # En la clase Action, sustituir el ID del actuador por el objeto actuador
    initial_state = ""
    for state in token[6].states_list:
        if(state.id == token[6].initial_state):
            initial_state = state
        for action in state.actions:
            for actuator in token[5]:
                if(action.actuator == actuator.identifier):
                    action.actuator = actuator

    # Asignar los valores de los sensores a las variables de la habitación
    presence=rain=smoke=gas=intruders=flood = False
    light_intensity=temperature=wind = 0.0
    time = "00:00"
    sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders, flood]
    for sensor in token[4]:
        check_sensor_type(sensor, sensors)

    # Asignar valores del estado inicial a los actuadores
    for actuator in token[5]:
        for action in initial_state.actions:
            if(action.actuator == actuator):
                actuator.value = action.value

    automaton = Automaton('autom_'+token[2], token[6].initial_state, token[6].transitions)
    token[0] = Room(token[2], "H", token[6].states_list, automaton, sensors[0], sensors[1], sensors[2], sensors[3], sensors[4], sensors[5], sensors[6], sensors[7], sensors[8], sensors[9], token[4], token[5], [])
    
def p_h_empty(token):
    '''
	h : ROOM ID LBRACKET RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "H", [], automaton, False, False, 0.0, "00:00", 0.0, False, False, False, False, [], [], [])

def p_p1(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lsl RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "P", [], automaton, False, False, 0.0, "00:00", 0.0, False, False, False, False, False, token[5], [], token[4])

def p_p2(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lal RBRACKET
	'''

    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "P", [], automaton, False, False, 0.0, "00:00", 0.0, False, False, False, False, False, [], token[5], token[4])

def p_p3(token):
    '''
	p : CORRIDOR ID LBRACKET l2id c RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], token[5].initial_state, token[5].transitions)
    token[0] = Room(token[2], "P", token[6].states_list, automaton, False, False, 0.0, "00:00", 0.0, False, False, False, False, False, [], [], token[4])

def p_p4(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lsl lal RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "P", [], automaton, False, False, False, False, False, False, False, False, False, False, token[5], token[6], token[4])

def p_p5(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lsl c RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], token[6].initial_state, token[6].transitions)
    token[0] = Room(token[2], "P", token[6].states_list, automaton, False, False, False, False, False, False, False, False, False, False, token[5], [], token[4])

def p_p6(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lal c RBRACKET
	'''
    for state in token[6].states_list:
        for action in state.actions:
            for actuator in token[5]:
                if(action.actuator == actuator.identifier):
                    action.actuator = actuator
    automaton = Automaton('autom_'+token[2], token[6].initial_state, token[6].transitions)
    token[0] = Room(token[2], "P", token[6].states_list, automaton, False, False, False, False, False, False, False, False, False, False, [], token[5], token[4])

def p_p7(token):
    '''
	p : CORRIDOR ID LBRACKET l2id lsl lal c RBRACKET
	'''
    for state in token[7].states_list:
        for action in state.actions:
            for actuator in token[6]:
                if(action.actuator == actuator.identifier):
                    action.actuator = actuator
    automaton = Automaton('autom_'+token[2], token[7].initial_state, token[7].transitions)
    token[0] = Room(token[2], "P", token[7].states_list, automaton, False, False, False, False, False, False, False, False, False, False, token[5], token[6], token[4])

def p_p8(token):
    '''
	p : CORRIDOR ID LBRACKET l2id RBRACKET
	'''
    automaton = Automaton('autom_'+token[2], False, [])
    token[0] = Room(token[2], "P", [], automaton, False, False, False, False, False, False, False, False, False, False, [], [], token[4])

def p_l2id1(token):
    '''
	l2id : ID COMMA l2id
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_l2id2(token):
    '''
	l2id : ID COMMA ID SEMICOLON
	'''
    connections_list = []
    connections_list.append(token[1])
    connections_list.append(token[3])
    token[0] = connections_list

def p_lsl1(token):
    '''
	lsl : s COMMA lsl
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lsl2(token):
    '''
	lsl : s SEMICOLON
	'''
    local_sensors_list = []
    local_sensors_list.append(token[1])
    token[0] = local_sensors_list

def p_lal1(token):
    '''
	lal : a COMMA lal
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lal2(token):
    '''
	lal : a SEMICOLON
	'''
    local_actuators_list = []
    local_actuators_list.append(token[1])
    token[0] = local_actuators_list

def p_lsg1(token):
    '''
	lsg : GLOBAL LBRACKET lsg1
	'''
    token[0] = token[3]

def p_lsg2(token):
    '''
	lsg1 : s COMMA lsg1
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lsg3(token):
    '''
	lsg1 : s RBRACKET SEMICOLON
	'''
    global_sensors_list = []
    global_sensors_list.append(token[1])
    token[0] = global_sensors_list

def p_lag1(token):
    '''
	lag : GLOBAL LBRACKET lag1
	'''
    token[0] = token[3]

def p_lag2(token):
    '''
	lag1 : a COMMA lag1
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lag3(token):
    '''
	lag1 : a RBRACKET SEMICOLON
	'''
    global_actuators_list = []
    global_actuators_list.append(token[1])
    token[0] = global_actuators_list

def p_s(token):
    '''
	s : spresencia
        | slluvia
        | siluminacion
        | sreloj
        | stemperatura
        | shumo
        | sviento
        | sintrusos
        | sgas
        | sinundacion
	'''
    token[0] = token[1]

def p_a(token):
    '''
	a : apuerta
        | acalefaccion
        | apersiana
        | aluz
        | aventana
        | afrio
        | agas 
        | atoldo
        | aalarma 
        | aemergencia 
	'''
    token[0] = token[1]

def p_c1(token):
    '''
	c : LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON
	'''
    token[0] = Behaviour(token[2], token[4], token[6])

def p_c2(token):
    '''
	c : LBRACKET lest SEMICOLON trans RBRACKET SEMICOLON
	'''
    # REVISAR, PUEDE NO FUNCIONAR
    initial_state = token[2][0]
    token[0] = Behaviour(token[2], initial_state, token[4])

def p_c3(token):
    '''
	c : LBRACKET lest SEMICOLON init SEMICOLON RBRACKET SEMICOLON
	'''
    token[0] = Behaviour(token[2], token[4])

def p_c4(token):
    '''
	c : LBRACKET lest SEMICOLON RBRACKET SEMICOLON
	'''
    token[0] = Behaviour(token[2])

def p_lest1(token):
    '''
	lest :  STATE ID LBRACKET lactions RBRACKET COMMA lest
	'''
    token[7].append(State(token[2], token[4]))
    token[0] = token[7]

def p_lest2(token):
    '''
	lest :  STATE ID LBRACKET RBRACKET COMMA lest
	'''
    token[6].append(State(token[2]))
    token[0] = token[6]

def p_lest3(token):
    '''
	lest :  STATE ID LBRACKET lactions RBRACKET
	'''
    states_list = []
    states_list.append(State(token[2], token[4]))
    token[0] = states_list

def p_lest4(token):
    '''
	lest :  STATE ID LBRACKET RBRACKET
	'''
    states_list = []
    states_list.append(State(token[2]))
    token[0] = states_list

def p_lactions1(token):
    '''
	lactions : action COMMA lactions
	'''
    token[3].append(token[1])
    token[0] = token[3]

def p_lactions2(token):
    '''
	lactions : action SEMICOLON
	'''
    actions_list = []
    actions_list.append(token[1])
    token[0] = actions_list

def p_action(token):
    '''
	action : ID SEQ BOOL
	'''
    value = False
    if(token[3].lower() == "true"):
        value = True
    token[0] = Action(token[1], value)

def p_init(token):
    '''
	init : INIT ID
	'''
    token[0] = token[2]

def p_trans1(token):
    '''
	trans : t trans
	'''
    token[2].append(token[1])
    token[0] = token[2]

def p_trans2(token):
    '''
	trans : t
	'''
    transitions_list = []
    transitions_list.append(token[1])
    token[0] = transitions_list

def p_t(token):
    '''
	t : ID COMMA ID COMMA COMBINATION SEMICOLON
	'''
    token[0] = Transition(token[5][::-1], token[1], token[3])

def p_spresencia(token):
    '''
	spresencia : SPRESENCIA ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorPresence(token[2], value)
    
def p_slluvia(token):
    '''
	slluvia : SLLUVIA ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorRain(token[2], value)

def p_siluminacion(token): 
    '''
	siluminacion : SILUMINACION OPL DOUBLE ID SEQ DOUBLE
	'''
    token[0] = SensorLight(token[4], float(token[3]), float(token[6]), token[2])

def p_stemperatura(token):
    '''
	stemperatura : STEMPERATURA OPL DOUBLE ID SEQ DOUBLE
	'''
    token[0] = SensorTemperature(token[4], float(token[3]), float(token[6]), token[2])

def p_sreloj(token):
    '''
	sreloj : SRELOJ OPL TIME ID SEQ TIME
	'''
    token[0] = SensorTime(token[4], token[3], token[6], token[2])

def p_shumo(token):
    '''
	shumo : SHUMO ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorSmoke(token[2], value)

def p_sviento(token):
    '''
	sviento : SVIENTO OPL DOUBLE ID SEQ DOUBLE
	'''
    token[0] = SensorWind(token[4], float(token[3]), float(token[6]), token[2])

def p_sintrusos(token):
    '''
	sintrusos : SINTRUSOS ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorIntruders(token[2],value)

def p_sinundacion(token):
    '''
	sinundacion : SINUNDACION ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorFlood(token[2], value)

def p_sgas(token):
    '''
	sgas : SGAS ID SEQ BOOL
	'''
    value = False
    if(token[4].lower() == "true"):
        value = True
    token[0] = SensorGas(token[2], value)

def p_apuerta(token):
    '''
	apuerta : APUERTA ID
	'''
    token[0] = ActuatorDoor(token[2], False)

def p_acalefaccion(token):
    '''
	acalefaccion : ACALEFACCION ID
	'''
    token[0] = ActuatorHeat(token[2], False)

def p_apersiana(token):
    '''
	apersiana : APERSIANA ID
	'''
    token[0] = ActuatorWindowBlind(token[2], False)

def p_aluz(token):
    '''
	aluz : ALUZ ID
	'''
    token[0] = ActuatorLight(token[2], False)

def p_aventana(token):
    '''
	aventana : AVENTANA ID
	'''
    token[0] = ActuatorWindow(token[2], False)

def p_frio(token):
    '''
	afrio : AFRIO ID
	'''
    token[0] = ActuatorCold(token[2], False)

def p_agas(token):
    '''
	agas : AGAS ID
	'''
    token[0] = ActuatorGas(token[2], False)

def p_atoldo(token):
    '''
	atoldo : ATOLDO ID
	'''
    token[0] = ActuatorAlarm(token[2], False)

def p_aalarma(token):
    '''
	aalarma : AALARMA ID
	'''
    token[0] = ActuatorAlarm(token[2], False)

def p_aemergencia(token):
    '''
	aemergencia : AEMERGENCIA ID
	'''
    token[0] = ActuatorEmergency(token[2], False)

def p_error(token):
    print(f'Syntax error at {token.value!r}')

def check_sensor_type(sensor, list):
    if isinstance(sensor, SensorPresence):
        list[0] = sensor.value
    elif isinstance(sensor, SensorRain):
        list[1] = sensor.value
    elif isinstance(sensor, SensorLight):
        list[2] = sensor.real_value
    elif isinstance(sensor, SensorTime):
        list[3] = sensor.real_value
    elif isinstance(sensor, SensorTemperature):
        list[4] = sensor.real_value
    elif isinstance(sensor, SensorSmoke):
        list[5] = sensor.value
    elif isinstance(sensor, SensorWind):
        list[6] = sensor.real_value
    elif isinstance(sensor, SensorGas):
        list[7] = sensor.value
    elif isinstance(sensor, SensorIntruders):
        list[8] = sensor.value
    elif isinstance(sensor, SensorFlood):
        list[9] = sensor.value
    print(list)

def main(file_name):
    ''' Main method '''
    ''' '''
    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return

    with open(file_name, 'r+', encoding = 'utf-8') as file:
        lexer = lex()
        parser = yacc()
        house = parser.parse(input = file.read(), lexer = lexer, debug = 1, tracking = 1)
        print(vars(house))
        counter = 1
        for room in house.room_list:
            print("Room nº " + str(counter))
            print("\tID: " + room.id)
            print("\tType: " + room.type)
            print("\tStates:")
            for state in room.states:
                print("\t\tID: " + str(state.id))
                print("\t\tActuators:")
                for action in state.actions:
                    print("\t\t\tActuator: " + str(action.actuator))
                    print("\t\t\tValue: " + str(action.value))
            print("\tAutomaton:")
            print("\t\tID: " + str(room.automaton.id))
            print("\t\tTransitions:")
            for transition in room.automaton.transitions:
                print("\t\t\tCombination: " + str(transition.combination))
                print("\t\t\tSource state: " + str(transition.source_state))
                print("\t\t\tTarget state: " + str(transition.target_state))
                print()
            print("\tSensors:")
            for sensor in room.sensors:
                print("\t\tID: " + str(sensor.identifier))
                print("\t\tType: " + str(type(sensor)))
                print("\t\tValue: " + str(sensor.value))
                print()
            print("\tActuators:")
            for actuator in room.actuators:
                print("\t\tID: " + str(actuator.identifier))
                print("\t\tType: " + str(type(actuator)))
                print("\t\tValue: : " + str(actuator.value))
            print()
            counter+=1
    return house
        #parser.parse('aabbabbbabbbcccc', lexer = lexer)

if __name__ == '__main__':
    main()