class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        maxc = 0

        count = 0
        l = 0
        currlen = 0


        for r in range(len(s)):
            currlen = r-l+1
            
            if s[r] in seen:
                seen[s[r]] +=1
                
            else:
                seen[s[r]] =1
            num_replace = currlen - max(seen.values())
            if num_replace > k:
                seen[s[l]]-=1
                l+=1
            maxc = max(maxc, r - l + 1)

        return maxc