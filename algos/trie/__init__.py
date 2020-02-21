from algos.trie.TrieNode import TrieNode
from algos.trie.Trie import Trie

root = Trie()
root.insert('hello')
root.insert('nitin')
root.insert('hell')
print(root.search('hel', False))