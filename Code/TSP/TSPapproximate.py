import sys

#Triangle inequality does not hold for my random graphs

sys.path.insert(0, r'C:\Users\glen3\Desktop\4th Year\Project\Code')

from KruskalsAlgDCWIP import *
from Functions import readFile

def ApxTspTrip(Graph, MST):
    Route = []
    RouteLength = 0
    #visited = set()       #dont need as if its in route its been visited
    stack = []             #stack of lists?
    vertices = list(Graph.keys())   
    
    Route.append(vertices[0])
    stack.append(list(MST[vertices[0]]))


    #print(MST)
    while stack:
        #print(Route, stack)
        neighbours = stack.pop()
        vertex = neighbours.pop()
        Route.append(vertex)
        
        if neighbours:  
            stack.append(neighbours)
        
        #get neighbours
        VertexNeighbours = set(MST[vertex])
        VertexNeighbours = VertexNeighbours.difference(Route)
        if VertexNeighbours:
            stack.append(list(VertexNeighbours))
    
    #return to first vertex
    Route.append(vertices[0])
    print(Route)
    return Route


filename = sys.argv[1]
Graph = readFile(filename)
MST, lengthMST = Kruskals(Graph)   #needs to inc the 'backwards edges'
print(MST, lengthMST)

ApxTspTrip(Graph, MST)
