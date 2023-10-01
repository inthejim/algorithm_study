class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=[[] for _ in range(n)]
        distance=[0]*n
        for (u,v), p in zip(edges, succProb):
            graph[u].append((v,p))
            graph[v].append((u,p))

        pq=[]
        heapq.heappush(pq,(-1,start_node))
        distance[start_node]=1
        
        while(pq):
            per, curr=heapq.heappop(pq)
            if(curr==end_node):
                return per*-1
            if(per*-1<distance[curr]):
                continue
            for i in graph[curr]:
                if(distance[i[0]]==-1 or distance[i[0]]*-1<i[1]*per*-1):
                    distance[i[0]]=i[1]*per*-1
                    heapq.heappush(pq,(-distance[i[0]], i[0]))
      
        return 0
                

            
            
            
        
