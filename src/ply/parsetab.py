
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AALARMA ACALEFACCION AEMERGENCIA AFRIO AGAS ALUZ APERSIANA APUERTA ATOLDO AVENTANA BOOL COMBINATION COMMA CORRIDOR DOUBLE GLOBAL HOUSE ID INIT LBRACKET OPL RBRACKET ROOM SEMICOLON SEQ SGAS SHUMO SILUMINACION SINTRUSOS SINUNDACION SLLUVIA SPRESENCIA SRELOJ STATE STEMPERATURA SVIENTO TIME\n\tcasa : HOUSE ID LBRACKET lh RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lp RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lsg RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lag RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lp lsg RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lp lag RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lsg lag RBRACKET SEMICOLON\n\t\n\tcasa : HOUSE ID LBRACKET lh lp lsg lag RBRACKET SEMICOLON\n\t\n\tlh : h COMMA lh\n\t\n\tlh : h SEMICOLON\n\t\n\tlp : p COMMA lp\n\t\n\tlp : p SEMICOLON\n\t\n\th : ROOM ID LBRACKET lsl RBRACKET\n\t\n\th : ROOM ID LBRACKET lal RBRACKET\n\t\n\th : ROOM ID LBRACKET c RBRACKET\n\t\n\th : ROOM ID LBRACKET lsl lal RBRACKET\n\t\n\th : ROOM ID LBRACKET lsl c RBRACKET\n\t\n\th : ROOM ID LBRACKET lal c RBRACKET\n\t\n\th : ROOM ID LBRACKET lsl lal c RBRACKET\n\t\n\th : ROOM ID LBRACKET RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lsl RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lal RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id c RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lsl lal RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lsl c RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lal c RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id lsl lal c RBRACKET\n\t\n\tp : CORRIDOR ID LBRACKET l2id RBRACKET\n\t\n\tl2id : ID COMMA l2id\n\t\n\tl2id : ID COMMA ID SEMICOLON\n\t\n\tlsl : s COMMA lsl\n\t\n\tlsl : s SEMICOLON\n\t\n\tlal : a COMMA lal\n\t\n\tlal : a SEMICOLON\n\t\n\tlsg : GLOBAL LBRACKET lsg1\n\t\n\tlsg1 : s COMMA lsg1\n\t\n\tlsg1 : s RBRACKET SEMICOLON\n\t\n\tlag : GLOBAL LBRACKET lag1\n\t\n\tlag1 : a COMMA lag1\n\t\n\tlag1 : a RBRACKET SEMICOLON\n\t\n\ts : spresencia\n        | slluvia\n        | siluminacion\n        | sreloj\n        | stemperatura\n        | shumo\n        | sviento\n        | sintrusos\n        | sgas\n        | sinundacion\n\t\n\ta : apuerta\n        | acalefaccion\n        | apersiana\n        | aluz\n        | aventana\n        | afrio\n        | agas \n        | atoldo\n        | aalarma \n        | aemergencia \n\t\n\tc : LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON\n\t\n\tc : LBRACKET lest SEMICOLON trans RBRACKET SEMICOLON\n\t\n\tc : LBRACKET lest SEMICOLON init SEMICOLON RBRACKET SEMICOLON\n\t\n\tc : LBRACKET lest SEMICOLON RBRACKET SEMICOLON\n\t\n\tlest :  STATE ID LBRACKET lactions RBRACKET COMMA lest\n\t\n\tlest :  STATE ID LBRACKET RBRACKET COMMA lest\n\t\n\tlest :  STATE ID LBRACKET lactions RBRACKET\n\t\n\tlest :  STATE ID LBRACKET RBRACKET\n\t\n\tlactions : action COMMA lactions\n\t\n\tlactions : action SEMICOLON\n\t\n\taction : ID SEQ BOOL\n\t\n\tinit : INIT ID\n\t\n\ttrans : t trans\n\t\n\ttrans : t\n\t\n\tt : ID COMMA ID COMMA COMBINATION SEMICOLON\n\t\n\tspresencia : SPRESENCIA ID SEQ BOOL\n\t\n\tslluvia : SLLUVIA ID SEQ BOOL\n\t\n\tsiluminacion : SILUMINACION OPL DOUBLE ID SEQ DOUBLE\n\t\n\tstemperatura : STEMPERATURA OPL DOUBLE ID SEQ DOUBLE\n\t\n\tsreloj : SRELOJ OPL TIME ID SEQ TIME\n\t\n\tshumo : SHUMO ID SEQ BOOL\n\t\n\tsviento : SVIENTO OPL DOUBLE ID SEQ DOUBLE\n\t\n\tsintrusos : SINTRUSOS ID SEQ BOOL\n\t\n\tsinundacion : SINUNDACION ID SEQ BOOL\n\t\n\tsgas : SGAS ID SEQ BOOL\n\t\n\tapuerta : APUERTA ID\n\t\n\tacalefaccion : ACALEFACCION ID\n\t\n\tapersiana : APERSIANA ID\n\t\n\taluz : ALUZ ID\n\t\n\taventana : AVENTANA ID\n\t\n\tafrio : AFRIO ID\n\t\n\tagas : AGAS ID\n\t\n\tatoldo : ATOLDO ID\n\t\n\taalarma : AALARMA ID\n\t\n\taemergencia : AEMERGENCIA ID\n\t'
    
_lr_action_items = {'HOUSE':([0,],[2,]),'$end':([1,18,32,36,39,93,95,96,135,],[0,-1,-2,-3,-4,-5,-6,-7,-8,]),'ID':([2,7,14,65,66,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,124,142,143,144,146,150,155,184,186,187,198,202,220,232,],[3,17,29,101,102,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,156,165,166,167,169,173,185,201,185,204,185,216,204,-75,]),'LBRACKET':([3,13,17,24,29,31,87,89,122,126,132,134,151,153,156,161,162,174,176,193,],[4,28,31,38,85,86,86,86,86,86,-32,-34,86,86,187,-31,-33,-29,86,-30,]),'ROOM':([4,15,],[7,7,]),'RBRACKET':([5,9,10,11,16,20,21,23,27,30,31,34,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,87,89,90,111,112,113,114,115,116,117,118,119,120,122,126,127,129,132,134,136,137,138,139,151,153,154,155,158,161,162,163,164,168,170,171,172,174,176,177,179,182,186,187,193,195,198,200,203,205,208,209,210,211,213,215,221,223,228,229,232,],[8,19,22,25,-10,33,35,37,-12,-9,88,94,-11,-35,-38,98,100,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,125,128,130,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,152,157,159,160,-32,-34,-36,-37,-39,-40,175,178,180,183,188,-31,-33,-76,-77,-81,-83,-85,-84,-29,194,196,197,199,-74,206,-30,212,214,-64,-73,218,-78,-80,-79,-82,222,-62,-70,-63,-69,-61,-75,]),'GLOBAL':([5,9,10,16,20,27,30,40,41,136,137,],[13,13,24,-10,24,-12,-9,-11,-35,-36,-37,]),'CORRIDOR':([5,16,26,30,],[14,-10,14,-9,]),'COMMA':([6,12,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,88,91,92,111,112,113,114,115,116,117,118,119,120,121,125,128,130,152,157,159,160,163,164,168,170,171,172,173,175,178,180,185,188,194,196,197,206,207,208,209,210,211,212,216,218,225,],[15,26,97,99,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-20,131,133,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,150,-13,-14,-15,-28,-16,-17,-18,-76,-77,-81,-83,-85,-84,150,-21,-22,-23,202,-19,-24,-25,-26,219,220,-78,-80,-79,-82,-27,224,226,-71,]),'SEMICOLON':([6,8,12,19,22,25,33,35,37,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,88,91,92,94,98,100,111,112,113,114,115,116,117,118,119,120,123,125,128,130,152,157,159,160,163,164,168,170,171,172,173,175,178,180,181,183,188,194,196,197,199,201,206,207,208,209,210,211,212,214,218,222,225,227,230,231,],[16,18,27,32,36,39,93,95,96,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-20,132,134,135,137,139,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,155,-13,-14,-15,-28,-16,-17,-18,-76,-77,-81,-83,-85,-84,193,-21,-22,-23,198,200,-19,-24,-25,-26,215,-72,-68,221,-78,-80,-79,-82,-27,223,-67,229,-71,-66,232,-65,]),'SPRESENCIA':([28,31,97,122,131,174,193,],[65,65,65,65,65,-29,-30,]),'SLLUVIA':([28,31,97,122,131,174,193,],[66,66,66,66,66,-29,-30,]),'SILUMINACION':([28,31,97,122,131,174,193,],[67,67,67,67,67,-29,-30,]),'SRELOJ':([28,31,97,122,131,174,193,],[68,68,68,68,68,-29,-30,]),'STEMPERATURA':([28,31,97,122,131,174,193,],[69,69,69,69,69,-29,-30,]),'SHUMO':([28,31,97,122,131,174,193,],[70,70,70,70,70,-29,-30,]),'SVIENTO':([28,31,97,122,131,174,193,],[71,71,71,71,71,-29,-30,]),'SINTRUSOS':([28,31,97,122,131,174,193,],[72,72,72,72,72,-29,-30,]),'SGAS':([28,31,97,122,131,174,193,],[73,73,73,73,73,-29,-30,]),'SINUNDACION':([28,31,97,122,131,174,193,],[74,74,74,74,74,-29,-30,]),'APUERTA':([28,31,38,87,99,122,132,133,151,161,174,193,],[75,75,75,75,75,75,-32,75,75,-31,-29,-30,]),'ACALEFACCION':([28,31,38,87,99,122,132,133,151,161,174,193,],[76,76,76,76,76,76,-32,76,76,-31,-29,-30,]),'APERSIANA':([28,31,38,87,99,122,132,133,151,161,174,193,],[77,77,77,77,77,77,-32,77,77,-31,-29,-30,]),'ALUZ':([28,31,38,87,99,122,132,133,151,161,174,193,],[78,78,78,78,78,78,-32,78,78,-31,-29,-30,]),'AVENTANA':([28,31,38,87,99,122,132,133,151,161,174,193,],[79,79,79,79,79,79,-32,79,79,-31,-29,-30,]),'AFRIO':([28,31,38,87,99,122,132,133,151,161,174,193,],[80,80,80,80,80,80,-32,80,80,-31,-29,-30,]),'AGAS':([28,31,38,87,99,122,132,133,151,161,174,193,],[81,81,81,81,81,81,-32,81,81,-31,-29,-30,]),'ATOLDO':([28,31,38,87,99,122,132,133,151,161,174,193,],[82,82,82,82,82,82,-32,82,82,-31,-29,-30,]),'AALARMA':([28,31,38,87,99,122,132,133,151,161,174,193,],[83,83,83,83,83,83,-32,83,83,-31,-29,-30,]),'AEMERGENCIA':([28,31,38,87,99,122,132,133,151,161,174,193,],[84,84,84,84,84,84,-32,84,84,-31,-29,-30,]),'OPL':([67,68,69,71,],[103,104,105,107,]),'STATE':([86,219,226,],[124,124,124,]),'SEQ':([101,102,106,108,109,110,165,166,167,169,204,],[140,141,145,147,148,149,189,190,191,192,217,]),'DOUBLE':([103,105,107,189,191,192,],[142,144,146,208,210,211,]),'TIME':([104,190,],[143,209,]),'BOOL':([140,141,145,147,148,149,217,],[163,164,168,170,171,172,225,]),'INIT':([155,],[184,]),'COMBINATION':([224,],[230,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'casa':([0,],[1,]),'lh':([4,15,],[5,30,]),'h':([4,15,],[6,6,]),'lp':([5,26,],[9,40,]),'lsg':([5,9,],[10,20,]),'lag':([5,9,10,20,],[11,21,23,34,]),'p':([5,26,],[12,12,]),'lsg1':([28,97,],[41,136,]),'lag1':([28,38,99,],[42,42,138,]),'s':([28,31,97,122,131,],[43,91,43,91,91,]),'a':([28,31,38,87,99,122,133,151,],[44,92,44,92,44,92,92,92,]),'spresencia':([28,31,97,122,131,],[45,45,45,45,45,]),'slluvia':([28,31,97,122,131,],[46,46,46,46,46,]),'siluminacion':([28,31,97,122,131,],[47,47,47,47,47,]),'sreloj':([28,31,97,122,131,],[48,48,48,48,48,]),'stemperatura':([28,31,97,122,131,],[49,49,49,49,49,]),'shumo':([28,31,97,122,131,],[50,50,50,50,50,]),'sviento':([28,31,97,122,131,],[51,51,51,51,51,]),'sintrusos':([28,31,97,122,131,],[52,52,52,52,52,]),'sgas':([28,31,97,122,131,],[53,53,53,53,53,]),'sinundacion':([28,31,97,122,131,],[54,54,54,54,54,]),'apuerta':([28,31,38,87,99,122,133,151,],[55,55,55,55,55,55,55,55,]),'acalefaccion':([28,31,38,87,99,122,133,151,],[56,56,56,56,56,56,56,56,]),'apersiana':([28,31,38,87,99,122,133,151,],[57,57,57,57,57,57,57,57,]),'aluz':([28,31,38,87,99,122,133,151,],[58,58,58,58,58,58,58,58,]),'aventana':([28,31,38,87,99,122,133,151,],[59,59,59,59,59,59,59,59,]),'afrio':([28,31,38,87,99,122,133,151,],[60,60,60,60,60,60,60,60,]),'agas':([28,31,38,87,99,122,133,151,],[61,61,61,61,61,61,61,61,]),'atoldo':([28,31,38,87,99,122,133,151,],[62,62,62,62,62,62,62,62,]),'aalarma':([28,31,38,87,99,122,133,151,],[63,63,63,63,63,63,63,63,]),'aemergencia':([28,31,38,87,99,122,133,151,],[64,64,64,64,64,64,64,64,]),'lsl':([31,122,131,],[87,151,161,]),'lal':([31,87,122,133,151,],[89,126,153,162,176,]),'c':([31,87,89,122,126,151,153,176,],[90,127,129,154,158,177,179,195,]),'l2id':([85,150,],[122,174,]),'lest':([86,219,226,],[123,227,231,]),'init':([155,],[181,]),'trans':([155,186,198,],[182,203,213,]),'t':([155,186,198,],[186,186,186,]),'lactions':([187,220,],[205,228,]),'action':([187,220,],[207,207,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> casa","S'",1,None,None,None),
  ('casa -> HOUSE ID LBRACKET lh RBRACKET SEMICOLON','casa',6,'p_casa1','LALR.py',225),
  ('casa -> HOUSE ID LBRACKET lh lp RBRACKET SEMICOLON','casa',7,'p_casa2','LALR.py',231),
  ('casa -> HOUSE ID LBRACKET lh lsg RBRACKET SEMICOLON','casa',7,'p_casa3','LALR.py',237),
  ('casa -> HOUSE ID LBRACKET lh lag RBRACKET SEMICOLON','casa',7,'p_casa4','LALR.py',243),
  ('casa -> HOUSE ID LBRACKET lh lp lsg RBRACKET SEMICOLON','casa',8,'p_casa5','LALR.py',249),
  ('casa -> HOUSE ID LBRACKET lh lp lag RBRACKET SEMICOLON','casa',8,'p_casa6','LALR.py',255),
  ('casa -> HOUSE ID LBRACKET lh lsg lag RBRACKET SEMICOLON','casa',8,'p_casa7','LALR.py',261),
  ('casa -> HOUSE ID LBRACKET lh lp lsg lag RBRACKET SEMICOLON','casa',9,'p_casa8','LALR.py',267),
  ('lh -> h COMMA lh','lh',3,'p_lh1','LALR.py',273),
  ('lh -> h SEMICOLON','lh',2,'p_lh2','LALR.py',279),
  ('lp -> p COMMA lp','lp',3,'p_lp1','LALR.py',287),
  ('lp -> p SEMICOLON','lp',2,'p_lp2','LALR.py',293),
  ('h -> ROOM ID LBRACKET lsl RBRACKET','h',5,'p_h1','LALR.py',301),
  ('h -> ROOM ID LBRACKET lal RBRACKET','h',5,'p_h2','LALR.py',308),
  ('h -> ROOM ID LBRACKET c RBRACKET','h',5,'p_h3','LALR.py',315),
  ('h -> ROOM ID LBRACKET lsl lal RBRACKET','h',6,'p_h4','LALR.py',322),
  ('h -> ROOM ID LBRACKET lsl c RBRACKET','h',6,'p_h5','LALR.py',329),
  ('h -> ROOM ID LBRACKET lal c RBRACKET','h',6,'p_h6','LALR.py',336),
  ('h -> ROOM ID LBRACKET lsl lal c RBRACKET','h',7,'p_h7','LALR.py',343),
  ('h -> ROOM ID LBRACKET RBRACKET','h',4,'p_h_empty','LALR.py',350),
  ('p -> CORRIDOR ID LBRACKET l2id lsl RBRACKET','p',6,'p_p1','LALR.py',357),
  ('p -> CORRIDOR ID LBRACKET l2id lal RBRACKET','p',6,'p_p2','LALR.py',364),
  ('p -> CORRIDOR ID LBRACKET l2id c RBRACKET','p',6,'p_p3','LALR.py',371),
  ('p -> CORRIDOR ID LBRACKET l2id lsl lal RBRACKET','p',7,'p_p4','LALR.py',378),
  ('p -> CORRIDOR ID LBRACKET l2id lsl c RBRACKET','p',7,'p_p5','LALR.py',385),
  ('p -> CORRIDOR ID LBRACKET l2id lal c RBRACKET','p',7,'p_p6','LALR.py',392),
  ('p -> CORRIDOR ID LBRACKET l2id lsl lal c RBRACKET','p',8,'p_p7','LALR.py',399),
  ('p -> CORRIDOR ID LBRACKET l2id RBRACKET','p',5,'p_p8','LALR.py',406),
  ('l2id -> ID COMMA l2id','l2id',3,'p_l2id1','LALR.py',412),
  ('l2id -> ID COMMA ID SEMICOLON','l2id',4,'p_l2id2','LALR.py',418),
  ('lsl -> s COMMA lsl','lsl',3,'p_lsl1','LALR.py',427),
  ('lsl -> s SEMICOLON','lsl',2,'p_lsl2','LALR.py',433),
  ('lal -> a COMMA lal','lal',3,'p_lal1','LALR.py',441),
  ('lal -> a SEMICOLON','lal',2,'p_lal2','LALR.py',447),
  ('lsg -> GLOBAL LBRACKET lsg1','lsg',3,'p_lsg1','LALR.py',455),
  ('lsg1 -> s COMMA lsg1','lsg1',3,'p_lsg2','LALR.py',461),
  ('lsg1 -> s RBRACKET SEMICOLON','lsg1',3,'p_lsg3','LALR.py',467),
  ('lag -> GLOBAL LBRACKET lag1','lag',3,'p_lag1','LALR.py',475),
  ('lag1 -> a COMMA lag1','lag1',3,'p_lag2','LALR.py',481),
  ('lag1 -> a RBRACKET SEMICOLON','lag1',3,'p_lag3','LALR.py',487),
  ('s -> spresencia','s',1,'p_s','LALR.py',495),
  ('s -> slluvia','s',1,'p_s','LALR.py',496),
  ('s -> siluminacion','s',1,'p_s','LALR.py',497),
  ('s -> sreloj','s',1,'p_s','LALR.py',498),
  ('s -> stemperatura','s',1,'p_s','LALR.py',499),
  ('s -> shumo','s',1,'p_s','LALR.py',500),
  ('s -> sviento','s',1,'p_s','LALR.py',501),
  ('s -> sintrusos','s',1,'p_s','LALR.py',502),
  ('s -> sgas','s',1,'p_s','LALR.py',503),
  ('s -> sinundacion','s',1,'p_s','LALR.py',504),
  ('a -> apuerta','a',1,'p_a','LALR.py',508),
  ('a -> acalefaccion','a',1,'p_a','LALR.py',509),
  ('a -> apersiana','a',1,'p_a','LALR.py',510),
  ('a -> aluz','a',1,'p_a','LALR.py',511),
  ('a -> aventana','a',1,'p_a','LALR.py',512),
  ('a -> afrio','a',1,'p_a','LALR.py',513),
  ('a -> agas','a',1,'p_a','LALR.py',514),
  ('a -> atoldo','a',1,'p_a','LALR.py',515),
  ('a -> aalarma','a',1,'p_a','LALR.py',516),
  ('a -> aemergencia','a',1,'p_a','LALR.py',517),
  ('c -> LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON','c',8,'p_c1','LALR.py',521),
  ('c -> LBRACKET lest SEMICOLON trans RBRACKET SEMICOLON','c',6,'p_c2','LALR.py',527),
  ('c -> LBRACKET lest SEMICOLON init SEMICOLON RBRACKET SEMICOLON','c',7,'p_c3','LALR.py',533),
  ('c -> LBRACKET lest SEMICOLON RBRACKET SEMICOLON','c',5,'p_c4','LALR.py',539),
  ('lest -> STATE ID LBRACKET lactions RBRACKET COMMA lest','lest',7,'p_lest1','LALR.py',545),
  ('lest -> STATE ID LBRACKET RBRACKET COMMA lest','lest',6,'p_lest2','LALR.py',551),
  ('lest -> STATE ID LBRACKET lactions RBRACKET','lest',5,'p_lest3','LALR.py',557),
  ('lest -> STATE ID LBRACKET RBRACKET','lest',4,'p_lest4','LALR.py',565),
  ('lactions -> action COMMA lactions','lactions',3,'p_lactions1','LALR.py',573),
  ('lactions -> action SEMICOLON','lactions',2,'p_lactions2','LALR.py',579),
  ('action -> ID SEQ BOOL','action',3,'p_action','LALR.py',587),
  ('init -> INIT ID','init',2,'p_init','LALR.py',593),
  ('trans -> t trans','trans',2,'p_trans1','LALR.py',599),
  ('trans -> t','trans',1,'p_trans2','LALR.py',605),
  ('t -> ID COMMA ID COMMA COMBINATION SEMICOLON','t',6,'p_t','LALR.py',613),
  ('spresencia -> SPRESENCIA ID SEQ BOOL','spresencia',4,'p_spresencia','LALR.py',619),
  ('slluvia -> SLLUVIA ID SEQ BOOL','slluvia',4,'p_slluvia','LALR.py',625),
  ('siluminacion -> SILUMINACION OPL DOUBLE ID SEQ DOUBLE','siluminacion',6,'p_siluminacion','LALR.py',631),
  ('stemperatura -> STEMPERATURA OPL DOUBLE ID SEQ DOUBLE','stemperatura',6,'p_stemperatura','LALR.py',637),
  ('sreloj -> SRELOJ OPL TIME ID SEQ TIME','sreloj',6,'p_sreloj','LALR.py',643),
  ('shumo -> SHUMO ID SEQ BOOL','shumo',4,'p_shumo','LALR.py',649),
  ('sviento -> SVIENTO OPL DOUBLE ID SEQ DOUBLE','sviento',6,'p_sviento','LALR.py',655),
  ('sintrusos -> SINTRUSOS ID SEQ BOOL','sintrusos',4,'p_sintrusos','LALR.py',661),
  ('sinundacion -> SINUNDACION ID SEQ BOOL','sinundacion',4,'p_sinundacion','LALR.py',667),
  ('sgas -> SGAS ID SEQ BOOL','sgas',4,'p_sgas','LALR.py',673),
  ('apuerta -> APUERTA ID','apuerta',2,'p_apuerta','LALR.py',679),
  ('acalefaccion -> ACALEFACCION ID','acalefaccion',2,'p_acalefaccion','LALR.py',685),
  ('apersiana -> APERSIANA ID','apersiana',2,'p_apersiana','LALR.py',691),
  ('aluz -> ALUZ ID','aluz',2,'p_aluz','LALR.py',697),
  ('aventana -> AVENTANA ID','aventana',2,'p_aventana','LALR.py',703),
  ('afrio -> AFRIO ID','afrio',2,'p_frio','LALR.py',709),
  ('agas -> AGAS ID','agas',2,'p_agas','LALR.py',715),
  ('atoldo -> ATOLDO ID','atoldo',2,'p_atoldo','LALR.py',721),
  ('aalarma -> AALARMA ID','aalarma',2,'p_aalarma','LALR.py',727),
  ('aemergencia -> AEMERGENCIA ID','aemergencia',2,'p_aemergencia','LALR.py',733),
]
