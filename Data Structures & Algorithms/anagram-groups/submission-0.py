from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        ahh = []
        
        mtx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        #strs = ["act","pots","tops","cat","stop","hat"]

        for i in strs:
            freq = []
            for let in mtx:
                if let in i:
                    freq.append(i.count(let))
                else:
                    freq.append(0)
            key = tuple(freq)
            if key not in my_dict:
                    my_dict[key] = []
            my_dict[key].append(i)

        for thing in my_dict.values():
            ahh.append(thing)
        return ahh

        print(freq)
        print(my_dict)


"""
    def isAnagram(self, s: str, t: str) -> bool:
            sorted_dictS = Counter(s)
            sorted_dictT = Counter(t)
            if sorted_dictT == sorted_dictS:
                return True
            else:
                return False
"""