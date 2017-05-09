from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm



if __name__ == '__main__':
    from Perlin_9P import generate_mnt
    t0 = [[10, 10], [10, 10]]
    mnt = generate_mnt(t0, 2, 5)
    
    X, Y, Z = [], [], []
    for i in range(len(mnt)):
        for j in range(len(mnt[i])):
            X.append(i)
            Y.append(j)
            Z.append(mnt[i][j])
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(X, Y, Z, cmap='afmhot', linewidth=0)
    ax.set_zlim(0, 20)
    plt.show()
