class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        full_set = set(nums)  
        res = 0
        n = len(nums)

        for left in range(n):
            window_set = set()
            for right in range(left, n):
                window_set.add(nums[right])
                if len(window_set) == len(full_set):
                    res += 1  

        return res
