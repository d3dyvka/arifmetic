import math
a = int(input())

print("z1 =", round(math.sin(math.pi / 2 + 3 * a) / (1 - math.sin(3 * a - math.pi)), 4),"\n","z2 =", round(math.cos(5 / 4 * math.pi + 3 / 2 * a) / math.sin(5 / 4 * math.pi + 3 / 2 * a), 4))