from collections import deque
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        queue = deque()
        queue.append(([], 0, 0)) 

        while queue:
            path, total, index = queue.popleft()
            if total == target:
                result.append(path)
                continue
            if total > target:
                continue
            for i in range(index, len(candidates)):
                num = candidates[i]
                queue.append((path + [num], total + num, i)) 

        return result
