#generator
import random


randarr = [0, 0, 0, 0, 0]
h, w = int(input()), int(input())
with open('map.txt', 'w') as f:
    for y in range(h):
        a = ''
        for x in range(w):
            if ((y == 0) or (y == h - 1)) or ((x == 0) or (x == w - 1)):
                a += '1'
            else:
                a += str(random.choice(randarr))
            a += ' '
        f.write(a + '\n')