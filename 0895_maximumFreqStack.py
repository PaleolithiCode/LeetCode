'''
Runtime: 360 ms, faster than 62.76% of Python3 online submissions for Maximum Frequency Stack.
Memory Usage: 23 MB, less than 12.69% of Python3 online submissions for Maximum Frequency Stack.
'''
import collections

class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.mostFreq = 0
    
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.mostFreq = max(self.mostFreq, self.freq[val])
        self.stack[self.freq[val]].append(val)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return None
        val = self.stack[self.mostFreq].pop()
        if not self.stack[self.mostFreq]:
            self.mostFreq -= 1
        self.freq[val] -= 1
        return val
    
    
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
freqStack.pop()
freqStack.pop()
freqStack.pop()
freqStack.pop()