'''
Runtime: 178 ms, faster than 84.08% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.6 MB, less than 89.43% of Python3 online submissions for Implement Trie (Prefix Tree).
'''
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str):
        cur = self.root
        for token in word:
            if not token in cur:
                cur[token] = {}
            cur = cur[token]
        cur["*"] = None

    def search(self, word: str) -> bool:
        cur = self.root
        for token in word:
            if token in cur:
                cur = cur[token]
            else:
                return False
        if "*" in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for token in prefix:
            if token in cur:
                cur = cur[token]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)