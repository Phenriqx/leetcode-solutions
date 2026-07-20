import java.util.*;;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        // using a hashmap to keep track of frequencies
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++)
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);

        // for each char in t, we subtract one from the value of the current key
        for (int i = 0; i < t.length(); i++) {
            // check if the char even exists in the map or if its frequency is 0
            if (!map.containsKey(t.charAt(i)) || map.get(t.charAt(i)) == 0)
                return false;

            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) - 1);
        }

        return true;
    }
}