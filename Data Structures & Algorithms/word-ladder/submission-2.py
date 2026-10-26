class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def compare_two_words(s1: str, s2: str) -> bool:
            counter = 0
            for k in range(n):
                if s1[k]!=s2[k]:
                    counter += 1
                if counter >= 2:
                    return False
            return True
        
        def find_path(crt_idx: int) -> int:

            queue = [(crt_idx, 1)]
            visited = {crt_idx}
            head = 0

            while head < len(queue):
                idx, dist = queue[head]

                if idx == end:
                    return dist
                
                head += 1

                for nei in links[idx]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, dist + 1))

            return 0 

        
        if endWord not in wordList:
            return 0
        else:
            end = wordList.index(endWord)
        n_words = len(wordList)
        if beginWord not in wordList:
            wordList.append(beginWord)
            begin = n_words
            n_words += 1
        else:
            begin = wordList.index(beginWord)
        
        n = len(beginWord)
        links = [[] for i in range(n_words)]
        visited = {}

        for i in range(n_words):
            word1 = wordList[i]
            for j in range(n_words):
                if i==j:
                    continue
                if compare_two_words(word1,wordList[j]):
                    links[i].append(j)
        
        return find_path(begin)
        


