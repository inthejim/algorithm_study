class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]

        for connection in connections:
            start, end= connection[0], connection[1]
            graph[start].append((end,-1))
            graph[end].append((start,1))

        visited=[0]*n

        count=0
        def dfs(node):
            nonlocal count
            visited[node]=1
            for i in graph[node]:
                if(visited[i[0]]==0):
                    if(i[1]==-1):
                        count+=1
                    dfs(i[0])
        dfs(0)
        return count
