from parserr import Parser
from graph import Graph
import  os

if __name__ == "__main__":



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

