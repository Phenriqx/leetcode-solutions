class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hash_map = {}
        max_count = 1

        i, j = 0, 1
        hash_map[s[i]] = 1
        while j < len(s):
            if s[j] not in hash_map:
                count = j - i + 1
                hash_map[s[j]] = 1
            else:
                while s[j] in hash_map:
                    hash_map.pop(s[i])
                    i += 1

                hash_map[s[j]] = 1
                count = j - i + 1

            max_count = max(max_count, count)
            j += 1

        return max_count

    def lengthOfLongestSubstringCleaner(self, s: str) -> int:
        max_count = 0
        i = 0
        substring = set([])

        for j in range(len(s)):
            while s[j] in substring:
                substring.remove(s[i])
                i += 1

            substring.add(s[j])
            count = j - i + 1
            max_count = max(count, max_count)

        return max_count
