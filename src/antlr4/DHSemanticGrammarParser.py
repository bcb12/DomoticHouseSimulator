# Generated from DHSemanticGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


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

def serializedATN():
    return [
        4,1,39,455,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,1,0,1,0,3,0,84,8,0,1,0,3,0,87,8,0,1,0,3,0,90,8,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,106,8,1,1,2,1,2,1,
        2,1,2,3,2,112,8,2,1,2,3,2,115,8,2,1,2,3,2,118,8,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,132,8,3,1,4,1,4,1,4,1,4,1,
        4,3,4,139,8,4,1,4,3,4,142,8,4,1,4,3,4,145,8,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,160,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,188,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,199,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,3,11,217,8,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,236,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,247,
        8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,264,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,281,8,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,3,17,313,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,345,8,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,0,0,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,0,0,454,0,78,1,0,0,0,2,105,1,0,0,0,4,107,1,0,0,0,6,131,
        1,0,0,0,8,133,1,0,0,0,10,159,1,0,0,0,12,161,1,0,0,0,14,187,1,0,0,
        0,16,198,1,0,0,0,18,200,1,0,0,0,20,205,1,0,0,0,22,216,1,0,0,0,24,
        218,1,0,0,0,26,235,1,0,0,0,28,246,1,0,0,0,30,263,1,0,0,0,32,280,
        1,0,0,0,34,312,1,0,0,0,36,344,1,0,0,0,38,346,1,0,0,0,40,352,1,0,
        0,0,42,358,1,0,0,0,44,364,1,0,0,0,46,370,1,0,0,0,48,376,1,0,0,0,
        50,382,1,0,0,0,52,390,1,0,0,0,54,398,1,0,0,0,56,406,1,0,0,0,58,414,
        1,0,0,0,60,418,1,0,0,0,62,422,1,0,0,0,64,426,1,0,0,0,66,430,1,0,
        0,0,68,434,1,0,0,0,70,438,1,0,0,0,72,442,1,0,0,0,74,446,1,0,0,0,
        76,450,1,0,0,0,78,79,5,22,0,0,79,80,5,29,0,0,80,81,5,35,0,0,81,83,
        3,2,1,0,82,84,3,6,3,0,83,82,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,
        85,87,3,30,15,0,86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,90,
        3,32,16,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,36,0,
        0,92,93,5,34,0,0,93,94,5,0,0,1,94,95,6,0,-1,0,95,1,1,0,0,0,96,97,
        3,4,2,0,97,98,5,37,0,0,98,99,3,2,1,0,99,100,6,1,-1,0,100,106,1,0,
        0,0,101,102,3,4,2,0,102,103,5,34,0,0,103,104,6,1,-1,0,104,106,1,
        0,0,0,105,96,1,0,0,0,105,101,1,0,0,0,106,3,1,0,0,0,107,108,5,21,
        0,0,108,109,5,29,0,0,109,111,5,35,0,0,110,112,3,26,13,0,111,110,
        1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,115,3,28,14,0,114,113,
        1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,118,3,12,6,0,117,116,
        1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,120,5,36,0,0,120,121,
        6,2,-1,0,121,5,1,0,0,0,122,123,3,8,4,0,123,124,5,37,0,0,124,125,
        3,6,3,0,125,126,6,3,-1,0,126,132,1,0,0,0,127,128,3,8,4,0,128,129,
        5,34,0,0,129,130,6,3,-1,0,130,132,1,0,0,0,131,122,1,0,0,0,131,127,
        1,0,0,0,132,7,1,0,0,0,133,134,5,23,0,0,134,135,5,29,0,0,135,136,
        5,35,0,0,136,138,3,10,5,0,137,139,3,26,13,0,138,137,1,0,0,0,138,
        139,1,0,0,0,139,141,1,0,0,0,140,142,3,28,14,0,141,140,1,0,0,0,141,
        142,1,0,0,0,142,144,1,0,0,0,143,145,3,12,6,0,144,143,1,0,0,0,144,
        145,1,0,0,0,145,146,1,0,0,0,146,147,5,36,0,0,147,148,6,4,-1,0,148,
        9,1,0,0,0,149,150,5,29,0,0,150,151,5,37,0,0,151,152,3,10,5,0,152,
        153,6,5,-1,0,153,160,1,0,0,0,154,155,5,29,0,0,155,156,5,37,0,0,156,
        157,5,29,0,0,157,158,5,34,0,0,158,160,6,5,-1,0,159,149,1,0,0,0,159,
        154,1,0,0,0,160,11,1,0,0,0,161,162,5,35,0,0,162,163,3,14,7,0,163,
        164,5,34,0,0,164,165,3,20,10,0,165,166,5,34,0,0,166,167,3,22,11,
        0,167,168,5,36,0,0,168,169,5,34,0,0,169,170,6,6,-1,0,170,13,1,0,
        0,0,171,172,5,25,0,0,172,173,5,29,0,0,173,174,5,35,0,0,174,175,3,
        16,8,0,175,176,5,36,0,0,176,177,5,37,0,0,177,178,3,14,7,0,178,179,
        6,7,-1,0,179,188,1,0,0,0,180,181,5,25,0,0,181,182,5,29,0,0,182,183,
        5,35,0,0,183,184,3,16,8,0,184,185,5,36,0,0,185,186,6,7,-1,0,186,
        188,1,0,0,0,187,171,1,0,0,0,187,180,1,0,0,0,188,15,1,0,0,0,189,190,
        3,18,9,0,190,191,5,37,0,0,191,192,3,16,8,0,192,193,6,8,-1,0,193,
        199,1,0,0,0,194,195,3,18,9,0,195,196,5,34,0,0,196,197,6,8,-1,0,197,
        199,1,0,0,0,198,189,1,0,0,0,198,194,1,0,0,0,199,17,1,0,0,0,200,201,
        5,29,0,0,201,202,5,33,0,0,202,203,5,28,0,0,203,204,6,9,-1,0,204,
        19,1,0,0,0,205,206,5,26,0,0,206,207,5,29,0,0,207,208,6,10,-1,0,208,
        21,1,0,0,0,209,210,3,24,12,0,210,211,3,22,11,0,211,212,6,11,-1,0,
        212,217,1,0,0,0,213,214,3,24,12,0,214,215,6,11,-1,0,215,217,1,0,
        0,0,216,209,1,0,0,0,216,213,1,0,0,0,217,23,1,0,0,0,218,219,5,29,
        0,0,219,220,5,37,0,0,220,221,5,29,0,0,221,222,5,37,0,0,222,223,5,
        32,0,0,223,224,5,34,0,0,224,225,6,12,-1,0,225,25,1,0,0,0,226,227,
        3,34,17,0,227,228,5,37,0,0,228,229,3,26,13,0,229,230,6,13,-1,0,230,
        236,1,0,0,0,231,232,3,34,17,0,232,233,5,34,0,0,233,234,6,13,-1,0,
        234,236,1,0,0,0,235,226,1,0,0,0,235,231,1,0,0,0,236,27,1,0,0,0,237,
        238,3,36,18,0,238,239,5,37,0,0,239,240,3,28,14,0,240,241,6,14,-1,
        0,241,247,1,0,0,0,242,243,3,36,18,0,243,244,5,34,0,0,244,245,6,14,
        -1,0,245,247,1,0,0,0,246,237,1,0,0,0,246,242,1,0,0,0,247,29,1,0,
        0,0,248,249,5,24,0,0,249,250,5,35,0,0,250,251,3,30,15,0,251,252,
        5,36,0,0,252,253,5,34,0,0,253,254,6,15,-1,0,254,264,1,0,0,0,255,
        256,3,34,17,0,256,257,5,37,0,0,257,258,3,30,15,0,258,259,6,15,-1,
        0,259,264,1,0,0,0,260,261,3,34,17,0,261,262,6,15,-1,0,262,264,1,
        0,0,0,263,248,1,0,0,0,263,255,1,0,0,0,263,260,1,0,0,0,264,31,1,0,
        0,0,265,266,5,24,0,0,266,267,5,35,0,0,267,268,3,32,16,0,268,269,
        5,36,0,0,269,270,5,34,0,0,270,271,6,16,-1,0,271,281,1,0,0,0,272,
        273,3,36,18,0,273,274,5,37,0,0,274,275,3,32,16,0,275,276,6,16,-1,
        0,276,281,1,0,0,0,277,278,3,36,18,0,278,279,6,16,-1,0,279,281,1,
        0,0,0,280,265,1,0,0,0,280,272,1,0,0,0,280,277,1,0,0,0,281,33,1,0,
        0,0,282,283,3,38,19,0,283,284,6,17,-1,0,284,313,1,0,0,0,285,286,
        3,40,20,0,286,287,6,17,-1,0,287,313,1,0,0,0,288,289,3,50,25,0,289,
        290,6,17,-1,0,290,313,1,0,0,0,291,292,3,56,28,0,292,293,6,17,-1,
        0,293,313,1,0,0,0,294,295,3,52,26,0,295,296,6,17,-1,0,296,313,1,
        0,0,0,297,298,3,42,21,0,298,299,6,17,-1,0,299,313,1,0,0,0,300,301,
        3,54,27,0,301,302,6,17,-1,0,302,313,1,0,0,0,303,304,3,44,22,0,304,
        305,6,17,-1,0,305,313,1,0,0,0,306,307,3,48,24,0,307,308,6,17,-1,
        0,308,313,1,0,0,0,309,310,3,46,23,0,310,311,6,17,-1,0,311,313,1,
        0,0,0,312,282,1,0,0,0,312,285,1,0,0,0,312,288,1,0,0,0,312,291,1,
        0,0,0,312,294,1,0,0,0,312,297,1,0,0,0,312,300,1,0,0,0,312,303,1,
        0,0,0,312,306,1,0,0,0,312,309,1,0,0,0,313,35,1,0,0,0,314,315,3,58,
        29,0,315,316,6,18,-1,0,316,345,1,0,0,0,317,318,3,60,30,0,318,319,
        6,18,-1,0,319,345,1,0,0,0,320,321,3,62,31,0,321,322,6,18,-1,0,322,
        345,1,0,0,0,323,324,3,64,32,0,324,325,6,18,-1,0,325,345,1,0,0,0,
        326,327,3,66,33,0,327,328,6,18,-1,0,328,345,1,0,0,0,329,330,3,68,
        34,0,330,331,6,18,-1,0,331,345,1,0,0,0,332,333,3,70,35,0,333,334,
        6,18,-1,0,334,345,1,0,0,0,335,336,3,72,36,0,336,337,6,18,-1,0,337,
        345,1,0,0,0,338,339,3,74,37,0,339,340,6,18,-1,0,340,345,1,0,0,0,
        341,342,3,76,38,0,342,343,6,18,-1,0,343,345,1,0,0,0,344,314,1,0,
        0,0,344,317,1,0,0,0,344,320,1,0,0,0,344,323,1,0,0,0,344,326,1,0,
        0,0,344,329,1,0,0,0,344,332,1,0,0,0,344,335,1,0,0,0,344,338,1,0,
        0,0,344,341,1,0,0,0,345,37,1,0,0,0,346,347,5,1,0,0,347,348,5,29,
        0,0,348,349,5,33,0,0,349,350,5,28,0,0,350,351,6,19,-1,0,351,39,1,
        0,0,0,352,353,5,2,0,0,353,354,5,29,0,0,354,355,5,33,0,0,355,356,
        5,28,0,0,356,357,6,20,-1,0,357,41,1,0,0,0,358,359,5,6,0,0,359,360,
        5,29,0,0,360,361,5,33,0,0,361,362,5,28,0,0,362,363,6,21,-1,0,363,
        43,1,0,0,0,364,365,5,9,0,0,365,366,5,29,0,0,366,367,5,33,0,0,367,
        368,5,28,0,0,368,369,6,22,-1,0,369,45,1,0,0,0,370,371,5,10,0,0,371,
        372,5,29,0,0,372,373,5,33,0,0,373,374,5,28,0,0,374,375,6,23,-1,0,
        375,47,1,0,0,0,376,377,5,7,0,0,377,378,5,29,0,0,378,379,5,33,0,0,
        379,380,5,28,0,0,380,381,6,24,-1,0,381,49,1,0,0,0,382,383,5,3,0,
        0,383,384,5,27,0,0,384,385,5,30,0,0,385,386,5,29,0,0,386,387,5,33,
        0,0,387,388,5,30,0,0,388,389,6,25,-1,0,389,51,1,0,0,0,390,391,5,
        4,0,0,391,392,5,27,0,0,392,393,5,30,0,0,393,394,5,29,0,0,394,395,
        5,33,0,0,395,396,5,30,0,0,396,397,6,26,-1,0,397,53,1,0,0,0,398,399,
        5,8,0,0,399,400,5,27,0,0,400,401,5,30,0,0,401,402,5,29,0,0,402,403,
        5,33,0,0,403,404,5,30,0,0,404,405,6,27,-1,0,405,55,1,0,0,0,406,407,
        5,5,0,0,407,408,5,27,0,0,408,409,5,31,0,0,409,410,5,29,0,0,410,411,
        5,33,0,0,411,412,5,31,0,0,412,413,6,28,-1,0,413,57,1,0,0,0,414,415,
        5,11,0,0,415,416,5,29,0,0,416,417,6,29,-1,0,417,59,1,0,0,0,418,419,
        5,12,0,0,419,420,5,29,0,0,420,421,6,30,-1,0,421,61,1,0,0,0,422,423,
        5,13,0,0,423,424,5,29,0,0,424,425,6,31,-1,0,425,63,1,0,0,0,426,427,
        5,14,0,0,427,428,5,29,0,0,428,429,6,32,-1,0,429,65,1,0,0,0,430,431,
        5,15,0,0,431,432,5,29,0,0,432,433,6,33,-1,0,433,67,1,0,0,0,434,435,
        5,16,0,0,435,436,5,29,0,0,436,437,6,34,-1,0,437,69,1,0,0,0,438,439,
        5,17,0,0,439,440,5,29,0,0,440,441,6,35,-1,0,441,71,1,0,0,0,442,443,
        5,18,0,0,443,444,5,29,0,0,444,445,6,36,-1,0,445,73,1,0,0,0,446,447,
        5,19,0,0,447,448,5,29,0,0,448,449,6,37,-1,0,449,75,1,0,0,0,450,451,
        5,20,0,0,451,452,5,29,0,0,452,453,6,38,-1,0,453,77,1,0,0,0,21,83,
        86,89,105,111,114,117,131,138,141,144,159,187,198,216,235,246,263,
        280,312,344
    ]

class DHSemanticGrammarParser ( Parser ):

    grammarFileName = "DHSemanticGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sensor_presence'", "'sensor_rain'", 
                     "'sensor_light'", "'sensor_temperature'", "'sensor_time'", 
                     "'sensor_smoke'", "'sensor_gas'", "'sensor_wind'", 
                     "'sensor_intruder'", "'sensor_flood'", "'actuator_door'", 
                     "'actuator_heat'", "'actuator_wblind'", "'actuator_light'", 
                     "'actuator_window'", "'actuator_cold'", "'actuator_gas'", 
                     "'actuator_wind'", "'actuator_alarm'", "'actuator_emergency'", 
                     "'room'", "'house'", "'corridor'", "'global'", "'state'", 
                     "'init'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':='", "';'", "'{'", "'}'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "SPRESENCIA", "SLLUVIA", "SILUMINACION", 
                      "STEMPERATURA", "SRELOJ", "SHUMO", "SGAS", "SVIENTO", 
                      "SINTRUSOS", "SINUNDACION", "APUERTA", "ACALEFACCION", 
                      "APERSIANA", "ALUZ", "AVENTANA", "AFRIO", "AGAS", 
                      "ATOLDO", "AALARMA", "AEMERGENCIA", "ROOM", "HOUSE", 
                      "CORRIDOR", "GLOBAL", "STATE", "INIT", "OPL", "BOOL", 
                      "ID", "DOUBLE", "TIME", "COMBINATION", "SEQ", "SEMICOLON", 
                      "LBRACKET", "RBRACKET", "COMMA", "SPACE", "COMMENT" ]

    RULE_casa = 0
    RULE_lh = 1
    RULE_h = 2
    RULE_lp = 3
    RULE_p = 4
    RULE_l2id = 5
    RULE_c = 6
    RULE_lest = 7
    RULE_lactions = 8
    RULE_action = 9
    RULE_init = 10
    RULE_trans = 11
    RULE_t = 12
    RULE_lsl = 13
    RULE_lal = 14
    RULE_lsg = 15
    RULE_lag = 16
    RULE_s = 17
    RULE_a = 18
    RULE_spresencia = 19
    RULE_slluvia = 20
    RULE_shumo = 21
    RULE_sintrusos = 22
    RULE_sinundacion = 23
    RULE_sgas = 24
    RULE_siluminacion = 25
    RULE_stemperatura = 26
    RULE_sviento = 27
    RULE_sreloj = 28
    RULE_apuerta = 29
    RULE_acalefaccion = 30
    RULE_apersiana = 31
    RULE_aluz = 32
    RULE_aventana = 33
    RULE_afrio = 34
    RULE_agas = 35
    RULE_atoldo = 36
    RULE_aalarma = 37
    RULE_aemergencia = 38

    ruleNames =  [ "casa", "lh", "h", "lp", "p", "l2id", "c", "lest", "lactions", 
                   "action", "init", "trans", "t", "lsl", "lal", "lsg", 
                   "lag", "s", "a", "spresencia", "slluvia", "shumo", "sintrusos", 
                   "sinundacion", "sgas", "siluminacion", "stemperatura", 
                   "sviento", "sreloj", "apuerta", "acalefaccion", "apersiana", 
                   "aluz", "aventana", "afrio", "agas", "atoldo", "aalarma", 
                   "aemergencia" ]

    EOF = Token.EOF
    SPRESENCIA=1
    SLLUVIA=2
    SILUMINACION=3
    STEMPERATURA=4
    SRELOJ=5
    SHUMO=6
    SGAS=7
    SVIENTO=8
    SINTRUSOS=9
    SINUNDACION=10
    APUERTA=11
    ACALEFACCION=12
    APERSIANA=13
    ALUZ=14
    AVENTANA=15
    AFRIO=16
    AGAS=17
    ATOLDO=18
    AALARMA=19
    AEMERGENCIA=20
    ROOM=21
    HOUSE=22
    CORRIDOR=23
    GLOBAL=24
    STATE=25
    INIT=26
    OPL=27
    BOOL=28
    ID=29
    DOUBLE=30
    TIME=31
    COMBINATION=32
    SEQ=33
    SEMICOLON=34
    LBRACKET=35
    RBRACKET=36
    COMMA=37
    SPACE=38
    COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CasaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self.lh1 = None # LhContext
            self.lp1 = None # LpContext
            self.lsg1 = None # LsgContext
            self.lag1 = None # LagContext

        def HOUSE(self):
            return self.getToken(DHSemanticGrammarParser.HOUSE, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def EOF(self):
            return self.getToken(DHSemanticGrammarParser.EOF, 0)

        def lh(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LhContext,0)


        def lp(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LpContext,0)


        def lsg(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LsgContext,0)


        def lag(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LagContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_casa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasa" ):
                listener.enterCasa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasa" ):
                listener.exitCasa(self)




    def casa(self):

        localctx = DHSemanticGrammarParser.CasaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_casa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(DHSemanticGrammarParser.HOUSE)
            self.state = 79
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 80
            self.match(DHSemanticGrammarParser.LBRACKET)
            self.state = 81
            localctx.lh1 = self.lh()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 82
                localctx.lp1 = self.lp()


            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 85
                localctx.lsg1 = self.lsg()


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 18872320) != 0:
                self.state = 88
                localctx.lag1 = self.lag()


            self.state = 91
            self.match(DHSemanticGrammarParser.RBRACKET)
            self.state = 92
            self.match(DHSemanticGrammarParser.SEMICOLON)
            self.state = 93
            self.match(DHSemanticGrammarParser.EOF)

            rooms = localctx.lh1.list_rooms
            rooms.extend(localctx.lp1.list_corridors)
            localctx.data = House((None if localctx._ID is None else localctx._ID.text), rooms, ([] if (None if localctx.lsg1 is None else self._input.getText(localctx.lsg1.start,localctx.lsg1.stop)) is None else localctx.lsg1.list_sensors), ([] if (None if localctx.lsg1 is None else self._input.getText(localctx.lsg1.start,localctx.lsg1.stop)) is None else localctx.lag1.list_actuators))
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_rooms = None
            self.h1 = None # HContext
            self.lh1 = None # LhContext

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def h(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.HContext,0)


        def lh(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LhContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lh

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLh" ):
                listener.enterLh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLh" ):
                listener.exitLh(self)




    def lh(self):

        localctx = DHSemanticGrammarParser.LhContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lh)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                localctx.h1 = self.h()
                self.state = 97
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 98
                localctx.lh1 = self.lh()
                localctx.list_rooms = localctx.lh1.list_rooms + [localctx.h1.data]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                localctx.h1 = self.h()
                self.state = 102
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_rooms = [localctx.h1.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self.lsl1 = None # LslContext
            self.lal1 = None # LalContext
            self.c1 = None # CContext

        def ROOM(self):
            return self.getToken(DHSemanticGrammarParser.ROOM, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def lsl(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LslContext,0)


        def lal(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LalContext,0)


        def c(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.CContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_h

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH" ):
                listener.enterH(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH" ):
                listener.exitH(self)




    def h(self):

        localctx = DHSemanticGrammarParser.HContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_h)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(DHSemanticGrammarParser.ROOM)
            self.state = 108
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 109
            self.match(DHSemanticGrammarParser.LBRACKET)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0:
                self.state = 110
                localctx.lsl1 = self.lsl()


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2095104) != 0:
                self.state = 113
                localctx.lal1 = self.lal()


            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 116
                localctx.c1 = self.c()


            self.state = 119
            self.match(DHSemanticGrammarParser.RBRACKET)

            presence=rain=smoke=gas=intruders=flood = False
            light_intensity=temperature=wind = 0.0
            time = '00:00'
            sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders,  flood]
            if((None if localctx.lsl1 is None else self._input.getText(localctx.lsl1.start,localctx.lsl1.stop)) is not None):
              for sensor in localctx.lsl1.list_sensors:
                check_sensor_type(sensor, sensors)
            transitions = []
            initial_state = ""
            if((None if localctx.c1 is None else self._input.getText(localctx.c1.start,localctx.c1.stop)) is not None):
              transitions = localctx.c1.comp.transitions

              for state in localctx.c1.comp.states_list:
                  if(state.id == localctx.c1.comp.initial_state):
                      initial_state = state
                  for action in state.actions:
                      for actuator in localctx.lal1.list_actuators:
                          if(action.actuator == actuator.identifier):
                              action.actuator = actuator

              if((None if localctx.lal1 is None else self._input.getText(localctx.lal1.start,localctx.lal1.stop)) is not None):
                for actuator in localctx.lal1.list_actuators:
                    for action in initial_state.actions:
                        if(action.actuator == actuator):
                            actuator.value = action.value
            automaton = Automaton("autom_"+(None if localctx._ID is None else localctx._ID.text), initial_state, transitions)
            localctx.data = Room((None if localctx._ID is None else localctx._ID.text), "H", (None if (None if localctx.c1 is None else self._input.getText(localctx.c1.start,localctx.c1.stop)) is None else localctx.c1.comp.states_list), automaton, sensors[0], sensors[1], sensors[2], 
            sensors[3], sensors[4], sensors[5], sensors[6], sensors[7], sensors[8], sensors[9], 
            ([] if (None if localctx.lsl1 is None else self._input.getText(localctx.lsl1.start,localctx.lsl1.stop)) is None else localctx.lsl1.list_sensors), ([] if (None if localctx.lal1 is None else self._input.getText(localctx.lal1.start,localctx.lal1.stop)) is None else localctx.lal1.list_actuators), [])
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_corridors = None
            self.pas = None # PContext
            self.corLs = None # LpContext

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def p(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.PContext,0)


        def lp(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LpContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLp" ):
                listener.enterLp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLp" ):
                listener.exitLp(self)




    def lp(self):

        localctx = DHSemanticGrammarParser.LpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lp)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                localctx.pas = self.p()
                self.state = 123
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 124
                localctx.corLs = self.lp()
                localctx.list_corridors = localctx.corLs.list_corridors + [localctx.pas.data]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                localctx.pas = self.p()
                self.state = 128
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_corridors = [localctx.pas.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._l2id = None # L2idContext
            self.lsl1 = None # LslContext
            self.lal1 = None # LalContext
            self.c1 = None # CContext

        def CORRIDOR(self):
            return self.getToken(DHSemanticGrammarParser.CORRIDOR, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def l2id(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.L2idContext,0)


        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def lsl(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LslContext,0)


        def lal(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LalContext,0)


        def c(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.CContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP" ):
                listener.enterP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP" ):
                listener.exitP(self)




    def p(self):

        localctx = DHSemanticGrammarParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(DHSemanticGrammarParser.CORRIDOR)
            self.state = 134
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 135
            self.match(DHSemanticGrammarParser.LBRACKET)
            self.state = 136
            localctx._l2id = self.l2id()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0:
                self.state = 137
                localctx.lsl1 = self.lsl()


            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2095104) != 0:
                self.state = 140
                localctx.lal1 = self.lal()


            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 143
                localctx.c1 = self.c()


            self.state = 146
            self.match(DHSemanticGrammarParser.RBRACKET)

            presence=rain=smoke=gas=intruders=flood = False
            light_intensity=temperature=wind = 0.0
            time = '00:00'
            sensors = [presence, rain, light_intensity, time, temperature, smoke, wind, gas, intruders,  flood]
            if((None if localctx.lsl1 is None else self._input.getText(localctx.lsl1.start,localctx.lsl1.stop)) is not None):
              for sensor in localctx.lsl1.list_sensors:
                check_sensor_type(sensor, sensors)
            transitions = []
            initial_state = ""
            if((None if localctx.c1 is None else self._input.getText(localctx.c1.start,localctx.c1.stop)) is not None):
              transitions = localctx.c1.comp.transitions

              for state in localctx.c1.comp.states_list:
                  if(state.id == localctx.c1.comp.initial_state):
                      initial_state = state
                  for action in state.actions:
                      for actuator in localctx.lal1.list_actuators:
                          if(action.actuator == actuator.identifier):
                              action.actuator = actuator

              if((None if localctx.lal1 is None else self._input.getText(localctx.lal1.start,localctx.lal1.stop)) is not None):
                for actuator in localctx.lal1.list_actuators:
                    for action in initial_state.actions:
                        if(action.actuator == actuator):
                            actuator.value = action.value

            automaton = Automaton("autom_"+(None if localctx._ID is None else localctx._ID.text), initial_state, transitions)
            localctx.data = Room((None if localctx._ID is None else localctx._ID.text), "P", ([] if (None if localctx.c1 is None else self._input.getText(localctx.c1.start,localctx.c1.stop)) is None else localctx.c1.comp.states_list), automaton, sensors[0], sensors[1], sensors[2], 
            sensors[3], sensors[4], sensors[5], sensors[6], sensors[7], sensors[8], sensors[9], 
            ([] if (None if localctx.lsl1 is None else self._input.getText(localctx.lsl1.start,localctx.lsl1.stop)) is None else localctx.lsl1.list_sensors), ([] if (None if localctx.lal1 is None else self._input.getText(localctx.lal1.start,localctx.lal1.stop)) is None else localctx.lal1.list_actuators), localctx._l2id.list_l2id)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class L2idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_l2id = None
            self._ID = None # Token
            self.l2id1 = None # L2idContext
            self.id1 = None # Token
            self.id2 = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.ID)
            else:
                return self.getToken(DHSemanticGrammarParser.ID, i)

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def l2id(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.L2idContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_l2id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL2id" ):
                listener.enterL2id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL2id" ):
                listener.exitL2id(self)




    def l2id(self):

        localctx = DHSemanticGrammarParser.L2idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_l2id)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                localctx._ID = self.match(DHSemanticGrammarParser.ID)
                self.state = 150
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 151
                localctx.l2id1 = self.l2id()
                localctx.list_l2id = localctx.l2id1.list_l2id + [(None if localctx._ID is None else localctx._ID.text)]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                localctx.id1 = self.match(DHSemanticGrammarParser.ID)
                self.state = 155
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 156
                localctx.id2 = self.match(DHSemanticGrammarParser.ID)
                self.state = 157
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_l2id = [(None if localctx.id2 is None else localctx.id2.text), (None if localctx.id1 is None else localctx.id1.text)]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.comp = None
            self._lest = None # LestContext
            self._init = None # InitContext
            self._trans = None # TransContext

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def lest(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LestContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.SEMICOLON)
            else:
                return self.getToken(DHSemanticGrammarParser.SEMICOLON, i)

        def init(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.InitContext,0)


        def trans(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.TransContext,0)


        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)




    def c(self):

        localctx = DHSemanticGrammarParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_c)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(DHSemanticGrammarParser.LBRACKET)
            self.state = 162
            localctx._lest = self.lest()
            self.state = 163
            self.match(DHSemanticGrammarParser.SEMICOLON)
            self.state = 164
            localctx._init = self.init()
            self.state = 165
            self.match(DHSemanticGrammarParser.SEMICOLON)
            self.state = 166
            localctx._trans = self.trans()
            self.state = 167
            self.match(DHSemanticGrammarParser.RBRACKET)
            self.state = 168
            self.match(DHSemanticGrammarParser.SEMICOLON)
            localctx.comp = Behaviour(localctx._lest.list_states, localctx._init.state, localctx._trans.list_trans)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_states = None
            self._ID = None # Token
            self.lac1 = None # LactionsContext
            self.lest1 = None # LestContext

        def STATE(self):
            return self.getToken(DHSemanticGrammarParser.STATE, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def lactions(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LactionsContext,0)


        def lest(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LestContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLest" ):
                listener.enterLest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLest" ):
                listener.exitLest(self)




    def lest(self):

        localctx = DHSemanticGrammarParser.LestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lest)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(DHSemanticGrammarParser.STATE)
                self.state = 172
                localctx._ID = self.match(DHSemanticGrammarParser.ID)
                self.state = 173
                self.match(DHSemanticGrammarParser.LBRACKET)
                self.state = 174
                localctx.lac1 = self.lactions()
                self.state = 175
                self.match(DHSemanticGrammarParser.RBRACKET)
                self.state = 176
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 177
                localctx.lest1 = self.lest()
                state = State((None if localctx._ID is None else localctx._ID.text), localctx.lac1.list_actions)
                localctx.list_states = localctx.lest1.list_states + [state] 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(DHSemanticGrammarParser.STATE)
                self.state = 181
                localctx._ID = self.match(DHSemanticGrammarParser.ID)
                self.state = 182
                self.match(DHSemanticGrammarParser.LBRACKET)
                self.state = 183
                localctx.lac1 = self.lactions()
                self.state = 184
                self.match(DHSemanticGrammarParser.RBRACKET)
                state = State((None if localctx._ID is None else localctx._ID.text), localctx.lac1.list_actions)
                localctx.list_states = [state] 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LactionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_actions = None
            self.a1 = None # ActionContext
            self.lactions1 = None # LactionsContext

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def action(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.ActionContext,0)


        def lactions(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LactionsContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLactions" ):
                listener.enterLactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLactions" ):
                listener.exitLactions(self)




    def lactions(self):

        localctx = DHSemanticGrammarParser.LactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lactions)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                localctx.a1 = self.action()
                self.state = 190
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 191
                localctx.lactions1 = self.lactions()
                localctx.list_actions = localctx.lactions1.list_actions + [localctx.a1.act]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                localctx.a1 = self.action()
                self.state = 195
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_actions = [localctx.a1.act]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.act = None
            self._ID = None # Token
            self._BOOL = None # Token

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = DHSemanticGrammarParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 201
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 202
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            value = False
            if (None if localctx._BOOL is None else localctx._BOOL.text) == 'true':
                value = True
            localctx.act= Action((None if localctx._ID is None else localctx._ID.text), value)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.state = None
            self._ID = None # Token

        def INIT(self):
            return self.getToken(DHSemanticGrammarParser.INIT, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)




    def init(self):

        localctx = DHSemanticGrammarParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(DHSemanticGrammarParser.INIT)
            self.state = 206
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            localctx.state = (None if localctx._ID is None else localctx._ID.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_trans = None
            self.t1 = None # TContext
            self.tr1 = None # TransContext

        def t(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.TContext,0)


        def trans(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.TransContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = DHSemanticGrammarParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_trans)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                localctx.t1 = self.t()
                self.state = 210
                localctx.tr1 = self.trans()
                localctx.list_trans = localctx.tr1.list_trans + [localctx.t1.tran]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                localctx.t1 = self.t()
                localctx.list_trans = [localctx.t1.tran]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tran = None
            self.src = None # Token
            self.dest = None # Token
            self.comb = None # Token

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.COMMA)
            else:
                return self.getToken(DHSemanticGrammarParser.COMMA, i)

        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.ID)
            else:
                return self.getToken(DHSemanticGrammarParser.ID, i)

        def COMBINATION(self):
            return self.getToken(DHSemanticGrammarParser.COMBINATION, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)




    def t(self):

        localctx = DHSemanticGrammarParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            localctx.src = self.match(DHSemanticGrammarParser.ID)
            self.state = 219
            self.match(DHSemanticGrammarParser.COMMA)
            self.state = 220
            localctx.dest = self.match(DHSemanticGrammarParser.ID)
            self.state = 221
            self.match(DHSemanticGrammarParser.COMMA)
            self.state = 222
            localctx.comb = self.match(DHSemanticGrammarParser.COMBINATION)
            self.state = 223
            self.match(DHSemanticGrammarParser.SEMICOLON)
            localctx.tran=Transition((None if localctx.comb is None else localctx.comb.text), (None if localctx.src is None else localctx.src.text), (None if localctx.dest is None else localctx.dest.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LslContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_sensors = None
            self.s1 = None # SContext
            self.lsl1 = None # LslContext

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def s(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SContext,0)


        def lsl(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LslContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lsl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLsl" ):
                listener.enterLsl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLsl" ):
                listener.exitLsl(self)




    def lsl(self):

        localctx = DHSemanticGrammarParser.LslContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lsl)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                localctx.s1 = self.s()
                self.state = 227
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 228
                localctx.lsl1 = self.lsl()
                localctx.list_sensors = localctx.lsl1.list_sensors + [localctx.s1.data]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                localctx.s1 = self.s()
                self.state = 232
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_sensors = [localctx.s1.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_actuators = None
            self.a1 = None # AContext
            self.lal1 = None # LalContext

        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def a(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AContext,0)


        def lal(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LalContext,0)


        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLal" ):
                listener.enterLal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLal" ):
                listener.exitLal(self)




    def lal(self):

        localctx = DHSemanticGrammarParser.LalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lal)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                localctx.a1 = self.a()
                self.state = 238
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 239
                localctx.lal1 = self.lal()
                localctx.list_actuators = localctx.lal1.list_actuators + [localctx.a1.data]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                localctx.a1 = self.a()
                self.state = 243
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_actuators = [localctx.a1.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LsgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_sensors = None
            self.lsg1 = None # LsgContext
            self.s1 = None # SContext

        def GLOBAL(self):
            return self.getToken(DHSemanticGrammarParser.GLOBAL, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def lsg(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LsgContext,0)


        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def s(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lsg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLsg" ):
                listener.enterLsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLsg" ):
                listener.exitLsg(self)




    def lsg(self):

        localctx = DHSemanticGrammarParser.LsgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lsg)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(DHSemanticGrammarParser.GLOBAL)
                self.state = 249
                self.match(DHSemanticGrammarParser.LBRACKET)
                self.state = 250
                localctx.lsg1 = self.lsg()
                self.state = 251
                self.match(DHSemanticGrammarParser.RBRACKET)
                self.state = 252
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_sensors = localctx.lsg1.list_sensors
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                localctx.s1 = self.s()
                self.state = 256
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 257
                localctx.lsg1 = self.lsg()
                localctx.list_sensors = localctx.lsg1.list_sensors + [localctx.s1.data]
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                localctx.s1 = self.s()
                localctx.list_sensors = [localctx.s1.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_actuators = None
            self.lag1 = None # LagContext
            self.a1 = None # AContext

        def GLOBAL(self):
            return self.getToken(DHSemanticGrammarParser.GLOBAL, 0)

        def LBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DHSemanticGrammarParser.RBRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(DHSemanticGrammarParser.SEMICOLON, 0)

        def lag(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.LagContext,0)


        def COMMA(self):
            return self.getToken(DHSemanticGrammarParser.COMMA, 0)

        def a(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_lag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLag" ):
                listener.enterLag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLag" ):
                listener.exitLag(self)




    def lag(self):

        localctx = DHSemanticGrammarParser.LagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lag)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(DHSemanticGrammarParser.GLOBAL)
                self.state = 266
                self.match(DHSemanticGrammarParser.LBRACKET)
                self.state = 267
                localctx.lag1 = self.lag()
                self.state = 268
                self.match(DHSemanticGrammarParser.RBRACKET)
                self.state = 269
                self.match(DHSemanticGrammarParser.SEMICOLON)
                localctx.list_actuators=localctx.lag1.list_actuators
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                localctx.a1 = self.a()
                self.state = 273
                self.match(DHSemanticGrammarParser.COMMA)
                self.state = 274
                localctx.lag1 = self.lag()
                localctx.list_actuators = localctx.lag1.list_actuators + [localctx.a1.data]
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                localctx.a1 = self.a()
                localctx.list_actuators = [localctx.a1.data]
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._spresencia = None # SpresenciaContext
            self._slluvia = None # SlluviaContext
            self._siluminacion = None # SiluminacionContext
            self._sreloj = None # SrelojContext
            self._stemperatura = None # StemperaturaContext
            self._shumo = None # ShumoContext
            self._sviento = None # SvientoContext
            self._sintrusos = None # SintrusosContext
            self._sgas = None # SgasContext
            self._sinundacion = None # SinundacionContext

        def spresencia(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SpresenciaContext,0)


        def slluvia(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SlluviaContext,0)


        def siluminacion(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SiluminacionContext,0)


        def sreloj(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SrelojContext,0)


        def stemperatura(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.StemperaturaContext,0)


        def shumo(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.ShumoContext,0)


        def sviento(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SvientoContext,0)


        def sintrusos(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SintrusosContext,0)


        def sgas(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SgasContext,0)


        def sinundacion(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.SinundacionContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = DHSemanticGrammarParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_s)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                localctx._spresencia = self.spresencia()
                localctx.data = localctx._spresencia.data
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                localctx._slluvia = self.slluvia()
                localctx.data = localctx._slluvia.data
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                localctx._siluminacion = self.siluminacion()
                localctx.data = localctx._siluminacion.data
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                localctx._sreloj = self.sreloj()
                localctx.data = localctx._sreloj.data
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 294
                localctx._stemperatura = self.stemperatura()
                localctx.data = localctx._stemperatura.data
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                localctx._shumo = self.shumo()
                localctx.data = localctx._shumo.data
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 300
                localctx._sviento = self.sviento()
                localctx.data = localctx._sviento.data
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 8)
                self.state = 303
                localctx._sintrusos = self.sintrusos()
                localctx.data = localctx._sintrusos.data
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 9)
                self.state = 306
                localctx._sgas = self.sgas()
                localctx.data = localctx._sgas.data
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 10)
                self.state = 309
                localctx._sinundacion = self.sinundacion()
                localctx.data = localctx._sinundacion.data
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._apuerta = None # ApuertaContext
            self._acalefaccion = None # AcalefaccionContext
            self._apersiana = None # ApersianaContext
            self._aluz = None # AluzContext
            self._aventana = None # AventanaContext
            self._afrio = None # AfrioContext
            self._agas = None # AgasContext
            self._atoldo = None # AtoldoContext
            self._aalarma = None # AalarmaContext
            self._aemergencia = None # AemergenciaContext

        def apuerta(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.ApuertaContext,0)


        def acalefaccion(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AcalefaccionContext,0)


        def apersiana(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.ApersianaContext,0)


        def aluz(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AluzContext,0)


        def aventana(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AventanaContext,0)


        def afrio(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AfrioContext,0)


        def agas(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AgasContext,0)


        def atoldo(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AtoldoContext,0)


        def aalarma(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AalarmaContext,0)


        def aemergencia(self):
            return self.getTypedRuleContext(DHSemanticGrammarParser.AemergenciaContext,0)


        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)




    def a(self):

        localctx = DHSemanticGrammarParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_a)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                localctx._apuerta = self.apuerta()
                localctx.data = localctx._apuerta.data
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                localctx._acalefaccion = self.acalefaccion()
                localctx.data = localctx._acalefaccion.data
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                localctx._apersiana = self.apersiana()
                localctx.data = localctx._apersiana.data
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                localctx._aluz = self.aluz()
                localctx.data = localctx._aluz.data
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 326
                localctx._aventana = self.aventana()
                localctx.data = localctx._aventana.data
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 329
                localctx._afrio = self.afrio()
                localctx.data = localctx._afrio.data
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 332
                localctx._agas = self.agas()
                localctx.data = localctx._agas.data
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
                localctx._atoldo = self.atoldo()
                localctx.data = localctx._atoldo.data
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 338
                localctx._aalarma = self.aalarma()
                localctx.data = localctx._aalarma.data
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 10)
                self.state = 341
                localctx._aemergencia = self.aemergencia()
                localctx.data = localctx._aemergencia.data
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpresenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SPRESENCIA(self):
            return self.getToken(DHSemanticGrammarParser.SPRESENCIA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_spresencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpresencia" ):
                listener.enterSpresencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpresencia" ):
                listener.exitSpresencia(self)




    def spresencia(self):

        localctx = DHSemanticGrammarParser.SpresenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_spresencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(DHSemanticGrammarParser.SPRESENCIA)
            self.state = 347
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 348
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 349
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorPresence(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SlluviaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SLLUVIA(self):
            return self.getToken(DHSemanticGrammarParser.SLLUVIA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_slluvia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlluvia" ):
                listener.enterSlluvia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlluvia" ):
                listener.exitSlluvia(self)




    def slluvia(self):

        localctx = DHSemanticGrammarParser.SlluviaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_slluvia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(DHSemanticGrammarParser.SLLUVIA)
            self.state = 353
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 354
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 355
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorRain(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShumoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SHUMO(self):
            return self.getToken(DHSemanticGrammarParser.SHUMO, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_shumo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShumo" ):
                listener.enterShumo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShumo" ):
                listener.exitShumo(self)




    def shumo(self):

        localctx = DHSemanticGrammarParser.ShumoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_shumo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(DHSemanticGrammarParser.SHUMO)
            self.state = 359
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 360
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 361
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorSmoke(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SintrusosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SINTRUSOS(self):
            return self.getToken(DHSemanticGrammarParser.SINTRUSOS, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_sintrusos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSintrusos" ):
                listener.enterSintrusos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSintrusos" ):
                listener.exitSintrusos(self)




    def sintrusos(self):

        localctx = DHSemanticGrammarParser.SintrusosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sintrusos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(DHSemanticGrammarParser.SINTRUSOS)
            self.state = 365
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 366
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 367
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorIntruders(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinundacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SINUNDACION(self):
            return self.getToken(DHSemanticGrammarParser.SINUNDACION, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_sinundacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinundacion" ):
                listener.enterSinundacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinundacion" ):
                listener.exitSinundacion(self)




    def sinundacion(self):

        localctx = DHSemanticGrammarParser.SinundacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sinundacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(DHSemanticGrammarParser.SINUNDACION)
            self.state = 371
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 372
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 373
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorFlood(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SgasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token
            self._BOOL = None # Token

        def SGAS(self):
            return self.getToken(DHSemanticGrammarParser.SGAS, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def BOOL(self):
            return self.getToken(DHSemanticGrammarParser.BOOL, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_sgas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSgas" ):
                listener.enterSgas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSgas" ):
                listener.exitSgas(self)




    def sgas(self):

        localctx = DHSemanticGrammarParser.SgasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sgas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(DHSemanticGrammarParser.SGAS)
            self.state = 377
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 378
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 379
            localctx._BOOL = self.match(DHSemanticGrammarParser.BOOL)

            id = (None if localctx._ID is None else localctx._ID.text)
            val = False
            if((None if localctx._BOOL is None else localctx._BOOL.text) == "true"):
              val = True
            localctx.data = SensorGas(id, val)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiluminacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._OPL = None # Token
            self.db1 = None # Token
            self._ID = None # Token
            self.db2 = None # Token

        def SILUMINACION(self):
            return self.getToken(DHSemanticGrammarParser.SILUMINACION, 0)

        def OPL(self):
            return self.getToken(DHSemanticGrammarParser.OPL, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def DOUBLE(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.DOUBLE)
            else:
                return self.getToken(DHSemanticGrammarParser.DOUBLE, i)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_siluminacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSiluminacion" ):
                listener.enterSiluminacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSiluminacion" ):
                listener.exitSiluminacion(self)




    def siluminacion(self):

        localctx = DHSemanticGrammarParser.SiluminacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_siluminacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(DHSemanticGrammarParser.SILUMINACION)
            self.state = 383
            localctx._OPL = self.match(DHSemanticGrammarParser.OPL)
            self.state = 384
            localctx.db1 = self.match(DHSemanticGrammarParser.DOUBLE)
            self.state = 385
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 386
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 387
            localctx.db2 = self.match(DHSemanticGrammarParser.DOUBLE)

            operator = (None if localctx._OPL is None else localctx._OPL.text)
            id = (None if localctx._ID is None else localctx._ID.text)
            real_value = float((None if localctx.db2 is None else localctx.db2.text))
            comp_value = float((None if localctx.db1 is None else localctx.db1.text))
            localctx.data = SensorLight(id, comp_value, real_value, operator)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StemperaturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._OPL = None # Token
            self.db1 = None # Token
            self._ID = None # Token
            self.db2 = None # Token

        def STEMPERATURA(self):
            return self.getToken(DHSemanticGrammarParser.STEMPERATURA, 0)

        def OPL(self):
            return self.getToken(DHSemanticGrammarParser.OPL, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def DOUBLE(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.DOUBLE)
            else:
                return self.getToken(DHSemanticGrammarParser.DOUBLE, i)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_stemperatura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStemperatura" ):
                listener.enterStemperatura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStemperatura" ):
                listener.exitStemperatura(self)




    def stemperatura(self):

        localctx = DHSemanticGrammarParser.StemperaturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stemperatura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(DHSemanticGrammarParser.STEMPERATURA)
            self.state = 391
            localctx._OPL = self.match(DHSemanticGrammarParser.OPL)
            self.state = 392
            localctx.db1 = self.match(DHSemanticGrammarParser.DOUBLE)
            self.state = 393
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 394
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 395
            localctx.db2 = self.match(DHSemanticGrammarParser.DOUBLE)

            operator = (None if localctx._OPL is None else localctx._OPL.text)
            id = (None if localctx._ID is None else localctx._ID.text)
            real_value = float((None if localctx.db2 is None else localctx.db2.text))
            comp_value = float((None if localctx.db1 is None else localctx.db1.text))
            localctx.data = SensorTemperature(id, comp_value, real_value, operator)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SvientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._OPL = None # Token
            self.db1 = None # Token
            self._ID = None # Token
            self.db2 = None # Token

        def SVIENTO(self):
            return self.getToken(DHSemanticGrammarParser.SVIENTO, 0)

        def OPL(self):
            return self.getToken(DHSemanticGrammarParser.OPL, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def DOUBLE(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.DOUBLE)
            else:
                return self.getToken(DHSemanticGrammarParser.DOUBLE, i)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_sviento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSviento" ):
                listener.enterSviento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSviento" ):
                listener.exitSviento(self)




    def sviento(self):

        localctx = DHSemanticGrammarParser.SvientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_sviento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(DHSemanticGrammarParser.SVIENTO)
            self.state = 399
            localctx._OPL = self.match(DHSemanticGrammarParser.OPL)
            self.state = 400
            localctx.db1 = self.match(DHSemanticGrammarParser.DOUBLE)
            self.state = 401
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 402
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 403
            localctx.db2 = self.match(DHSemanticGrammarParser.DOUBLE)

            operator = (None if localctx._OPL is None else localctx._OPL.text)
            id = (None if localctx._ID is None else localctx._ID.text)
            real_value = float((None if localctx.db2 is None else localctx.db2.text))
            comp_value = float((None if localctx.db1 is None else localctx.db1.text))
            localctx.data = SensorWind(id, comp_value, real_value, operator)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SrelojContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._OPL = None # Token
            self.t1 = None # Token
            self._ID = None # Token
            self.t2 = None # Token

        def SRELOJ(self):
            return self.getToken(DHSemanticGrammarParser.SRELOJ, 0)

        def OPL(self):
            return self.getToken(DHSemanticGrammarParser.OPL, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def SEQ(self):
            return self.getToken(DHSemanticGrammarParser.SEQ, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(DHSemanticGrammarParser.TIME)
            else:
                return self.getToken(DHSemanticGrammarParser.TIME, i)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_sreloj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSreloj" ):
                listener.enterSreloj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSreloj" ):
                listener.exitSreloj(self)




    def sreloj(self):

        localctx = DHSemanticGrammarParser.SrelojContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sreloj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(DHSemanticGrammarParser.SRELOJ)
            self.state = 407
            localctx._OPL = self.match(DHSemanticGrammarParser.OPL)
            self.state = 408
            localctx.t1 = self.match(DHSemanticGrammarParser.TIME)
            self.state = 409
            localctx._ID = self.match(DHSemanticGrammarParser.ID)
            self.state = 410
            self.match(DHSemanticGrammarParser.SEQ)
            self.state = 411
            localctx.t2 = self.match(DHSemanticGrammarParser.TIME)

            operator = (None if localctx._OPL is None else localctx._OPL.text)
            id = (None if localctx._ID is None else localctx._ID.text)
            real_value = (None if localctx.t2 is None else localctx.t2.text)
            comp_value = (None if localctx.t1 is None else localctx.t1.text)
            localctx.data = SensorTime(id, comp_value, real_value, operator)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApuertaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def APUERTA(self):
            return self.getToken(DHSemanticGrammarParser.APUERTA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_apuerta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApuerta" ):
                listener.enterApuerta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApuerta" ):
                listener.exitApuerta(self)




    def apuerta(self):

        localctx = DHSemanticGrammarParser.ApuertaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_apuerta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(DHSemanticGrammarParser.APUERTA)
            self.state = 415
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorDoor(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcalefaccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def ACALEFACCION(self):
            return self.getToken(DHSemanticGrammarParser.ACALEFACCION, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_acalefaccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcalefaccion" ):
                listener.enterAcalefaccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcalefaccion" ):
                listener.exitAcalefaccion(self)




    def acalefaccion(self):

        localctx = DHSemanticGrammarParser.AcalefaccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_acalefaccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(DHSemanticGrammarParser.ACALEFACCION)
            self.state = 419
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorHeat(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApersianaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def APERSIANA(self):
            return self.getToken(DHSemanticGrammarParser.APERSIANA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_apersiana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApersiana" ):
                listener.enterApersiana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApersiana" ):
                listener.exitApersiana(self)




    def apersiana(self):

        localctx = DHSemanticGrammarParser.ApersianaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_apersiana)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(DHSemanticGrammarParser.APERSIANA)
            self.state = 423
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorWindowBlind(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AluzContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def ALUZ(self):
            return self.getToken(DHSemanticGrammarParser.ALUZ, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_aluz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAluz" ):
                listener.enterAluz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAluz" ):
                listener.exitAluz(self)




    def aluz(self):

        localctx = DHSemanticGrammarParser.AluzContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_aluz)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(DHSemanticGrammarParser.ALUZ)
            self.state = 427
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorLight(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AventanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def AVENTANA(self):
            return self.getToken(DHSemanticGrammarParser.AVENTANA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_aventana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAventana" ):
                listener.enterAventana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAventana" ):
                listener.exitAventana(self)




    def aventana(self):

        localctx = DHSemanticGrammarParser.AventanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_aventana)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(DHSemanticGrammarParser.AVENTANA)
            self.state = 431
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorWindow(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AfrioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def AFRIO(self):
            return self.getToken(DHSemanticGrammarParser.AFRIO, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_afrio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAfrio" ):
                listener.enterAfrio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAfrio" ):
                listener.exitAfrio(self)




    def afrio(self):

        localctx = DHSemanticGrammarParser.AfrioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_afrio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(DHSemanticGrammarParser.AFRIO)
            self.state = 435
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorCold(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def AGAS(self):
            return self.getToken(DHSemanticGrammarParser.AGAS, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_agas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgas" ):
                listener.enterAgas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgas" ):
                listener.exitAgas(self)




    def agas(self):

        localctx = DHSemanticGrammarParser.AgasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_agas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(DHSemanticGrammarParser.AGAS)
            self.state = 439
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorGas(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtoldoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def ATOLDO(self):
            return self.getToken(DHSemanticGrammarParser.ATOLDO, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_atoldo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtoldo" ):
                listener.enterAtoldo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtoldo" ):
                listener.exitAtoldo(self)




    def atoldo(self):

        localctx = DHSemanticGrammarParser.AtoldoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_atoldo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(DHSemanticGrammarParser.ATOLDO)
            self.state = 443
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorSunBlind(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AalarmaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def AALARMA(self):
            return self.getToken(DHSemanticGrammarParser.AALARMA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_aalarma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAalarma" ):
                listener.enterAalarma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAalarma" ):
                listener.exitAalarma(self)




    def aalarma(self):

        localctx = DHSemanticGrammarParser.AalarmaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_aalarma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(DHSemanticGrammarParser.AALARMA)
            self.state = 447
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorAlarm(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AemergenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None
            self._ID = None # Token

        def AEMERGENCIA(self):
            return self.getToken(DHSemanticGrammarParser.AEMERGENCIA, 0)

        def ID(self):
            return self.getToken(DHSemanticGrammarParser.ID, 0)

        def getRuleIndex(self):
            return DHSemanticGrammarParser.RULE_aemergencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAemergencia" ):
                listener.enterAemergencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAemergencia" ):
                listener.exitAemergencia(self)




    def aemergencia(self):

        localctx = DHSemanticGrammarParser.AemergenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_aemergencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(DHSemanticGrammarParser.AEMERGENCIA)
            self.state = 451
            localctx._ID = self.match(DHSemanticGrammarParser.ID)

            id = (None if localctx._ID is None else localctx._ID.text)
            localctx.data = ActuatorEmergency(id, False)
              
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





