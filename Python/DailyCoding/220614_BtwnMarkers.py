class Solution():
    def between_markers(text: str, begin: str, end: str) -> str:
        if begin not in text:
            return 
        strIdx = text.index(begin)
        endIdx = strIdx + text[strIdx:].index(end)
        return text[strIdx+1:endIdx]