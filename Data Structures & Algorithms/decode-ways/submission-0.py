class Solution:
    def numDecodings(self, s: str) -> int:

        #single digit encodeing
        #two digent if <= 26 

        dp = [1] + [0] * len(s)

        for i in range(1, len(s)+1):
            if s[i-1]!='0':
                dp[i] = dp[i-1]

            #check if not 0, if its valid int, and after first digit
            if i>1 and s[i-2]!= '0' and int(s[i-2:i]) <= 26:
                dp[i] +=dp[i-2] #counter single ways and double ways
        
        return dp[len(s)] # if prev character 0 its same either way