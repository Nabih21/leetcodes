# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(0, lists[0])

        for i in range(len(lists)):
            if i != 0 : 
                node = curr1 = dummy
                curr2 = lists[i]
                while curr1 and curr2 :
                    if curr1.val < curr2.val: 
                        node.next = curr1
                        curr1 = curr1.next
                    else : 
                        node.next = curr2
                        curr2 = curr2.next
                    node = node.next
        return dummy.next

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

    list1 = create_linked_list([1,2,4])
    list2 = create_linked_list([1, 3, 5])
    list3 = create_linked_list([3, 6])
    n = 2
    listAll = [list1, list2, list3]

    merged_list = solution.mergeKLists(listAll)

    def print_linked_list(head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        print(values)

    print_linked_list(merged_list)  # Output the result

                

