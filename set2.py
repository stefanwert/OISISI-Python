import random

class Set(object):

    def __init__(self,capacity=30):

        self._data=capacity*[None]
        self._capacity=capacity
        self._size=0
        self.prime=109345121
        self._a=1+random.random.randrange(self.prime-1)
        self._b=random.randrange(self.prime)

    def __len__(self):
            return  self._size

    def _hash(self,x):
        hashed_value = (hash(x) * self._a + self._b) % self.prime
        compressed = hashed_value % self._capacity
        return compressed

    def _resize(self,capacity):
        old_data = list(self.items())
        self._data = capacity * [None]
        self._size = 0

