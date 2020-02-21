

class Set:
    def __init__(self):
        self.list=[]
        self.max=0

    def addElement(self,el):
        if el not in self.list:
            self.list.append(el)
            self.max+=1

    def union(self,s):
        for el in s.list:
            self.addElement(el)

    def printSet(self):
        for el in self.list:
            print(el)

    def diffrence(self,s):
        for el in self.list:
            if el not in s.list:
                list.remove(el)

    def intersection(self,s):
        ret=Set()
        for el in s:
            if el in self.list:
                ret.addElement(el)
        return ret

    def complement(self,s):
        for el in self.list:
            s.remove(el)
        self.list=s

    def remove(self,el):    #da li treba vidi???
        self.list.remove(el)

    def __iter__(self):
         self.n = 0
         return self

    def __next__(self):
        if self.n>= self.max:     #moze i self.n>= len(self.list)
            raise StopIteration
        current=self.n
        self.n+=1
        return  self.list[current]