class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        last=len(height)-1


        w=len(height)-1
        h=min(height[start],height[last])
        s=w*h
        m=s
        
        while(start<last):
            if(height[start]<=height[last]):
                start+=1
            else:
                last-=1
            h=min(height[start],height[last])
            w-=1
            s=w*h
            m=max(m,s)

        print(m)
        return m
