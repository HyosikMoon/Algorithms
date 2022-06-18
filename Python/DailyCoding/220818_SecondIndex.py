def second_index(text: str, symbol: str) -> int or None:
    if text.count(symbol) >= 2:
        fst = text.index(symbol)
        text = text[fst+1:]
        snd = text.index(symbol) + fst + 1
    else:
        return
    return snd

print(second_index("hi", " "))