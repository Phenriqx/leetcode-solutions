class Solution:
    # first solution i came up with
    def characterReplacementSolution1(self, s: str, k: int) -> int:
        mapp = {}
        i, max_len = 0, 0

        for j in range(len(s)):
            mapp[s[j]] = mapp.get(s[j], 0) + 1
            window_len = j - i + 1
            most_frequent = max(mapp.values())

            while window_len - most_frequent > k:
                mapp[s[i]] -= 1
                i += 1
                window_len = j - i + 1
                most_frequent = max(mapp.values())

            max_len = max(max_len, window_len)

        return max_len

    # a little more optimized solution
    def characterReplacementSolution2(self, s: str, k: int) -> int:
        mapp = {}
        i, max_len = 0, 0
        res = 0

        for j in range(len(s)):
            mapp[s[j]] = mapp.get(s[j], 0) + 1
            window_len = j - i + 1
            max_len = max(max_len, mapp[s[j]])

            while window_len - max_len > k:
                mapp[s[i]] -= 1
                i += 1
                window_len = j - i + 1

            res = max(res, window_len)

        return res