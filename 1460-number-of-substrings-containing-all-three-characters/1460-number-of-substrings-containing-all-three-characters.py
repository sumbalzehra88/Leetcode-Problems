class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        occurance = {'a':0, 'b':0, 'c':0}
        l = 0
        res = 0
        for r in range(len(s)):
            # Add current char to counts
            occurance[s[r]] += 1
            
            # While window contains all three chars, shrink from left
            while all(occurance[ch] > 0 for ch in 'abc'):
                occurance[s[l]] -= 1
                l += 1
            
            # Add count of valid substrings ending at r
            res += l
            
        return res


        