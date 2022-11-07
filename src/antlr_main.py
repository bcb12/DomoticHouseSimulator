''' MODULE FOR IMPLMENTING THE MAIN FOR ANTLR '''

import sys
import logging
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from antlr4 import InputStream
from DHGrammarLexer import DHGrammarLexer
from DHGrammarListener import DHGrammarListener
from DHGrammarParser import DHGrammarParser

logging.basicConfig(
    format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

def main():
    ''' MAIN METHOD '''
    if len(sys.argv) == 1:
        logging.error('No file was provided. Try to provide a text file for the lexer to work.')
        return

    with open(sys.argv[1], 'r+', encoding = 'utf-8') as file:
        lexer = DHGrammarLexer(InputStream(file.read()))
        token_stream = CommonTokenStream(lexer)
        parser = DHGrammarParser(token_stream)

        syntax_tree = parser.casa()
        listener = DHGrammarListener()
        walker = ParseTreeWalker()
        walker.walk(listener, syntax_tree)

if __name__ == '__main__':
    main()
