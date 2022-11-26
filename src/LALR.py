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
def t_COMMENT(t):
    r'\\\*.*?\*/'
    pass
    # No return value. Token discarded

def t_IGNORE(t):
    r'(\t|\n|\r)+'
    pass
    # No return value. Token discarded

def t_SPRESENCIA(t):
    r'sensor_presence'
    return t

def t_SLLUVIA(t):
    r'sensor_rain'
    return t

def t_SILUMINACION(t):
    r'sensor_light'
    return t

def t_STEMPERATURA(t):
    r'sensor_temperature'
    return t

def t_SRELOJ(t):
    r'sensor_time'
    return t

def t_SHUMO(t):
    r'sensor_smoke'
    return t

def t_SGAS(t):
    r'sensor_gas'
    return t

def t_SVIENTO(t):
    r'sensor_wind'
    return t

def t_SINTRUSOS(t):
    r'sensor_intruder'
    return t

def t_SINUNDACION(t):
    r'sensor_flood'
    return t

def t_APUERTA(t):
    r'actuator_door'
    return t

def t_ACALEFACCION(t):
    r'actuator_heat'
    return t

def t_APERSIANA(t):
    r'actuator_wblind'
    return t

def t_ALUZ(t):
    r'actuator_light'
    return t

def t_AVENTANA(t):
    r'actuator_window'
    return t

def t_AFRIO(t):
    r'actuator_cold'
    return t

def t_AGAS(t):
    r'actuator_gas'
    return t

def t_ATOLDO(t):
    r'actuator_wind'
    return t

def t_AALARMA(t):
    r'actuator_alarm'
    return t

def t_AEMERGENCIA(t):
    r'actuator_emergency'
    return t

def t_ROOM(t):
    r'room'
    return t

def t_HOUSE(t):
    r'house'
    return t

def t_CORRIDOR(t):
    r'corridor'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_STATE(t):
    r'state'
    return t

def t_INIT(t):
    r'init'
    return t

def t_OPL(t):
    r'eqlow|equp|eq|up|low'
    return t

def t_BOOL(t):
    r'true|false'
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_DOUBLE(t):
    r'-?[0-9]([0-9]*)\.([0-9]+)'
    return t

def t_TIME(t):
    r'((0|1)[0-9]|2[0-3]):[0-5][0-9]'
    return t

def t_COMBINATION(t):
    r'(0|1)+'
    return t

def t_SEQ(t):
    r':='
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LBRACKET(t):
    r'{'
    return t

def t_RBRACKET(t):
    r'}'
    return t

def t_COMMA(t):
    r','
    return t

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()
    
# Productions
def p_casa(p):
	'''
	casa : HOUSE ID LBRACKET lh RBRACKET SEMICOLON
        | HOUSE ID LBRACKET lh lp RBRACKET SEMICOLON 
        | HOUSE ID LBRACKET lh lsg RBRACKET SEMICOLON 
        | HOUSE ID LBRACKET lh lag RBRACKET SEMICOLON 
        | HOUSE ID LBRACKET lh lp lsg RBRACKET SEMICOLON 
        | HOUSE ID LBRACKET lh lp lag RBRACKET SEMICOLON 
        | HOUSE ID LBRACKET lh lsg lag RBRACKET SEMICOLON
        | HOUSE ID LBRACKET lh lp lsg lag RBRACKET SEMICOLON
	'''

def p_lh(p):
	'''
	lh : h COMMA lh
        | h SEMICOLON
	'''

def p_lp(p):
	'''
	lp : p COMMA lp
        | p SEMICOLON
	'''
def p_h(p):
	'''
	h : ROOM ID LBRACKET lsl RBRACKET
        | ROOM ID LBRACKET lal RBRACKET
        | ROOM ID LBRACKET c RBRACKET
        | ROOM ID LBRACKET lsl lal RBRACKET
        | ROOM ID LBRACKET lsl c RBRACKET
        | ROOM ID LBRACKET lal c RBRACKET
        | ROOM ID LBRACKET RBRACKET
        | ROOM ID LBRACKET lsl lal c RBRACKET
	'''
def p_p(p):
	'''
	p : CORRIDOR ID LBRACKET l2id lsl RBRACKET
        | CORRIDOR ID LBRACKET l2id lal RBRACKET
        | CORRIDOR ID LBRACKET l2id c RBRACKET
        | CORRIDOR ID LBRACKET l2id lsl lal RBRACKET
        | CORRIDOR ID LBRACKET l2id lsl c RBRACKET
        | CORRIDOR ID LBRACKET l2id lal c RBRACKET
        | CORRIDOR ID LBRACKET l2id lsl lal c RBRACKET
        | CORRIDOR ID LBRACKET l2id RBRACKET
	'''
def p_l2id(p):
	'''
	l2id : ID COMMA l2id
        | ID COMMA ID SEMICOLON
	'''
def p_lsl(p):
	'''
	lsl : s COMMA lsl
        | s SEMICOLON
	'''
def p_lal(p):
	'''
	lal : a COMMA lal
        | a SEMICOLON
	'''
def p_lsg1(p):
	'''
	lsg1 : s COMMA lsg1
        | s RBRACKET SEMICOLON
	'''
def p_lsg(p):
	'''
	lsg : GLOBAL LBRACKET lsg1
	'''
def p_lag1(p):
	'''
	lag1 : a COMMA lag1
        | a RBRACKET SEMICOLON
	'''
def p_lag(p):
	'''
	lag : GLOBAL LBRACKET lag1
	'''
def p_s(p):
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
def p_a(p):
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
def p_c(p):
	'''
	c : LBRACKET lest SEMICOLON init SEMICOLON trans RBRACKET SEMICOLON
        | LBRACKET lest SEMICOLON trans RBRACKET SEMICOLON
        | LBRACKET lest SEMICOLON init SEMICOLON RBRACKET SEMICOLON
        | LBRACKET lest SEMICOLON RBRACKET SEMICOLON
	'''
def p_lest(p):
	'''
	lest :  STATE ID LBRACKET lactions RBRACKET COMMA lest
        | STATE ID LBRACKET RBRACKET COMMA lest
        | STATE ID LBRACKET lactions RBRACKET
        | STATE ID LBRACKET RBRACKET
	'''
def p_lactions(p):
	'''
	lactions : action COMMA lactions
        | action SEMICOLON
	'''
def p_action(p):
	'''
	action : ID SEQ BOOL
	'''
def p_init(p):
	'''
	init : INIT ID
	'''
def p_trans(p):
	'''
	trans : t trans
        | t
	'''
def p_t(p):
	'''
	t : ID COMMA ID COMMA COMBINATION SEMICOLON
	'''
def p_spresencia(p):
	'''
	spresencia : SPRESENCIA ID SEQ BOOL
	'''
def p_slluvia(p):
	'''
	slluvia : SLLUVIA ID SEQ BOOL
	'''
def p_siluminacion(p): 
	'''
	siluminacion : SILUMINACION OPL DOUBLE ID SEQ DOUBLE
	'''
def p_stemperatura(p):
	'''
	stemperatura : STEMPERATURA OPL DOUBLE ID SEQ DOUBLE
	'''
def p_sreloj(p):
	'''
	sreloj : SRELOJ OPL TIME ID SEQ TIME
	'''
def p_shumo(p):
	'''
	shumo : SHUMO ID SEQ BOOL
	'''
def p_sviento(p):
	'''
	sviento : SVIENTO OPL DOUBLE ID SEQ DOUBLE
	'''
def p_sintrusos(p):
	'''
	sintrusos : SINTRUSOS ID SEQ BOOL
	'''
def p_sinundacion(p):
	'''
	sinundacion : SINUNDACION ID SEQ BOOL
	'''
def p_sgas(p):
	'''
	sgas : SGAS ID SEQ BOOL
	'''
def p_apuerta(p):
	'''
	apuerta : APUERTA ID
	'''
def p_acalefaccion(p):
	'''
	acalefaccion : ACALEFACCION ID
	'''
def p_apersiana(p):
	'''
	apersiana : APERSIANA ID
	'''
def p_aluz(p):
	'''
	aluz : ALUZ ID
	'''
def p_aventana(p):
	'''
	aventana : AVENTANA ID
	'''
def p_frio(p):
	'''
	afrio : AFRIO ID
	'''
def p_agas(p):
	'''
	agas : AGAS ID
	'''
def p_atoldo(p):
	'''
	atoldo : ATOLDO ID
	'''
def p_aalarma(p):
	'''
	aalarma : AALARMA ID
	'''
def p_aemergencia(p):
	'''
	aemergencia : AEMERGENCIA ID
	'''

def p_error(p):
    print(f'Syntax error at {p.value!r}')

def main():
    ''' Main method '''
    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return

    with open(sys.argv[1], 'r+', encoding = 'utf-8') as file:
        lexer = lex()
        parser = yacc()
        parser.parse(input = file.read(), lexer = lexer, debug = 1, tracking = 1)
        #parser.parse('aabbabbbabbbcccc', lexer = lexer)

if __name__ == '__main__':
    main()