from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in freqs:
                freqs[s[i]] = 1
            else:
                freqs[s[i]] += 1
            if t[i] not in freqt:
                freqt[t[i]] = 1
            else:
                freqt[t[i]] += 1           
        #count1 = Counter(s)
        #count2 = Counter(t)
        #print(count1)
        #print(count2)

        if freqs == freqt:
            return True
        else:
            return False




