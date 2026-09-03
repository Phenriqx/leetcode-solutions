class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapp = {}
        for i in range(len(t)):
            mapp[t[i]] = mapp.get(t[i], 0) + 1

        i, min_length = 0, float('inf')
        map_count = sum(mapp.values())
        substring = ""

        for j in range(len(s)):
            if s[j] in mapp:
                if mapp[s[j]] > 0:
                    map_count -= 1

                mapp[s[j]] -= 1

            while map_count == 0:
                if (j - i + 1) <= min_length:
                        substring = s[i:j + 1]
                        min_length = j - i + 1

                if s[i] in mapp:
                    mapp[s[i]] += 1
                    if mapp[s[i]] > 0:
                        map_count += 1

                i += 1

        return substring