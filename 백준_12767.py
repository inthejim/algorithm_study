import sys

si=sys.stdin.readline
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintType(self,depth,setAtom):
        if not self.left and not self.right:
            setAtom.add(str(depth))
        if self.left:
            self.left.PrintType(2*depth,setAtom)
        if self.right:
            self.right.PrintType(2*depth+1,setAtom)

n,k=map(int,si().split(' '))
types={}
for _ in range(n):
    graph=[*map(int,si().split(' '))]
    root=Node(graph[0])
    for k in range(1,len(graph)):
        root.insert(graph[k])
    setAtom=set([])
    root.PrintType(1,setAtom)
    
    Stype=''.join(setAtom)

    if Stype in types.keys():
        types[Stype]+=1
    else:
        types[Stype]=1

print(len(types.keys()))
