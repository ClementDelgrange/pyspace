import matplotlib.pyplot as plt
import matplotlib.cm as cm
from courbe_niveau.utilitaire import calcule_courbe_niveau


def affiche_mnt(mnt):
    """
    Affichage d'un MNT dans matplotlib.

    Une échelle de couleur gist_heat est utilisée pour représenter les
    altitudes (http://matplotlib.org/users/colormaps.html).

    :param mnt: tableau contenant les altitudes
    """
    fig, ax = plt.subplots()

    # Image
    im = ax.imshow(mnt, interpolation='nearest', cmap=cm.gist_heat, alpha=1.0)
    ax.set_title("MNT")

    # Barre de couleur (légende)
    cbar = fig.colorbar(im, ticks=[-10, 10, 100])
    cbar.set_ticklabels(["0", "10", "100"])
    cbar.set_label("Altitude")

    plt.show()


def affiche_mnt_avec_courbes(mnt, *args):
    """
    Affichage d'un MNT dans matplotlib en y figurant des courbes de niveau.

    Une échelle de couleur gist_heat est utilisée pour représenter les
    altitudes (http://matplotlib.org/users/colormaps.html).
    Les courbes de niveau sont représentées en bleu.

    :param mnt: tableau contenant les altitudes
    :param args: ensemble des altitudes à faire figurer
    """
    fig, ax = plt.subplots()

    # Image
    im = ax.imshow(mnt, interpolation='nearest', cmap=cm.gist_heat, alpha=1.0)
    ax.set_title("MNT")

    # Courbes de niveau
    for h in sorted(args):
        affiche_courbe_niveau(mnt, h, ax, '-b')

    # Barre de couleur (légende)
    cbar = fig.colorbar(im, ticks=[-10, 10, 100])
    cbar.set_ticklabels(["10", "10", "100"])
    cbar.set_label("Altitude")

    plt.show()


def affiche_courbe_niveau(mnt, h, ax, color):
    """
    Calcul et affichage d'une courbe de niveau dans un graphique matplotlib.

    :param mnt: tableau contenant les altitudes
    :param h: altitude de la courbe de niveau
    :param ax: graphique matplotlib contenant le mnt
    :param color: code couleur de la courbe de niveau
    """
    n = len(mnt)
    m = len(mnt[0])
    for i in range(n-1):
        for j in range(m-1):
            xx, yy = calcule_courbe_niveau(h,
                                           i, j, mnt[i][j],
                                           i+1, j, mnt[i+1][j],
                                           i, j+1, mnt[i][j+1])
            if xx and yy:
                ax.plot(xx, yy, color)

            xx, yy = calcule_courbe_niveau(h,
                                           i+1, j+1, mnt[i+1][j+1],
                                           i, j+1, mnt[i][j+1],
                                           i+1, j, mnt[i+1][j])
            if xx and yy:
                ax.plot(xx, yy, color)


if __name__ == '__main__':
    from Perlin_9P import generate_mnt
    t0 = [[10, 10], [10, 10]]
    mnt = generate_mnt(t0, 2, 5)
    affiche_mnt_avec_courbes(mnt, 9, 10, 11)


