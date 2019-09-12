import stdio
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

stdio.write(str(min(num1, num2, num3)) + ' ')
stdio.write(str(min(max(num1, num2), num3)) + ' ')
stdio.writeln(str(max(num1, num2, num3)))
