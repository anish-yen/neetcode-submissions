from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            sorted_dictS = sorted(Counter(s).items())
            sorted_dictT = sorted(Counter(t).items())
            print(sorted_dictS)
            print(sorted_dictT)
            if sorted_dictT == sorted_dictS:
                return True
            else:
                return False

        