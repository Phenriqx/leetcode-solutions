import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0)
            return new ArrayList<List<String>>();

        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String newStr = new String(chars);

            List<String> anagrams = map.getOrDefault(newStr, new ArrayList<>());
            anagrams.add(str);
            map.put(newStr, anagrams);
        }

        return new ArrayList<>(map.values());
    }
}