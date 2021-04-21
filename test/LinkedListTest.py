import unittest

from linked_list.util.LinkedList import LinkedList


class TestStringMethods(unittest.TestCase):

    def test_get_list(self):
        linkedList = LinkedList()
        linkedList.addAtHead(20)
        result = linkedList.get_list(linkedList.head)
        self.assertEqual(result, [20])

    def test_add_head(self):
        linkedList = LinkedList()
        linkedList.addAtHead(40)
        linkedList.addAtHead(30)
        linkedList.addAtHead(20)
        result = linkedList.get_list(linkedList.head)
        self.assertEqual(result, [20, 30, 40])

    def test_add_tail(self):
        linkedList = LinkedList()
        linkedList.addAtTail(20)
        linkedList.addAtTail(30)
        linkedList.addAtTail(40)
        result = linkedList.get_list(linkedList.head)
        self.assertEqual(result, [20, 30, 40])

    def test_add_1(self):
        linkedList = LinkedList()
        linkedList.addAtTail(9)
        linkedList.addAtTail(9)
        linkedList.addAtTail(1)
        addOne = linkedList.addOne(linkedList.head)
        result = linkedList.get_list(addOne.head)
        self.assertEqual(result, [0, 0, 2])

    def test_odd_and_even(self):
        linkedList = LinkedList()
        linkedList.addAtTail(0)
        linkedList.addAtTail(1)
        linkedList.addAtTail(2)
        linkedList.addAtTail(3)
        linkedList.addAtTail(4)
        odd_and_even = linkedList.even_and_odd(linkedList.head)
        result = linkedList.get_list(odd_and_even.head)
        self.assertEqual(result, [0, 2, 4, 1, 3])

if __name__ == '__main__':
    unittest.main()
