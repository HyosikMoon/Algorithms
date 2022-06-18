class Solution:
    def count_digits(text: str) -> int:
    # your code here
        results = []
        text = text.split()
        cnt = 0
        for w in text:
            for c in w:
                if c in '0123456789':
                    cnt += 1
        return cnt