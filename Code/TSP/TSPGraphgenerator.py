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

weightmax = int(sys.argv[2])      #x weight of edges (without randomness included)
filename = sys.argv[3]

Graph = {}

for i in range (noof_vertices):    #initialise graph with empty sets/dicts for each vertex
    Graph[i] = {}

for i in range (noof_vertices):
    for j in range (i, noof_vertices):
        if (i != j):    #probably a smart way to not have to check this condition as often. loop for i then loop for j ?
            wweight = safeRandom(1, weightmax)
            Graph[i][j] = wweight
            Graph[j][i] = wweight
        

        
with open (filename, 'w') as f:
    line = ""
    for key in list(Graph.keys()):
        f.write(str(key) + " = " + str(Graph[key]) + '\n')
    
 
 

    
    