import sys
import heapq
#수정 필요...ㅎ
si=sys.stdin.readline

n,e=map(int,si().split(' '))

graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,si().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))

u,v=map(int,si().split(' '))


def solution(start):
    distance=[float('inf')]*(n+1)
    distance[start]=0
    queue=[]
    heapq.heappush(queue,[distance[start], start])

    while queue:
        current_distance, current=heapq.heappop(queue)

        if distance[current]<current_distance:
            continue
        
        for new, new_distance in graph[current]:
            tmp=current_distance+new_distance
            
            if tmp<distance[new]:
                distance[new]=tmp
                heapq.heappush(queue, [tmp, new])

    return distance


print(solution(1))
