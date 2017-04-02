from courbe_niveau.plan import Plan
from courbe_niveau.point import Point2D, Point3D


class TriangleMNT(Plan):
    """
    Triangle constitué de 3 points d'une grille régulière de MNT.
    """
    def __init__(self, p1, p2, p3):
        """
        Par construction, dans le plan (x,y), p1 est le sommet à l'angle droit
        du triangle, p2 est le sommet à l'horizontale de p1 et p3 à la
        verticale de p1.

        :type p1: Point3D
        :type p2: Point3D
        :type p3: Point3D
        """
        if p1.x != p3.x:
            msg = ("p1 et p3 ne sont pas alignés verticalement "
                   "dans le triangle MNT : {} - {}")
            raise ValueError(msg.format(p1, p3))
        if p1.y != p2.y:
            msg = ("p1 et p2 ne sont pas alignés horizontalement "
                   "dans le triangle MNT : {} - {}")
            raise ValueError(msg.format(p1, p2))

        # On appelle le constructeur de la classe mère (équation du plan)
        Plan.__init__(self, p1, p2, p3)

        # On conserve aussi les 3 points constituant le triangle
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calcule_segment_niveau(self, h0):
        """
        Calcul des intersections de la courbe de niveau d'altitude h0 avec les
        bords du triangle.

        Si l'altitude h0 n'intersecte pas le triangle, la fonction retourne
        None.

        :param h0: altitude de la courbe de niveau
        :return:
        """
        # On écarte les cas où le triangle est en dessous ou au dessus de h0
        if h0 < self.zmin or h0 > self.zmax:
            return None
        if h0 == self.zmax and h0 == self.zmin:
            pass

        # Equation de la droite d'altitude h0
        u, v = self.calcule_courbe_niveau(h0)

        # Cas particuliers
        if not u:
            # L'altitude du triangle ne dépend que de x
            pass
        if u == 0:
            # L'altitude du triangle ne dépend que de y
            pass

        # Cas général
        # Intersections avec les droites (p1, p2) et (p1, p3)
        p12_x = (self.p1.y - v) / u
        p12_y = self.p1.y
        p13_y = u*self.p1.x + v
        p13_x = self.p1.x

        x_sorted = sorted([self.p1.x, self.p2.x])
        y_sorted = sorted([self.p1.y, self.p3.y])
        if x_sorted[0] <= p12_x <= x_sorted[1] \
                and y_sorted[0] <= p13_y <= y_sorted[1]:
            # La courbe de niveau intersecte les segments (p1, p2) et (p1, p3)
            return Point2D(p12_x, p12_y), Point2D(p13_x, p13_y)
        else:
            # Calcul de l'intersection avec (p2, p3)
            p23_x = (self.p2.x + self.p2.y - v) / (u + 1)
            p23_y = u * p23_x + v
            if x_sorted[0] <= p12_x <= x_sorted[1]:
                # La courbe de niveau intersecte les segments (p1, p2) et (p2, p3)
                return Point2D(p12_x, p12_y), Point2D(p23_x, p23_y)
            elif y_sorted[0] <= p13_y <= y_sorted[1]:
                # La courbe de niveau intersecte les segments (p1, p3) et (p2, p3)
                return Point2D(p13_x, p13_y), Point2D(p23_x, p23_y)


    @property
    def zmin(self):
        """
        Altitude minimale du triangle
        """
        return min(self.p1.z, self.p2.z, self.p3.z)

    @property
    def zmax(self):
        """
        Altitude maximale du triangle
        """
        return max(self.p1.z, self.p2.z, self.p3.z)
