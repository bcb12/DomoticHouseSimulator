grammar DHSemanticGrammar;
import DHLexerRules;

@header {
from sensors import SensorPresence, SensorRain, SensorLight, SensorTemperature, SensorTime, SensorSmoke, SensorWind, SensorIntruders, SensorFlood, SensorGas
from actuators import ActuatorDoor, ActuatorHeat, ActuatorWindowBlind, ActuatorLight, ActuatorWindow, ActuatorCold, ActuatorGas, ActuatorSunBlind, ActuatorAlarm, ActuatorEmergency
from Action import Action
from Transition import Transition
from behaviour import Behaviour
from State import State
from House import House
from Room import Room
from Automaton import Automaton
from sensors import check_sensor_type
}

casa returns [House data]
  : HOUSE ID LBRACKET lh1=lh lp1=lp? lsg1=lsg? lag1=lag? RBRACKET SEMICOLON EOF 
  {
rooms = $lh1.list_rooms
rooms.extend($lp1.list_corridors)
$data = House($ID.text, rooms, ([] if $lsg1.text is None else $lsg1.list_sensors), ([] if $lsg1.text is None else $lag1.list_actuators))
  };

lh returns [List list_rooms]
  : h1=h COMMA lh1=lh {$list_rooms = $lh1.list_rooms + [$h1.data]}
  | h1=h SEMICOLON {$list_rooms = [$h1.data]} ;

h returns [Room data]
  : ROOM ID LBRACKET lsl1=lsl? lal1=lal? c1=c? RBRACKET 
  {
presence=rain=smoke=gas=intruders=flood = False
light_intensity=temperature=wind = 0.0
time = '00:00'
sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders,  flood]
if($lsl1.text is not None):
  for sensor in $lsl1.list_sensors:
    check_sensor_type(sensor, sensors)
transitions = []
initial_state = ""
if($c1.text is not None):
  transitions = $c1.comp.transitions

  for state in $c1.comp.states_list:
      if(state.id == $c1.comp.initial_state):
          initial_state = state
      for action in state.actions:
          for actuator in $lal1.list_actuators:
              if(action.actuator == actuator.identifier):
                  action.actuator = actuator

  if($lal1.text is not None):
    for actuator in $lal1.list_actuators:
        for action in initial_state.actions:
            if(action.actuator == actuator):
                actuator.value = action.value
automaton = Automaton("autom_"+$ID.text, (None if $c1.text is None else $c1.comp.initial_state), transitions)
$data = Room($ID.text, "H", (None if $c1.text is None else $c1.comp.states_list), automaton, sensors[0], sensors[1], sensors[2], 
sensors[3], sensors[4], sensors[5], sensors[6], sensors[7], sensors[8], sensors[9], 
([] if $lsl1.text is None else $lsl1.list_sensors), ([] if $lal1.text is None else $lal1.list_actuators), [])
  } ;

lp returns [List list_corridors]
  : pas=p COMMA corLs=lp {$list_corridors = $corLs.list_corridors + [$pas.data]}
  | pas=p SEMICOLON {$list_corridors = [$pas.data]};

p returns [Room data]
  : CORRIDOR ID LBRACKET l2id lsl1=lsl? lal1=lal? c1=c? RBRACKET
  {
presence=rain=smoke=gas=intruders=flood = False
light_intensity=temperature=wind = 0.0
time = '00:00'
sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders,  flood]
if($lsl1.text is not None):
  for sensor in $lsl1.list_sensors:
    check_sensor_type(sensor, sensors)
transitions = []
initial_state = ""
if($c1.text is not None):
  transitions = $c1.comp.transitions

  for state in $c1.comp.states_list:
      if(state.id == $c1.comp.initial_state):
          initial_state = state
      for action in state.actions:
          for actuator in $lal1.list_actuators:
              if(action.actuator == actuator.identifier):
                  action.actuator = actuator

  if($lal1.text is not None):
    for actuator in $lal1.list_actuators:
        for action in initial_state.actions:
            if(action.actuator == actuator):
                actuator.value = action.value

automaton = Automaton("autom_"+$ID.text, initial_state, transitions)
$data = Room($ID.text, "P", ([] if $c1.text is None else $c1.comp.states_list), automaton, sensors[0], sensors[1], sensors[2], 
sensors[3], sensors[4], sensors[5], sensors[6], sensors[7], sensors[8], sensors[9], 
([] if $lsl1.text is None else $lsl1.list_sensors), ([] if $lal1.text is None else $lal1.list_actuators), $l2id.list_l2id)
  } ;

l2id returns [List list_l2id]
  : ID COMMA l2id1=l2id {$list_l2id = $l2id1.list_l2id + [$ID.text]}
  | id1=ID COMMA id2=ID SEMICOLON {$list_l2id = [$id1.text, $id2.text]}
  ;

c returns [Comportamiento comp]
  : LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON
  {$comp = Behaviour($lest.list_states, $init.state, $trans.list_trans)};

lest returns [List list_states]
  : STATE ID LBRACKET lac1=lactions RBRACKET COMMA lest1=lest 
  {state = State($ID.text, $lac1.list_actions)
$list_states = $lest1.list_states + [state] }
  | STATE ID LBRACKET lac1=lactions RBRACKET 
  {state = State($ID.text, $lac1.list_actions)
$list_states = [state] }
  ;

lactions returns [List list_actions]
  : a1=action COMMA lactions1=lactions {$list_actions = $lactions1.list_actions + [$a1.act]}
  | a1=action SEMICOLON {$list_actions = [$a1.act]}
  ;

action returns [Action act]
  : ID SEQ BOOL {
value = False
if $BOOL.text == 'true':
    value = True
$act= Action($ID.text, value)
  } ;

init returns [string state]
  : INIT ID {$state = $ID.text}
  ;

trans returns [List list_trans]
  : t1=t tr1=trans {$list_trans = $tr1.list_trans + [$t1.tran]}
  | t1=t {$list_trans = [$t1.tran]} 
  ;

t returns [Transicion tran]
  : src=ID COMMA dest=ID COMMA comb=COMBINATION SEMICOLON {$tran=Transition($comb.text, $src.text, $dest.text)};

lsl returns [List list_sensors]
  : s1=s COMMA lsl1=lsl {$list_sensors = [$s1.data] + $lsl1.list_sensors}
  | s1=s SEMICOLON {$list_sensors = [$s1.data]}
  ; 

lal returns [List list_actuators]
  : a1=a COMMA lal1=lal {$list_actuators = [$a1.data] + $lal1.list_actuators}
  | a1=a SEMICOLON {$list_actuators = [$a1.data]}
  ;

lsg returns [List list_sensors]
  : GLOBAL LBRACKET lsg1=lsg RBRACKET SEMICOLON {$list_sensors = $lsg1.list_sensors}
  | s1=s COMMA lsg1=lsg {$list_sensors = [$s1.data] + $lsg1.list_sensors}
  | s1=s {$list_sensors = [$s1.data]}
  ;

lag returns [List list_actuators]
  : GLOBAL LBRACKET lag1=lag RBRACKET SEMICOLON {$list_actuators=$lag1.list_actuators}
  | a1=a COMMA lag1=lag {$list_actuators = [$a1.data] + $lag1.list_actuators}
  | a1=a {$list_actuators = [$a1.data]}
  ;

s returns [Sensor data]
  : spresencia    {$data = $spresencia.data}
  | slluvia       {$data = $slluvia.data}
  | siluminacion  {$data = $siluminacion.data}
  | sreloj        {$data = $sreloj.data}
  | stemperatura  {$data = $stemperatura.data}
  | shumo         {$data = $shumo.data}
  | sviento       {$data = $sviento.data}
  | sintrusos     {$data = $sintrusos.data}
  | sgas          {$data = $sgas.data}
  | sinundacion   {$data = $sinundacion.data}
  ;

a returns [string data]
  : apuerta             {$data = $apuerta.data}
  | acalefaccion        {$data = $acalefaccion.data}
  | apersiana           {$data = $apersiana.data}
  | aluz                {$data = $aluz.data}
  | aventana            {$data = $aventana.data}
  | afrio               {$data = $afrio.data}
  | agas                {$data = $agas.data}
  | atoldo              {$data = $atoldo.data}
  | aalarma             {$data = $aalarma.data}
  | aemergencia         {$data = $aemergencia.data}
  ;

spresencia returns [Sensor data]
  : SPRESENCIA ID SEQ BOOL
  {
id = $ID.text
val = False
if($BOOL.text == "true"):
  val = True
$data = SensorPresence(id, val)
  } ;

slluvia returns [Sensor data]
  : SLLUVIA id1=ID SEQ t1=BOOL 
  {
id = $id1.text
val = False
if($t1.text == "true"):
  val = True
$data = SensorRain(id, val)
  } ;

shumo returns [Sensor data]
  : SHUMO ID SEQ BOOL 
  {
id = $ID.text
val = False
if($BOOL.text == "true"):
  val = True
$data = SensorSmoke(id, val)
  } ;

sintrusos returns [Sensor data]
  : SINTRUSOS ID SEQ BOOL 
  {
id = $ID.text
val = False
if($BOOL.text == "true"):
  val = True
$data = SensorIntruders(id, val)
  } ;

sinundacion returns [Sensor data]
  : SINUNDACION ID SEQ BOOL 
  {
id = $ID.text
val = False
if($BOOL.text == "true"):
  val = True
$data = SensorFlood(id, val)
  } ;

sgas returns [Sensor data]
  : SGAS ID SEQ BOOL 
  {
id = $ID.text
val = False
if($BOOL.text == "true"):
  val = True
$data = SensorGas(id, val)
  } ;

siluminacion returns [Sensor data]
  : SILUMINACION OPL db1=DOUBLE ID SEQ db2=DOUBLE 
  {
operator = $OPL.text
id = $ID.text
real_value = float($db2.text)
comp_value = float($db1.text)
$data = SensorLight(id, comp_value, real_value, operator)
  } ;

stemperatura returns [Sensor data]
  : STEMPERATURA OPL db1=DOUBLE ID SEQ db2=DOUBLE 
  {
operator = $OPL.text
id = $ID.text
real_value = float($db2.text)
comp_value = float($db1.text)
$data = SensorTemperature(id, comp_value, real_value, operator)
  } ;

sviento returns [Sensor data]
  : SVIENTO OPL db1=DOUBLE ID SEQ db2=DOUBLE 
  {
operator = $OPL.text
id = $ID.text
real_value = float($db2.text)
comp_value = float($db1.text)
$data = SensorWind(id, comp_value, real_value, operator)
  } ;

sreloj returns [Sensor data]
  : SRELOJ OPL t1=TIME ID SEQ t2=TIME 
  {
operator = $OPL.text
id = $ID.text
real_value = $t2.text
comp_value = $t1.text
$data = SensorTime(id, comp_value, real_value, operator)
  } ;

apuerta returns [Actuator data]
  : APUERTA ID {
id = $ID.text
$data = ActuatorDoor(id, False)
  } ;
acalefaccion returns [Actuator data]
  : ACALEFACCION ID {
id = $ID.text
$data = ActuatorHeat(id, False)
  } ;
apersiana returns [Actuator data]
  : APERSIANA ID {
id = $ID.text
$data = ActuatorWindowBlind(id, False)
  } ;
aluz returns [Actuator data]
  : ALUZ ID {
id = $ID.text
$data = ActuatorLight(id, False)
  } ;
aventana returns [Actuator data]
  : AVENTANA ID {
id = $ID.text
$data = ActuatorWindow(id, False)
  } ;
afrio returns [Actuator data]
  : AFRIO ID {
id = $ID.text
$data = ActuatorCold(id, False)
  } ;
agas returns [Actuator data]
  : AGAS ID {
id = $ID.text
$data = ActuatorGas(id, False)
  } ;
atoldo returns [Actuator data]
  : ATOLDO ID {
id = $ID.text
$data = ActuatorSunBlind(id, False)
  } ;
aalarma returns [Actuator data]
  : AALARMA ID {
id = $ID.text
$data = ActuatorAlarm(id, False)
  } ;
aemergencia returns [Actuator data]
  : AEMERGENCIA ID {
id = $ID.text
$data = ActuatorEmergency(id, False)
  } ;
