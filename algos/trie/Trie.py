class Node:
    def __init__(self, char=''):
        self.char = char
        self.children = [None]*26
        self.isEndOfWord = False

    def mark_end_of_word(self):
        self.isEndOfWord = True


class Trie:
    def __init__(self):
        self.root = Node()

    def index_of_char(self, ch): #As we are starting with a
        return ord(ch) - ord('a')

    def insert(self, key):
        current = self.root
        for char in key:
            index = self.index_of_char(char)
            if current.children[index] is None:
                current.children[index] = Node(char)
                current = current.children[index]
        current.mark_end_of_word()

    def search(self, key, prefix=True):
        current = self.root
        for char in key:
            index = self.index_of_char(char)
            if not current.children[index]:
                return False
            current = current.children[index]

        if not current.isEndOfWord and not prefix:
            return False
        return True


dictionary = Trie()
dictionary.insert('hello')
print(dictionary.search('he', False))


