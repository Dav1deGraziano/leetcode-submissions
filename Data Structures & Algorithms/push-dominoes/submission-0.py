class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dominoes = list(dominoes)
        nxt = dict()
        n = len(dominoes)

        for i in range(n):
            if dominoes[i] != '.':
                continue
            left = i > 0 and dominoes[i-1] == 'R'
            right = i < n-1 and dominoes[i+1] == 'L'
            if left and right:
                continue                      
            elif left:
                nxt[i] = 'R'
            elif right:
                nxt[i] = 'L'

        while nxt:

            crt = nxt
            nxt = dict()

            for i, move in crt.items():       
                dominoes[i] = move

            for i, move in crt.items():       
                j = i + 1 if move == 'R' else i - 1
                if j < 0 or j >= n or dominoes[j] != '.':
                    continue
                if j in nxt and nxt[j] != move:
                    del nxt[j]                
                else:
                    nxt[j] = move

        return ''.join(dominoes)