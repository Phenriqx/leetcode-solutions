from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for i in range(len(heights) + 1):
            curr_element = heights[i] if i < len(heights) else 0
            while stack and curr_element <= heights[stack[-1]]:
                right = i
                popped_index = stack.pop()
                left = stack[-1] if stack else -1

                curr_size = heights[popped_index] * (right - left - 1)
                largest = max(largest, curr_size)
            stack.append(i)

        return largest