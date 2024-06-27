class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        branch_one = edges[0]
        branch_two = edges[1]
        if branch_one[0] in branch_two:
            return branch_one[0]
        return branch_one[1]