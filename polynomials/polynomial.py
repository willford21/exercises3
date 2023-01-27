from numbers import Number


class Polynomial():

    def __init__(self, coefs):
        self.coefficients = coefs

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f'{coefs[1]}x')
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]
        return ' + '.join(reversed(terms)) or '0'

    def __eq__(self, other_poly):
        return (isinstance(other_poly, Polynomial) and
                self.coefficients == other_poly.coefficients)

    def __add__(self, other_poly):
        if isinstance(other_poly, Number):
            return Polynomial((self.coefficients[0] + other_poly,)
                              + self.coefficients[1:])
        elif isinstance(other_poly, Polynomial):
            common = min(self.degree(), other_poly.degree()) + 1
            coefs = tuple(a + b for a, b in
                          zip(self.coefficients[:common],
                              other_poly.coefficients[:common]))
            coefs += (self.coefficients[common:]
                      + other_poly.coefficients[common:])
            return Polynomial(coefs)
        else:
            return NotImplemented

    def __radd__(self, other_poly):
        return self + other_poly

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
            coefs = [other_poly * coef for coef in self.coefficients]
            return Polynomial(tuple(coefs))
        elif isinstance(other_poly, Polynomial):
            ans = [0] * (len(self.coefficients)
                         + len(other_poly.coefficients)
                         - 1)
            for p1, c1 in enumerate(self.coefficients):
                for p2, c2 in enumerate(other_poly.coefficients):
                    ans[p1+p2] += c1*c2
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

    def __call__(self, val):
        if isinstance(val, Number):
            ans = self.coefficients[0]
            for pow, coef in enumerate(self.coefficients[1:]):
                ans += coef * (val ** (pow+1))
            return ans
        else:
            return NotImplemented

    def degree(self):
        return len(self.coefficients) - 1

    def dx(self):
        if len(self.coefficients) == 1:
            return 0
        elif len(self.coefficients) > 0:
            coefs = tuple([(i+1)*j for i, j in
                          enumerate(self.coefficients[1:])])
            return Polynomial(coefs)
        else:
            return NotImplemented


def derivative(poly):
    return poly.dx()


p1 = Polynomial((1, 2, 3))
p2 = Polynomial((1, 2, 3))
p3 = Polynomial((5, 4, 6))
print(1-p2)
