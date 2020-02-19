
class TrieNode:
    def __init__(self, letter=""):
        self.key = letter
        self.files = []
        self.parent = None
        self.children = {}
        self.is_end_of_word = False


class RetrunHtml:
    def __init__(self,html,num):
        self.num=num
        self.html=html

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0


class Trie:
    def __init__(self):
        self.root = TrieNode(" ")
        self.links_to = {}
        self.links_from = {}

    def is_empty(self):
        return self.root is None

    def depth(self, x):
        if x.is_root():
            return 0
        else:
            return 1 + self.depth(x.parent)

    def height(self, x):
        if x.is_leaf():
            return 0
        else:
            return 1 + max(self.height(c) for c in x.children)

    def insert(self, word, file):
        word = word.lower()
        curr_node = self.root
        for l in word:
            if l not in curr_node.children:
                curr_node.children[l] = TrieNode(l)
                curr_node.children[l].parent = curr_node
                curr_node = curr_node.children[l]
            else:
                curr_node = curr_node.children[l]
        curr_node.is_end_of_word = True


        if file not in curr_node.files:
            curr_node.files.append(file)

        if file not in self.links_to:
            self.links_to[file] = []
            self.links_from[file] = []

    def ispis(self):
        pass

    def does_word_exist(self, word):
        word = word.lower() # postavljanje svih slova na lower case
        if word == "":
            return True
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.files

    def add_links(self, links, file, directory):
        for link in links:
            self.links_to[file].append(link)
            parts = link.split("\\")
            link_to = parts[-1]
            if link_to not in self.links_from:
                self.links_from[link_to] = []
            self.links_from[link_to].append(directory + "\\" + file)
