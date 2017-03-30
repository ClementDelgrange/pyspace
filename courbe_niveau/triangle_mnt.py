from courbe_niveau.plan import Plan


class TriangleMNT(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calcule_plan(self):
        """
        Retourne l'objet Plan pour le triangle
        :return:
        """
        return Plan(self.p1, self.p2, self.p3)

    def calcule_ligne_niveau(self, h0):
        plan = self.calcule_plan()
        droite_h0 = plan.calcule_courbe_niveau(h0)
        # calculer le segment de la droite_ho à l'intérieur du triangle

