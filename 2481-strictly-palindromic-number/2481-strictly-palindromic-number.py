class Solution:

    def to_base(self, n, base):
        digits = []
        while n > 0:
            digits.append(str(n % base))
            n = n // base
        return ''.join(digits[::-1])

    def is_palindrome(self, s):
        return s == s[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            converted = self.to_base(n, base)
            if not self.is_palindrome(converted):
                return False
        return True


        