from Graph import *

file = open('SampleGraph.txt', 'r')
lines = file.readlines()
file.close()

templine = []
for x in lines:
    templine.append(x.replace('\n', ''))

g = Graph()

for x in templine[1]:
    if x == ' ':
        pass
    else:
        g.add_vertex(x)
templine.pop(0)
templine.pop(0)

for x in templine:
    try:
        number = x[4]+x[5]
        g.add_edge_with_weight(x[0],x[2],int(number))
    except:
        try:
            g.add_edge_with_weight(x[0],x[2],int(x[4]))
        except:
            g.add_edge(x[0],x[2])


# The above part takes care of reading the file /////////////////////////////////

g.remove_vertex('h')
g.is_complete()
print('number of edges in the graph:',g.n_edges())
print(g.adjacent('a','f'))
g.get_weight('b','h')
g.degree('c')
print('number of vertices in the graph:',g.size())

g.add_vertex('k')
g.add_edge_with_weight('k','a',5)
g.add_edge_with_weight('g','k',2)
g.set_weight('a','c',7)
print('')

g.print_sample_graph()
