class Solution:
    def evenTheLast(self, array:list) -> int:
        if array == []: return 0
        val, mul, evens = 0, 0, []
        for i, v in enumerate(array):
            if i%2 == 0: evens.append(v)
        val = sum(evens)
        mul = val*array[-1]
        return mul

