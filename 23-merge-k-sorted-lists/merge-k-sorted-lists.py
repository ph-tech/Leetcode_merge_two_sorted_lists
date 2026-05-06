import heapq

class Solution:
    def mergeKLists(self, lists):
        
        heap = []
        
        # Add first node of each list to heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy node
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            
            # Get smallest node
            val, i, node = heapq.heappop(heap)
            
            current.next = node
            current = current.next
            
            # Move to next node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next