import stdio
import sys

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

F = 6.674e-11 * ((m1 * m2) / r ** 2)
stdio.writeln(F)
