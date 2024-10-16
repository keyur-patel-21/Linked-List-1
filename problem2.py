# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# - We use two pointers: `l` (left) and `r` (right). Both start at a dummy node that points to the head of the list.
# - First, we move the `r` pointer `n` steps ahead, creating a gap of `n` nodes between `l` and `r`.
# - Then, we move both `l` and `r` forward until `r` reaches the end of the list.
# - At this point, `l` will be just before the node that needs to be removed. We update `l.next` to skip the node that needs to be removed.
# - We return `dummy.next`, which is the head of the updated list.
#
# Time Complexity (TC): O(n), where n is the length of the linked list. 
# Space Complexity (SC): O(1), since we are using a constant amount of extra space (just pointers).

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        l, r = dummy, head

        while n > 0:
            r = r.next
            n -= 1

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next
