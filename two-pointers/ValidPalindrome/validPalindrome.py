class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(c for c in s if c.isalnum())
        j = len(newStr) - 1
        for i in range(len(newStr)):
            if newStr[i].lower() != newStr[j].lower():
                return False
            j -= 1

        return True