class Point2D(object):
    """
    Point2D du plan.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
          return "Point2D ({}, {})".format(self.x, self.y)


class Point3D(Point2D):
    """
    Point3D de l'espace.
    """
    def __init__(self, x, y, z):
        Point2D.__init__(self, x, y)
        self.z = z

    def __str__(self):
        return "Point3D ({}, {}, {})".format(self.x, self.y, self.z)