from Graph import *

file = open('SampleGraph.txt', 'r')
lines = file.readlines()
file.close()

templine = []
for x in lines:
    templine.append(x.replace('\n', ''))

graph = Graph()

for x in templine[1]:
    if x == ' ':
        pass
    else:
        graph.add_vertex(x)
templine.pop(0)
templine.pop(0)

for x in templine:
    try:
        number = x[4]+x[5]
        graph.add_edge_with_weight(x[0],x[2],int(number))
    except:
        try:
            graph.add_edge_with_weight(x[0],x[2],int(x[4]))
        except:
            graph.add_edge(x[0],x[2])


# The above part takes care of reading the file /////////////////////////////////

graph.remove_vertex('h')
graph.is_complete()
print('number of edges in the graph:',graph.n_edges())
print(graph.adjacent('a','f'))
graph.get_weight('b','h')
graph.degree('c')
print('number of vertices in the graph:',graph.size())

graph.add_vertex('k')
graph.add_edge_with_weight('k','a',5)
graph.add_edge_with_weight('g','k',2)
graph.set_weight('a','c',7)
print('')

graph.print_sample_graph()
