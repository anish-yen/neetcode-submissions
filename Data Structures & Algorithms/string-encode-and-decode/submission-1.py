class Solution:

    def encode(self, strs: List[str]) -> str:

        e = ""

        for s in strs:
            e += str(len(s)) + "#" + s

        return e
        

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!= "#":
                j+=1
            count = int(s[i:j])
            word = s[j+1:j+count+1]
            arr.append(word)
            i=j+count+1
        return arr



        #5#hello5#world
