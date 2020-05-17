# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # This code provides a strategy with which we can use extra space to 
    # make operations on linked list easier by first converting it to a
    # python list, doing the operations on it and then converting it back
    # to a linked list. This has a lot of disadvantages but it works in this scenario
    # Time complexity O(nlogn) and space complexity O(n)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        listVals = []

        self.addToList(listVals, l1)
        
        self.addToList(listVals, l2)
        
        listVals.sort()

        print(listVals)
        
        res = ListNode(listVals[0])

        # It is interesting to note that if the code of the function was 
        # pasted here it will always move res to the end of the list
        self.constructList(listVals, res)
        return res
    
    def constructList(self, listVals, res):
        for i in range(1, len(listVals)):
            res.next = ListNode(listVals[i])
            res = res.next
        
    
    def addToList(self, l, listNode):
        while True:
            l.append(listNode.val)
            if listNode.next != None:
                listNode = listNode.next
            else:
                break



