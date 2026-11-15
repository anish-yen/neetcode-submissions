class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        #iterate backwards

        dp = [False] * (len(s) +1)
        dp[len(s)] = True

        #[f, f, f, f, f, f, f, f, T]

        for i in range(len(s)-1, -1, -1):

            for word in wordDict:
               # if len(s[i:i+len(word)]) < len(word): # just continue- dont need these part
                  #  continue
                if s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]: #remember this part important
                    break #try other parts now
        #different words combinations so need word break
        #if cant be split into words no break
        return dp[0]
        