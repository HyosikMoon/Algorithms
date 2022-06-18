def popular_words(text: str, words: list) -> dict:
    results = {}
    text = text.lower().split()
    for word in words:
        cnt = 0
        cnt = text.count(word)
        results[word] = cnt
    return results