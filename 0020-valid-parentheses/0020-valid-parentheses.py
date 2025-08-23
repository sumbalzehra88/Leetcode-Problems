class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charHash = {")":"(", "]": "[", "}" : "{"}

        for char in s:
            if char in charHash:
                if stack and stack[-1] == charHash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
