from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            sorted_dictS = Counter(s)
            sorted_dictT = Counter(t)
            if sorted_dictT == sorted_dictS:
                return True
            else:
                return False

        