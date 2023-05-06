# Базовые структуры данных
# 4 Стек с поддержкой максимума
# Stack with Maximum Support


def special_stack(count, command):
    max = []
    stack = []
    test_result = ''
    for i in command:
        if max and i == 'max':
            test_result += str(max[-1]) + '\n'
            print(max[-1])
        elif i == 'pop':
            if stack:
                if stack[-1] == max[-1]:
                    max.pop(-1)
                stack.pop(-1)
        elif i.split()[0] == 'push':
            elem = int(i.split()[1])
            stack.append(elem)
            if not max or elem >= max[-1]:
                max.append(elem)
    return test_result.strip()


n = int(input)
data = [input() for i in range(n)]
special_stack(n, data)


def test():
    tests = [
        [3, 'push 1\npush 7\npop', '', '01'],
        [5, 'push 2\npush 1\nmax\npop\nmax', '2\n2', '02'],
        [6, 'push 7\npush 1\npush 7\nmax\npop\nmax', '7\n7', '03'],
        [5, 'push 1\npush 2\nmax\npop\nmax', '2\n1', '04'],
        [10, 'push 2\npush 3\npush 9\npush 7\npush 2\nmax\nmax\nmax\npop\nmax',
         '9\n9\n9\n9', '05']
    ]
    for i in tests:
        print(i[3], special_stack(i[0], i[1].splitlines()) == i[2])
