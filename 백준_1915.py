import sys
si=sys.stdin.readline

n,m=map(int,si().split(' '))
data=[[*map(int,si().strip())] for _ in range(n)]
print(data)
for i in range(1,n):
    for j in range(1,m):
        if(data[i][j]==0):
            continue
        data[i][j]+=min(data[i-1][j],data[i][j-1],data[i-1][j-1])

print(max(map(max,data))**2)


