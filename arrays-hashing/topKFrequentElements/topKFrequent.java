import java.util.*;
// import java.util.stream.Collectors;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();

        // count and store the frequencies of each number
        for (int i = 0; i < nums.length; i++) {
            int val = count.getOrDefault(nums[i], 0);
            count.put(nums[i], val + 1);
        }

        /*
            1st approach: sorting -> O(n log n)

            List<Map.Entry<Integer, Integer>> list = count.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .collect(Collectors.toList());

            int[] res = new int[k];
            for (int i = 0; i < k; i++)
                res[i] = list.remove(list.size() - 1).getKey();

            return res;
        */

        /*
            2nd approach: heap -> O(n log k)

            PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(Comparator.comparing(Map.Entry::getValue));
            for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
                minHeap.add(entry);
                if (minHeap.size() > k)
                    minHeap.remove();
            }
            int[] res = new int[k];
            for (int i = 0; i < k; i++)
                res[i] = minHeap.remove().getKey();

            return res;
        */

        /* 3rd approach: Bucket Sort -> O(n) */
        List<List<Integer>> buckets = new ArrayList<>(nums.length + 1);

        for (int i = 0; i <= nums.length; i++)
            buckets.add(new ArrayList<>());

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int frequency = entry.getValue();
            buckets.get(frequency).add(entry.getKey());
        }

        int[] res = new int[k];
        int index = 0;
        for (int i = nums.length; i > 0; i--) {
            if (!buckets.get(i).isEmpty()) {
                for (int item : buckets.get(i)) {
                    if (index == k)
                        break;

                    res[index] = item;
                    index++;
                }
            }
        }

        return res;
    }
}