import sys
from heapq import heappop, heappush

si=sys.stdin.readline

n=int(si())
heap=[]

for _ in range(n):
    item=int(si())
    
    if(item!=0):
        heappush(heap,(abs(item), -1 if item<0 else 1))
    else:
        if(heap):
            x=heappop(heap)
            print(x[0]*x[1])
        else:
            print(0)

