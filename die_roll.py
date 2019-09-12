import random
import stdio
import sys

n = int(sys.argv[1])

roll = random.randint(1, n) + random.randint(1, n)
stdio.writeln(roll)
