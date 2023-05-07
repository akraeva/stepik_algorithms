# Базовые структуры данных
# 5 Максимум в скользящем окне
# Sliding Window Maximum

# Failed test. Time limit exceeded
# def max_in_subarray(length, array, size):
#     res = [max(array[i: i + size]) for i in range(length + 1 - size)]
#     return ' '.join([str(i) for i in res])


def max_in_subarray(length, array, size):
    stack_in, stack_out, res = [[], [], []]
    max_in, max_out = [0, 0]
    for i in array:
        max_in = max(max_in, i)
        stack_in.append([i, max_in])
        if len(stack_in) == size:
            while stack_in:
                max_out = max(max_out, stack_in[-1][0])
                stack_out.append([stack_in.pop(-1)[0], max_out])
            max_in = 0
        if stack_out:
            res.append(max(max_out, max_in))
            stack_out.pop(-1)
            max_out = stack_out[-1][-1] if stack_out else 0
    return ' '.join([str(i) for i in res])


# n = int(input())
# data = [int(i) for i in input().split()]
# window = int(input())
# print(max_in_subarray(n, data, window))


def test():
    tests = [
             ['01', 3, '2 1 5', 1, '2 1 5'],
             ['02', 8, '2 7 3 1 5 2 6 2', 4, '7 7 5 6 6'],
             ['03', 15, '73 65 24 14 44 20 65 97 27 6 42 1 6 41 16', 7,
              '73 97 97 97 97 97 97 97 42'],
             ['04', 15, '28 7 64 40 68 86 80 93 4 53 32 56 68 18 59', 12,
              '93 93 93 93'],
             ['05', 15, '16 79 20 19 43 72 78 33 40 52 70 79 66 43 60', 12,
              '79 79 79 79'],
             ['06', 15, '34 51 61 90 26 84 2 25 7 8 25 78 21 47 25 ', 3,
              '61 90 90 90 84 84 25 25 25 78 78 78 47'],
             ['07', 15, '27 83 29 77 6 3 48 2 16 72 46 38 55 2 58', 5,
              '83 83 77 77 48 72 72 72 72 72 58']
           ]
    for i in tests:
        print(i[0],
              max_in_subarray(i[1], [int(j) for j in i[2].split()], i[3])
              == i[4])
