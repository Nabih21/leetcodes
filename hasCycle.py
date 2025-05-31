# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        count = 1

        while fast : 
            fast = fast.next 
            if count % 2 == 0 : 
                slow = slow.next 
            if fast == slow : 
                return True
            count += 1
            
        return False
    

if __name__ == "__main__":
    solution = Solution()
    def create_linked_list(values, index):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        nodes = [head]  # Keep track of all nodes to create a cycle later
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
            nodes.append(current)
        if index != -1 and 0 <= index < len(nodes):
            current.next = nodes[index]  # Create a cycle
        return head
    index = 1
    head = create_linked_list([1, 2, 3, 4], index)

    has_cycle = solution.hasCycle(head)
    print("Has cycle:", has_cycle)  # Output the result
