class Solution:
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==1):
                    answer+=4
                    for k in range(4):
                        nx=i+self.dx[k]
                        ny=j+self.dy[k]
                        if(0<=nx<row and 0<=ny<col):
                            if(grid[nx][ny]==1):
                                answer-=1
        
        return answer
        
        
