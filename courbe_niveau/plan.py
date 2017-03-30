import numpy as np


class Plan(object):
    """
    Un plan est déterminé par une équation z = ax + by + c
    """
    def __init__(self, p1, p2, p3):
        a = np.array([p1.x, p1.y, 1], [p2.x, p2.y, 1], [p3.x, p3.y, 1])
        b = np.array([p1.z, p2.z, p3.z])
        x = np.linalg.solve(a, b)
        self.a = x[0]
        self.b = x[1]
        self.c = x[2]

    def calcule_courbe_niveau(self, h0):
        """
        Retourne la droite d'altitude h0 du plan.

        La droite est données par l'équation h0 = ax + by + c.
        La méthode calcule les paramètres u et v tels que y = ux + v

        :param h0: altitude de la courbe de niveau
        :return:
        """
        u = -self.a / self.b
        v = (h0 - self.c) / self.b
        return u, v

