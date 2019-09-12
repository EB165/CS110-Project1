import math
import stdio
import sys

lamb = float(sys.argv[1])
t = float(sys.argv[2])

P = math.exp(-lamb * t)
stdio.writeln(P)