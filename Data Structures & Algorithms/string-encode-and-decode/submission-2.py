class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()
        for string in strs:
            num = len(string)
            res += str(num)+"#"+string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        len_s = len(s)-1
        while i<=len_s:
            j = 0
            num = str()
            while s[i+j]!="#":
                num += s[i+j]
                j += 1
            num = int(num)
            i += j+1
            res.append(s[i:i+num])
            i = i+num
        return res

