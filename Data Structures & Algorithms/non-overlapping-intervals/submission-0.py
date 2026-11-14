class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        #sort by intervals that end earliest

        previous_end = float("-inf")

        #intervals to remove default ot length
        remove = len(intervals)

        for start, end in intervals:

            if previous_end<=start: #no overlap
                remove-=1
            previous_end = end
        return remove


