# Базовые структуры данных
# 2 Высота дерева


# решение прошло проверку, потому что хранятся промежуточные длины
def tree_hight_per_node(tree, len_tree):
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


count = int(input())
parents = [int(i) for i in (input().split())]
print(tree_hight_per_node(parents, count))


# решение не проходит проверку из-за рекурсии
# import sys
# sys.setrecursionlimit(20000)

# def tree_hight(tree, parent, hight):
#     if not tree:
#         return 0
#     if parent not in tree:
#         hight += 1
#         return hight
#     else:
#         hight += 1
#         return max([tree_hight(tree, i, hight) for i in range(len(tree))
#                     if tree[i] == parent])

# решения не проходит проверку: Time limit exceeded

# def tree_hight_cycle(tree, children):
#     hight = 0
#     if tree:
#         while children:
#             hight += 1
#             children = [j for j in range(len(tree)) if tree[j] in children]
#     return hight

# def tree_hight_cycle_pairs(tree, parent):
#     hight = 0
#     if tree:
#         pairs = [[tree[i], i] for i in range(len(tree))]
#         while parent:
#             hight += 1
#             parent = [j[1] for j in pairs if j[0] in parent]
#     return hight

# def tree_hight_childres_counter(tree):
#     if not tree:
#         return 0
#     length = 0
#     parent = tree.index(-1)
#     last_children = [i for i in range(count) if i not in tree]
#     for i in last_children:
#         branch_len = 1
#         parent = tree[i]
#         while parent != -1:
#             branch_len += 1
#             parent = tree[parent]
#         length = max(length, branch_len)
#     return length

# def tree_hight_childres_glossary(tree, parent):
#     if not tree:
#         return 0
#     length = 1
#     childrens = {i: tree[i] for i in range(len(tree))}
#     last_childrens = [i for i in childrens.keys()
#                        if i not in childrens.values()]
#     for i in last_childrens:
#         branch_len = 1
#         parent = childrens[i]
#         while parent != -1:
#             branch_len += 1
#             parent = childrens[parent]
#         length = max(length, branch_len)
#     return length


# def tree_height_chatgpt(parents):
#     max_height = 0
#     queue = [i for i, p in enumerate(parents) if p == -1]
#     while queue:
#         level_size = len(queue)
#         for i in range(level_size):
#             node = queue.pop(0)
#             for j, p in enumerate(parents):
#                 if p == node:
#                     queue.append(j)
#         max_height += 1
#     return max_height


# def tree_hight_childres_glossary_pop(tree):
#     length = 0
#     childrens = {i: tree[i] for i in range(len(tree))}
#     while childrens:
#         length += 1
#         last_childrens = [i for i in childrens.keys()
#                           if i not in childrens.values()]
#         for i in last_childrens:
#             childrens.pop(i)
#     return length


# def tests():
#     test_data = [
#         [10, '9 7 5 5 2 9 9 9 2 -1', 4],
#         [5, '4 -1 4 1 1', 3],
#         [5, '-1 0 4 0 3', 4],
#         [1, '-1', 1]
#     ]
#     for i in test_data:
#         parents = [int(j) for j in (i[1].split())]
#         print(tree_hight_per_node(parents, i[0]) == i[2])


# tests()
