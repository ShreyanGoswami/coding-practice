
def reverse(head, k):
    if head is None:
        return None
    s = []
    temp = head
    curr = head
    while curr is not None:
        for i in range(0, k):
            s.append(temp.data)
            temp = temp.next
            if temp is None:
                break
        while len(s) > 0:
            curr.data = s.pop()
            curr = curr.next
            if curr is None:
                break
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print("")

if __name__ == '__main__':
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1