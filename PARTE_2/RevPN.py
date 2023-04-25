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


def scan(source):
    tokens = []
    for char in source:
        if char.isdigit():
            tokens.append(Token(TokenType.NUM, char))
        elif char == '+':
            tokens.append(Token(TokenType.PLUS, char))
        elif char == '-':
            tokens.append(Token(TokenType.MINUS, char))
        elif char == '*':
            tokens.append(Token(TokenType.MULTIPLY, char))
        elif char == '/':
            tokens.append(Token(TokenType.DIVIDE, char))
        else:
            raise ValueError(f"Unexpected character: {char}")

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
        rpn_expression = file.read().split()
    return rpn_expression


if __name__ == '__main__':
    input_file_path = 'input.txt'

    rpn_expression = read_rpn_expression_from_file(input_file_path)
    try:
        token_list = scan(rpn_expression)
        print(f"Lista de tokens reconhecida: {token_list}")
        result = rpn_evaluator(token_list)
        print(f'Resultado: {result}')
    except ValueError as e:
        print(e)
