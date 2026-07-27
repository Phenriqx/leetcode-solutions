import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0)
            return 0;

        Set<Integer> set = new HashSet<>();
        for (int num : nums)
            set.add(num);
        
        int longestStreak = 1;
        int currentStreak;
        for (int num : set) {
            int x = num - 1;
            if (!set.contains(x)) {
                currentStreak = 1;
                int curr = num;
                while (set.contains(curr + 1)) {
                    currentStreak++;
                    curr++;
                }
                if (currentStreak > longestStreak)
                    longestStreak = currentStreak;
            }
            else
                continue;
        }

        return longestStreak;
    }
}