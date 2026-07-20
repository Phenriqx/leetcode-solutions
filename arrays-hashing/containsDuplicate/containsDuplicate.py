from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i, val in enumerate(nums):
            if val in counter:
                return True
            else:
                counter[val] = 1

        return False