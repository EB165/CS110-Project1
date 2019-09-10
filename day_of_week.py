import stdio
import sys

month = int(sys.argv[1])
day = int(sys.argv[2])
year = int(sys.argv[3])
y = year - (14 - month) / 12
x = y + y / 4 - y / 100 + y / 400
m = month + 12 * ((14 - month) / 12) - 2
stdio.write(str(int((day + x + 31 * m / 12) % 7)) + '\n')
