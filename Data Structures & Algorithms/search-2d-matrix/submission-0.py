class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new = []

        for num in matrix:
            for ch in num:
                new.append(ch)
            if target in new:
                return True
        return False

        