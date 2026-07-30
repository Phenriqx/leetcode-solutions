from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        i = 0
        max_water = 0
        while i < j:
            curr_water_val = (j - i) * min(heights[i], heights[j])
            max_water = max(max_water, curr_water_val)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return max_water