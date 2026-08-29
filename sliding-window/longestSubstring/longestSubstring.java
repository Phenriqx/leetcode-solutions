import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String str) {
        int max = 0, i = 0;
        HashSet<Character> substring = new HashSet<>();

        for (int j = 0; j < str.length(); j++) {
            while (substring.contains(str.charAt(j))) {
                substring.remove(str.charAt(j));
                i++;
            }

            substring.add(str.charAt(j));
            max = Math.max(max, j - i + 1);
        }

        return max;
    }
}
