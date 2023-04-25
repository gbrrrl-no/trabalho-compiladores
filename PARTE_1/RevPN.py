def rpn_evaluator(rpn_expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in rpn_expression:
        if token not in operators:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]


def read_rpn_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        rpn_expression = file.read().split()
    return rpn_expression


if __name__ == '__main__':
    input_file_path = './input.txt'

    rpn_expression = read_rpn_expression_from_file(input_file_path)
    result = rpn_evaluator(rpn_expression)

    print(f'Resultado: {result}')
