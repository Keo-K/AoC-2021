import numpy as np
import re
from scipy.ndimage import label

with open("09-01.txt") as f:
    data = f.read()

lava_map = np.fromiter(map(int, re.findall(r"\d", data)), dtype=int).reshape(100, 100)

border_map = np.pad(lava_map, 1, mode="constant", constant_values=9)

mask = (
    (lava_map < border_map[2:, 1:-1])
    & (lava_map < border_map[:-2, 1:-1])
    & (lava_map < border_map[1:-1, 2:])
    & (lava_map < border_map[1:-1, :-2])
)


print((lava_map[mask] + 1).sum())

# libararies are a very nice thing, lol
# regex is copy and pasted because i suck at it
