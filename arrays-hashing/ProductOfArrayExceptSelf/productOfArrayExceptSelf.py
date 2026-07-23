from typing import List

class Solution:

    # This solution is O(n) for space and time complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]

        i = len(nums)
        while (i > 0):
            suffix[i - 1] = suffix[i] * nums[i - 1]
            i -= 1

        res = []
        for i in range(len(nums)):
            suffix_prod = suffix[i + 1] / suffix[len(nums)]
            prefix_prod = prefix[i] / prefix[0]
            res.append(int(suffix_prod * prefix_prod))

        return res

    def productExceptSelfBetter(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res