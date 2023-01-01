''' MODULE FOR IMPLMENTING THE MAIN FOR ANTLR '''

import sys
import logging
from antlr4 import CommonTokenStream
from antlr4 import ParseTreeWalker
from antlr4 import InputStream
from DHSemanticGrammarLexer import DHSemanticGrammarLexer
from DHSemanticGrammarListener import DHSemanticGrammarListener
from DHSemanticGrammarParser import DHSemanticGrammarParser

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
        # lexer
        lexer = DHSemanticGrammarLexer(InputStream(file.read()))
        stream = CommonTokenStream(lexer)
        # parser
        parser = DHSemanticGrammarParser(stream)
        tree = parser.casa()
        print(tree.data)

if __name__ == '__main__':
    main()
