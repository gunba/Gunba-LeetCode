class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        while current:
            if current.next == -1:
                return True

            next_node = current.next
            current.next = -1
            current = next_node

        return False