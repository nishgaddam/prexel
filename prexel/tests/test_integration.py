import unittest

from prexel.parser.lexer import Lexer
from prexel.parser.interpreter import Interpreter, InterpreterException
from prexel.encoders.pretty_print_encoder import PrettyPrintEncoder
from prexel.encoders.source_code_encoder import SourceCodeEncoder


class TestIntegration(unittest.TestCase):
    def test_full(self):
        text = "|Room >> Kitchen color square_feet show_kitchen() " \
               "<>*-cupboards--1> Cupboard open()"
        lexer = Lexer(text)

        # Interpret the tokens and create a diagram object
        try:
            interpreter = Interpreter(lexer)
            diagram = interpreter.evaluate()
        except InterpreterException as e:
            print(e)

        # Pretty-print encode diagram for output to the view
        pretty_print = PrettyPrintEncoder()
        result = pretty_print.generate(diagram)

        print(result)

        # Source-code encode diagram for files
        source_code = SourceCodeEncoder()
        classes = source_code.generate(diagram)

        for class_item in classes:
            print(class_item)
            