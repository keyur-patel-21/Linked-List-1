# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach:
# - This solution uses Floyd's Cycle Detection Algorithm (Tortoise and Hare Algorithm).
# - We use two pointers, `slow` and `fast`. `slow` moves one step at a time, while `fast` moves two steps at a time.
# - If there is a cycle, `slow` and `fast` will eventually meet inside the cycle. If not, `fast` will reach the end (null).
# - Once a cycle is detected, we reset `fast` to `head` and move both `slow` and `fast` one step at a time. The point where they meet is the start of the cycle.
#
# Time Complexity (TC): O(n), where n is the number of nodes in the list. We traverse the list at most twice.
# Space Complexity (SC): O(1), as we are using only a few pointers and no extra space.

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return None

        slow, fast = head, head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                flag = True
                break

        if not flag:
            return None

        fast = head    
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  
