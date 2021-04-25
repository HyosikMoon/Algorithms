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


def max_value(items, L):
    sub_problems = [[0 for _ in range(L+1)] for i in range(len(items) + 1)]
    pred = {}
    #  ks(i, c) = Case1. Include i  or  Case2. Exclude i case
    #  ks(i, c) = max(ks(i - 1, c), Vi + ks(i - 1, c - Wi))
    for i in range(1, len(items) + 1):
        for c in range(1, L+1):
            # If Exclude i case's weight is greater than limit weight c, then ks(i, c) -> ks(i-1, c)
            if c < items[i-1].weight:
                sub_problems[i][c] = sub_problems[i-1][c]
                pred[(i,c)] = (i-1,c)
            else:
                # Case2. If Exclude i case is greater than Include i case then ks(i, c) -> Exclude i case
                if sub_problems[i-1][c] > sub_problems[i-1][c-items[i-1].weight] + items[i-1].value:
                    sub_problems[i][c] = sub_problems[i-1][c]
                    pred[(i,c)] = (i-1,c)
                else:
                    # Case1. ks(i,c) -> Include i case
                    sub_problems[i][c] = sub_problems[i-1][c-items[i-1].weight] + items[i-1].value
                    pred[(i,c)] = (i-1,c-items[i-1].weight)
    #print(sub_problems)
    #print("Number of sub problems solved: " + str(len(sub_problems) * len(sub_problems[0])))
    #print("Max value: " + str(sub_problems[len(items)][C]))
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


def time_test(f, items, L):
    start = timeit.default_timer()
    f(items, L)
    return timeit.default_timer() - start

items = create_random_items(900,100)