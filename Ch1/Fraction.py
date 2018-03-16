#Implement the simple methods getNum and getDen that will return the numerator and denominator of a fraction.
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return (str(self.num)+ "/" +str(self.den))

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


myfraction = Fraction(6,18)
print (myfraction)

print(myfraction.getNum())
print(myfraction.getDen())

