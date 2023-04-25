import re
from enum import Enum


class TokenType(Enum):
    NUM = 'NUM'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'


class Token:
    def __init__(self, token_type, lexeme):
        self.type = token_type
        self.lexeme = lexeme

    def __repr__(self):
        return f"Token [type={self.type}, lexeme={self.lexeme}]"


class Regex:
    @staticmethod
    def scan(source):
        pattern = re.compile(r'(\d+|[+\-*/])')
        return pattern.findall(source)


def scan_using_regex(source):
    regex = Regex()
    return regex.scan(source)


def tokenize(rpn_expression):
    tokens = []
    for match in rpn_expression:
        if match.isdigit():
            tokens.append(Token(TokenType.NUM, match))
        else:
            if match == '+':
                tokens.append(Token(TokenType.PLUS, match))
            elif match == '-':
                tokens.append(Token(TokenType.MINUS, match))
            elif match == '*':
                tokens.append(Token(TokenType.MULTIPLY, match))
            elif match == '/':
                tokens.append(Token(TokenType.DIVIDE, match))

    return tokens


def rpn_evaluator(token_list):
    stack = []

    for token in token_list:
        if token.type == TokenType.NUM:
            stack.append(float(token.lexeme))
        else:
            b = stack.pop()
            a = stack.pop()
            if token.type == TokenType.PLUS:
                stack.append(a + b)
            elif token.type == TokenType.MINUS:
                stack.append(a - b)
            elif token.type == TokenType.MULTIPLY:
                stack.append(a * b)
            elif token.type == TokenType.DIVIDE:
                stack.append(a / b)

    return stack[0]


def read_rpn_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        rpn_expression = file.read()
    return rpn_expression


if __name__ == '__main__':
    input_file_path = 'input.txt'

    rpn_expression = read_rpn_expression_from_file(input_file_path)
    try:
        rpn_expression_scanned = scan_using_regex(rpn_expression)
        token_list = tokenize(rpn_expression_scanned)
        print(f"Lista de tokens reconhecida: {token_list}")
        result = rpn_evaluator(token_list)
        print(f'Resultado: {result}')
    except ValueError as e:
        print(e)
