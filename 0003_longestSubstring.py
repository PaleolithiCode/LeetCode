'''
Runtime: 744 ms, faster than 10.91% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 68.08% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
def lengthOfLongestSubstring(s: str) -> int:
    witness = set()
    char2idx = {}
    maxLength = 0
    idx = 0
    while(idx < len(s)):
        if s[idx] not in witness:
            witness.add(s[idx])
            char2idx[s[idx]] = idx
        else:
            maxLength = len(witness) if len(witness) >= maxLength else maxLength
            witness.clear()
            idx = char2idx[s[idx]]
            char2idx[s[idx]] = idx
        idx += 1
        
    maxLength = len(witness) if len(witness) > maxLength else maxLength
    
    return maxLength