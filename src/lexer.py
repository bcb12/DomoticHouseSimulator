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

def print_token(token):
    ''' METHOD FOR PRINTING A TOKEN '''
    logging.info('Token found :- Type: %s , Value: %s , Line: %s , Column: %s', token.type, token.value, token.lineno, find_column(INPUT_CHAIN, token))


keywords = {
    'sensor_presence' : 'SPRESENCIA' ,
    'sensor_rain' : 'SLLUVIA',
    'sensor_light' : 'SILUMINACION',
    'sensor_temperature' : 'STEMPERATURA',
    'sensor_time' : 'SRELOJ',
    'sensor_smoke' : 'SHUMO',
    'actuator_door' : 'APUERTA',
    'actuator_heat' : 'ACALEFACCION',
    'actuator_wblind' : 'APERSIANA',
    'actuator_light' : 'ALUZ',
    'actuator_window' : 'AVENTANA',
    'actuator_cold' : 'AFRIO',
    'room' : 'ROOM',
    'house' : 'HOUSE',
    'corridor' : 'CORRIDOR',
    'global' : 'GLOBAL',
    'state' : 'STATE',
    'init' : 'INIT',
    'eqlow' : 'OPL',
    'eq' : 'OPL',
    'equp' : 'OPL',
    'up' : 'OPL',
    'low' : 'OPL',
    'true' : 'BOOL',
    'false' : 'BOOL',
}

tokens = [
    'ID',
    'SEQ',
    'DOUBLE',
    'TIME',
    'COMBINATION',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'COMMA'
] + list(set(keywords.values()))

"""
    REGULAR EXPRESSIONS THAT DEFINE THE PATTERNS OF THE TOKENS
"""

t_COMBINATION = r'(0|1)+'
t_SEQ = r'\:\='
t_SEMICOLON = r';'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_COMMA = r','
t_ignore = r' '

def t_ID(token):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    token.type = keywords.get(token.value, 'ID')
    return token

def t_BOOL(token):
    r'true|false'
    token.type = 'BOOL'
    return token

def t_DOUBLE(token):
    r'\-?[0-9]([0-9]*)\.([0-9]+)'
    token.type = 'DOUBLE'
    return token

def t_TIME(token):
    r'((0|1)[0-9] | 2[0-3])\:[0-5][0-9]'
    token.type = 'TIME'
    return token

def t_newline(token):
    r'\n+'
    token.lexer.lineno += len(token.value)

def t_ignore_COMMENT(token):
    r'/\*(.|\n)*\*/'
    print_token(token)

def t_error_date(token):
    r'[0-9][0-9]\:[0-9][0-9]'
    logging.error('Illegal date in: %s , Line: %s , Column: %s', token.value, token.lineno, find_column(INPUT_CHAIN, token))


def t_error_comment_open(token):
    r'/\*(.|\n)*'
    logging.error('Paranthesis not closed in: %s , Line: %s , Column: %s', token.value, token.lineno, find_column(INPUT_CHAIN, token))
    token.lexer.skip(1)

def t_error(token):
    logging.error('Illegal Character for the chain: %s , Line: %s , Column: %s', token.value, token.lineno, find_column(INPUT_CHAIN, token))
    token.lexer.skip(1)

def find_column(text, token):
    line_start = text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def main():
    """
        MAIN METHOD DECLARATION
    """
    global INPUT_CHAIN
    lexer = lex.lex()

    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return

    with open(sys.argv[1], 'r+', encoding = 'utf-8') as file:
        lexer.input(file.read())
        
    INPUT_CHAIN = lexer.lexdata

    while True:
        token = lexer.token()
        if not token:
            break
        print_token(token)

if __name__ == '__main__':
    main()
