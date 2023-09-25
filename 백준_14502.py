import sys
import copy
from collections import deque
from itertools import combinations

si=sys.stdin.readline
n,m=map(int, si().split(' '))

maplist=[[*map(int,si().split())] for _ in range(n)]
emptylist=[(i,j) for i in range(n) for j in range(m) if maplist[i][j]==0]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def findVirus(queue):
    for i in range(n):
        for j in range(m):
            if(maplist[i][j]==2):
                queue.append((i,j))
    
    return queue

def bfs():
    global answer

    for walls in combinations(emptylist, 3):
        visited=copy.deepcopy(maplist)
        for i,j in walls:
            visited[i][j]=1
        queue=deque()
        queue=findVirus(queue)

        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if(0<=nx<n and 0<=ny<m and visited[nx][ny]==0):
                        visited[nx][ny]=2
                        queue.append((nx,ny))

        a=0
        for row in visited:
            a+=row.count(0)
        answer=max(a,answer)

answer=0
bfs()
print(answer)
