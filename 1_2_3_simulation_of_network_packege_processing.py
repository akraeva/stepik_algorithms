# Базовые структуры данных
# 3 Симуляция обработки сетевых пакетов
# Simulation of network packege processing


def packege_processor(buf_size, count, packages):
    result = []
    if count != 0:
        time = packages[0][0]
        buf = []
        for i in packages:
            if len(buf) == buf_size and i[0] < buf[0]:
                result.append(-1)
            else:
                if buf and i[0] > buf[-1]:
                    time += i[0] - buf[-1]
                result.append(time)
                if len(buf) == buf_size:
                    buf.pop(0)
                time += i[-1]
                buf.append(time)
    return result


# size, n = [int(i) for i in input().split()]
# data = [[int(i) for i in input().split()] for j in range(n)]
# [print(i) for i in packege_processor(size, n, data)]


def test():
    tests = [
             ['01', '1 0', '', ''],
             ['02', '1 1', '0 0', '0'],
             ['03', '1 1', '0 1', '0'],
             ['04', '1 2', '0 1\n0 1', '0 -1'],
             ['05', '1 2', '0 1\n1 1', '0 1'],
             ['06', '2 8', '0 0\n0 0\n0 0\n1 0\n1 0\n1 1\n1 2\n1 3', '0 0 0 1 1 1 2 -1'],
             ['07', '2 8', '0 0\n0 0\n0 0\n1 1\n1 0\n1 0\n1 2\n1 3', '0 0 0 1 2 -1 -1 -1'],
             ['08', '1 5', '999999 1\n1000000 0\n1000000 1\n1000000 0\n1000000 0', '999999 1000000 1000000 -1 -1'],
             ['09', '3 6', '0 7\n0 0\n2 0\n3 3\n4 0\n5 0', '0 7 7 -1 -1 -1'],
             ['10', '2 6', '0 2\n0 0\n2 0\n3 0\n4 0\n5 0', '0 2 2 3 4 5'],
             ['11', '2 5', '2 9\n4 8\n10 9\n15 2\n19 1', '2 11 -1 19 21'],
             ['12', '1 2', '0 1\n10 10', '0 10'],
             ['13', '2 3', '0 0\n10 0\n10 0', '0 10 10'],
             ['14', '4 5', '0 7\n2 7\n4 7\n6 7\n21 7', '0 7 14 21 28'],
             ['15', '3 6', '2 2\n2 3\n3 1\n3 4\n10 2', '2 4 7 -1 10'],
             ]
    for i in tests:
        test_size, test_n = [int(j) for j in i[1].split()]
        test_data = [[int(j) for j in k.split()] for k in i[2].splitlines()]
        print(i[0], ' '.join([str(i) for i in
              packege_processor(test_size, test_n, test_data)]) == i[3])


test()
