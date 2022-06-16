def checkio(data: list) -> list:
    #Your code here
    dict = {}
    for v in data:
        cnt = data.count(v)
        dict[v] = cnt
    for (key, cnt) in zip(dict.keys(), dict.values()):
        if cnt == 1:
            data.remove(key)
    return data