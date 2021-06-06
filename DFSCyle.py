graph = []
color = { }


def initialize(n):
    for i in range(n):
        edge = []
        graph.append(edge)
        color[i] = 'W'

def addEdge( u, v ):
    graph[u].append(v)

initialize(6)
addEdge(0,1)
addEdge(1,3)
addEdge(3,2)
addEdge(2,0)
addEdge(1,5)
addEdge(0,4)


def dfsCore(source):
    print("Graph  : ",graph, "\n color : ", color)
    if( color[source] == 'W'):
        print("Visiting Node", source)
        color[source] = 'G'
        for nei in graph[source]:
            dfsCore(nei)
        color[source] = 'B'
    elif color[source] == 'G':
        print("Cycle Found On Node : ",source)


dfsCore(0)




