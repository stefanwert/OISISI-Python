import random

class Set(object):

    def __init__(self):
        self.dict={}

    def __len__(self):
        return self.dict.keys().__len__()

    def addElement(self, el):
        self.dict[el]=1

    def remove(self,el):
        if el in self.dict:
            self.dict.pop(el)

    def union(self, s):
        for el in s.dict.keys():
            self.addElement(el)

    def intersection(self, s):
        ret={}
        for el in s.dict.keys():
            if el in self.dict.keys():
                ret[el]=1
        self.dict=ret

    def complement(self, s):
        for el in self.dict.keys():
            s.remove(el)
        self.dict=s.dict

    def __add__(self, other):
        for o in other.dict.keys():
            self.addElement(o)
        return self

    def printSet(self):
        print("elemenit su:------")
        for el in self.dict.keys():
            print(el)




