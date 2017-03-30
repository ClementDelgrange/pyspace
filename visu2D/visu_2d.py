import matplotlib.pyplot as plt
import matplotlib.cm as cm


def affiche_mnt(mnt):
    fig, ax = plt.subplots()

    # Image
    im = ax.imshow(mnt, interpolation='nearest', cmap=cm.afmhot, alpha=1.0)
    ax.set_title("MNT")

    # Barre de couleur (légende)
    cbar = fig.colorbar(im, ticks=[-10, 10, 100])
    cbar.set_ticklabels(["0", "10", "100"])
    cbar.set_label("Altitude")

    plt.show()


if __name__ == '__main__':
    from Perlin_9P import generate_mnt
    t0 = [[10, 10], [10, 10]]
    mnt = generate_mnt(t0, 2, 6)
    affiche_mnt(mnt)


