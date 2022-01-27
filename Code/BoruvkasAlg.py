#loop components, every edge gets added to MST through normal method

import sys
from Functions import readFile

def Boruvkas(Graph):
    total = 0
    #init MST as empty dict and components as a set of all vertices
    MST = {}
    components = [set([item]) for item in list(Graph.keys())] #list of sets
    # set of sets ???
    
    while (len(components) > 1):    #keep looping through components until there is only 1 left
        for component in components:
            #find shortest edge and tentatively add it to MST
            bestvertexFROM, bestvertexTO = findShortestEdge(Graph, component)
            addEdge(MST, [bestvertexFROM, bestvertexTO])
            
            #for as long as theres a cycle remove edge that causes cycle, find a new edge and tentatively add it to MST            
            while detectCycle(MST):         
                removeEdge(MST, [bestvertexFROM, bestvertexTO])
                del Graph[bestvertexFROM][bestvertexTO]
                del Graph[bestvertexTO][bestvertexFROM]
                bestvertexFROM, bestvertexTO = findShortestEdge(Graph, component)
                addEdge(MST, [bestvertexFROM, bestvertexTO])
            
            #best edge and no cycle, merge components and remove edge from Graph
            mergeComponents(components, bestvertexFROM, bestvertexTO)
            total += Graph[bestvertexFROM][bestvertexTO]
            del Graph[bestvertexFROM][bestvertexTO]
            del Graph[bestvertexTO][bestvertexFROM] 
                   
    return MST, total

def mergeComponents(components, bestvertexFROM, bestvertexTO):
    optimise = 0
    for component in components:

        #if bestvertexFROM in component:       
            #component1 = component              
            #optimise += 1
        #if bestvertexTO in component:
            #component2 = component            
            #optimise += 1
            
        if bestvertexFROM in component:       
            component1 = component              
            optimise += 1
        elif bestvertexTO in component:
            component2 = component            
            optimise += 1

        if optimise == 2: #trying to merge the same component ? maybe problem in few lines above ?
            #print(bestvertexFROM, bestvertexTO)
            #print(component1, component2)
            components.remove(component1)
            components.remove(component2)
            components.append(component1.union(component2))
            return
            

                
def findShortestEdge(Graph, component):
    min = 999
    for vertex in component:
        for adjvertex in list(Graph[vertex].keys()):
            if Graph[vertex][adjvertex] < min:
                bestvertexFROM = vertex
                bestvertexTO = adjvertex
                min = Graph[vertex][adjvertex]
    return bestvertexFROM, bestvertexTO
            
        
    

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
        MST[vertex1] = set([vertex2]) #this line will never run ?
        
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
  
print(Boruvkas(Graph))
