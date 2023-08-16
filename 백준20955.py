#실패...
import sys

si=sys.stdin.readline
N,M=map(int,si().strip().split())
data=list(list(map(int,si().strip().split())) for _ in range(M))

child=[[] for _ in range(N+1)]
#heap: parent[child]:parentnode
parent={}
for u,v in data:
    p=min(u,v)
    c=max(u,v)
    parent[c]=p
    child[p].append(c)

cnt=0
visited=[0 for _ in range(N+1)]

#dfs -> parent node, child node 모두 확인하기
def dfs(node):
    if(visited[node]==1):
        return 0
    else:
        visited[node]=1
    if(node in parent):
        dfs(node)
    for i in child[node]:
        dfs(i)
    return 1

for i in range(1,N+1):
    cnt+=dfs(i)

print(cnt-1)
    
