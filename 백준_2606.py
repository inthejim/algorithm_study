n=int(input())
m=int(input())
visited=[False for i in range(n+1)]
l=[]
graph=[[] for i in range(n+1)]
for i in range(m):
  l.append(list(map(int, input().split())))

for i in range(m):
  graph[l[i][0]].append(l[i][1])
  graph[l[i][1]].append(l[i][0])

def bfs(graph, visited, i):
  visited[i]=True
  for j in graph[i]:
    if not visited[j]:
      bfs(graph, visited, j)

bfs(graph, visited, 1)
print(visited.count(True)-1)
  
