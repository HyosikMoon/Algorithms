def frequency_sort(items):
    dict = {}
    for e in items:
        dict[e] = items.count(e)

    results = []
    for _ in range(len(dict)):
        maxKey = max(dict, key=lambda x: dict[x])
        maxValue = dict.pop(maxKey)
        for _ in range(maxValue):
            results.append(maxKey)
    
    return results

print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))