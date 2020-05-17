class Node:
    def __init__(self, c):
        self.endOfWord = False
        self.d = {}
    
    def addChild(self, char, child):
        if char not in self.d:
            self.d[char] = child
    
    def setEndOfWord(self):
        self.endOfWord = True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for x in word:
            if x in curr.d:
                curr = curr.d[x]
            else:
                newNode = Node(x)
                curr.addChild(x, newNode)
                curr = newNode
        curr.setEndOfWord()
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for x in word:
            if x not in curr.d:
                return False
            curr = curr.d[x]
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for x in prefix:
            if x not in curr.d:
                return False
            curr = curr.d[x]
        return True

if __name__ == "__main__":
    obj = Trie()
    word = 'apple'
    obj.insert(word)
    obj.insert('cde')
    print(obj.search('app'))
    x = 1
    # param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)