class Node(object):
    def __init__(self, value):
        self.value = value
        self.Next = None

def reverseLinkedList(head):
    previous = None
    NextNode = None

    current = head

    while current:
        NextNode = current.Next
        current.Next = previous
        previous = current
        current = NextNode
    return previous

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.Next = b
    b.Next = c
    #print(a.Next.value)
    #print(b.Next.value)
    print(reverseLinkedList(a))
    #print(c.value)
