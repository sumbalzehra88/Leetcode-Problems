from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        numbers = list(range(1, n*n + 1))
    
        matrix = [[0]*n for _ in range(n)]
        
        top, bottom, left, right = 0, n-1, 0, n-1
        index = 0
        
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = numbers[index]
                index += 1
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = numbers[index]
                index += 1
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = numbers[index]
                    index += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = numbers[index]
                    index += 1
                left += 1

        return matrix

