class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        l,r =0,0
        best = 0

        #key condition window_size - max_freq ≤ k

        while r < len(s):
            window_size = r-l+1
            if s[r] not in seen:
                seen[s[r]] =1
            else:
                seen[s[r]] +=1
            
            replace = window_size - max(seen.values())
            if replace>k: #check entire window each iteration so if is fine
                seen[s[l]]-=1
                l+=1
            window_size = r-l+1    
            best = max(best, window_size)
            r+=1
        return best

