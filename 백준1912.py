import sys

sys.setrecursionlimit(10**6)

si=sys.stdin.readline

n=int(si().strip())
data=list(map(int,si().strip().split()))
memo=[0 for _ in range(n)]
def solution(i):
    if(i==n-1):
        memo[i] = data[i]
        return memo[i]
    if(memo[i]):
        return memo[i]
    memo[i] = max(data[i], data[i]+solution(i+1))
    return memo[i]

for i in range(n-1,-1,-1):
    solution(i)

print(max(memo))
