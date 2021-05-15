import timeit
import random

class Item:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return "Item(" + str(self.weight) + ", " + str(self.value) + ")" 


def create_random_items(n, k):
    return [Item(random.randint(1,k), random.randint(1,k)) for _ in range(n)]


# def max_value(items, L):
#     ks = [[0 for _ in range(L+1)] for i in range(len(items) + 1)]
#     pred = {}
#     #  ks(i, c) = Case1. Include i: Vi + ks(i - 1, c - Wi)
#     #             Case2. Exclude i: ks(i - 1, c)
#     #  ks(i, c) = max(Vi + ks(i - 1, c - Wi), ks(i - 1, c))
#     for i in range(1, len(items) + 1):
#         for c in range(1, L+1):
#             # If i-th weight is greater than the limit weight c, then ks(i, c) -> ks(i-1, c)
#             # Check [c-items[i-1].weight]
#             if c < items[i-1].weight:
#                 ks[i][c] = ks[i-1][c]
#                 pred[(i,c)] = (i-1,c)
#             else:
#                 # If Case2 > Case1, then ks(i, c) -> Case2
#                 if ks[i-1][c] > ks[i-1][c-items[i-1].weight] + items[i-1].value:
#                     ks[i][c] = ks[i-1][c]
#                     pred[(i,c)] = (i-1,c)
#                 else:
#                     # ks(i, c) -> Case1
#                     ks[i][c] = ks[i-1][c-items[i-1].weight] + items[i-1].value
#                     pred[(i,c)] = (i-1,c-items[i-1].weight)
#     print(ks)
#     print("Number of sub problems solved: " + str(len(ks) * len(ks[0])))
#     print("Max value: " + str(ks[len(items)][L]))
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


# def max_value(items, L):
#     ks = [[0 for _ in range(L + 1)] for i in range(len(items) + 1)]
#     pred = {}
#     # There are two cases to find the ks[i][c]
#     # i) Case1. Include i : ks[i][c] = i.value + ks[i][c - i.weight]
#     # ii) Case2. Exclude i : ks[i][c] = ks[i - 1][c]
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             # When the item's weight is larger than the limit c, then ks[i][c] = ks[i - 1][c]
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 # If Case2 > Case1, then ks[i][c] = Case2
#                 if ks[i - 1][c] > ks[i - 1][c - items[i - 1].weight] + items[i - 1].value:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#                 # Else, ks[i][c] = Case1
#                 else:
#                     ks[i][c] = ks[i - 1][c - items[i - 1].weight] + items[i - 1].value
#                     pred[(i, c)] = (i - 1, c - items[i - 1].weight)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         # If cell[1] != pred[cell][1] -> it means Case1 (Include i) -> append ith item
#         # If cell[1] == pred[cell][1] -> it means Case2 (Exclude i) -> move next cell(pred cell)
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


# def max_value(items, L):
#     ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
#     pred = {}
#     # insert values in ks map
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 # Include i
#                 if ks[i - 1][c] < items[i - 1].value + ks[i - 1][c - items[i - 1].weight]:
#                     ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
#                     pred[(i, c)] = (i, c - items[i - 1].weight)
#                 # Exclude i
#                 else:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


# def max_value(items, L):
#     ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
#     pred = {}
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 # Exclude i < Include i -> ks = Include i
#                 if ks[i - 1][c] < items[i - 1].value + ks[i - 1][c - items[i - 1].weight]:
#                     ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
#                     pred[(i, c)] = (i - 1, c - items[i - 1].weight)
#                 # Exclude i > Include i -> ks = Exclude i
#                 else:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


# def max_value(items, L):
#     ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
#     pred = {}
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 # include i
#                 if items[i - 1].value + ks[i - 1][c - items[i - 1].weight] > ks[i - 1][c]:
#                     ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
#                     pred[(i, c)] = (i - 1, c - items[i - 1].weight)
#                 # exclude i
#                 else:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


# def max_value(items, L):
#     ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
#     pred = {}
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 if items[i - 1].value + ks[i - 1][c - items[i - 1].weight] > ks[i - 1][c]:
#                     ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
#                     pred[(i, c)] = (i - 1, c - items[i - 1].weight)
#                 else:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


## Knapsack problem
# def knapsack(items, L):
#     ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
#     pred = {}
#     for i in range(1, len(items) + 1):
#         for c in range(1, L + 1):
#             if c < items[i - 1].weight:
#                 ks[i][c] = ks[i - 1][c]
#                 pred[(i, c)] = (i - 1, c)
#             else:
#                 if items[i - 1].value + ks[i - 1][c - items[i - 1].weight] > ks[i - 1][c]:
#                     ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
#                     pred[(i, c)] = (i - 1, c - items[i - 1].weight)
#                 else:
#                     ks[i][c] = ks[i - 1][c]
#                     pred[(i, c)] = (i - 1, c)
#     opt_items = []
#     cell = (len(items), L)
#     while cell in pred:
#         if cell[1] != pred[cell][1]:
#             opt_items.append(items[cell[0] - 1])
#         cell = pred[cell]
#     return opt_items


## Knapsack problem
def knapsack(items, L):
    ks = [[0 for _ in range(L + 1)] for _ in range(len(items) + 1)]
    pred = {}
    for i in range(1, len(items) + 1):
        for c in range(1, L + 1):
            if c < items[i - 1].weight:
                ks[i][c] = ks[i - 1][c]
                pred[(i, c)] = (i - 1, c)
            else:
                if items[i - 1].value + ks[i - 1][c - items[i - 1].weight] > ks[i - 1][c]:
                    ks[i][c] = items[i - 1].value + ks[i - 1][c - items[i - 1].weight]
                    pred[(i, c)] = (i - 1, c - items[i - 1].weight)
                else:
                    ks[i][c] = ks[i - 1][c]
                    pred[(i, c)] = (i - 1, c)
    opt_items = []
    cell = (len(items), L)
    while cell in pred:
        if cell[1] != pred[cell][1]:
            opt_items.append(items[cell[0] - 1])
        cell = pred[cell]
    return opt_items


def top_down(items, L):
    sub_problems = {}
    for i in range(len(items)):
        sub_problems[(i,0)] = 0
    for c in range(L+1):
        sub_problems[(0,c)] = 0
    solve(items, L, sub_problems, len(items), L)
    print("Number of sub problems solved: " + str(len(sub_problems)))
    return sub_problems[(len(items), L)]


def solve(items, L, sub_problems, i, c):
    if (i-1, c) not in sub_problems:
        solve(items, L, sub_problems, i-1, c)

    if c < items[i-1].weight:
        sub_problems[(i, c)] = sub_problems[(i-1, c)]
    else:
        if (i-1, c-items[i-1].weight) not in sub_problems:
            solve(items, L, sub_problems, i-1, c-items[i-1].weight)
        sub_problems[(i, c)] = max(sub_problems[(i-1, c)], sub_problems[(i-1, c-items[i-1].weight)] + items[i-1].value)


items = [Item(1,2), Item(2,3), Item(6,6), Item(8,9)]
print(knapsack(items, 10))

# def time_test(f, items, L):
#     start = timeit.default_timer()
#     f(items, L)
#     return timeit.default_timer() - start

# items = create_random_items(900,100)