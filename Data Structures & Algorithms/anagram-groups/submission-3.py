from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        # defaultdict hashmap
        # use each string's letter-count pattern as the key
        # then return the grouped strings

        # use ord to map each letter to an index from 0 to 25
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            d[tuple(chars)].append(s)

        return list(d.values())