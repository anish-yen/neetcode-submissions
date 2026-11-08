from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                i = ord(c) - ord("a")
                count[i]+=1
            groups[tuple(count)].append(word) # lists cant be keys but tuples can?
           # print(groups)
        return list(groups.values())
        

