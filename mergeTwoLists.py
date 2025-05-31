# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1, list2
                
        if curr1 == None or curr2 == None:
            if curr1 == None:
                return curr2
            else:
                return curr1 
        if curr1.val <= curr2.val :
            head = curr1 
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next



        res = head
        while curr1 or curr2:
            if curr1 == None or curr2 == None : 
                if curr1 == None:
                    res.next = curr2
                else:
                    res.next = curr1
                break
            if curr1.val <= curr2.val :
                res.next = curr1
                curr1 = curr1.next
            else: 
                res.next = curr2
                curr2 = curr2.next
            res = res.next
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

    list1 = create_linked_list([])
    list2 = create_linked_list([1, 3, 5])

    merged_list = solution.mergeTwoLists(list1, list2)

    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)

    print_linked_list(merged_list)  # Output the result

                