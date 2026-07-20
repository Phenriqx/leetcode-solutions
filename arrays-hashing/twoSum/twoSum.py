class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) == 0:
            return 0

        # Bruteforce solution -> not optimal O(n²)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             continue

        # Optimized solution using hashmap -> O(n)
        tracker = {} # key: number, value: index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in tracker:
                return i, tracker[complement]
            else:
                tracker[nums[i]] = i