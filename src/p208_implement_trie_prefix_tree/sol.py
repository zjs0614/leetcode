class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'flag': 0, 'value': {}}



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node['value']:
                node['value'][char] = {'flag': 0, 'value': {}}
            node = node['value'][char]
        node['flag'] = 1


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node['value']:
                return False
            node = node['value'][char]
        return True if node['flag'] == 1 else False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node['value']:
                return False
            node = node['value'][char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)