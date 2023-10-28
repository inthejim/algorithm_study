import sys
si=sys.stdin.readline

n=int(si())

timetable=[[*map(int,si().split(' '))] for _ in range(n)]
timetable.sort(key=lambda x: (x[1],x[0]))

count=0

base=0

for start_time, end_time in timetable:
    if start_time>=base:
        base = end_time
        count+=1

print(count)
