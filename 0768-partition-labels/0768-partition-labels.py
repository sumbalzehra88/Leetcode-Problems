class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {}
        for i in range(len(s)):
            last_occurence[s[i]] = i


        result = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end,last_occurence[s[i]])
            if i == end:
                result.append(end-start+1)
                start = i+1
        return result

