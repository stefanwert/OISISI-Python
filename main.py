from parserr import Parser
from trie import Trie
from graph import Graph
import re
import os
from set import Set
from trie import RetrunHtml

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x.brReci>pivot.brReci:
            left.append(x)
        elif x.brReci<pivot.brReci:
            right.append(x)
        else:
            if x.rang>pivot.rang:
                left.append(x)
            elif x.rang==pivot.rang:
                middle.append(x)
            else:
                right.append(x)
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":

    flagForPutanja=1
    while flagForPutanja:
        putanja=input("Unesite putanju(ne sme se zavrisavati sa html ili tackom): ")
        if not putanja.endswith("html") and not putanja.endswith("."):
            flagForPutanja=0
    tr = Trie()
    g = Graph()
    parser = Parser()

    for(directory_path, directory_names, file_names) in os.walk(putanja): # krecemo se kroz sve direktorije i poddirektorije
        for filename in file_names:
            if filename.endswith('.html'): # parsiramo samo html fajlove iz liste fajlova
                parser.parse(directory_path + '\\' + filename)
                for word in parser.words:
                    tr.insert(word, directory_path + '\\' + filename) # svaka rijec parsirana iz fajlova se ubacuje u stablo
                #ovo je za graf ispod
                g.addVertex(directory_path + '\\' + filename)
                for lin in parser.links:
                    g.addEdge(directory_path + '\\' + filename, lin)

    logicki = ("AND", "OR", "NOT")
    #print("Za prekid programa unesite rec kraj.")
    #ulaz = input("Unesite kriterijum pretrage: ")
    ulaz=""
    while ulaz != "kraj":
        firstTimeNot=0
        print("------------------------------------")
        print("Za prekid programa unesite rec kraj.")
        ulaz = input("Unesite kriterijum pretrage: ")
        if ulaz=="kraj":
            break
        upit = re.sub('\s+', " ", ulaz).strip().split(" ") # \s+ znaci ako naidje na jedan ili vise razmaka zamjeni ih sa jednim
        index_log_op = -1
        rezulatati = {}  # rijecnik sa kljucevima koji su rijeci pretrage a vrijednosti su fajlovi u kojima se nalaze
        flag=0 # flag za los upit
        returnHtmlSet = Set()
        for index,rec in enumerate(upit):  # za svaku rijec u upitu
            if rec == "":
                continue
            if rec in logicki:
                if rec=="NOT":
                    firstTimeNot=1
                if index==0:
                    print("Upit nije validan jer ne moze poceti sa logickim operatorom.\n")
                    flag=2
                    break
                flag=flag+1
                if flag > 1:
                    print("Upit nije validan jer moze da postoji samo jedan logicki operator.\n")
                    break
                index_log_op = index  # indeks logickog operatora u upitu
                continue
            if  firstTimeNot:
                fajlovi = tr.does_word_exist(rec.lower(), Set())
                firstTimeNot=0
            else:
                fajlovi = tr.does_word_exist(rec.lower(),returnHtmlSet)  # ako rijec postoji i nije logicki operator vraca sve fajlove u kojima se nalazi
            if fajlovi:
                rezulatati[rec] = fajlovi  # stavljam fajlove u rijecnik
            else:
                print("Ne postoji rec: " + rec)
                flag = 2  # ako riijec ne postoji postavljamo flag na 2 da ne bi izracunavao rezultate
        if flag > 1:
            print("Za prekid programa unesite rec kraj.")
            ulaz = input("Unesite kriterijum pretrage: ")
            continue

        search_results = Set()
        if index_log_op != -1:  # ako je nasao logicki operator
            search_results.union(rezulatati[upit[index_log_op - 1]])  # dodaje set rezultata prve rijeci
            if upit[index_log_op] == "NOT":  # logicki operatori poredani po prednosti izvrsavanja prvo ide NOT pa AND pa OR
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
                       obj2.num+=obj.num
                       obj2.brReci+=1

                if a==0:
                    returnHtmlSet2.addElement(obj)
        returnHtmlSet=returnHtmlSet2

        fajlovi = g.ranking(returnHtmlSet, search_results)  # rangiranje
        l=[]
        for el in fajlovi.dict.keys():
            l.append(el)

        l=quicksort(l)
        if len(l)==0:
            print("zadata pretraga ne daje ni jedno resenje !!!")
            continue
        #paginacija
        iin="a"
        k=0
        while not k:
            print("Unesite koliko stranica zelite da vam se prikaze(broj mora biti manji ili jednak od ukupnog broja stranica:",len(l),")")
            try:
                k = int(input())
            except:
                print("Unesite broj !")
                k=0
            if k> len(l) or k<0:
                k=0
            if len(l)==0:
                k=0
                print("Ne postoji ni jedna html stranica sa zadatim kriterijumom !!!!!!!!!!!!!!!!!!!!!")
                break
        a = 0
        b = a+k
        myFlag=0
        while iin:
            if iin.lower()=="d":
                if b+k>len(l)-1 and b<len(l)-1:
                    a+=k
                    b=len(l)
                elif b+k>len(l)-1:        #provera da ne izadjemo iz opsega liste za desnu granicu
                    myFlag=1
                else:
                    a += k
                    b+=k
            elif iin.lower()=="l":
                if b-a!=k:
                    b=b-(b-a)
                    a-=k
                else:
                    if a-k<0:       #provera da ne izadjemo iz opsega liste za levu granicu
                        myFlag=2
                    else:
                        a-=k
                        b-=k
            if myFlag==1:
                print("Nije moguce dalje kretanje u desno!!!")
                myFlag=0
            elif myFlag==2:
                print("Nije moguce dalje kretanje u levo!!!")
                myFlag = 0
            else:
                for f in l[a:b]:
                    print(f.html, " :", "broj reci kombinovano:",f.num, " rang:", f.rang, "br razlicitih reci:",f.brReci)
            print("od:",a+1," do:",b)
            print("Ukupan broj stranica:", len(l))
            print("\n")
            iin=input("<---l d---> \nZa kretanje u levo unesite l, za kretanje u desno unesite d\nZa sledecu pretragu pritisnite samo enter: ")
            #kraj paginacije




    print("------------------------------------")

