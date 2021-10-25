import math
import numpy
import itertools
from numpy.core.fromnumeric import transpose

import constants
import plotter
import transformations


# Functions
def readInertial(coordinates):
    x = []
    y = []
    z = []
    for coordinate in coordinates:
        x.append(coordinate[0])
        y.append(coordinate[1])
        z.append(coordinate[2])
    return x, y, z

def inertialToEarthFixed(coordinates, satellite):
    t = 0

    x = []
    y = []
    z = []

    for coordinate in coordinates:
        coordinatesEarthBound = transformations.inertialToEarthfixed(coordinate, t)
        
        x.append(coordinatesEarthBound[0,0])
        y.append(coordinatesEarthBound[0,1])
        z.append(coordinatesEarthBound[0,2])

        if satellite == "Lageos1": t += 120
        else: t += 300
    #print(satellite, t)
    return x, y, z

def toLatLong(coordinates, satellite):
    latitude = []
    longitude = []
    
    x, y, z = inertialToEarthFixed(coordinates, satellite)

    for (x, y, z) in itertools.zip_longest(x, y, z):
        if x > 0 : #1st / fourth quadrant
            lat = math.atan(z / math.sqrt(x**2 + y**2)) * (180 / math.pi)
            long = math.atan(y / x) * (180 / math.pi)
        elif y > 0: #2nd quadrant
            lat = math.atan(z / math.sqrt(x**2 + y**2)) * (180 / math.pi)
            long = (math.atan(y / x) + math.pi) * (180 / math.pi)
        else:  #3rd quadrant
            lat = (math.atan(z / math.sqrt(x**2 + y**2))) * (180 / math.pi)
            long = (math.atan(y / x) - math.pi) * (180 / math.pi)
        #print(x,y, long, math.atan(y/x))

        latitude.append(lat)
        longitude.append(long)
    return latitude, longitude

def intertialToTopo(coordinates, satellite):
    t = 0

    n = []
    e = []
    u = []

    xW = constants.R * math.cos(constants.WETTZELL["latitude"]) * math.cos(constants.WETTZELL["longitude"])
    yW = constants.R * math.cos(constants.WETTZELL["latitude"]) * math.sin(constants.WETTZELL["longitude"])
    zW = constants.R * math.sin(constants.WETTZELL["latitude"])

    p0 = numpy.matrix([xW, yW, zW])
    print(constants.WETTZELL["latitude"], constants.WETTZELL["longitude"], xW, yW, zW, p0)

    r2 = transformations.rotationmatrices.ry((math.pi / 2) + constants.WETTZELL["latitude"])
    r3 = transformations.rotationmatrices.rz(-constants.WETTZELL["longitude"])

    r2test = transformations.rotationmatrices.ry(math.pi / 2 - math.pi / 4)
    r3test = transformations.rotationmatrices.rz(math.pi / 2)

    mirror = numpy.matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    #print(p0)
    #newCoords = numpy.empty((0,3))

    for coordinate in coordinates:
        
        c1 = transformations.inertialToEarthfixed(coordinate, t)
        a = c1 - p0
        d = (c1 - p0).transpose()
        #c2 = transpose(numpy.linalg.multi_dot([mirror, r2, r3, transpose(c1 - p0)]))
        c2 = mirror @ r2 @ r3 @ d
        #c2.transpose()

        n.append(c2[0,0])
        e.append(c2[1,0])
        u.append(c2[2,0] - constants.WETTZELL["h"] / 1000) #up is h (meters) / 1000 of Wettzell smaller (Wettzell is "closer" to satellite)

        if satellite == "Lageos1": t += 120
        elif satellite == "TEST": t += 2400
        else: t += 300
    return n, e, u

# Task 1
def task1(satellites):
    for satellite in satellites:
        x, y, z = readInertial(satellites[satellite])
        plotter.plot3Dtrajectory(satellite,  "Inertial 24h", x, y, z)

# Task 2
def task2(satellites):
    for satellite in satellites:
        x, y, z = inertialToEarthFixed(satellites[satellite], satellite)
        plotter.plot3Dtrajectory(satellite, "Erdfest 24h", x, y, z)

# Task 3
def task3(satellites):
    for satellite in satellites:
        lat, long = toLatLong(satellites[satellite], satellite)
        
        minLat = round(min(lat), 3)
        maxLat = round(max(lat), 3)
        
        plotter.plotGroundTrack(satellite, "Bodenspur 24h", lat, long, minLat, maxLat)

# Task 4
def task4(satellites):
    for satellite in satellites:
        n, e, u = intertialToTopo(satellites[satellite], satellite)
        #print(satellite, coordinates)
        
        az = []
        el = []
        
        #n = n0.to_list()
        #e = e0.to_list()
        #u = u0.to_list()

        for (ni, ei, ui) in itertools.zip_longest(n, e, u):
            elevation = 0
            azimuth = 0
            if ui < 0: # below horizon
                continue 

            if ei < 0 and ni > 0: #1st quadrant
                azimuth = (-math.atan(ei / ni) * 180 / math.pi)
            elif ni < 0: #2nd / 3rd quadrant
                azimuth = ((-math.atan(ei / ni) + math.pi) * 180 / math.pi)
            else: #4th quadrant
                azimuth = ((-math.atan(ei / ni) + 2 * math.pi) * 180 / math.pi)

            elevation = (math.pi / 2 - math.atan(math.sqrt((ni ** 2) + (ei ** 2)) / ui)) * 180 / math.pi

            el.append(elevation)
            az.append(azimuth * math.pi / 180)
            print(ni, ei, ui, elevation, azimuth)
             
        plotter.polarPlot(satellite, "Topozentrisch 24h von Wetzell", az, el)