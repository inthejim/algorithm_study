import sys

si=sys.stdin.readline

n=int(si())
dp=[0]*(16)
dp[1]=3
for i in range(2,n//2+1):
    dp[i]=3*dp[i-1]+2
    for j in range(1,i-1):
        dp[i]+=dp[j]*2
if(n%2==0):
    print(dp[n//2])
else:
    print(0)
