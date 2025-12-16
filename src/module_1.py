# Stepick.org — Алгоритмы: теория и практика. Структуры данных
# 1. Базовые структуры данных

# === Задача 1 ===


def pair_brackets(data):
    """Задача 1. Расстановка скобок в коде"""
    abc = {")": "(", "]": "[", "}": "{"}
    stack = []
    error = [0]
    if not data:
        return 0
    for i in range(len(data)):
        if data[i] in abc.values():
            stack.append(data[i])
            error.append(i)
        elif data[i] in abc.keys():
            if not stack or stack[-1] != abc[data[i]]:
                return i + 1
            else:
                stack.pop(-1)
                error.pop(-1)
    return error[-1] + 1 if stack else "Success"


m_1_2_1 = pair_brackets
# print(m_1_2_1(input()))


# === Задача 2 ===


def tree_hight_per_node(tree, len_tree):
    """Задача 2. Высота дерева"""
    if not tree:
        return 0
    heights = {-1: 0}
    for i in range(len_tree):
        if i not in heights:
            branch_len = 1
            parent = tree[i]
            while parent not in heights:
                parent = tree[parent]
                branch_len += 1
            heights[i] = branch_len + heights[parent]
    return max(heights.values())


# count = int(input())
# parents = [int(i) for i in (input().split())]
# print(tree_hight_per_node(parents, count))
m_1_2_2 = tree_hight_per_node


# === Задача 3 ===


def packege_processor(buf_size, count, packages):
    """Задача 3. Симуляция обработки сетевых пакетов"""
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
m_1_2_3 = packege_processor


# === Задача 4 ===


def special_stack(count, command):
    """Задача 4. Стек с поддержкой максимума"""
    max = []
    stack = []
    test_result = ""
    for i in command:
        if max and i == "max":
            test_result += str(max[-1]) + "\n"
            print(max[-1])
        elif i == "pop":
            if stack:
                if stack[-1] == max[-1]:
                    max.pop(-1)
                stack.pop(-1)
        elif i.split()[0] == "push":
            elem = int(i.split()[1])
            stack.append(elem)
            if not max or elem >= max[-1]:
                max.append(elem)
    return test_result.strip()


# n = int(input())
# data = [input() for i in range(n)]
# special_stack(n, data)
m_1_2_4 = special_stack


# === Задача 5 ===


def max_in_subarray(length, array, size):
    """Задача 5. Максимум в скользящем окне"""
    stack_in, stack_out, res = [], [], []
    max_in, max_out = 0, 0
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
    return " ".join([str(i) for i in res])


# n = int(input())
# data = [int(i) for i in input().split()]
# window = int(input())
# print(max_in_subarray(n, data, window))

m_1_2_5 = max_in_subarray
