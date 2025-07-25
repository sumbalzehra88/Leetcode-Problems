class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def explore(index, curr):
            if index >= len(s):
                result.append(curr.copy())

            for i in range(index,len(s)):
                substr = s[index : i+1]
                if substr == substr[ : : -1]:
                    curr.append(substr)
                    explore(i+1,curr)
                    curr.pop()
        explore(0,[])
        return result
        
