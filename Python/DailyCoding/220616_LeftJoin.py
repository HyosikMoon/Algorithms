class Solution:
    def leftJoin(self, phrases: tuple) -> str:
        words = '' + phrases[0]
        phrases = phrases[1:]
        for w in phrases:
            if w != '':
                words += ',' + w
        return words.replace('right', 'left')

sol = Solution()
print(sol.leftJoin(("left", "right", "left", "stop")))