def is_all_upper(text: str) -> bool:
    # your code here
    text = text.replace(' ', '')
    if text == '': return False
    
    letter = False
    for c in text:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': letter = True
        if c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890': return False
    return letter