def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    
    dict = {}
    diff = 0
    lst = list(values)
    lst.sort()
    for i, v in enumerate(lst):
        diff = abs(v - one)
        dict[i]=diff
    
    minIdx = list(dict.values()).index(min(dict.values()))
    return lst[minIdx]

