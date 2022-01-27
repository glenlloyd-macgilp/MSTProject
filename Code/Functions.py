import pprint
import sys

def readFile(filename):     #works with numbers as keys
    Graph = {}
    with open (filename, 'r') as f:
        for line in f:
            line = line.strip("\n")
            key, vals = line.split(" = ")
            
            vals = vals[1:-1]

            vals = vals.split(", ")
            Graph[int(key)] = {}
            #print(vals)
            for pair in vals:
                splitpair = pair.split(":")
                Graph[int(key)][int(splitpair[0])] = int(splitpair[1])
    return Graph


if len(sys.argv) != 2: 
    if sys.argv[2] == "print":
        pprint.pprint(readFile("Graph3.txt"))
        