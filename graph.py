
class Graph :

    def __init__(self):
        self.dict={}

    def addVertex(self, v):
        self.dict[v]=[]

    def addEdge(self,fromV,toV):
        if fromV not in self.dict.keys():
            self.addVertex(fromV)
        if toV not in self.dict.keys():
            self.addVertex(toV)
        self.dict[fromV].append(toV)

    def getEdge(self,fromV):
        return self.dict[fromV]

    def printVertexs(self):
        for i in self.dict.keys():
            print("Vertex:",i)
            print("Veze:")
            #if len(self.dict[i])==0:
                #print("---",i)     #provera za vertekse bez linkova
            for j in self.dict[i]:
                print(j)


