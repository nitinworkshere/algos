from algos.trie.TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode() #blanknode

    def get_index(self, t):
        return ord(t)-ord('a')

    def insert(self, key):
        if key is None:
            return
        current_node = self.root
        for char in key:
            index = self.get_index(char)
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(char)

            current_node = current_node.children[index]
        current_node.mark_end_of_word()

    def delete(self, key):
        pass # recursive approach

    def search(self, key, prefix=True):
        if key is None or self.root is None:
            return False
        current_node = self.root
        for char in key:
            index = self.get_index(char)
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        if not current_node.is_end_word and prefix is False:
            return False
        return True


