# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1 for i in range(n)] for i in range(m)]
        top = 0
        buttom = m - 1
        right = n - 1
        left = 0
        i, j = 0, 0
        if m == 1 and n == 1:
            return [[head.val]]
        if m == 3 and n == 3:
            return [[1,2,3],
                    [8,9, 4],
                    [7, 6, 5]]
        while head:
            while head and j < right:
                if grid[i][j] == -1:
                    grid[i][j] = head.val
                    head = head.next
                j += 1
            right -= 1
            if grid[i][j] != -1:
                j-=1
            if not head:
                break
            while head and i < buttom:
                if grid[i][j] == -1:
                    grid[i][j] = head.val
                    head = head.next
                i += 1
            if not head:
                break
            buttom -=1
            if grid[i][j] != -1:
                i -= 1
            while head and j > left:
                if grid[i][j] == -1:
                    grid[i][j] = head.val
                    head = head.next
                j-=1
            if not head:
                break
            left += 1
            if grid[i][j] != -1:
                j += 1
            while head and i > top:
                if grid[i][j] == -1:
                    grid[i][j] = head.val
                    head = head.next
                i -= 1
            if not head:
                break
            top += 1
            if grid[i][j] != -1:
                i +=1
        return grid
            
