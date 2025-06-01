# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = slow = head
        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next
       
        prev = None
        curr = slow 

        while curr :
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        p1, p2 = head, prev 
        
        while p1 and p2 and p1.next and p2.next : 
            temp = p1.next
            temp2 = p2.next
            p1.next = p2
            p1.next.next = temp
            p1 = p1.next.next
            p2 = temp2
        return head  # Return the modified list head
            


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

    list1 = create_linked_list([ 0,1,2,3,4,5,6])
    list2 = create_linked_list([1, 3, 5])

    merged_list = solution.reorderList(list1)

    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)

    print_linked_list(merged_list)  # Output the result

        

