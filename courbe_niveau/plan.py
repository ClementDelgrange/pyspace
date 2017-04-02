import numpy as np


class Plan(object):
    """
    Plan de l'espace.

    Un plan est déterminé par une équation z = ax + by + c
    """
    def __init__(self, p1, p2, p3):
        """
        Un plan est construit à partir de 3 points 3D.

        :type p1: Point3D
        :type p2: Point3D
        :type p3: Point3D
        """
        a = np.matrix([[p1.x, p1.y, 1], [p2.x, p2.y, 1], [p3.x, p3.y, 1]])
        b = np.array([p1.z, p2.z, p3.z])
        x = np.linalg.solve(a, b)
        self.a = x[0]
        self.b = x[1]
        self.c = x[2]

    def calcule_courbe_niveau(self, h0):
        """
        Retourne l'équation de la droite d'altitude h0 du plan.

        La droite est données par l'équation h0 = ax + by + c.
        La méthode calcule les paramètres u et v tels que y = ux + v (ie. la
        pente et l'origine de la droite).

        :param h0: altitude de la courbe de niveau
        :return: pente et origine de la droite d'altitude h0 du plan
        """
        # Cas particuliers
        if self.b == 0:
            # L'altitude du plan ne dépend pas de y
            if self.a == 0:
                # Plan d'altitude fixe
                return False, False
            return False, (h0 - self.c) / self.a

        # Cas général
        u = -self.a / self.b
        v = (h0 - self.c) / self.b
        return u, v

