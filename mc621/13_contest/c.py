# triangle intersection implementation from https://stackoverflow.com/questions/1585459/whats-the-most-efficient-way-to-detect-triangle-triangle-intersections
# https://rosettacode.org/wiki/Determine_if_two_triangles_overlap
import numpy as np


def CheckTriWinding(tri, allowReversed):
    trisq = np.ones((3, 3))
    trisq[:, 0:2] = np.array(tri)
    detTri = np.linalg.det(trisq)
    if detTri < 0.0:
        if allowReversed:
            a = trisq[2, :].copy()
            trisq[2, :] = trisq[1, :]
            trisq[1, :] = a
    return trisq


def tri_intersect2(t1, t2, eps=0.0, allowReversed=False, onBoundary=True):
    # Trangles must be expressed anti-clockwise
    t1s = CheckTriWinding(t1, allowReversed)
    t2s = CheckTriWinding(t2, allowReversed)

    if onBoundary:
        # Points on the boundary are considered as colliding
        def chkEdge(x): return np.linalg.det(x) < eps
    else:
        # Points on the boundary are not considered as colliding
        def chkEdge(x): return np.linalg.det(x) <= eps

    # For edge E of trangle 1,
    for i in range(3):
        edge = np.roll(t1s, i, axis=0)[:2, :]

        # Check all points of trangle 2 lay on the external side of the edge E. If
        # they do, the triangles do not collide.
        if (chkEdge(np.vstack((edge, t2s[0]))) and
                chkEdge(np.vstack((edge, t2s[1]))) and
                chkEdge(np.vstack((edge, t2s[2])))):
            return False

    # For edge E of trangle 2,
    for i in range(3):
        edge = np.roll(t2s, i, axis=0)[:2, :]

        # Check all points of trangle 1 lay on the external side of the edge E. If
        # they do, the triangles do not collide.
        if (chkEdge(np.vstack((edge, t1s[0]))) and
                chkEdge(np.vstack((edge, t1s[1]))) and
                chkEdge(np.vstack((edge, t1s[2])))):
            return False

    # The triangles collide
    return True


def main():

    t = int(input())
    cont = 1
    while (cont <= t):
        a0 = [0]*2
        a1 = [0]*2
        a2 = [0]*2
        b0 = [0]*2
        b1 = [0]*2
        b2 = [0]*2
        lal = input()

        a0[0], a0[1], a1[0], a1[1], a2[0], a2[1] = [
            int(x) for x in input().split()]
        b0[0], b0[1], b1[0], b1[1], b2[0], b2[1] = [
            int(x) for x in input().split()]
        t1 = [a0, a1, a2]
        t2 = [b0, b1, b2]

        if tri_intersect2(t1, t2, onBoundary=False):
            print(f"pair {cont}: yes")
        else:
            print(f"pair {cont}: no")

        cont += 1


main()
