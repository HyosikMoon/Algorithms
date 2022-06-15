class Solution:
    def split_pairs(self, s):
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s+'_']
        results = []
        while len(s) > 2:
            results.append(s[:2])
            s = s[2:]
        if len(s) == 2:
            results.append(s)
        else:
            results.append(s+'_')
        return results