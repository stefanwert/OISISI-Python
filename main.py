from parserr import Parser
from trie import Trie
from graph import Graph
import re
import os
from set2 import Set

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    #left = [x for x in arr if x.rang < pivot]
    #middle = [x for x in arr if x.rang == pivot]
    #right = [x for x in arr if x.rang > pivot]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x.rang>pivot.rang:
          left.append(x)
        elif x.rang==pivot.rang:
           middle.append(x)
        else:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":

    putanja = "test-skup"
    tr = Trie()
    g = Graph()
    parser = Parser()

   # for (dirpath, dirnames, filenames) in os.walk('test-skup'):
        #for filename in filenames:
           # p = Parser()
           # if filename.endswith('.html'):
            #    p.parse(dirpath + '\\' + filename)


    for(directory_path, directory_names, file_names) in os.walk(putanja): # krecemo se kroz sve direktorije i poddirektorije
        for filename in file_names:
            if filename.endswith('.html'): # parsiramo samo html fajlove iz liste fajlova
                parser.parse(directory_path + '\\' + filename)
                for word in parser.words:
                    tr.insert(word, directory_path + '\\' + filename) # svaka rijec parsirana iz fajlova se ubacuje u stablo
                #ovo je za graf ispod
                g.addVertex(directory_path + '\\' + filename)
                for lin in parser.links:
                    print(directory_path + '\\' + filename,"  ", lin)
                    g.addEdge(directory_path + '\\' + filename, lin)


    logicki = ("AND", "OR", "NOT")
    ulaz = input("Unesite kriterijum pretrage: ")
    while ulaz != "kraj":
        upit = re.sub('\s+', " ", ulaz).strip().split(" ") # \s+ znaci ako naidje na jedan ili vise razmaka zamjeni ih sa jednim

        rezulatati = {}  # rijecnik sa kljucevima koji su rijeci pretrage a vrijednosti su fajlovi u kojima se nalaze
        flag=0 # flag za los upit
        for rec in upit:  # za svaku rijec u upitu
            if rec == "":
                continue
            if rec in logicki:  # ako je logicki operator ispisu je se poruka i preskace se
                flag=flag+1
                if flag > 1:
                    print("Upit nije validan, moze da postoji samo jedan logicki operator.")
                    break
                continue
            fajlovi = tr.does_word_exist(rec.lower())  # ako rijec postoji i nije logicki operator vraca sve fajlove u kojima se nalazi
            if not fajlovi:
                print("Ne postoji rec: " + rec)
                flag = 2
        if flag > 1:
            ulaz = input("Unesite kriterijum pretrage: ")
            continue

        fajlovi = g.ranking(fajlovi)  # rangiranje
        l=[]
        for el in fajlovi.dict.keys():
            l.append(el)


        l=quicksort(l)
        for f in l:
            print(f.html, " :", f.num, " rang:", f.rang)
        print("-------------")
        ulaz = input("Unesite kriterijum pretrage: ")




    print("------------------------")
    #t.ispis()
    #g.printVertexs()

