import sys

si=sys.stdin.readline

n=int(si().strip())
podo=[int(si().strip()) for _ in range(n)]

dp=[0]*(n+1)
dp[1]=podo[0]
if(n>1):
    dp[2]=podo[0]+podo[1]

for i in range(3,len(podo)+1):
    dp[i]=max(dp[i-3]+podo[i-2]+podo[i-1], dp[i-2]+podo[i-1], dp[i-1])

print(dp[n])
