from collections import deque
#BFS:
graph=[]
visited={}

def initialize(n):
    for i in range(n):
        edge=[]
        graph.append(edge)
        visited[i]=False

def addEdge(u,v):
    graph[u].append(v)
    graph[v].append(u)

def bfsTraverse(source):
    print("Graph : ",graph)
    q = []
    q.append(source)
    visited[source] = True
    while len(q)>0:
        print("Q : ",q)
        top = q.pop()
        print(top)
        for neg in graph[top]:
            if(visited[neg] == False):
                q.append(neg)
                visited[neg] = True

initialize(6)
addEdge(0,1)
addEdge(0,2)
addEdge(0,3)
addEdge(1,4)
addEdge(2,5)
addEdge(4,5)

bfsTraverse(0)
