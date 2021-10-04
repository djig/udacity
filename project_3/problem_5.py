import collections
class TrieNode(object):
    def __init__(self):
        self.is_end = False
        self.children = collections.defaultdict(TrieNode)
    def suffixes(self, suffix = '', res =[]):
        if self.is_end == True:
            if len(suffix)> 0:
                res.append(suffix)
        for c in self.children:
            self.children[c].suffixes( suffix + c, res)
        return res

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_end = True

    def find (self, suffix):
        curr = self.root
        for ch in suffix:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        
        return curr

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

test_cases = [
    'a',
    'an',
    'f',
    'fun',
    'tr',
    'not'
]
for test in test_cases:
    prefixNode = MyTrie.find(test)
    print('Suffix for ' + test)
    if prefixNode:
        res = prefixNode.suffixes('', [])
        print(res)
    else:
        print('No Results')
