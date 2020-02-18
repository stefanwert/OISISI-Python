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
                tr.add_links(pf[0], filename, directory_path)

    g=Graph()
    t = Trie()
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
                for word in p.words:
                    t.insert(word.lower(),dirpath+'\\'+filename)
    ulaz=input("unesite rec")
    while ulaz!="kraj":
        b=t.does_word_exist(ulaz.lower())
        if b ==True:
            print("ima")
        elif  b==False:
            print("nema")
        else:
            for ret in b:
                #print(ret)
                print(ret.html," ",ret.num)
        print("-------------")
        ulaz = input("unesite rec")

    print("------------------------")
    #t.ispis()
    #g.printVertexs()

