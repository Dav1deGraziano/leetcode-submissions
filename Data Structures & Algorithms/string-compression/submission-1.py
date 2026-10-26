class Solution:
    def compress(self, chars: List[str]) -> int:

        if not chars[1:]:
            return 1

        prev = chars[0]
        crt_len = 1
        i = 0

        for ch in chars[1:]:
            if ch == prev:
                crt_len += 1
            elif crt_len == 1:
                chars[i] = prev
                i += 1
                prev = ch
            else:
                dummy = prev + str(crt_len)
                len_dummy = len(dummy)
                for j in range(i,i+len_dummy):
                    chars[j] = dummy[j-i]
                i += len_dummy
                prev = ch
                crt_len = 1
        
        if crt_len == 1:
            chars[i] = prev
            i += 1
        else:
            dummy = prev + str(crt_len)
            len_dummy = len(dummy)
            for j in range(i,i+len_dummy):
                chars[j] = dummy[j-i]
            i += len_dummy

        return i
        
        