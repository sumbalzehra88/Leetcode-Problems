class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        l = 0
        for r in range(len(s)):
            if (r - l + 1) == 10:
                substring = s[l:r+1]
                if substring in seen:
                    repeated.add(substring)
                else:
                    seen.add(substring)
                l += 1
        return list(repeated)


        