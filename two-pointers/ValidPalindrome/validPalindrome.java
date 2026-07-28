class Solution {
    public boolean isPalindrome(String s) {
        String newStr = String.join("", s).toLowerCase();
        int j = newStr.length() - 1;
        for (int i = 0; i < newStr.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i)) && Character.isLetterOrDigit(s.charAt(j)))
                if (s.charAt(i) != s.charAt(j))
                    return false;
            j--;
        }
        return true;
    }
}
