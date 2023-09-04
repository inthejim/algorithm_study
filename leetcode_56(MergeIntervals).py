class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        prev_start=intervals[0][0]
        prev_end=intervals[0][1]
        for start, end in intervals:
            if(start<=prev_end):
                prev_end= max(prev_end,end)
            else:
                result.append([prev_start,prev_end])
                prev_start=start
                prev_end=end
        result.append([prev_start,prev_end])

        return result         



        
