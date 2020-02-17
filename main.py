from parserr import Parser
from graph import Graph
from set import Set
from trie import Trie
import  os
import time

if __name__ == "__main__":

    putanja = 'C:\\Users\\Petrovic\\Desktop\\stefan\\test-skup'



    #tr = Trie()
    #pf = parseF(putanja)
    #for w in pf:
        #for i in w.words:
            #tr.insert(i, w.putanja)
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

    #rec=input("unesite rec")
    #fajl=input("unesite naziv fajla")
    print("------------------------")
    #t.ispis()
    g.printVertexs()

