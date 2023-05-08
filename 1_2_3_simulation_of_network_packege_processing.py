# Базовые структуры данных
# 3 Симуляция обработки сетевых пакетов
# Simulation of network packege processing


def packege_processor(buf_size, count, packages):
    if count != 0:
        buf = []
        time = packages[0][0]
        while packages:
            if len(buf) < buf_size:
                time += packages[0][0] - buf[-1] if buf and packages[0][0] > buf[-1] else 0
                print(time)
                time = time + packages[0][-1]
                buf.append(time)
            elif packages[0][0] < buf[0]:
                print(-1)
            else:
                
                time += packages[0][0] - buf[-1] if buf and packages[0][0] > buf[-1] else 0
                print(time)
                buf.pop(0)
                time = time + packages[0][-1]
                buf.append(time)
            packages.pop(0)



# size, n = [int(i) for i in input().split()]
# data = [[int(i) for i in input().split()] for j in range(n)]
# packege_processor(size, n, data)


def test():
    tests = [
            #  ['01', '1 0', '', ''],
            #  ['02', '1 1', '0 0', '0'],
            #  ['03', '1 1', '0 1', '0'],
            #  ['04', '1 2', '0 1\n0 1', '0 -1'],
            #  ['05', '1 2', '0 1\n1 1', '0 1'],
            #  ['06', '2 8', '0 0\n0 0\n0 0\n1 0\n1 0\n1 1\n1 2\n1 3', '0 0 0 1 1 1 2 -1'],
            #  ['07', '2 8', '0 0\n0 0\n0 0\n1 1\n1 0\n1 0\n1 2\n1 3', '0 0 0 1 2 -1 -1 -1'],
            #  ['08', '1 5', '999999 1\n1000000 0\n1000000 1\n1000000 0\n1000000 0', '999999 1000000 1000000 -1 -1'],
            #  ['09', '3 6', '0 7\n0 0\n2 0\n3 3\n4 0\n5 0', '0 7 7 -1 -1 -1'],
            #  ['10', '2 6', '0 2\n0 0\n2 0\n3 0\n4 0\n5 0', '0 2 2 3 4 5'],
            #  ['11', '2 5', '2 9\n4 8\n10 9\n15 2\n19 1', '2 11 -1 19 21'],
            #   ['12', '1 2', '0 1\n10 10', '0 10'],
             ['13', '2 3', '0 0\n10 0\n10 0', '0 10 10'],
             ['14', '4 5', '0 7\n2 7\n4 7\n6 7\n21 7', '']
             ]
    for i in tests:
        test_size, test_n = [int(j) for j in i[1].split()]
        test_data = [[int(j) for j in k.split()] for k in i[2].splitlines()]
        print('\n', i[0])
        print(i[3])
        packege_processor(test_size, test_n, test_data)


test()
