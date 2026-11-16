from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp]) #problem already says timestaps are in increasing order

        

    def get(self, key: str, timestamp: int) -> str:
            #if key not in self.store:
               # return ''
            vals = self.store[key]
            l ,r = 0, len(vals) -1

            res = ""

            while l<=r: #why <=?
                mid = l + (r-l) //2
                if vals[mid][1] <= timestamp:
                    res = vals[mid][0] #reutrn closest value <=timestamp
                    l = mid+1 #res needs to get closer and closer till reachest largest time stamp <=
                else:
                    r = mid-1
            return res #if empty cant find return

        
