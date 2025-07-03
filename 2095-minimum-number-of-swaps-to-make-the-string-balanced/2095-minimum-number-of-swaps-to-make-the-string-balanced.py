class Solution:
    def minSwaps(self,s: str) -> int:
        s = list(s)
        n = len(s)
        i = 0     
        j = n - 1  
        swaps = 0
        balance = 0

        while i < n:
            if s[i] == '[':
                balance += 1
            else:
                balance -= 1

            
            if balance < 0:
                # Find the next '[' from the end to swap with current ']'
                while i < j and s[j] != '[':
                    j -= 1

                # Swap characters at i and j
                s[i], s[j] = s[j], s[i]
                swaps += 1

                # After swap, assume this position is balanced
                balance = 1

            i += 1

        return swaps


                
