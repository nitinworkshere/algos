def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    curA, curB = headA, headB
    countA, countB = 0, 0
    while curA:
        curA = curA.next
        countA += 1
    while curB:
        curB = curB.next
        countB += 1

    curA, curB = headA, headB
    diff = abs(countA - countB)
    if countA > countB:
        for _ in range(diff):
            curA = curA.next
    else:
        for _ in range(diff):
            curB = curB.next
    while curA and curB:
        if curA == curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None


def find_intersection(headA, headB):
    l1, l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1