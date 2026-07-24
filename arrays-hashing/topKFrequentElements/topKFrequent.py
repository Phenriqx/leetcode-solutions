from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # 1st approach: sorting -> O(n log n)
        # sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        # return [item[0] for item in sorted_dict[:k]]

        # 2nd approach: min Heap -> O(n log k)

        # minHeap = []
        # for num, frequncy in count.items():
        #     heapq.heappush(minHeap, (frequncy, num))

        #     if (len(minHeap) > k):
        #         heapq.heappop(minHeap)

        # return [num for freq, num in minHeap]

        # 3rd approach: Bucket Sort -> O(n)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count.items():
            buckets[frequency].append(num)

        res = []
        index = 0
        for i in range(len(nums), 0, -1):
            if buckets[i] is not None:
                for item in buckets[i]:
                    if index == k:
                        break

                    res[index] = item
                    index += 1


        return res