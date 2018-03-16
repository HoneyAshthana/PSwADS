from pythonds.basic.deque import Deque

def checkPalindrome(cString):
    charDeque=Deque()
    for ch in cString:
        charDeque.addRear(ch)
    stillEqual=True
    if charDeque.size()>1:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first!=last:
            stillEqual= False

    return stillEqual

print(checkPalindrome("radaro"))