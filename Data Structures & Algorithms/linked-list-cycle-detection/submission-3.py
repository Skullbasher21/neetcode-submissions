# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        h = head
        t = head
        while not (h.next == None and t == None):
            if h.next == None:
                return False
            h = h.next.next
            t = t.next
            if h == t:
                return True
            if h == None:
                return False
        return False
        