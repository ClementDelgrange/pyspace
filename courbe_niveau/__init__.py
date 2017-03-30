
if __name__ == '__main__':
    # from Perlin_9P import generate_mnt
    # t0 = [[10, 10], [10, 10]]
    # mnt = generate_mnt(t0, 5, 10)

    mnt = [[1 for i in range(10000)] for j in range(1000)]

    from time import time
    t0 = time()
    for x, ligne in enumerate(mnt):
        for y, altitude in enumerate(ligne):
            altitude += 1
    t1 = time()
    print(t1-t0)

    mnt = [[1 for i in range(10000)] for j in range(1000)]

    t0 = time()
    for y in range(len(mnt) - 1):
        for x in range(len(mnt[y])):
            mnt[y][x] += 1
    t1 = time()
    print(t1-t0)
