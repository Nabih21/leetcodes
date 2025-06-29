# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        dummy = head

        while count <= n and dummy :
            if count == n -1 : 
                dummy.next = dummy.next.next 
                break
            if dummy.next == None: 
                dummy = head
            else :     
                dummy = dummy.next 
            count += 1
        
        
        return head
    

if __name__ == "__main__":
    solution = Solution()
    def create_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    list1 = create_linked_list([1,2,3,4])
    list2 = create_linked_list([1,2])

    merged_list = solution.removeNthFromEnd(list2, 2 )

    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)

    print_linked_list(merged_list)  # Output the result

        