noof_vertices = sys.argv[1]
saturation = sys.argv[2]     #percentage of vertices
randomness = sys.argv[3]     #multiplier for variance
weightmax = sys.argv[4]      #x weight of edges (without randomness included)

Graph = {}
real_noof_edges = (round(noof_vertices + noof_vertices * (1 / randint(-randomness, randomness))))
real_weightmax = (weightmax + weightmax * (1 / randint(-randomness, randomness))


for i in range (real_noof_edges):
    Graph[i] = {}
    
    for i in range (((1 / saturation) * noof_vertices) * 1 / randint(-randomness, randomness)):
        #add vertices and weights
        Graph[i][randint(real_noof_edges)] = randint(real_weightmax)