grammar DHGrammar;

import DHLexerRules;

casa : HOUSE ID LBRACKET lh lp? lsg? lag? RBRACKET SEMICOLON EOF ;
lh : (h COMMA)* h SEMICOLON ;
lp : (p COMMA)* p SEMICOLON ;
h : ROOM ID LBRACKET lsl? lal? c? RBRACKET ;
p : CORRIDOR ID LBRACKET l2id lsl? lal? c? RBRACKET ;
l2id : (ID COMMA)* ID COMMA ID SEMICOLON ;
lsl : (s COMMA) s ;
lal : (a COMMA) a ;
lsg : GLOBAL LBRACKET (s COMMA)* s RBRACKET SEMICOLON ;
lag : GLOBAL LBRACKET (a COMMA)* a RBRACKET SEMICOLON ;
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
  ;
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
  ;
c  : LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON ;
lest : (STATE ID LBRACKET lactions? RBRACKET COMMA)* STATE ID LBRACKET lactions? RBRACKET ;
lactions : (action COMMA) action SEMICOLON ;
action : ID SEQ BOOL ;
init : INIT ID ;
trans : t+ ;
t : ID COMMA ID COMMA COMBINATION SEMICOLON ;
spresencia : SPRESENCIA ID SEQ BOOL ;
slluvia : SLLUVIA ID SEQ BOOL ;
siluminacion : SILUMINACION OPL DOUBLE ID SEQ DOUBLE ;
stemperatura : STEMPERATURA OPL DOUBLE ID SEQ DOUBLE ;
sreloj : SRELOJ OPL TIME ID SEQ TIME ;
shumo : SHUMO ID SEQ BOOL ;
sviento : SVIENTO OPL DOUBLE ID SEQ DOUBLE ;
sintrusos : SINTRUSOS ID SEQ BOOL ;
sinundacion : SINUNDACION ID SEQ BOOL ;
sgas : SGAS ID SEQ BOOL ;
apuerta : APUERTA ID ;
acalefaccion : ACALEFACCION ID ;
apersiana : APERSIANA ID ;
aluz : ALUZ ID ;
aventana : AVENTANA ID ;
afrio : AFRIO ID ;
agas : AGAS ID ;
atoldo : ATOLDO ID ;
aalarma : AALARMA ID ;
aemergencia : AEMERGENCIA ID ;