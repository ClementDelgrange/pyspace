from courbe_niveau.triangle_mnt import TriangleMNT
from courbe_niveau.point import Point3D, Point2D


def calcule_courbe_niveau(h0, x1, y1, z1, x2, y2, z2, x3, y3, z3):
    p1 = Point3D(x1, y1, z1)
    p2 = Point3D(x2, y2, z2)
    p3 = Point3D(x3, y3, z3)

    t = TriangleMNT(p1, p2, p3)

    res = t.calcule_segment_niveau(h0)

    if res:
        p_start, p_stop = res
        return (p_start.x, p_stop.x), (p_start.y, p_stop.y)
    else:
        return None, None
