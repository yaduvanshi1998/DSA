# Valid Palindrome

'''Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.'''

s = "Was it a car or a cat I saw?"

def isalphanum(s):
        return (ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9'))


def valid_plaindrome(s, isalphanum):
    left = 0
    right = len(s)-1
    while left < right:
        while left < right and not isalphanum(s[left]):
            left += 1
        while right > left and not isalphanum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(valid_plaindrome(s, isalphanum))

# Time Complexity: O(n) 
# Space Complexity: O(1) 



