import sys
from collections import deque

si=sys.stdin.readline

n,m=map(int,si().split(' '))
bingsan=[[*map(int,si().split(' '))] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]


def bfs(x,y):
    visited=[[0]*m for _ in range(n)]
    queue=deque([[x,y]])
    
    while(queue):
        i,j=queue.popleft()
        if(visited[i][j]!=0):
            continue

        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if(0<=nx<n and 0<=ny<m and bingsan[nx][ny]>0 and visited[nx][ny]==0):
                queue.append([nx,ny])
            elif(0<=nx<n and 0<=ny<m and bingsan[nx][ny]<=0):
                visited[i][j]-=1
        if(visited[i][j]==0):
            visited[i][j]=1

    return visited
def find():
    for i in range(n):
        for j in range(m):
            if(bingsan[i][j]>0):
                s=i
                e=j
                return s,e
    return -1,-1

def solve():
    time=1
    while(not all(map(all, bingsan))):
        s,e=find()
        
        if(s==-1 and e==-1):
            return 1
        
        visited = bfs(s,e)
        for i in range(n):
            for j in range(m):
                if(visited[i][j]==0 and bingsan[i][j]>0):
                    return time
                            
                if(visited[i][j]!=1):
                    bingsan[i][j]+=visited[i][j]
                    
        time+=1

    return 1

print(solve()-1)
