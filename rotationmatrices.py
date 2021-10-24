import numpy

def rx(a): return numpy.matrix([[1, 0, 0], [0, numpy.cos(a), numpy.sin(a)], [0, -numpy.sin(a), numpy.cos(a)]])

def ry(a): return numpy.matrix([[numpy.cos(a), 0, -numpy.sin(a)], [0, 1, 0], [numpy.sin(a), 0, numpy.cos(a)]])

def rz(a): return numpy.matrix([[numpy.cos(a), numpy.sin(a), 0], [-numpy.sin(a), numpy.cos(a), 0], [0, 0, 1]])