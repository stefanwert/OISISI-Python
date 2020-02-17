
from set import Set

class TrieNode:
    def __init__(self, letter=""):
        self.key = letter
        self.doc ={} #Set()
        self.children = {}
        self.is_end_of_word = False
        #self.numberOfRepetition=0

class RetrunHtml:
    def __init__(self,html,num):
        self.num=num
        self.html=html



class Trie:
    def __init__(self):
        self.root = TrieNode(" ")
        self.dict = {}

    def insert(self, word, doc):
        word.lower()
        curr_node = self.root
        for l in word:
            if l not in curr_node.children:
                curr_node.children[l] = TrieNode(l)
                curr_node = curr_node.children[l]
            else:
                curr_node = curr_node.children[l]
        curr_node.is_end_of_word = True
       # curr_node.numberOfRepetition+=1

        #curr_node.doc.addElement(doc)  #kad ide set sporije je
        if doc in curr_node.doc.keys():
            curr_node.doc[doc]+=1
        else:
            curr_node.doc[doc]=1
        self.dict.update({word: doc})

    def ispis(self):
        for (key, value) in self.dict.items():
            print(key, "::", value)

    def does_word_exist(self, word):
        word.lower()
        print(word)
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        setRet=Set()
        for i in curr_node.doc:
            if curr_node.is_end_of_word:
                setRet.addElement(RetrunHtml(i,curr_node.doc[i]))
        return setRet
