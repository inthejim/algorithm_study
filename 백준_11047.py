import sys
si=sys.stdin.readline


n,k=map(int,si().split(' '))
coins=[int(si()) for _ in range(n)]
count=0
i=len(coins)-1
while(i>=0 and k!=0):
    if(k%coins[i]==k):
        i-=1
    else:
        coin_number=k//coins[i]
        count+=coin_number
        k-=coins[i]*coin_number
        i-=1

print(count)
