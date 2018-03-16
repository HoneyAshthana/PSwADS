#In many ways it would be better if all fractions were maintained in lowest terms right from the start.
#Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately.
#Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self, top, bottom):
        # 5.if not integer raise an exception
        if not isinstance(top, int):
            valErr = ValueError("{} is not integer".format(top))
            raise valErr
        if not isinstance(bottom, int):
            valErr = ValueError("{} is not integer".format(bottom))
            raise valErr

        #6.changes to positive no
        if top < 0 and bottom < 0:
            top = abs(top)
            bottom = abs(bottom)
        elif bottom < 0:
            top = -top
            bottom = abs(bottom)

        #self.num = top
        #self.den = bottom
        common = gcd(abs(top), abs(bottom))
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    #2.to implement addition in fractions
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    #3.to implement addition in fractions
    def __sub__(self, otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    #3.to implement multiplication in fractions
    def __mul__(self, otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den*otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

    #3.to implement true division in fractions
    def __truediv__(self, otherfraction):
        newnum = self.num*otherfraction.den
        newdem = self.den*otherfraction.num
        common = gcd(newnum,newdem)
        return Fraction(newnum//common,newdem//common)

    #4.to implement relational operators
    def __gt__(self, otherfraction):
        first_num = self.num * otherfraction.den
        second_num = self.den * otherfraction.num
        return first_num > second_num

    def __ge__(self, otherfraction):
        first_num = self.num * otherfraction.den
        second_num = self.den * otherfraction.num
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num <= second_num

    def __ne__(self, otherfraction):
        first_num = self.num * otherfraction.den
        second_num = self.den * otherfraction.num
        return first_num != second_num

    #7.__radd__method
    def __radd__(self, otherfraction):
        if otherfraction == 0:
            return self
        else:
            return self.__add__(otherfraction)

    #8.iadd method
    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        print(self.__add__(other))

    #9.repr method
    def __repr__(self):
        print( '%s(%r)' % (self.__class__, self.__str__()))


x = Fraction(-1,-2)
y = Fraction(2,4)

#print(x+y)
print(x.__add__(y))
print(x-y)
print(x*y)
print(x.__truediv__(y))
print(x.__ge__(y))
print(x.__ne__(y))
print(x.__gt__(y))
print(x.__lt__(y))
print(x.__le__(y))
print(x.__radd__(y))

