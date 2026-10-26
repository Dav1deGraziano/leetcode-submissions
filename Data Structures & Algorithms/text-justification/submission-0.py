class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def justify_line(line: List[str], crt_len: int) -> List[str]:

            n_words = len(line)
            if n_words == 1:
                return line[0] + " "*(maxWidth-crt_len)
            
            n_spaces = int((maxWidth-crt_len)//(n_words-1))
            n_only_left = (maxWidth-crt_len) % (n_words-1)
            res = line[0]

            for word in line[1:]:
                if n_only_left == 0:
                    res += " "*n_spaces + word
                else:
                    res += " "*(n_spaces+1) + word
                    n_only_left -= 1

            return res


        res = []
        crt_line = [words[0]]
        len_crt_line = len(words[0])

        for word in words[1:]:
            crt_word_len = len(word)
            if len_crt_line + 1 + crt_word_len <= maxWidth:
                len_crt_line += 1 + crt_word_len
                crt_line.append(" "+word)
            else:
                res.append(justify_line(crt_line,len_crt_line))
                crt_line = [word]
                len_crt_line = len(word)
        
        dummy = ""
        for word in crt_line:
            dummy += word
        res.append(dummy+" "*(maxWidth-len_crt_line))
        return res
