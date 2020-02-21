

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

    def ranking(self,fajlovi):
        for fajl in fajlovi.list:
            fajl.rang+=fajl.num         #rang se povecava za broj reci na toj stranici
            for link in self.dict[fajl.html]:
                for fajlLink in fajlovi.list:
                    if link.endswith(fajlLink.html):
                        print(link ," ",fajlLink.html)
                        fajlLink.rang+=(fajl.rang/len(self.dict[fajl.html]))
                    else :
                        print("--- ",link, " ", fajlLink.html)
        #for f in fajlovi:
            #print(f.html, " :", f.num, " rang:", f.rang)
        return fajlovi



