class TrieNode:

    def __init__(self, char=''):
        self.char = char
        self.children = [None]*26
        self.is_end_word = False

    def mark_end_of_word(self):
        self.is_end_word = True

    def unmark_end_of_word(self):
        self.is_end_word = False