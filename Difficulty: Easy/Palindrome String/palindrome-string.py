#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		# code here
		left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return 0
            left += 1
            right -= 1

        return 1