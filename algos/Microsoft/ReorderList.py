def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head or not head.next: return head

    prev, slow, fast = None, head, head
    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next
    prev.next = None

    prev, cur = None, slow
    while cur:
        cur.next, prev, cur = prev, cur, cur.next

    cur, nxt = head, prev
    while nxt:
        cur.next, cur, nxt = nxt, nxt, cur.next

    return head
