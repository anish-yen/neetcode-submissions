
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mydict = {}
        freq = []

        # create buckets (index = frequency)
        for i in range(len(nums) + 1):
            freq.append([])

        # count frequencies
        for n in nums:
            mydict[n] = mydict.get(n, 0) + 1

        # put numbers into correct bucket
        for n, c in mydict.items():
            freq[c].append(n)

        res = []

        # go from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    #Across the ENTIRE algorithm, every number only gets appended once. - O(n) -> 3n
    # num of nums is still same so loop runs zero for most buckes
    # 🚨 When WOULD it be O(n²)? It would be O(n²) if each bucket had n elements. -> but notp ossblybecause a number cant go into mult buckets