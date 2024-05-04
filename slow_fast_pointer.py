def slowFastPointer(self, head: Optional[ListNode]) -> bool:
	# A) Slow and Fast start the same index for finding Cycling Linked List
	slow = fast = head
            # OR
	# B) Fast start at Slow.next for finding Middle of the linked list
	slow, fast = head, head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		# A) Found a Cycle
		if slow == fast:
			return True
		
	return False # A) No cycle
            # OR
	# B) Out of while, we have 2 arrays head
    left_array_head = head
    right_array_head = slow.next
    slow.next = None # Break the link if you need 2 list