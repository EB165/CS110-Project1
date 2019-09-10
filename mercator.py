import math
import stdio
import sys

slat = math.sin(math.radians(float(sys.argv[1])))
y = math.log((1.0 + slat) / (1.0 - slat)) / 2.0
stdio.write(str(sys.argv[2]) + ' ' + str(y) + '\n')
