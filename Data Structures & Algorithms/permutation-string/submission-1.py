from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #hashmap dict match to characters s2
        # sliding

        freq1= Counter(s1)
        freq2 = {}

        
        #Input: s1 = "abc", s2 = "lecabee"
        #decreent left, increment right, drop
        #wreturn true if maps are equal
        #consider the windowsize- delete character if 

        l,r = 0,0

        window_size = len(s1)
        #freq2  c:1, a:1, b:1
        #space is o(1) bc capped at 26 letters
        # one pass build and one pass slide

        while r<len(s2):
            if s2[r] in freq2:
                freq2[s2[r]] += 1
            else:
                freq2[s2[r]] = 1
            
            if r-l+1 > window_size:
                freq2[s2[l]] -=1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l+=1
            if r-l+1 == window_size and freq1 == freq2: #at any point if frequency is same return true order doesnt matter in hashamp
                return True
            r+=1
        return False #reach end no match


        