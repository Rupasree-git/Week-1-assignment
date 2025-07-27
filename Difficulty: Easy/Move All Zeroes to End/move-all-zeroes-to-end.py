#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	count = 0  # Position to place the next non-zero element
        for i in range(len(arr)):
            if arr[i] != 0:
                # Swap non-zero element to the position of count
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
        return arr