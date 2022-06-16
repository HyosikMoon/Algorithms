class Solution:
    def firstWord(self, text: str) -> str:
        text = text.replace('.', ' ')
        text = text.replace(',', '')
        words = text.split()
        return words[0]
                
sol = Solution()
print(sol.firstWord("greetings, friends"))