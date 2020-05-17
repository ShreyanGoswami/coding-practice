class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def reverseList(self):
    # Code here
    if self.head is None:
        return None
    if self.head.next is None:
        return self.head
    else:
        nextPtr = self.head.next
        curr = self.head
        curr.next = None
        while nextPtr is not None:
            temp = nextPtr.next
            nextPtr.next = curr
            curr = nextPtr
            nextPtr = temp
        self.head = curr
        return curr


class LinkedList:
    def __init__(self):
        self.head = None
        self.lastNode = None
    
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node
    
    def createList(self, arr, n):
        for x in arr:
            self.insert(x)
        return self.head

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end= " ")
            temp = temp.next
        print()

    reverse_List = reverseList

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = LinkedList()
        head = lis.createList(arr, n)
        lis.reverse_List()
        lis.printList()

main()