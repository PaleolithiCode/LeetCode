'''
Runtime: 69 ms, faster than 67.63% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14 MB, less than 93.54% of Python3 online submissions for Zigzag Conversion.
'''
def zigzagConversion(s: str, numRows: int) -> str:
    if len(s) == 1 or numRows == 1 or len(s) <= numRows:
        return s
    final = ["" for _ in range(numRows)]
    batch = numRows * 2 - 2
    repeat = int(len(s) / batch)
    remain = len(s) % batch
    iter = 0
    for iter in range(repeat):
        for i in range(batch):
            idx = iter * batch + i
            if i < numRows:
                final[i] += s[idx]
            else:
                final[len(final) - (i - numRows + 1) - 1] += s[idx]
    if repeat != 0: iter += 1
    else: iter = 0
    for i in range(remain):
        idx = iter * batch + i
        if i < numRows:
            final[i] += s[idx]
        else:
            final[len(final) - (i - numRows + 1) - 1] += s[idx]

    return "".join(final)

# print(zigzagConversion("PAYPALISHIRING", 3))
print(zigzagConversion("ABC", 2))