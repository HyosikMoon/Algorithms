def backward_string_by_word(text: str) -> str:
    text = text.split(' ')
    for i, w in enumerate(text):
        if w != '':
            text[i] = w[::-1]
    return ' '.join(text)

print(backward_string_by_word('hello world'))