from collections import deque

def bfs(graph, d):
    visited=set([])
    visited.add(d)
    queue=deque([[d,0]])
    while(queue):
        v=queue.popleft()
        current, depth=v[0],v[1]
        if(answer[current]==-1):
            answer[current]=depth    
        for node in graph[current]:
            if(node not in visited):
                visited.add(node)
                queue.append([node, depth+1])
                

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    global answer
    answer=[-1]*(n+1)

    for road in roads:
        a, b = road[0], road[1]
        graph[a].append(b)
        graph[b].append(a)

    bfs(graph, destination)
    result=[]
    for source in sources:
        result.append(answer[source])

    return result
