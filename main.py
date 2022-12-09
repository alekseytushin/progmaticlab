from itertools import product

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
signs = ['', ' + ', ' - ']

total_options = [x + y for (x, y) in product(digits[:-1], signs)]

total_options = [total_options[_:_ + 3] for _ in range(0, len(total_options), 3)]
total_options += [[digits[-1]]]


def solution(num):
    expressions = []

    for expr_list in product(*total_options):
        expression = "".join(expr_list)
        if eval(expression) == num:
            print(expression + ' = 200')
            expressions.append(expression)

    print(f'Total: {len(expressions)}')


if __name__ == '__main__':
    solution(200)