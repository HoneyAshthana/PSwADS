from pythonds.basic.stack import Stack
def divBy2(decNo):
    remStack = Stack()
    while decNo>0:
        rem=decNo%2
        remStack.push(rem)
        decNo=decNo//2
    bString =" "
    while not remStack.isEmpty():
        bString = bString+str(remStack.pop())
    return bString
print(divBy2(42))
