# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach:
# - We initialize two pointers: `prev` (initially None) to store the previous node, and `cur` (initially `head`) to store the current node.
# - We iterate through the list and reverse the link between each node by setting `cur.next` to `prev`.
# - Then, we move `prev` to `cur` and `cur` to `nxt` (the original next node) in each iteration.
# - Once the list is fully reversed, `prev` will point to the new head of the reversed list, which is returned.
#
# Time Complexity (TC): O(n), where n is the number of nodes in the linked list. We visit each node exactly once.
# Space Complexity (SC): O(1), since we are using a constant amount of extra space (only a few pointers).

class Solution(object):
    def reverseList(self, head):
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
