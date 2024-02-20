class Fraction :
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):
        return self.a / self.b
def trans_to_frac(a):
    return Fraction(a,1)

def add(a,b):
    if type(a) != Fraction:
        a = Fraction(a,1)
    if type(b) != Fraction:
        b = Fraction(b,1)
    return Fraction(a.a + b.a, a.b + b.b)

print(add(54,312))
print(add(Fraction(3,5),22))