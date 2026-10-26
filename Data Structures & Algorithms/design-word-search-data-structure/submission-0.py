class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False
        

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:

        current = [self] 

        for ch in word:
            
            next_level = []

            if ch == ".":
                for node in current:
                    for child in node.children.values():
                        next_level.append(child)
            else:
                for node in current:
                    if ch in node.children:
                        next_level.append(node.children[ch])

            if not next_level:
                return False

            current = next_level

        return any(node.is_end for node in current)



