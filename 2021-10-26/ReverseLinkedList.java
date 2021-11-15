public ListNode reverseList(ListNode head) {
    ListNode curr = null;
    ListNode temp = head;
    ListNode prev = null;
    while(temp != null){
        prev = curr;
        curr = temp;
        temp = curr.next;
        curr.next = prev;
    }
    return curr; 
}
