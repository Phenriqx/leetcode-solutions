class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Solution using only one hash map
        counter = {}
        for _, val in enumerate(s):
            counter[val] = counter.get(val, 0) + 1
        for _, val in enumerate(t):
            counter[val] = counter.get(val, 0) - 1
            if counter.get(val) < 0:
                return False

        return all(x == 0 for x in counter.values())