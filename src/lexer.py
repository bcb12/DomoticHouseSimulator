"""
    PYTHON MODULE TO IMPLEMENT THE LEXICAL ANALYZER OF OUR LANGUAGE: ADL
"""

import ply.lex as lex

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
    'OPL'
]

"""
    REGULAR EXPRESSIONS THAT DEFINE THE PATTERNS OF THE TOKENS
"""

t_ID = r'[a-zA-Z][a-zA-Z0-9]*'
t_SEQ = r'\:\:\='

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

def t_error(token):
    print('Illegal Character!')
    token.lexer.skip(1)


def main():
    """
        MAIN METHOD DECLARATION
    """

    lexer = lex.lex()
    #input = 'vA1 ::= sensor_presence sensor_rain sensor_light sensor_temperature'
    #input = 'sensor_time sensor_smoke actuator_door actuator_heat actuator_wblind'
    input = 'actuator_light actuator_window actuator_cold true false'
    lexer.input(input)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f'Token found: {token}')


if __name__ == '__main__':
    main()
