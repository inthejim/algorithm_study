import sys

si=sys.stdin.readline

a,b,c=map(int,si().split(' '))
data=[[*map(int,si().split())] for _ in range(3)]

time=[0]*101

for s,e in data:
    for j in range(s,e):
        time[j]+=1

time=str(time)

print(sum([a*time.count('1'),b*time.count('2')*2,c*time.count('3')*3]))
