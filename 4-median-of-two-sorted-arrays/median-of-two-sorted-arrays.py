class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x = len(nums1)
        y = len(nums2)
        
        low = 0
        high = x
        
        while low <= high:
            
            # Partition positions
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # Left and right values
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            # Correct partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                
                # Odd total length
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                
                # Even total length
                return (max(maxLeftX, maxLeftY) + 
                        min(minRightX, minRightY)) / 2
            
            # Move left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            
            # Move right
            else:
                low = partitionX + 1
        