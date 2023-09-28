import sys
si=sys.stdin.readline
n, k=map(int, si().split(' '))
lines=[int(si()) for _ in range(n)]

start, end=1, max(lines)

while(start<end):
    mid=(start+end)//2
    count=0
    for line in lines:
        count+=line//mid
    
    if count>=k:
        start=mid+1
    else:
        end=mid-1

print(end)
