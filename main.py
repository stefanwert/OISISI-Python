from parserr import Parser
from trie import Trie
from graph import Graph
import re
import os
from set2 import Set
from trie import RetrunHtml

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
    #putanja ='C:\\Users\\Petrovic\\Desktop\\stefan\\test-skup'
    #putanja ='C:\\Users\\Korisnik DT\\Desktop\\test-skup'
    tr = Trie()
    g = Graph()
    parser = Parser()

   # for (dirpath, dirnames, filenames) in os.walk('test-skup'):
        #for filename in filenames:
           # p = Parser()
           # if filename.endswith('.html'):
            #    p.parse(dirpath + '\\' + filename)


    for(directory_path, directory_names, file_names) in os.walk(putanja): # krecemo se kroz sve direktorije i poddirektorije
        print(directory_path)
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
        index_log_op = -1
        rezulatati = {}  # rijecnik sa kljucevima koji su rijeci pretrage a vrijednosti su fajlovi u kojima se nalaze
        flag=0 # flag za los upit
        returnHtmlSet = Set()
        for index,rec in enumerate(upit):  # za svaku rijec u upitu
            if rec == "":
                continue
            if rec in logicki:  # ako je logicki operator ispisu je se poruka i preskace se
                flag=flag+1
                if flag > 1:
                    print("Upit nije validan, moze da postoji samo jedan logicki operator.")
                    break
                index_log_op = index  # indeks logickog operatora u upitu
                continue
            fajlovi = tr.does_word_exist(rec.lower(),returnHtmlSet)  # ako rijec postoji i nije logicki operator vraca sve fajlove u kojima se nalazi
            if fajlovi:
                rezulatati[rec] = fajlovi  # stavljam fajlove u rijecnik
            else:
                print("Ne postoji rec: " + rec)
                flag = 2  # ako riijec ne postoji postavljamo flag na 2 da ne bi izracunavao rezultate
        if flag > 1:
            ulaz = input("Unesite kriterijum pretrage: ")
            continue

        search_results = Set()
        if index_log_op != -1:  # ako je nasao logicki operator
            search_results.union(rezulatati[upit[index_log_op - 1]])  # dodaje set rezultata prve rijeci
            if upit[index_log_op] == "NOT":  # logicki operandi poredani po prednosti izvrsavanja prvo ide NOT pa AND pa OR
                search_results.complement(rezulatati[upit[index_log_op + 1]])
            elif upit[index_log_op] == "AND":
                search_results.intersection(rezulatati[upit[index_log_op + 1]])
            else:
                search_results.union(rezulatati[upit[index_log_op + 1]])
            del rezulatati[upit[index_log_op - 1]]
            del rezulatati[upit[index_log_op + 1]]  # brisanje vec dodatih rezultata iz rijecnika rezultata

        for key, rezultat in rezulatati.items():
            search_results.union(rezultat)

        #skracujem returnHtmlSet
        returnHtmlSet2=Set()
        for obj in returnHtmlSet.dict.keys():
            if obj.html in search_results.dict:
                a=0
                for obj2 in returnHtmlSet2.dict.keys():
                   if obj.html == obj2.html:
                       a+=1
                if a==0:
                    returnHtmlSet2.addElement(obj)
        returnHtmlSet=returnHtmlSet2

        fajlovi = g.ranking(returnHtmlSet, search_results)  # rangiranje
        l=[]
        for el in fajlovi.dict.keys():
            l.append(el)

        l=quicksort(l)

        for f in l:
            print(f.html, " :", f.num, " rang:", f.rang)
        print("broj stranica",len(l))
        print("ocekivani broj stranica", len(search_results))
        print("-------------")
        ulaz = input("Unesite kriterijum pretrage: ")

    print("------------------------")
    #t.ispis()
    #g.printVertexs()

