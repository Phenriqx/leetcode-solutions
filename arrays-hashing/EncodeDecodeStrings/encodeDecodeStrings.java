import java.util.*;

class Solution {
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder("");

        for (String str : strs)
            sb.append(str.length()).append("@").append(str);

        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            StringBuilder sb = new StringBuilder("");
            while (str.charAt(i) != '@') {
                sb.append(str.charAt(i));
                i++;
            }

            int len = Integer.parseInt(sb.toString());
            String word = str.substring(i + 1, i + len + 1);
            strs.add(word);

            i += len + 1;
        }

        return strs;
    }
}