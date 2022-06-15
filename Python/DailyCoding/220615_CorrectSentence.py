class Solution:
    def correct_sentence(text: str) -> str:
        f = text[0].upper()
        if text[-1] == '.': 
            l = text[-1]
            text = text[1:-1]
        else:
            l = '.'
            text = text[1:]

        return f + text + l