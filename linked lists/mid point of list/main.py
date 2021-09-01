class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for x in arr:
        lis.insert(x)
    return lis.head


def findMid(head):
    slowPtr = head
    if head.next is not None:
        fastPtr = head
        while fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
            if fastPtr.next is not None:
                fastPtr = fastPtr.next
    return slowPtr


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)


main()
