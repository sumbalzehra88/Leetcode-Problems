class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        result = ""
        i = 0 
        for ch in s:
            if i < len(t) and ch == t[i]:
                result += ch
                i += 1
        new_string = t[len(result):]
        return len(new_string)
