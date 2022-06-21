def words_order(text: str, words: list) -> bool:
    indices = []
    text = text.split()
    words2 = words.copy()
    for w in words2:
        words.remove(w)
        if w in words: return False
        if w not in text: return False
        indices.append(text.index(w))

    for i in range(len(indices) - 1):
        if indices[i] < indices[i+1]: continue
        else: return False

    return True

words_order("hi world im here", ["here", "world"])