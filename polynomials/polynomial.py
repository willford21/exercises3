

from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        coefs = [-c for c in self.coefficients]
        return Polynomial(tuple(coefs))

    def __sub__(self, other_poly):
        if (isinstance(other_poly, Number) or
                isinstance(other_poly, Polynomial)):
            return self + -other_poly
        else:
            return NotImplemented

    def __rsub__(self, other_poly):
        if (isinstance(other_poly, Number) or
                isinstance(other_poly, Polynomial)):
            return other_poly + -self
        else:
            return NotImplemented

    def __mul__(self, other_poly):
        if isinstance(other_poly, Number):
            coefs = [other_poly * c for c in self.coefficients]
            return Polynomial(tuple(coefs))
        elif isinstance(other_poly, Polynomial):
            ans = [0] * (len(self.coefficients)
                         + len(other_poly.coefficients)
                         - 1)
            for p1, c1 in enumerate(self.coefficients):
                for p2, c2 in enumerate(other_poly.coefficients):
                    ans[p1+p2] += c1 * c2
            return Polynomial(tuple(ans))
        else:
            return NotImplemented

    def __rmul__(self, other_poly):
        return self * other_poly

    def __pow__(self, pow):
        if isinstance(pow, int) and pow >= 0:
            if pow == 0:
                return 1
            elif pow == 1:
                return self
            else:
                ans = self
                for i in range(pow-1):
                    ans *= self
                return ans
        else:
            return NotImplemented

    def __call__(self, num):
        if isinstance(num, Number):
            ans = self.coefficients[0]
            for pow, coef in enumerate(self.coefficients[1:]):
                ans += coef * (num ** (pow + 1))
            return ans
        else:
            return NotImplemented

    def dx(self):
        if len(self.coefficients) == 1:
            return Polynomial((0,))
        elif len(self.coefficients):
            coefs = tuple([(i+1)*j for i, j in
                          enumerate(self.coefficients[1:])])
            return Polynomial(coefs)
        else:
            return NotImplemented


def derivative(poly):
    return poly.dx()
