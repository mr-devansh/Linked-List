class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        traverse = self.head
        while traverse:
            count += 1
            traverse = traverse.next
        return count

    def printme(self):
        if self.head == None:
            print("empty list")
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_list(self, listy):
        self.head = None
        for data in listy:
            self.insert_at_end(data)

    def insert_at_start(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_in_between(self, index, data):
        traverse = self.head
        if index == 0:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        count = 0
        while traverse:
            if count == index - 1:
                newnode = Node(data)
                newnode.next = traverse.next
                traverse.next = newnode
                break
            traverse = traverse.next
            count += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        traverse = self.head
        while traverse.next:
            traverse = traverse.next
        traverse.next = Node(data)

    def remove_first(self):
        self.head = self.head.next

    def remove_last(self):
        traverse = self.head
        count = 0
        while traverse:
            if count == self.get_length() - 2:
                traverse.next = None
                break
            traverse = traverse.next
            count += 1


l = LinkedList()
l.insert_list(["banana", "mango", "grapes", "orange"])
l.insert_at_start("a")
l.insert_at_end("z")
l.insert_in_between(2, "apple")
l.remove_first()
l.remove_last()
l.printme()
