class Solution:

    def encode(self, strs: List[str]) -> str:

        

        res = ""

        for s in strs:
            res+= str(len(s)) + "#" + s
        return res

def decode(self, s: str) -> List[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        if s[j] == "#":                       
            count = int(s[i:j])               
            res.append(s[j+1:j+count+1])      
            i = j + count + 1

    return res

 #skip all characters with anothe rpointer j not #
 # count can be double digit so account for that and appeend is [inc: exc] update i pointer
 #two ptr approach
        
    
