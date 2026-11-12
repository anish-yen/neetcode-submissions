class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best =0

        seen = {}

        #"zxyzxyz"

        l,r =0,0

        while r<len(s):
            if s[r] not in seen:
                seen[s[r]] =1
            else:
                seen[s[r]] +=1
            
                while seen[s[r]] >1:
                    seen[s[l]] -=1
                    l+=1
            
            currlen = r-l+1
            best = max(currlen, best)
            r+=1

        return best





        