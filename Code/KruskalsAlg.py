#problem terminating program. originally checking len(Graph) however must check len(graph.leys()) also
#make a better method for deleting from Graph so as not to end up with lots of keys

import sys
from Functions import readFile

def Kruskals(Graph):

    edges = sort(Graph)
    #print(edges)
    
    MST = {}                    #Graph of edges making MST
    
    #while len(MST) < (len(Graph) - 1):
    for i in range (len(Graph) - 1):
        min = 999
        #print(MST)
        
                           
                    
        #find shortest edge
        #print(Graph)
        #vertex1, vertex2 = findShortestEdge(Graph)
        vertex1, vertex2 = edges.pop()[1]

        #print(vertex1, vertex2)
        #add vertices to MST
        #MST.append({vertex1 : vertex2})
        MST = addEdge(MST, [vertex1, vertex2])
        #detect cycle, if it makes a cycle remove edge from Graph and look for shortest edge again    
        while detectCycle(MST):
            #is a cycle, delete edge from Graph and MST and 
            #print(MST)
            #print(vertex1, vertex2)
            removeEdge(MST, [vertex1, vertex2])
            #print(vertex1, vertex2)
            
            #del Graph[vertex1][vertex2]
            #del Graph[vertex2][vertex1]
            
            #vertex1, vertex2 = findShortestEdge(Graph)
            vertex1, vertex2 = edges.pop()[1]
            addEdge(MST, [vertex1, vertex2])
            #print(MST)
            
        #suitable edge found, remove it from the Graph, already added to MST
        
        #del Graph[vertex1][vertex2]
        #del Graph[vertex2][vertex1] 
        #print(MST)
                    
    
    return MST
    
def findShortestEdge(Graph):
    min = 999
    #print(Graph)
    for vertex in list(Graph.keys()):
        vertexEdges = Graph[vertex]     #dict
        for edge in list(vertexEdges.keys()):
            if vertexEdges[edge] < min:
                min = vertexEdges[edge]
                vertex1 = vertex
                vertex2 = edge
    return vertex1, vertex2  

def detectCycle(Graph):
    vertices = (list(Graph.keys()))   #change vertices to set
    
    while vertices:
        vertex = vertices.pop()
        visited = set()    #set of visited nodes for current vertex
        stack = []     #stack is for vertices to visit
        
        stack.append(vertex)
        while stack:
            curvertex = stack.pop()

            #print("um")
            
            if curvertex in visited:
                #print(Graph, "TRUE")
                return True
             

            #print(Graph, curvertex)
            visited.add(curvertex)
            #print(curvertex, vertices)
            if curvertex in vertices:
                vertices.remove(curvertex)                      ##backward edges can break this alg ????? line below. maybe nb ?
            if curvertex in list(Graph.keys()):          ##else vertex isnt a key in graph
                stack.extend(list(Graph[curvertex]))
            
            #print(list(Graph[curvertex]))
            #print(curvertex, stack, visited)
    return False
    
def addEdge(MST, edge):
    vertex1, vertex2 = edge[0], edge[1]
    if vertex1 in MST:
        MST[vertex1].add(vertex2)
    elif vertex2 in MST:
        MST[vertex2].add(vertex1)
    else:
        #print(vertex1, vertex2)
        MST[vertex1] = set([vertex2])
    return MST
        
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
    #return MST
            

def sort(Graph):    #returns a list of edges in order length ascending
    #[[len, [vertex1, vertex2]], ... ]
    edgesList = []
        
    for vertex in list(Graph.keys()):
        adjVertices = Graph[vertex]     #set
        for adjVerticex in list(adjVertices.keys()):
            edgesList.append([Graph[vertex][adjVerticex], [vertex, adjVerticex]])
            
            #very dodgey
            del Graph[vertex][adjVerticex]
            del Graph[adjVerticex][vertex]
            
    edgesList.sort(reverse=True)
            
    return edgesList

filename = sys.argv[1]        
Graph = readFile(filename)      
  
print(Kruskals(Graph))