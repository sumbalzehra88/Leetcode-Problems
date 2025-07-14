class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = [""]
        for _ in range(n):
            new_result = []
            for s in result:
                new_result.append(s + "1")  
                if not s or s[-1] != "0":
                    new_result.append(s + "0")  
            result = new_result
        return result
