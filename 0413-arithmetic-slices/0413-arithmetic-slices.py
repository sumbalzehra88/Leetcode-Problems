class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        current = 0
        total = 0
        for r in range(2,len(nums)):
            if nums[r] - nums[r-1] == nums[r-1] - nums[r-2]:
                current += 1
                total += current
            else:
                current = 0
        return total
