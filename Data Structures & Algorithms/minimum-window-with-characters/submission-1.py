class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        result = ""
        min_length = float("inf")

        for i in range(len(s)):
            window_count = {}

            for j in range(i, len(s)):
                ch = s[j]
                window_count[ch] = window_count.get(ch, 0) + 1

                valid = True

                for c in t_count:
                    if window_count.get(c, 0) < t_count[c]:
                        valid = False
                        break

                if valid:
                    if (j - i + 1) < min_length:
                        min_length = j - i + 1
                        result = s[i:j + 1]

        return result