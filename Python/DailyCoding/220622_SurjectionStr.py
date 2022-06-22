def isometric_strings(a, b):
    results = {}
    for i, c in enumerate(a):
        if c in results:
            if results[c] != b[i]: return False
        else:
            results[a[i]] = b[i]
    return True