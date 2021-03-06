from NormalGraph import *

file = open('SampleGraph.txt', 'r')
lines = file.readlines()
file.close()

templine = []
for x in lines:
    templine.append(x.replace('\n', ''))

g = Graph(6,True)

for x in templine[1]:
    if x == ' ':
        pass
    else:
        g.addVertex(x)
templine.pop(0)
templine.pop(0)

for x in templine:
    try:
        number = x[4]+x[5]
        g.addEdge_W(x[0],x[2],int(number))
    except:
        try:
            g.addEdge_W(x[0],x[2],int(x[4]))
        except:
            g.addEdge(x[0],x[2])


# The above part takes care of reading the file /////////////////////////////////

g.removeVertex('h')
g.isComplete()
print('number of edges in the graph:',g.nEdges())
print(g.adjacent('a','f'))
g.getWeight('b','h')
g.degree('c')
print('number of vertices in the graph:',g.size())

g.addVertex('k')
g.addEdge_W('k','a',5)
g.addEdge_W('g','k',2)
g.setWeight('a','c',7)
print('')

g.printSampleGraph()
