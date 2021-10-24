# Packages
import numpy as np

# Modules
import tasks

# load data
GPS07       = np.loadtxt('Data/PG07asc.sec')
GLONASS07   = np.loadtxt('Data/PR07asc.sec')
GALILEO07   = np.loadtxt('Data/PE07asc.sec')
QZSS03      = np.loadtxt('Data/PJ03asc.sec')
Beidou07    = np.loadtxt('Data/PC07asc.sec')
Lageos1     = np.loadtxt('Data/PL52asc.sec')
TEST        = np.loadtxt('Data/TEST.sec')

satellites = {"GPS07": GPS07, "GLONASS07": GLONASS07, "GALILEO07": GALILEO07, "QZSS03": GALILEO07, "Beidou07": Beidou07, "Lageos1": Lageos1}
#satellites = {"Lageos1": Lageos1}
#satellites = {"TEST": TEST}

#tasks.task1(satellites)
#tasks.task2(satellites)
#tasks.task3(satellites)
tasks.task4(satellites)
