#정답을 구하지 못했습니다ㅠ..

class Solution(object):
    parent=[]
    terminal=[]
    visited=[]

    def findTerminalNode(self, graph, node):
        if(not graph[node]):
            self.terminal.append(node)
            return
        for i in range(len(graph[node])):
            self.parent[graph[node][i]].append(node)
            if(self.visited[graph[node][i]]==0):
                self.visited[graph[node][i]]=1
                self.findTerminalNode(graph, graph[node][i])

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        self.parent=[[] for _ in range(len(graph))]
        self.visited=[0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if(self.visited[i]==0):
                self.visited[i]=1
                self.findTerminalNode(graph,i)

        result=[]
        for i in self.terminal:
            result.append(i)
            print(self.parent)

        result.sort()
        print(result)
