import sys

si=sys.stdin.readline
n=si().strip()
dp=[0]*len(n)
dp[0]=1

if len(n)>=2:
    if(n[1]!='0' and int(n[0]+n[1])<=34):
        dp[1]=2
    else:
        dp[1]=dp[0]

if len(n)>=3:
    for i in range(2, len(n)):
        if(n[i]!='0' and 10<int(n[i-1]+n[i])<=34):
            dp[i]=dp[i-1]+dp[i-2]
        elif n[i]!='0':
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-2]

print(dp[len(n)-1])
