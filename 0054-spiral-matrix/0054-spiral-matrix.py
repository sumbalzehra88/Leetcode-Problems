class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        top,bottom,left,right = 0, m-1, 0, n-1
        while top <= bottom and left<= right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1
        return res
        