class TrieNode:
    def __init__(self, letter=""):
        self.key = letter
        self.doc = Set()
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode(" ")
        self.dict = {}

    def insert(self, word, doc):
        curr_node = self.root
        for l in word:
            if l not in curr_node.children:
                curr_node.children[l] = TrieNode(l)
                curr_node = curr_node.children[l]
            else:
                curr_node = curr_node.children[l]
        curr_node.is_end_of_word = True

        curr_node.doc.add(doc)

        self.dict.update({word: doc})

    def ispis(self):
        for (key, value) in self.dict.items():
            print(key, "::", value)

    def does_word_exist(self, word, pf):
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]

        return curr_node.doc
