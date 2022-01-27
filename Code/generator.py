import sys
import random

def safeRandom(a, b):
    retnum = random.randint(a, b)
    escapetest = 0
    while (retnum == 0):
        retnum = random.randint(a, b)
        escapetest+=1
        if escapetest == 25:
            print(a, b)
        
    return retnum

noof_vertices = int(sys.argv[1])
#must make sure that x->y => y->x-
#must makes sure x-> x cant exist


saturation = int(sys.argv[2])     #number of edges
randomness = int(sys.argv[3])     #multiplier for variance
weightmax = int(sys.argv[4])      #x weight of edges (without randomness included)
filename = sys.argv[5]

Graph = {}
real_noof_edges = (round(noof_vertices + noof_vertices * (1 / safeRandom(-randomness, randomness))))
real_weightmax = (weightmax + weightmax * (1 / safeRandom(-randomness, randomness)))

real_noof_edges = int(real_noof_edges)
real_weightmax = int(real_weightmax)

for i in range (real_noof_edges):    #initialise graph with empty sets/dicts for each vertex
    Graph[i] = {}

for i in range (real_noof_edges):
    
    edgesloop = ((saturation) + round(saturation * 1 / safeRandom(-randomness, randomness)))
    while (edgesloop == 0):
        edgesloop = ((saturation) + round(saturation * 1 / safeRandom(-randomness, randomness)))
    
    for j in range (edgesloop):
        #add vertices and weights
        wweight = safeRandom(0, real_weightmax)
        adjvertex = safeRandom(0, real_noof_edges-1)
        while (i == adjvertex):
            adjvertex = safeRandom(0, real_noof_edges-1)
        
        Graph[i][adjvertex] = wweight
        Graph[adjvertex][i] = wweight
        
with open (filename, 'w') as f:
    line = ""
    for key in list(Graph.keys()):
        f.write(str(key) + " = " + str(Graph[key]) + '\n')
    
 
 

    
    