from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count_row = {}
        count_col = {}
        count_subBox = {}

        