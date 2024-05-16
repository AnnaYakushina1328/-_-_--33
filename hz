import math

class Rational:
  def __init__(self, numerator, denominator):
    g = math.gcd(numerator, denominator)
    self.numerator = numerator // g
    self.denominator = denominator // g

  def gcd(self, a, b):
    return b if b == 0 else self.gcd(b, a % b)

my_rational = Rational(6, 9)
print("Numerator: ", my_rational.numerator)
print("Denominator: ", my_rational.denominator)
