class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        best= 0
        #"AAABABB"
        # l l l l
        seen = {}
        #"AAABABB"
        a:3

        #window is valid if k>0 and window same characters

        #aba, k =r
        l,r = 0,0

        #a: 1, b: 2

        while r < len(s):
            window_size = r-l+1
            
            if s[r] in seen:
                seen[s[r]] +=1
            else: 
                seen[s[r]] =1 
            #ey point window size - most freq characters has to be 
            while (r-l+1) - max(seen.values()) > k: #when windo too long and invalid pop from left
                seen[s[l]] -=1
                l+=1
            best = max(best, (r-l+1)) #<=k valid #else js calc max length
            r+=1
        return best