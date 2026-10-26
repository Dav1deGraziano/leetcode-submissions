from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            signature = [0] * 26

            for c in s:
                signature[ord(c) - ord('a')] += 1

            groups[tuple(signature)].append(s)

        return list(groups.values())