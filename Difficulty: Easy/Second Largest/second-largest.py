class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        largest = second_largest = -1
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and num > second_largest:
                second_largest = num
        return second_largest if second_largest != -1 else -1