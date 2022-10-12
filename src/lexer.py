"""
    PYTHON MODULE TO IMPLEMENT THE LEXICAL ANALYZER OF OUR LANGUAGE: ADL
"""

import logging
import sys
import ply.lex as lex

logging.basicConfig(
    format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

tokens = [
    'ID',
    'SEQ',
    'SPRESENCIA',
    'SLLUVIA',
    'SILUMINACION',
    'STEMPERATURA',
    'SRELOJ',
    'SHUMO',
    'APUERTA',
    'ACALEFACCION',
    'APERSIANA',
    'ALUZ',
    'AVENTANA',
    'AFRIO',
    'BOOL',
    'DOUBLE',
    'TIME',
    'COMBINATION',
    'HOUSE',
    'ROOM',
    'CORRIDOR',
    'GLOBAL',
    'STATE',
    'INIT',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'OPL',
    'COMMA'
]

"""
    REGULAR EXPRESSIONS THAT DEFINE THE PATTERNS OF THE TOKENS
"""

t_ID = r'[a-zA-Z][a-zA-Z0-9]*'
t_COMBINATION = r'(0|1)+'
t_DOUBLE = r'\-?(0|[1-9][0-9]*)\.([0-9]+)'
t_TIME = r'((0|1)[0-9] | 2[0-3])\:[0-5][0-9]'
t_SEQ = r'\:\='
t_SEMICOLON = r';'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_COMMA = r','

t_ignore = r' '

def t_SPRESENCIA(token):
    r'sensor_presence'
    token.type = 'SPRESENCIA'
    return token

def t_SLLUVIA(token):
    r'sensor_rain'
    token.type = 'SLLUVIA'
    return token

def t_SILUMINACION(token):
    r'sensor_light'
    token.type = 'SILUMINACION'
    return token

def t_STEMPERATURA(token):
    r'sensor_temperature'
    token.type = 'STEMPERATURA'
    return token

def t_SRELOJ(token):
    r'sensor_time'
    token.type = 'SRELOJ'
    return token

def t_SHUMO(token):
    r'sensor_smoke'
    token.type = 'SHUMO'
    return token

def t_APUERTA(token):
    r'actuator_door'
    token.type = 'APUERTA'
    return token

def t_ACALEFACCION(token):
    r'actuator_heat'
    token.type = 'ACALEFACCION'
    return token

def t_APERSIANA(token):
    r'actuator_wblind'
    token.type = 'APERSIANA'
    return token

def t_ALUZ(token):
    r'actuator_light'
    token.type = 'ALUZ'
    return token

def t_AVENTANA(token):
    r'actuator_window'
    token.type = 'AVENTANA'
    return token

def t_AFRIO(token):
    r'actuator_cold'
    token.type = 'AFRIO'
    return token

def t_BOOL(token):
    r'true|false'
    token.type = 'BOOL'
    return token

def t_HOUSE(token):
    r'house'
    token.type = 'HOUSE'
    return token

def t_ROOM(token):
    r'room'
    token.type = 'ROOM'
    return token

def t_CORRIDOR(token):
    r'corridor'
    token.type = 'CORRIDOR'
    return token

def t_GLOBAL(token):
    r'global'
    token.type = 'GLOBAL'
    return token

def t_STATE(token):
    r'state'
    token.type = 'STATE'
    return token

def t_INIT(token):
    r'init'
    token.type = 'INIT'
    return token

def t_OPL(token):
    r'eqlow|equp|eq|low|up'
    token.type = 'OPL'
    return token

def t_newline(token):
    r'\n+'

def t_error(token):
    logging.error('Illegal Character: %s', token)
    token.lexer.skip(1)

def main():
    """
        MAIN METHOD DECLARATION
    """

    lexer = lex.lex()

    if(len(sys.argv) == 1):
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')

    with open(sys.argv[1], 'r+', encoding = 'utf-8') as file:
        lexer.input(file.read())

    while True:
        token = lexer.token()
        if not token:
            break
        logging.info('Token found: %s', token)


if __name__ == '__main__':
    main()
