def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the total length of the linked list
        node = head
        total_length = 0
        while node:
            total_length += 1
            node = node.next

        # Step 2: Calculate the size of each part and how many parts should be bigger by 1
        part_size = total_length // k
        extra_parts = total_length % k  # number of parts that will have an extra node

        # Step 3: Prepare result array
        result = []
        node = head

        # Step 4: Split the list
        for i in range(k):
            part_head = node
            current_part_size = part_size + (1 if i < extra_parts else 0)

            # Traverse current part size - 1 nodes (stop at last node of the current part)
            for j in range(current_part_size - 1):
                if node:
                    node = node.next

            # If the node is not None, detach it from the rest of the list
            if node:
                next_part_head = node.next
                node.next = None
                node = next_part_head

            result.append(part_head)

        # Step 5: If the list is shorter than k, append None for empty parts
        return result