class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def dfs(start, end):
            if start >= end:
                return 1  # base case

            if (start, end) in memo:
                return memo[(start, end)]  # return cached result

            total = 0
            for root in range(start, end + 1):
                left = dfs(start, root - 1)
                right = dfs(root + 1, end)
                total += left * right

            memo[(start, end)] = total  # store result
            return total

        return dfs(1, n)
