class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        out = []
        h = 0
        for name in names:
            out.append([name, heights[h]])
            h+=1
        ret = sorted(out, key= lambda x: x[1])
        ret = ret[::-1]
        sorted_people = [x[0] for x in ret]
        return (sorted_people)