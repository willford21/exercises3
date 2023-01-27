from math import sqrt


class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        x1, y1, x2, y2 = self.centre[0], self.centre[1], point[0], point[1]
        dist = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        if dist <= self.radius:
            return True
        else:
            return False
