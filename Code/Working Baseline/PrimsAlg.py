import sys
from Functions import readFile


def Prims(Graph):
    MST = {}                    #list of edges making MST
    Visited = []                #list of visited vertices
    Vertices = list(Graph.keys())
    looptimes = len(Vertices)-1
    Visited.append(Vertices[0])             #add first vertex to Visited
    
    
    for i in range (looptimes):
        minlen = 999
        bestvertex = None
        for vertex in Visited:
            #curvertex = vertex
            edges = Graph[vertex]  #dict
            keys = list(Graph[vertex].keys()) #list
            for key in keys:
                if (edges[key] < minlen) and (key not in Visited):     # fix = key not in Visited
                    minlen = edges[key]
                    bestvertex = key
                    curvertex = vertex
        
        del Graph[curvertex][bestvertex]
        del Graph[bestvertex][curvertex]
        
        Visited.append(bestvertex)
        addEdge(MST, [curvertex, bestvertex])
    
    return MST
    
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
    
filename = sys.argv[1]        
Graph = readFile(filename)      
  
print(Prims(Graph))