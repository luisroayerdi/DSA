# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        #two pointers (iterative solution)

        prev = None
        current = head

        while current:
            nxt = current.next # prevent loosing link when reversing
            current.next = prev
            prev = current
            current = nxt
        return prev
        