from linked_list.util.Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def getSize(self):
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def add_node(self, n):
        n.setNext(self.root)
        self.root = n
        self.size += 1

    def remove(self, d):
        node = self.root
        prev_node = None

        while node is not None:
            if node.getData() == d:
                if prev_node is not None:
                    prev_node.setNext(node.getNext())
                else:
                    self.root = node.getNext()
                self.size -= 1
                return True  # data removed
            else:
                prev_node = node
                node = node.getNext()
        return False  # data not found

    def find(self, d):
        node = self.root
        while node is not None:
            if node.getData() == d:
                return d
            elif node.getNext() is None:
                return False
            else:
                node = node.getNext()

    def printList(self):
        if self.root is None:
            return
        node = self.root
        print(node.toString(), end=" ")
        while node.hasNext():
            node = node.getNext()
            print(node.toString(), end=" ")

        print()

    def sort(self):
        if self.size > 1:
            list = []
            current = self.root
            list.append(self.root)
            while current.hasNext():
                current = current.getNext()
                list.append(current)
            list = sorted(list, key=lambda node: node.getData(), reverse=True)
            newll = LinkedList()
            for node in list:
                newll.add_node(node)
            return newll
        return self

    def get(self, index: int) -> int:
        index_count = 0
        current_node = self.head
        while current_node:
            if index_count == index:
                return current_node.val
            else:
                current_node = current_node.next
            index_count += 1  # used to check when at index
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current_node = self.head
        if self.head is not None:  # if there is a head
            while current_node.next is not None:
                current_node = current_node.next
            new_node = Node(val)
            # current_node is last element .next is None it make .next the new node
            current_node.next = new_node
        else:  # if there isn't a head node does same as addAtHead
            new_node = Node(val, self.head)
            self.head = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        elif index < 0:  # cant add at a - index
            return None
        elif index == self.size:
            self.addAtTail(val)  # we can just add it to the tail (append onto end)

        # main part
        else:  # This happens when the index is less than the size and none above have triggered
            if index == 0:
                self.addAtHead(val)  # just add it to the head
            else:
                loop_num = 0
                current_node = self.head
                while loop_num != index - 1:  # -1 to insert before else it would insert after
                    current_node = current_node.next
                    loop_num += 1
                new_node = Node(val, n=current_node.next)
                current_node.next = new_node
        self.size += 1  # + 1 to size because we added 1 node

    def deleteAtIndex(self, index: int) -> None:
        prev = None  # previous node
        index_count = 0  # used to count what index we are on
        current_node = self.head  # start at the head of the list
        while current_node is not None:
            if index_count == index:
                if prev is not None:  # This means its on the not on head node
                    prev.next_node = current_node.next
                else:  # this means it is on the head node
                    self.head = current_node.next
                self.size -= 1  # change size because we deleted something
            else:
                # Travel through list
                prev = current_node  # makes the previous node the current_node
                current_node = current_node.next  # then the current node the node after the current node
            index_count += 1  # adds one to the index count

        return None

    def get_list(self, head):
        node = head
        result = []
        while node:
            print(node.val)
            result.append(node.val)
            node = node.next
        return result

    def addOne(self, head):
        carry = 0
        current = head
        linkedList = LinkedList()
        carry += 1  # add one
        while current:
            carry = current.val + carry
            value = carry % 10
            linkedList.addAtTail(value)
            carry = carry // 10
            current = current.next

        return linkedList

    def even_and_odd(self, head):
        even = LinkedList()
        odd = LinkedList()

        current = head
        index = 0
        while current:
            if index % 2 == 0:
                even.addAtTail(current.val)
            else:
                odd.addAtTail(current.val)
            current = current.next
            index += 1

        even.addNodeAtTail(odd)
        self.get_list(even.head)
        return even

    def addNodeAtTail(self, linkedlist) -> None:
        node = linkedlist.head
        current_node = self.head
        if self.head is not None:  # if there is a head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        else:  # if there isn't a head node does same as addAtHead
            self.head = node
        self.size += linkedlist.size


# llist = LinkedList(["a", "b", "c", "d", "e"])
linkedList = LinkedList()
linkedList.addAtTail("a")
linkedList.addAtTail("b")
linkedList.addAtTail("c")
# print(linkedList)
for node in linkedList:
    print(node)
