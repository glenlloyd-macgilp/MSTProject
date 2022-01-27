#problem terminating program. originally checking len(Graph) however must check len(graph.leys()) also
#make a better method for deleting from Graph so as not to end up with lots of keys

import pickle

import copy
import sys
from Functions import readFile

def Kruskals(Graph):

    total = 0
    edges = sort(Graph)
    #print(edges)
    
    #keeps the MST in a nicer format for finding edges
    GraphMST = {}   #dict of sets #MUST BE A BETTER WAY TO INIT THIS ?
    for vertex in list(Graph.keys()):
        GraphMST[vertex] = set()
    
    
    MST = {}                    #Graph of edges making MST
    
    #while len(MST) < (len(Graph) - 1):
    for i in range (len(Graph) - 1):
        min = 999
        #print(MST)
        
                           
                    
        #find shortest edge
        #print(Graph)
        #vertex1, vertex2 = findShortestEdge(Graph)
        #vertex1, vertex2 = edges.pop()[1]
        
        edge = edges.pop()
        length = edge[0]
        vertex1, vertex2 = edge[1]
        
        #print(vertex1, vertex2)
        #add vertices to MST
        #MST.append({vertex1 : vertex2})
        #print(GraphMST)
        MST, GraphMST = addEdge(MST, GraphMST, [vertex1, vertex2])
        #print(edge)
        #print("here", GraphMST)
        #detect cycle, if it makes a cycle remove edge from Graph and look for shortest edge again    
        while detectCycle(GraphMST):   #this somehow touches GraphMST, watch scope and referencing ?
            #is a cycle, delete edge from Graph and MST and 
            #print(MST)
            #print(vertex1, vertex2)
            MST, GraphMST = removeEdge(MST, GraphMST, [vertex1, vertex2])
            #print(GraphMST)
            #print(vertex1, vertex2)
            
            #del Graph[vertex1][vertex2]
            #del Graph[vertex2][vertex1]     
            
            #vertex1, vertex2 = findShortestEdge(Graph)
            
            #vertex1, vertex2 = edges.pop()[1]
            edge = edges.pop()
            length = edge[0]
            vertex1, vertex2 = edge[1]
            
            
            MST, GraphMST = addEdge(MST, GraphMST, [vertex1, vertex2])
            #print("EEK")
            
        #print("also here", GraphMST)
        #print(MST)
        
        #print(Graph, vertex1, vertex2)
        total += length
        
        #suitable edge found, remove it from the Graph, already added to MST
        
        #del Graph[vertex1][vertex2]
        #del Graph[vertex2][vertex1] 
        #print(MST)
                    
    
    #return MST, total
    return GraphMST, total
    
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
    
def detectCycle(PassedGraphMST):     #uses a DFS algorithm
    #GraphMST = copy.deepcopy(PassedGraphMST)
    GraphMST = pickle.loads(pickle.dumps(PassedGraphMST, -1))
    #which is faster ??
    vertices = (list(GraphMST.keys()))   #change vertices to set
    #print(GraphMST)
    
                                        #doesn't work for backward edges
                                        #eg [vertex1][vertex2] AND [vertex2][vertex1]
                                        #mst is only a->b and not b->a
    
    #use a var called JustCameFrom to store last checked vertex. for ret True the naughty vertex must not be JCF vertex
    #doesnt work as stack can fill up and JCF vertex will change
    #delete edges that have been traversed ??
    
    
    while vertices:
        vertex = vertices.pop()
        visited = set()    #set of visited nodes for current vertex
        stack = []     #stack is for vertices to visit
        
        stack.append(vertex)
        while stack:
            curvertex = stack.pop()
            #print(curvertex, visited, stack)

            #print("um")
            
            if (curvertex in visited):
                
                #print(curvertex, visited, JustCameFrom)
                #print(PassedGraphMST, "TRUE")
                #print("TRUE TRUE TRUE TRUE!!!!!")
                return True
             

            #print(Graph, curvertex)
            visited.add(curvertex)
            #print(curvertex, vertices)
            if curvertex in vertices:
                vertices.remove(curvertex)                      ##backward edges can break this alg ????? line below. maybe nb ?
                
            adjedges = list(GraphMST[curvertex])
            stack.extend(adjedges)
            #print(adjedges)
            for adjedge in adjedges:
                #print(adjedge, GraphMST[adjedge])
                GraphMST[adjedge].remove(curvertex)
            GraphMST[curvertex] = set()    #delete all edges connected to this vertex 
        #print(GraphMST)
                
            
            #print(list(Graph[curvertex]))
            #print(vertex, curvertex, stack, visited)
    #print(PassedGraphMST, "FALSE")
    return False    
    
def addEdge(MST, GraphMST, edge):
    vertex1, vertex2 = edge[0], edge[1]
    if vertex1 in MST:
        MST[vertex1].add(vertex2)
    elif vertex2 in MST:
        MST[vertex2].add(vertex1)
    else:
        #print(vertex1, vertex2)
        MST[vertex1] = set([vertex2])
    
    GraphMST[vertex1].add(vertex2)
    GraphMST[vertex2].add(vertex1)
    return MST, GraphMST
    
    
    
        
def removeEdge(MST, GraphMST, edge):     #will need to delete key as well if len(MST[vertexn]) = 1. also use dict of sets
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
    
    GraphMST[vertex1].remove(vertex2)
    GraphMST[vertex2].remove(vertex1)
    
    return MST, GraphMST
            

def sort(Graph):    #returns a list of edges in order length ascending
    #[[len, [vertex1, vertex2]], ... ]
    edgesList = []
        
    for vertex in list(Graph.keys()):
        adjVertices = Graph[vertex]     #set
        for adjVerticex in list(adjVertices.keys()):
            edgesList.append([Graph[vertex][adjVerticex], [vertex, adjVerticex]])
            
            #very dodgey
            #update: i think this is fine as im actually looping over a list of keys and not the 'graph'
            #hence im not actually updating the lists im looping over?
            del Graph[vertex][adjVerticex]
            del Graph[adjVerticex][vertex]
            
    edgesList.sort(reverse=True)
            
    return edgesList

filename = sys.argv[1]        
Graph = readFile(filename)      
  
print(Kruskals(Graph))