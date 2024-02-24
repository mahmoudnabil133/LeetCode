"(miduim level)"
# i solved this linked list problem with 2 solution2
# first (with recursion)
class Solution:
    def removeNodes(self, head):
        head2,_ = self.rm(head)
        return head2

    def rm(self, head):
        if not head:
            return None, 0
        pastNode, pastMax = self.rm(head.next)
        
        if head.val < pastMax:
            return pastNode, pastMax
        else:
            head.next = pastNode
            return head, head.val
# second (with stack)
class Solution:
    def removeNodes(self, head):
        if not head:
            return None
        st = []
        temp = head
        while temp:
            st.append(temp)
            temp = temp.next
        
        past = st.pop()
        maxNode = past.val

        while st:
            curr = st.pop()
            if curr.val < maxNode:
                continue
            else:
                maxNode = curr.val
                curr.next = past
                past = curr
        return past
