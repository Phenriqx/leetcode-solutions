import heapq
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this solution is not correct, but ill leave it here to show my mistakes
        # heap = heapq.heapify(nums)

        # res = []
        # prev = heapq.heappop(heap)
        # res.append(prev)
        # for i in range(len(heap)):
        #     item = heapq.heappop(heap)
        #     if item == prev + 1:
        #         prev = item
        #         res.append(item)
        #     else:
        #         break

        # return len(res)


        count = set(nums)
        longest_streak = 0
        
        for num in count:
            x = num - 1
            if x not in count:
                current_streak = 1
                curr = num
                while (curr + 1 in count):
                    current_streak += 1
                    curr += 1

                longest_streak = max(longest_streak, current_streak)
            else:
                continue

        return longest_streak
