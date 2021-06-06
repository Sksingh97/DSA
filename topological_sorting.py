graph = []
color = { }

def initialize(n):
    for i in range(n):
        edge = []
        graph.append(edge)
        color[i] = 'W'

def addEdge( u, v):
    graph[u].append(v)


initialize(4)
addEdge(0,2)
addEdge(0,1)
addEdge(1,3)
addEdge(2,3)
st=[]
def dfsCore(source):
    if color[source] == 'W':
        print("Visited Node : ", source)
        color[source] = 'G'
        for nei in graph[source]:
            dfsCore(nei)
        color[source] = 'B'
        st.append(source)
    elif color[source] == 'G':
        print("Cycle Found at Node : ", source)

dfsCore(0)
while(len(st)>0):
    print(st[-1])
    st.pop()