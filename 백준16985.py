import sys
import itertools
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

