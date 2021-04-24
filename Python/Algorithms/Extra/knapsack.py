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

    
def max_value(items, C):
    sub_problems = [[0 for _ in range(C+1)] for i in range(len(items) + 1)]
    pred = {}
    for i in range(1, len(items) + 1):
        for j in range(1, C+1):
            if j < items[i-1].weight:
                sub_problems[i][j] = sub_problems[i-1][j]
                pred[(i,j)] = (i-1,j)
            else:
                if sub_problems[i-1][j] > sub_problems[i-1][j-items[i-1].weight] + items[i-1].value:
                    sub_problems[i][j] = sub_problems[i-1][j]
                    pred[(i,j)] = (i-1,j)
                else:
                    sub_problems[i][j] = sub_problems[i-1][j-items[i-1].weight] + items[i-1].value
                    pred[(i,j)] = (i-1,j-items[i-1].weight)
    #print(sub_problems)
    #print("Number of sub problems solved: " + str(len(sub_problems) * len(sub_problems[0])))
    #print("Max value: " + str(sub_problems[len(items)][C]))
    opt_items = []
    cell = (len(items), C)
    while cell in pred:
        if cell[1] != pred[cell][1]:
            opt_items.append(items[cell[0] - 1])
        cell = pred[cell]
    return opt_items


def top_down(items, C):
    sub_problems = {}
    for i in range(len(items)):
        sub_problems[(i,0)] = 0
    for j in range(C+1):
        sub_problems[(0,j)] = 0
    solve(items, C, sub_problems, len(items), C)
    print("Number of sub problems solved: " + str(len(sub_problems)))
    return sub_problems[(len(items), C)]


def solve(items, C, sub_problems, i, j):
    if (i-1, j) not in sub_problems:
        solve(items, C, sub_problems, i-1, j)
    if j < items[i-1].weight:
        sub_problems[(i, j)] = sub_problems[(i-1, j)]
    else:
        if (i-1, j-items[i-1].weight) not in sub_problems:
            solve(items, C, sub_problems, i-1, j-items[i-1].weight)
        sub_problems[(i, j)] = max(sub_problems[(i-1, j)], sub_problems[(i-1, j-items[i-1].weight)] + items[i-1].value)



items = [Item(1,2), Item(2,3), Item(6,6), Item(8,9)]


def time_test(f, items, C):
    start = timeit.default_timer()
    f(items, C)
    return timeit.default_timer() - start

items = create_random_items(900,100)