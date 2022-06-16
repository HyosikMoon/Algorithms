class solution:
    def sum_numbers(self, text):
        lst = text.split()
        numbers = []
        for w in lst:
            isnum = 0
            for c in w:
                if c in '0123456789': 
                    isnum += 1
            if isnum == len(w):
                numbers.append(int(w))
        return sum(numbers)

