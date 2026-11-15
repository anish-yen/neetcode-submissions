class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        #iterate backwards

        dp = [False] * (len(s) +1)
        dp[len(s)] = True

        #[f, f, f, f, f, f, f, f, T]

        for i in range(len(s)-1, -1, -1):

            for word in wordDict:
                if len(s[i:i+len(word)]) < len(word):
                    continue
                if s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
        
        return dp[0]
        