from pythonds.basic.stack import Stack
def infixToPostfix(infixexp):
    pres ={"*":3,"/":3,"+":2,"-":2,"(":1}
    openStack=Stack()
    postfixList=[]
    tokenList=infixexp.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "012346789":
            postfixList.append(token)
        elif token =="(":
            openStack.push(token)
        elif token ==")":
            topToken = openStack.pop()
            while token!="(":
                postfixList.append(topToken)
                topToken=openStack.pop()
        else:
            while (not openStack.isEmpty())and (pres[openStack.peek()] >=pres[token]):
                postfixList.append(openStack.pop())
            openStack.push(token)
    while not openStack.isEmpty():
        postfixList.append(openStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
