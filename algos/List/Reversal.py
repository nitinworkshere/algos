from algos.List.LinkedList import LinkedList

def reverse_linked_list(ll):
    curr = ll.head
    prev = None
    while curr:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    ll.head = curr
