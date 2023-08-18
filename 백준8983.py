import sys
from collections import deque

si=sys.stdin.readline

M,N,L=map(int,si().strip().split())
location=list(map(int,si().strip().split()))

animals=list(list(map(int,si().strip().split())) for _ in range(N))

dx=[-1,1,0]
dy=[0,0,1]

#그래프 방향이 반대로 된거 같음,,,다시 작성하기,,
def bfs(i,j,result,sum):
    queue=deque([])
    queue.apped([i,j,0])
    visited=[[0]*1000000000 for _ in range(1000000000)]
    visited[i][j]=1
    while(queue):
        x,y,depth=queue.popleft()
        if(depth<=L):
            for k in range(3):
                nx=x+dx[k]
                ny=y+dy[k]
                
                if(0<=nx<1000000000 and 0<=ny<1000000000 and visited[nx][ny]==0 and result[nx][ny]==0):
                    visited[nx][ny]=1
                    if [nx,ny] in animals:
                        result[nx][ny]=1
                        sum+=1
                    queue.append([nx,ny,depth+1])

