from parserr import Parser
from trie import Trie
from graph import Graph
import os

if __name__ == "__main__":

    putanja = "C:\\Users\\Korisnik DT\\Desktop\\test-skup"
    pf = []
    tr = Trie()
    parser = Parser()

    for(directory_path, directory_names, file_names) in os.walk(putanja):
        for filename in file_names:
            if filename.endswith('.html'):
                pf = parser.parse(directory_path + '\\' + filename)
                for word in pf[1]:
                    tr.insert(word, filename)
                tr.addLinks(pf[0], filename, directory_path)



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

