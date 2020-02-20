from parserr import Parser
from trie import Trie
from graph import Graph
import os

if __name__ == "__main__":

    putanja = "C:\\Users\\Korisnik DT\\Desktop\\test-skup"
    pf = []
    tr = Trie()
    parser = Parser()

    for(directory_path, directory_names, file_names) in os.walk(putanja): # krecemo se kroz sve direktorije i poddirektorije
        for filename in file_names:
            if filename.endswith('.html'):
                pf = parser.parse(directory_path + '\\' + filename) # putanja do fajla koji se parsira se do
                for word in pf[1]:
                    tr.insert(word, filename)
                tr.add_links(pf[0], filename, directory_path)


    logicki = ("AND", "OR", "NOT")
    ulaz = input("Unesite rec")
    while ulaz != "kraj":
        upit = ulaz.split(" ")
        rezulatati = {}  # rijecnik sa kljucevima koji su rijeci pretrage a vrijednosti su fajlovi u kojima se nalaze

        for rec in upit:  # za svaku rijec u upitu
            if rec in logicki:  # ako je logicki operator ispisu je se poruka i preskace se
                print("Postoji operator " + rec)
                continue
            fajlovi = tr.does_word_exist(rec.lower())  # ako rijec postoji i nije logicki operator vraca sve fajlove u kojima se nalazi
            if fajlovi:
                print("Postoji")
                rezulatati[rec] = fajlovi  # stavljam fajlove u rijecnik
            elif not fajlovi:
                print("Ne postoji")
            print("-------------")

        unique_files = []
        for key, rezultat in rezulatati.items():
            for rez in rezultat:
                if rez not in unique_files:
                    unique_files.append(rez)

        print(len(unique_files))
        ulaz = input("unesite rec")

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


    print("------------------------")
    #t.ispis()
    #g.printVertexs()

