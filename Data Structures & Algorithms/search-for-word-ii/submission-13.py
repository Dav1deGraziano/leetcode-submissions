class Trie:
    
    def __init__(self,val=0):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word: str):
        dct = self
        for ch in word:
            if ch not in dct.children:
                dct.children[ch] = Trie()
            dct = dct.children[ch]
        dct.is_end = True
    
    def delete_word(self, word: str):
        node = self
        stack = []

        for ch in word:
            stack.append((node, ch))
            node = node.children[ch]

        node.is_end = False

        for parent, ch in reversed(stack):
            child = parent.children[ch]
            if child.children or child.is_end:
                break
            del parent.children[ch]


                
        
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def word_exists(i: int, j: int, node: Optional[Trie], visited: List[List[int]], prefix: str) -> List[str]:
            
            if node.is_end:
                res = [prefix]
                node.is_end = False
            else:
                res = []
            
            if not node.children:
                return res

            if i+1<=m-1 and [i+1,j] not in visited and board[i+1][j] in node.children:
                visited.append([i+1,j])
                res.extend(word_exists(i+1,j,node.children[board[i+1][j]],visited,prefix+board[i+1][j]))
                visited.pop(-1)

            if i-1>=0 and [i-1,j] not in visited and board[i-1][j] in node.children:
                visited.append([i-1,j])
                res.extend(word_exists(i-1,j,node.children[board[i-1][j]],visited,prefix+board[i-1][j]))
                visited.pop(-1)
                
            if j+1<=n-1 and [i,j+1] not in visited and board[i][j+1] in node.children:
                visited.append([i,j+1])
                res.extend(word_exists(i,j+1,node.children[board[i][j+1]],visited,prefix+board[i][j+1]))
                visited.pop(-1)
                
            if j-1>=0 and [i,j-1] not in visited and board[i][j-1] in node.children:
                visited.append([i,j-1])
                res.extend(word_exists(i,j-1,node.children[board[i][j-1]],visited,prefix+board[i][j-1]))
                visited.pop(-1)
            
            return res

        dictionary = Trie()
        for word in words:
            dictionary.add_word(word)

        m,n = len(board),len(board[0])

        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in dictionary.children:
                    res.extend(word_exists(i,j,dictionary.children[board[i][j]],[[i,j]],board[i][j]))
        
        return res

        

            