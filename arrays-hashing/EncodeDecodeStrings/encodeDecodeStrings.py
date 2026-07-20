from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += f"{len(s)}@{s}"

        return new_str

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            len_word = ""
            while (s[i] != '@'):
                len_word += f"{s[i]}"
                i += 1

            word = s[i + 1: i + int(len_word) + 1]
            res.append(word)
            i += int(len_word) + 1

        return res


def main():
    solution = Solution()
    list_str = ["Hello@World", "Nome"]
    encoded_str = solution.encode(list_str)

    print(encoded_str)

    decoded_strs = solution.decode(encoded_str)

    print(decoded_strs)
    print(f"Input: {list_str}\nOutput: {decoded_strs}")

if __name__ == '__main__':
    main()