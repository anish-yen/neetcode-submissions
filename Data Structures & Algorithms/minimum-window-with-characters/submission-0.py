from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        have = 0
        l = 0
        best_len = float("inf")
        best_l = 0

        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            while have == len(need):
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]