def is_acceptable_password(text:str) -> int:
    # more than 6 letters
    if len(text) < 6: return False
    # 'password' not permitted
    if 'password' in text.lower(): return False

    # include digit and letter
    digit = False
    char = False
    for c in text:
        if c in '1234567890':
            digit = True
        if 65 <= ord(c) <= 122:
            char = True

    # 3 different letters or digits
    letters = []
    digits = []
    for c in text:
        if 48 <= ord(c) <= 57:
            digits.append(c)
        else:
            letters.append(c)
    if len(set(digits)) + len(set(letters)) < 3:
        return False

    # more than 9 digits
    if len(text) > 9 and not char: return True
    if len(text) > 9 and not digit: return True

    return digit and char

print(is_acceptable_password("aaaaaabbbbb"))