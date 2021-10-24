import constants
import rotationmatrices
import numpy

def earthRotation(coordinates, theta):
    r = rotationmatrices.rz(theta)
    return coordinates.dot(r)

def polarMotion(coordinates):
    r1 = rotationmatrices.rx(-constants.Yp)
    r2 = rotationmatrices.ry(-constants.Xp)
    m = r2.dot(r1)
    return coordinates.dot(m)

def inertialToEarthfixed(coordinates, t):
    return polarMotion(earthRotation(coordinates, constants.OMEGAE * t))