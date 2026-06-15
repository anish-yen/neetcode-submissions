class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxC = 0
        l=0
        r=0

        if not s:
            return 0
        #key is letter value is pair

        mydict= {}
        #mydict[s[l]] = l

        while r<len(s) :
            if s[r] not in mydict or mydict[s[r]] < l:
                count+=1
                if count>maxC:
                    maxC = count
            else:
                l = mydict[s[r]] + 1
                count=r-l+1
            mydict[s[r]] = r
            r+=1
        return maxC
