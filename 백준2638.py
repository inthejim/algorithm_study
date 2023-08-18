import sys
import copy
from collections import deque

si=sys.stdin.readline

N,M=map(int,si().strip().split())
data=list(list(map(int,si().strip().split())) for _ in range(N))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def find_outer(sx,sy,visited):
    queue=deque([])
    queue.append([sx,sy])

    while(queue):
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<N and 0<=ny<M and data[nx][ny]==0 and visited[nx][ny]==0):
                visited[nx][ny]=1
                queue.append([nx,ny])

def find_delete(visited):
    list=[]
    for i in range(N):
        for j in range(M):
            if(data[i][j]==1):
                cnt=0
                for k in range(4):
                    x=i+dx[k]
                    y=j+dy[k]
                    if(0<=x<N and 0<=y<M and data[x][y]==0 and visited[x][y]==1):
                        cnt+=1
                if(cnt>=2):
                    list.append([i,j])
    return list

time=0
while(True):
    visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if(i!=0 and i!=N-1 and j!=0 and j!=N-1):
                continue
            if(visited[i][j]==0):
                find_outer(i,j,visited)
    
    a=find_delete(visited)
    time+=1
    
    if(not a or len(a)==0):
        time-=1
        break

    for x,y in a:
        data[x][y]=0

print(time)