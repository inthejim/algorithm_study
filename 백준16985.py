#시간초과..

import sys
import itertools
from collections import deque
#한 판당 4가지의 경우
#판 당 4가지 중 1 선택, *5 조합
#조합들의 층 순서 결정, 순열

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

si=sys.stdin.readline

def rotate(sq):
    ret=[[0]*5 for _ in range(5)]

    for r in range(5):
        for c in range(5):
            ret[c][5-r-1]=sq[r][c]
    
    return ret

#cube[5][4]:1번부터 5번까지 판에 각 판이 돌아간 경우 4가지 포함
cube=[]
for i in range(5):
    sqs=[]
    sq=[]
    for j in range(5):
        l=si().strip()
        sq.append(list(map(int,l.split())))
    sqs.append(sq)
    for _ in range(3):
        sq=rotate(sq)
        sqs.append(sq)
    cube.append(sqs)

def bfs(miro):
    visited=[list([0]*5 for _ in range(5)) for _ in range(5)]
    queue=deque([])
    queue.append([0,0,0,0])
    visited[0][0][0]=1

    while(queue):
        x,y,z,depth=queue.popleft()
        if(x==4 and y==4 and z==4):
            return depth
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if(0<=nx<5 and 0<=ny<5 and 0<=nz<5 and visited[nx][ny][nz]==0):
                visited[nx][ny][nz]=1
                queue.append([nx,ny,nz,depth+1])
    return -1

min_value=100000
for id1,id2,id3,id4,id5 in itertools.permutations([0,1,2,3,4]):
    for idx in itertools.product([0,1,2,3],repeat=5):
        miro=[]
        miro.append(cube[id1][idx[0]])
        miro.append(cube[id2][idx[1]])
        miro.append(cube[id3][idx[2]])
        miro.append(cube[id4][idx[3]])
        miro.append(cube[id5][idx[4]])
        min_value=min(bfs(miro),min_value)

print(min_value)
    
