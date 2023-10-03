class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head1 = ListNode(2)
head2 = ListNode(3)
head3 = ListNode(4)
head4 = ListNode(5)
head5 = ListNode(6)

head.next = head1
head1.next = head2
head2.next = head3
head3.next = head4
head4.next = head5


def print_list(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next

def reverseList(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next
    return prev

reverse_list = reverseList(head)
print_list(reverse_list)
