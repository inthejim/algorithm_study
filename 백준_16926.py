import sys

si=sys.stdin.readline
n,m,r=map(int,si().split(' '))
data=[[*map(int, si().split(' '))] for _ in range(n)]

def rotation():
    for i in range(min(n,m)//2):
        n_m=n-i-1
        m_m=m-i-1
        
        tmp=data[i][i]
        for j in range(i,m_m):
            data[i][j]=data[i][j+1]
        
        for j in range(i,n_m):
            data[j][m_m]=data[j+1][m_m]
        
        for j in range(m_m,i,-1):
            data[n_m][j]=data[n_m][j-1]
        
        for j in range(n_m,i,-1):
            data[j][i]=data[j-1][i]

        data[i+1][i]=tmp


for i in range(r):
    rotation()

for i in data:
    print(' '.join(list(map(str,i))))
