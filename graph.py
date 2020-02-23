

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

    def ranking(self, returnHtmlSet,set):
        a=0
        b=0
        for struc in returnHtmlSet.dict.keys():
            struc.rang+=struc.num         #rang se povecava za broj reci na toj stranici
            for link in self.dict[struc.html]:
                #for fajlLink in returnHtmlSet.dict.keys():
                    #if link.endswith(fajlLink.html):
                        #print(link ," ",fajlLink.html)
                        #fajlLink.rang+=(struc.num+10000/len(self.dict[struc.html]))
                    #else :
                        #print("--- ",link, " ", fajlLink.html)
                if link in set.dict:
                    #print(b, "bbb")
                    b += 1
                    for fajlLink in returnHtmlSet.dict.keys():
                        if link.endswith(fajlLink.html):
                            fajlLink.rang+=(struc.num+10000/len(self.dict[struc.html]))
                            break
                else:
                    #print(a,"aaa")
                    a+=1

        #for f in fajlovi:
            #print(f.html, " :", f.num, " rang:", f.rang)
        return returnHtmlSet



