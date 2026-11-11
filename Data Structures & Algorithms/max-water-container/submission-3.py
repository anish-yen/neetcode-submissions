class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #[1,7,2,5,4,7,3,6]
        #[1,4,2,3,4,0,3,2]
        #[1,8, 10, 3, 0, 0 9 8]
        #8x6 vs 9x5

        best = 0

        l ,r = 0, len(heights)-1

        while l < r:
            width = r-l

            height = min(heights[l] , heights[r])

            best = max(best, (height*width))
            #print(width, height, best)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return best
        #movve pointer inward either way and capped at smaller height so move that pointer closer in

