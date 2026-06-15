class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = re.sub(r'[^a-zA-Z0-9]', '', s)
        #print(s)
        #print(int(len(s)/2))
        #print(s[len(s) -1])
        left = 0
        right = len(s) -1
        while left < right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
                continue
            else:
                return False
        return True 

