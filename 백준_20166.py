import sys
from collections import deque
si=sys.stdin.readline

n,m,k=map(int,si().split(' '))
data1=[list(si()) for _ in range(n)]
data2=[si().strip() for _ in range(k)]

dict={}
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, - 1, 1, -1]
def bfs(i,j):
    queue=deque()
    queue.append((i,j,data1[i][j]))

    while queue:
        x,y,string=queue.popleft()
        if string not in dict:
            dict[string]=1
        else:
            dict[string]+=1
        
        if(len(string)>5):
            continue
        
        for k in range(8):
            nx=x+dx[k]
            ny=y+dy[k]

            if nx==n:
                nx=0
            elif nx==-1:
                nx=n-1
            if ny==n:
                ny=0
            elif ny==-1:
                ny=m-1

            queue.append((nx,ny,string+data1[nx][ny]))

for i in range(n):
    for j in range(m):
        bfs(i,j)

for k in range(len(data2)):
    if data2[k] in dict:
        print(dict[data2[k]])
    else:
        print(0)
