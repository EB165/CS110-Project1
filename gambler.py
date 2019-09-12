import stdio
import sys
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])
q = 1.0 - p
pq = p / q

P1 = (1 - pq ** n2) / (1 - pq ** (n1 + n2))
P2 = (1 - (1 / pq) ** n1) / (1 - (1 / pq) ** (n1 + n2))
stdio.writeln(str(P1) + ' ' + str(P2))
