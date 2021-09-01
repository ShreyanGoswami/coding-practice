# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return []
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        res = ListNode("start")
        self.mergeList(l1, l2, res)
        return res

    def mergeList(self, l1: ListNode, l2: ListNode, res: ListNode):
        greaterVal, listToChose = self.checkGreater(l1, l2)
        if res.val == "start":
            res.val = greaterVal
        else:
            res.next = ListNode(greaterVal)
            res = res.next

        if listToChose == "first":
            res.next = ListNode(l2.val)
        else:
            res.next = ListNode(l1.val)
        res = res.next

        if l1.next != None and l2.next != None:
            self.mergeList(l1.next, l2.next, res)
        elif l1.next == None and l2.next != None:
            self.appendToList(l2.next, res)
        elif l2.next == None and l1.next != None:
            self.appendToList(l1.next, res)
        else:
            return

    def checkGreater(self, l1: ListNode, l2: ListNode):
        if l1.val < l2.val:
            return (l1.val, "first")
        return (l2.val, "second")

    def appendToList(self, l: ListNode, res: ListNode):
        while l.next != None:
            res.next = ListNode(l.val)
            l = l.next
