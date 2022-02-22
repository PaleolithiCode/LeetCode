'''
Runtime: 216 ms, faster than 94.99% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 97.89% of Python3 online submissions for Longest Palindromic Substring.
'''
def longestPalindrome(s: str):
    if len(s) == 1 or s[::-1] == s:
        return s
    
    def center_expansion(center, odd=False):
        if odd:
            start = center - 1
            end = center + 1
        else:
            start = center
            end = center + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]
    
    ans = ""
    for idx in range(len(s)):
        odd = center_expansion(idx, True)
        even = center_expansion(idx)
        cur = odd if len(odd) > len(even) else even
        ans = cur if len(cur) > len(ans) else ans
        
    return ans

print("ans :", longestPalindrome("aabadsf"))