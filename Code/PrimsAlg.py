import sys
from queue import PriorityQueue

from Functions import readFile    #MINE

## add length to total before iterations start



def Prims(Graph):
    total = 0
    MST = {}                    #list of edges making MST
    Visited = []                #list of visited vertices    
    looptimes = len(list(Graph.keys()))
    pqueue = PriorityQueue()
    startvertex = list(Graph.keys())[0]
    startadjvertices = list(Graph[startvertex].keys())
    min = 999   #arbitrary
    
                                                             #can start anywhere ?????
    for adjvertex in startadjvertices:                       #find shortest edge for startvertex
        if (Graph[startvertex][adjvertex] < min):
            startadjvertex = adjvertex
            min = Graph[startvertex][adjvertex]
    
    addNeighbours(Graph, pqueue, startvertex)
    addNeighbours(Graph, pqueue, startadjvertex)
    Visited.append(startvertex)
    Visited.append(startadjvertex)
    addEdge(MST, [startvertex, startadjvertex])   #add best edge for first vertex to MST
    total += Graph[startvertex][startadjvertex]
    count = 2 #2 vertices in MST at this stage of execution 
    
    
    while (count != looptimes):
        _, edge = pqueue.get(pqueue)     #_ ignore the value, dont care about weight as its already been dealt with 
        
        if edge[0] not in Visited:
            newVertex = edge[0]
        elif edge[1] not in Visited:
            newVertex = edge[1]
        else:                           #both vertices in MST, ignore edge
            continue
            
        
        
        Visited.append(newVertex)
        addEdge(MST, edge)  #edge is a list of 2 vertices
        total += Graph[edge[0]][edge[1]]
        addNeighbours(Graph, pqueue, newVertex)
        count += 1
    
    return MST, total
    
def addEdge(MST, edge):
    vertex1, vertex2 = edge[0], edge[1]
    if vertex1 in MST:
        MST[vertex1].add(vertex2)
    elif vertex2 in MST:
        MST[vertex2].add(vertex1)
    else:
        MST[vertex1] = set([vertex2])
        
def removeEdge(MST, edge):     #will need to delete key as well if len(MST[vertexn]) = 1. also use dict of sets
    vertex1, vertex2 = edge[0], edge[1]
    if vertex1 in MST:
        if len(MST[vertex1]) == 1:
            del MST[vertex1]
        else:
            MST[vertex1].discard(vertex2)
    
    if vertex2 in MST:
        if len(MST[vertex2]) == 1:
            del MST[vertex2]
        else:
            MST[vertex2].discard(vertex1)
            
def addNeighbours(Graph, pqueue, vertex):    #duplicates ?
    for adjvertex in list(Graph[vertex]):
        pqueue.put((Graph[vertex][adjvertex], [vertex, adjvertex]))
    
#filename = sys.argv[1]        
#Graph = readFile(filename)      
#print(Prims(Graph))