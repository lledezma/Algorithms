class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.visited = {}
        self.depth_result = []

    def isDirect(self):
        adjan = []
        wgt = []
        vertic = []
        for y in self.vert_dict:
            if (len(vertic) == 1):
                pass
            else:
                vertic.append(y)
            for x in self.vert_dict[y]:
                adjan.append(x)
                for z in self.vert_dict[y][x]:
                    wgt.append(z)
        for y in self.vert_dict:
            if y == vertic[0]:
                pass
            for x in self.vert_dict[y]:
                if(x in vertic and y in adjan):
                    return False
                else:
                    pass
        return True

    def adjacent(self,v,u):
        if(v not in self.vert_dict):
            return False
        if(u in self.vert_dict[v]):
            return True
        else:
            return False

    def neighbors(self, v):
        try:
            temp = []
            for x in (self.vert_dict[v]):
                temp.append(x)
            print(temp)
        except:
            print('vertix:', v, 'not in the graph')



    def addVertex(self, node):
        if node not in self.vert_dict:
            self.num_vertices = self.num_vertices + 1
            self.vert_dict[node] = {}
        else:
            print('error')

    def removeVertex(self,v):
        if(v in self.vert_dict):
            temp = []
            for x in self.vert_dict:
                for y in self.vert_dict[x]:
                    if(y == v):
                        temp.append(x)
            for i in temp:
                del self.vert_dict[i][v]
            del self.vert_dict[v]
        else:
            print(v, 'vertex not in the graph')


    def addEdge_W(self, frm, to, weight):
        if frm not in self.vert_dict:
            self.addVertex(frm)
        if to not in self.vert_dict:
            self.addVertex(to)
        if(to in self.vert_dict[frm]):
            print("multiple edges not allowed")
            return
        else:
            self.vert_dict[frm][to] = []

        if(len(self.vert_dict[frm][to]) == 1):
            print("multiple edges not allowed")
            return

        self.vert_dict[frm][to].append(weight)



    def addEdge(self, frm, to):
        if frm not in self.vert_dict:
            self.addVertex(frm)
        if to not in self.vert_dict:
            self.addVertex(to)
        if(to in self.vert_dict[frm]):
            print("multiple edges not allowed")
            return
        else:
            self.vert_dict[frm][to] = []
        if(len(self.vert_dict[frm][to]) == 1):
            print("multiple edges not allowed")
            return
        self.vert_dict[frm][to].append('')


    def removeEdge(self,v,u):
        if(v in self.vert_dict) or (u in self.vert_dict):
            try:
                if(u not in self.vert_dict[v] and v not in self.vert_dict[u]):
                    print("no edge between vertices:", v, 'and', u)
                if u in self.vert_dict[v]:
                    del self.vert_dict[v][u]
                if v in self.vert_dict[u]:
                    del self.vert_dict[u][v]
            except:
                print("no edge between vertices:", v, 'and', u)
        else:
            print("no edge between vertices:", v, 'and', u)


    def getWeight(self,v,u):
        if v in self.vert_dict:
            if u in self.vert_dict[v]:
                if self.vert_dict[v][u][0] == '':
                    print("edge has no weight")
                else:
                    print('weight:',self.vert_dict[v][u][0])
            else:
                print("no edge from", v, 'to', u)
        else:
            print("no edge from", v, 'to', u)

    def setWeight(self,v,u,w):
        if v in self.vert_dict:
            if u in self.vert_dict[v]:
                self.vert_dict[v][u][0] = w
            else:
                print('no edge from', v, 'to', u)
        else:
            print(v, 'not in graph')


    def isEmpty(self):
        if len(self.vert_dict) == 0:
            print("The graph is empty")
        else:
            print("The graph not empty")


    def isComplete(self):
        n = len(self.vert_dict)
        calculation = (n*(n-1))/2
        if self.nEdges() < calculation:
            print("the graph is not complete")
        else:
            print("the graph is complete")


    def vertices(self):
        temp = []
        for i in self.vert_dict:
           temp.append(i)
        print(temp)


    def edges(self):
        for y in self.vert_dict:
            for x in self.vert_dict[y]:
                for z in self.vert_dict[y][x]:
                    print(y, '-->',x)

    def degree(self,v):
        count = 0
        if(v in self.vert_dict):
            print('deg+(',v,')', '=', (len(self.vert_dict[v])))

            for x in self.vert_dict:
                for y in self.vert_dict[x]:
                    if y == v:
                        count+=1
            print('deg-(',v,')', '=', count)
        else:
            print('vertex',v,'not in the graph')


    def size(self):
        return self.num_vertices

    def nEdges(self):
        count = 0
        for y in self.vert_dict:
            for x in self.vert_dict[y]:
                count = count + (len(self.vert_dict[y][x]))
        return(count)

    def clear(self):
        self.vert_dict = {}

    def vertexExists(self,v):
        if v in self.vert_dict:
            print('True')
        else:
            print('False')

    def print(self):
        for y in self.vert_dict:
            for x in self.vert_dict[y]:
                for z in self.vert_dict[y][x]:
                    print(y, '-->',x, 'weight:', z )

    def printSampleGraph(self):
        print(self.num_vertices)
        for x in self.vert_dict:
            print(x, end=' ')
        print('')
        for y in self.vert_dict:
            for x in self.vert_dict[y]:
                for z in self.vert_dict[y][x]:
                    print(y,x,z)
##########################################################  Depth-first search 

    def DFS(self):
        for x in self.vert_dict:
            self.visited[x] = []
            self.visited[x].append("x") #not visited
            self.visited[x].append(0)
        time = 0
        for x in self.vert_dict:
            if self.visited[x][0] == "x":
                self.DFS_Visit(x)
        # print(self.visited)

    def DFS_Visit(self,u):
        self.visited[u][0] = "o"     #visited
        self.visited[u][1] +=1

        self.depth_result.append(u)
        # print(self.depth_result)
        print(u, end = " ")

        for x in self.vert_dict[u]:
            if self.visited[x][0] == "x":
                self.DFS_Visit(x)

########################################################## 
    def BFS(self,x):
        for y in self.vert_dict:
            self.visited[y] = []
            self.visited[y].append("x") #not visited

        queue = []
        queue.append(x)
        self.visited[x][0] = "o"

        while queue:
            x = queue.pop(0)
            print(x, end = " ")
            for i in self.vert_dict[x]:
                if self.visited[i][0] == "x":
                    queue.append(i)
                    self.visited[i][0] = "o"
