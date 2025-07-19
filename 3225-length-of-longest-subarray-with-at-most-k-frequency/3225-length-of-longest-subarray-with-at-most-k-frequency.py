class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        l = 0
        res = 0

        for r in range(len(nums)):
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1

            res = max(res, r - l + 1)

        return res
