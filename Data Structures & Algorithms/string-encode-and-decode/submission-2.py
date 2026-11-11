class Solution:

    def encode(self, strs: List[str]) -> str:

        

        res = ""

        for s in strs:
            res+= str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        
        #edge case if word contains #
        5#hello5#world
        res = []
        i = 0
        while i < len(s):
            i+=1
            if s[i] == "#":
                j = i+1
                count = int(s[i-1])
                res.append(s[j:j+count])
                i=j+count
        return res


        
    
