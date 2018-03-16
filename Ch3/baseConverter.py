from pythonds.basic.stack import Stack
def baseConverter(decNo,base):
    digits="0123456789ABCDEF"
    remStack=Stack()
    while decNo>0:
        rem=decNo%base
        remStack.push(rem)
        decNo=decNo//base

    newString = " "
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
    return newString
print(baseConverter(25,16))