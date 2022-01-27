with open("GlensKruskalsResults.txt", 'r') as f:
    GlensKruskalsResults = f.readlines()
    
with open("GlensPrimsResults.txt", 'r') as f:
    GlensPrimsResults = f.readlines()
    
with open("kruskal_results.txt", 'r') as f:
    kruskal_results = f.readlines()
    
with open("prim-results.txt", 'r') as f:
    prim_results = f.readlines()

i = 0    
#print(GlensKruskalsResults)
#print(kruskal_results)
print("Kruskals Results:")
for i in range(1000):
    if GlensKruskalsResults[i] != kruskal_results[i]:
        print("difference on line" + str(i) + ".  " + GlensKruskalsResults[i][:-1] + "   vs    " + kruskal_results[i][:-1])
    else:
        print(i)
    i += 1
    
print("Prims Results:")
for i in range(1000):
    if GlensPrimsResults[i] != prim_results[i]:
        print("difference on line" + str(i) + ".  " + GlensPrimsResults[i][:-1] + "   vs    " + prim_results[i][:-1])
    else:
        print(i)
    i += 1   