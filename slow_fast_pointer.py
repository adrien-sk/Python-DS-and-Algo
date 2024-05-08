def slowFastPointer(self, head: Optional[ListNode]) -> bool:
	slow = fast = head
	# If you need to find Left mid-point of an Even list instead of right, start Fast pointer at head.next
	# slow, fast = head, head.next

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		# Found a Cycle
		if slow == fast:
			return True
		
	return slow # Slow is middle right of the list (or left if Fast started at head.next)

    # Break the link if you need 2 list (require fast started at head.next)
	# slow.next = None 