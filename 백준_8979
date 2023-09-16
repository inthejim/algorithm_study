#20%성공,,
import sys
si=sys.stdin.readline

n, k =map(int,si().split(' '))
medals=[[] for _ in range(n)]
ranking=set()
for i in range(n):
    idx,g,s,b=map(int,si().split(' '))
    medals[i]=[idx,g,s,b]
    ranking.add((g,s,b))

ranking=list(ranking)
ranking.sort(key=lambda x:(x[0],x[1],x[2]) , reverse=True)

for i in range(n):
    if(medals[i][0]==k):
        print(ranking.index(tuple(medals[i][1:]))+1)
