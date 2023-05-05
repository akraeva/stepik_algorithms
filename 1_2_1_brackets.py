# Базовые структуры данных
# 1 Расстановка скобок в коде


def pair_brackets(data):
    abc = {')': '(', ']': '[', '}': '{'}
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
            else:  # stack[-1] == abc[data[i]]
                stack.pop(-1)
                error.pop(-1)
    return error[-1]+1 if stack else 'Success'


print(pair_brackets(input()))

# Test
# print('#01', pair_brackets("([](){([])})") == 'Success')
# print('#02', pair_brackets("()[]}") == 5)
# print('#03', pair_brackets("{{[()]]")  == 7)
# print('#04', pair_brackets("{{{[][][]") == 3)
# print('#05', pair_brackets("{*{{}") == 3)
# print('#06', pair_brackets("[[*") == 2)
# print('#07', pair_brackets("{*}") == 'Success')
# print('#08', pair_brackets("{{") == 2)
# print('#09', pair_brackets("{}") == 'Success')
# print('#10', pair_brackets("") == 0)
# print('#11', pair_brackets("}") == 1)
# print('#12', pair_brackets("*{}") == 'Success')
# print('#13', pair_brackets("{{{**[][][]") == 3)
# print('#14', pair_brackets("((({[]})") == 2)
# print('#15', pair_brackets("{}([]") == 3)
# print('#16', pair_brackets("(slkj, (lk[lve]) ,l)") == 'Success')
# print('#17', pair_brackets("dasdsadsadas]]]") == 13)
# print('#18', pair_brackets("[]([]") == 3)
# print('#19', pair_brackets("{{{[][][]") == 3)
# print('#20', pair_brackets("{{[()]}") == 1)
# print('#21', pair_brackets("(slkj{lk[lsj]}") == 1)
# print('#22', pair_brackets("{}[}([]:") == 4)
