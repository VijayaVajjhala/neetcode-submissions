class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordNode()
            cur = cur.children[c]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        
        def dfs(root,i):
            if i == len(word):
                return root.endOfWord

            c = word[i]
            if c == '.':
                for child in root.children.values():
                    if dfs(child,i+1):
                        return True
                return False

            else:
                if c not in root.children:
                    return False
                return dfs(root.children[c],i+1)


        if not word:
            return False

        root = self.root
        return dfs(root,0)


        
  

        
