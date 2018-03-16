def reverseList(alist):
    if len(alist) == 1:
        return alist #base case
    else:
        return reverseList(alist[1:]) + [alist[0]]

print reverseList([1,2,3,4])