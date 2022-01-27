import sys
import os

def Translate(filename):     #works with numbers as keys
    Graph = {}
    with open (filename, 'r') as f:
        for line in f:
            line = line.strip("\n")
            key, vals = line.split(" -> ")
            
            vals = vals[1:-1]

            vals = vals.split(")(")
            Graph[int(key)] = {}
            #print(vals)
            for pair in vals:
                splitpair = pair.split(",")
                #print(splitpair)
                Graph[int(key)][int(splitpair[0])] = int(splitpair[1])
              
    return Graph
    
def WriteToFile(Graph, filename):
    with open (filename, 'w') as f:
        line = ""
        for key in list(Graph.keys()):
            f.write(str(key) + " = " + str(Graph[key]) + '\n')
    
inputpath = r'C:\Users\glen3\Desktop\4th Year\Project\Code\TestingCollab\Graphs-20220121T222339Z-001\Graphs'
outputpath = r'C:\Users\glen3\Desktop\4th Year\Project\Code\TestingCollab\TranslatedGraphs'

inputdir = os.listdir(inputpath)

i = 0
for file in inputdir:
    InputFilename = inputpath + file
    OutputFilename = outputpath + r'\Graph' + str(i) + ".txt" 
    print(file, OutputFilename)
    WriteToFile(Translate(file), OutputFilename)
    

    
#InputFilename = sys.argv[1]
#OutputFilename = sys.argv[2]

#WriteToFile(Translate(InputFilename), OutputFilename)

