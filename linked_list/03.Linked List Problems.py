from linked_list.util.Node import Node


def has_cycle(head):
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        head = head.next

        if head == fast:
            return True

    return False


def sortList(head: Node) -> Node:
    # Splitting the list into two parts
    def mergeSort(head):
        if not head or not head.next:
            return head

        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = mergeSort(head)
        right = mergeSort(slow)
        return merge(left, right)

    # Sorting the list
    def merge(left, right):
        head_ref = dummy = Node()
        while left and right:
            if left.val > right.val:
                dummy.next = right
                right = right.next

            else:
                dummy.next = left
                left = left.next

            dummy = dummy.next

        if left:
            dummy.next = left

        if right:
            dummy.next = right

        return head_ref.next

    return mergeSort(head)


def deleteDuplicates(head: Node) -> Node:
    head_ref = head
    if not head:
        return head_ref
    while head.next != None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return head_ref
