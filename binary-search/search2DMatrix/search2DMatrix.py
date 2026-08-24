from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = 0, len(matrix) - 1
        # while l <= r:
        #     m_row = l + (r - l) // 2
        #     lcol, rcol = 0, len(matrix[m_row]) - 1
        #     while lcol <= rcol:
        #         m_col = lcol + (rcol - lcol) // 2
        #         if matrix[m_row][m_col] == target:
        #             return True
        #         elif matrix[m_row][m_col] < target:
        #             lcol = m_col + 1
        #         else:
        #             rcol = m_col - 1
        #     if matrix[m_row][0] > target:
        #         r = m_row - 1
        #     else:
        #         l = m_row + 1

        # return False

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid // m][mid % n] == target:
                return True
            elif matrix[mid % m][mid // n] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
