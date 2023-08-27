from collections import deque
import sys

def bfs(i,j):
    q.append([i,j,0])
    visit = [[False]*m for _ in range(n)]
    visit[i][j] = True
    maxs=0

    while q:
        x,y,c = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and s[nx][ny]=='L':
                visit[nx][ny] = True
                q.append([nx,ny,c+1])

        maxs = max(maxs,c)
    return maxs        

n,m= map(int,input().split())
s =[sys.stdin.readline().strip() for _ in range(n)]

dx  =[1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

res = 0
for i in range(n):
    for j in range(m):
        if s[i][j]=='L':

            #시간초과때문에 조건 추가
            cnt=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if(0<=nx<n and 0<=ny<m and s[nx][ny]=='L'):
                    cnt+=1
                if(cnt>2):
                    break
            if(cnt<=2):
                res = max(res,bfs(i,j))
print(res)
