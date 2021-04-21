def has_cycle(head):
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        head = head.next

        if head == fast:
            return True

    return False


