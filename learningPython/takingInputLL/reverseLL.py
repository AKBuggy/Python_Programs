# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next


if __name__ == '__main__':
    nums = list(map(int, input().split()))

    lis = LinkedList()
    for n in nums:
        lis.insert(n)

    sol = Solution()
    newHead = sol.reverseList(lis.head)
    printList(newHead)
