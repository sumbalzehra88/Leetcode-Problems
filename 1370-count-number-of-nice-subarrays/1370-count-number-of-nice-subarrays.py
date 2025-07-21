class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        total = 0
        l = 0
        for r in range(len(nums)):
            if (nums[r] % 2) != 0:
                odd += 1
            while odd > k:
                if (nums[l] % 2) != 0:
                    odd -= 1
                l+=1
            if odd == k:
                temp = l
                while temp < len(nums) and nums[temp] % 2 == 0:
                    temp += 1
                total += (temp - l + 1)
        return total
