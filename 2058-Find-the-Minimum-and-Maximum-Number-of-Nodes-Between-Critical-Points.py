# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        cur = head
        nxt = head.next
        critical_idxs = []
        idx = 0
        minDis = float("inf")

        if not head.next.next:
            return [-1, -1]
        while cur:
            if cur and prev and nxt :
                if (cur.val < prev.val and cur.val < nxt.val) or (cur.val >prev.val and cur.val > nxt.val):
                    critical_idxs.append(idx)
                if len(critical_idxs) >= 2:
                    minDis = min(minDis, critical_idxs[-1] - critical_idxs[-2])
            prev = cur
            cur = nxt
            nxt = nxt.next
            if not nxt:
                break
            idx += 1
        if len(critical_idxs) < 2:
            return [-1, -1]
        maxDis = critical_idxs[-1] - critical_idxs[0]

        return [minDis, maxDis]