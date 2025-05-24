class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        inc = 0
        for w in words:
            if x in w:
                out.append(inc)
            inc+= 1
        return out