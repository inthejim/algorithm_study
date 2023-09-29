import sys
import heapq

si=sys.stdin.readline

n,m=map(int,si().split(' '))
dp=[int(2e9) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,si().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))

q=[]
heapq.heappush(q,(1,0))
dp[1]=0
while q:
    curr,d=heapq.heappop(q)
    if(dp[curr]>=d):
        for i in graph[curr]:
            c=d+i[1]
            if c<dp[i[0]]:
                dp[i[0]]=c
                heapq.heappush(q,(i[0],c))

print(dp[n])
