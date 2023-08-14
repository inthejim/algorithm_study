from collections import deque
import sys

data=[]
n,m,a,b,k=map(int,input().split())

mp=[[0]*m for _ in range(n)]
for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    mp[x-1][y-1]=2

sx,sy=map(int,input().split())
d_x,d_y=map(int,input().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[0]*m for _ in range(n)]

def check(sx,sy,d_x,d_y):
    for i in range(sx,sy):
        for j in range(d_x,d_y):
            if(mp[i][j]==2):
                return 0
    return 1

def bfs(sx,sy,d_x,d_y):
    visited[sx-1][sy-1]=1
    queue=deque([])
    queue.append([sx-1,sy-1,0])
    while(queue):
        x,y,dis=queue.pop()
        if(x==d_x-1 and y==d_y-1):
            return dis
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx and 0<=ny and nx+b<n and ny+a<m and visited[nx][ny]==0):
                #장애물 체크
                if(check):
                    visited[nx][ny]=1
                    queue.append([nx,ny,dis+1])
    return -1


print(bfs(sx,sy,d_x,d_y))
