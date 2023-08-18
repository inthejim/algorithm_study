import sys
from collections import deque

si=sys.stdin.readline

N,M=map(int,si().strip().split())
data=list(list(map(int,si().strip().split())) for _ in range(N))
d=[-1,0,1]

def bfs():
    res=[100000]
    queue=deque([])

    for i in range(M):
        queue.append([0,i,2,data[0][i]])

    while(queue):
        x,y,dir,s=queue.popleft()
        if(x==(N-1)):
            res.append(s)
            continue
        for k in range(3):
            if(dir==d[k]):
                continue
            nx=x+1
            ny=y+d[k]
            if(0<=nx<N and 0<=ny<M):
                queue.append([nx,ny,d[k],s+data[nx][ny]])
    return res

print(min(bfs()))
