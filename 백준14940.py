import sys
from collections import deque

n,m=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

visited=[[0]*m for _ in range(n)]

goal_x,goal_y=0,0

for i in range(n):
    for j in range(m):
        if(data[i][j]==2):
            goal_x,goal_y=i,j

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    queue=deque([])
    queue.append([goal_x,goal_y,0])
    visited[goal_x][goal_y]=1

    while(queue):
        x,y,depth=queue.popleft()
        data[x][y]=depth

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<n and 0<=ny<m and data[nx][ny]!=0 and visited[nx][ny]==0):
                visited[nx][ny]=1
                queue.append([nx,ny,depth+1])

bfs()

for i in range(n):
    for j in range(m):
        if(data[i][j]!=0 and visited[i][j]==0):
            data[i][j]=-1


for i in range(n):
    res=""
    for j in range(m):
        res+=str(data[i][j])+" "
    print(res)

