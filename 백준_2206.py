import sys
from collections import deque
si=sys.stdin.readline
n,m=map(int,si().strip().split())

data=list(list(map(int,si().strip())) for _ in range(n))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[[0,0] for _ in range(m)] for _ in range(n)]

def bfs():
    queue=deque([[0,0,0]])
    visited[0][0][0]=1
    while(queue):
        cur=queue.popleft()
        x=cur[0]
        y=cur[1]
        cnt=cur[2]
        if(x==n-1 and y==m-1):
            return visited[x][y][cnt]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<n and 0<=ny<m and visited[nx][ny][cnt]==0):
                if(data[nx][ny]==0):
                    visited[nx][ny][cnt]=visited[x][y][cnt]+1
                    queue.append([nx,ny,cnt])
                if(data[nx][ny]==1 and cnt==0):
                    
                    visited[nx][ny][1]=visited[x][y][cnt]+1
                    queue.append([nx,ny,1])
    return -1

print(bfs())





