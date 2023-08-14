from collections import deque
import sys

data=[]
global n,m,a,b
n,m,a,b,k=map(int,input().split())
global map
map=[[0]*m for _ in range(n)]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    map[x][y]=2
sx,sy=map(int,input().split())
d_x,d_y=map(int,input().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[0]*m for _ in range(n)]

def bfs(sx,sy,d_x,d_y):
    visited[sx][sy]=1
    queue=deque([])
    queue.append([sx,sy,0])
    while(queue):
        x,y,dis=queue.pop()
        if(x==dx and y==dy):
            return dis
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(visited[nx][ny]==0 and 0<=nx and 0<=ny and nx+a<n and ny+b<m):
                visited[nx][ny]=1
                queue.append([nx,ny,dis+1])
    return -1


print(bfs(sx,sy,d_x,d_y))
