import sys

from numba import jit
import numpy as np
import scipy


@jit(nopython=True)
def do_it(xmax, ymax, zmax, pmax):
    crd = np.empty((pmax, 3))
    cut = 1.5

    cutsq = cut*cut

    cnt = 0
    totneighs = 0

    for i in range(xmax):
        for j in range(ymax):
            for k in range(zmax):
                cnt += 1
                crd[cnt, 0] = 1.0 * (i + 1)
                crd[cnt, 1] = 1.0 * (j + 1)
                crd[cnt, 2] = 1.0 * (k + 1)

    numneigh = {}
    for i in range(1, pmax + 1):
        numneigh[i] = 0
        for j in range(1, pmax + 1):
            if j == i:
                continue
            dx = crd[j, 0] - crd[i, 0]
            dy = crd[j, 1] - crd[i, 1]
            dz = crd[j, 2] - crd[i, 2]
            rsq = dx * dx + dy * dy + dz * dz
            if rsq <= cutsq:
                numneigh[i] += 1
        totneighs += numneigh[i]
    return totneighs

xmax, ymax, zmax = [int(x) for x in sys.argv[1:]]
pmax = xmax * ymax * zmax
totneighs = do_it(xmax, ymax, zmax, pmax)

print(f"The number of first neighbors is {totneighs}")
print(f"The dimensions of the box are {xmax}, {ymax}, {zmax}")
print(f"The total number of points is {pmax}")
