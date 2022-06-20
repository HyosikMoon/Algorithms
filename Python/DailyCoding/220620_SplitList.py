def split_list(items: list) -> list:
    # your code here
    if len(items)%2 == 0:
        m = int(len(items)/2)
        return [items[:m], items[m:]]
    else:
        m = int(len(items)/2)
        return [items[:m+1], items[m+1:]]
