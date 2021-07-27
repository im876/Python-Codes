#program to find the hypotenuse of a triangle using command line arguments

import math
adj = float(input().strip())
opp = float(input().strip())

#a² + b² = c²

hyp = math.sqrt((adj*adj)+(opp*opp))
print(hyp)
