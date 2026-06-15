class Solution:

    def encode(self, strs: List[str]) -> str:
        poo = ""
        for s in strs:
            poo += str(len(s)) + "#" + s
        return poo

    def decode(self, s: str) -> List[str]:
        arr = []

        i = 0
        "4#neet5#code"

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            wrd = s[j+1:j+count+1]
            arr.append( wrd)
            i=j+count+1
        return arr