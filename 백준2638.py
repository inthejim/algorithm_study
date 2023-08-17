#시간초과..
import sys
import copy
from collections import deque

si=sys.stdin.readline

N,M=map(int,si().strip().split())
data=list(list(map(int,si().strip().split())) for _ in range(N))

def find():
    for i in range(N):
        for j in range(M):
            if(data[i][j]==1):
                return i,j
    return -1,-1

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
            cnt=0
            for k in range(4):
                x=i+dx[k]
                y=i+dy[k]
                if(0<=x<N and 0<=y<M and data[x][y]==0 and visited[i][j]==1):
                    cnt+=1
            if(cnt>=2):
                list.append([i,j])
            visited[i][j]=1
    return list

check=True
time=0
while(check):
    visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if(i!=0 and i!=N-1 and j!=0 and j!=N-1):
                continue
            if(visited[i][j]==0):
                find_outer(i,j,visited)
    
    a=find_delete(visited)
    time+=1
    if(len(a)==0):
        check=False
        time-=1

print(time)
