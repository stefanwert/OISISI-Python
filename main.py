from parserr import Parser
from graph import Graph
import  os

if __name__ == "__main__":

    putanja = input('C:\\Users\\Korisnik DT\\Desktop\\test-skup')

    pf = []
    tr = Trie()
    pf = parseF(putanja)
    for w in pf:
        for i in w.words:
            tr.insert(i, w.putanja)

    list_of_files={}
    g=Graph()
    for(dirpath,dirnames,filenames)in os.walk('C:\\Users\\Petrovic\\Desktop\\stefan\\test-skup'):
        #print(dirpath,dirnames)
        for filename in filenames:
           #print(filename)
            p = Parser()
            if filename.endswith('.html'):
                p.parse(dirpath+'\\'+filename)
                g.addVertex(dirpath+'\\'+filename)
                for lin in p.links:
                    g.addEdge(dirpath+'\\'+filename,lin)


    g.printVertexs()

