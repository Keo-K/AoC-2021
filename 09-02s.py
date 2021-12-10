import numpy as np
import re
from scipy.ndimage import label

with open("09-01.txt") as f:
    data = f.read()

lava_map = np.fromiter(map(int, re.findall(r"\d", data)), dtype=int).reshape(100, 100)

labels, nbins = label(lava_map != 9)
labels = labels.reshape(-1)


print(
    (np.partition(np.bincount(labels, labels != 0), nbins - 3)[-3:].prod().astype(int))
)

# libararies are a very nice thing, lol
# regex is copy and pasted because i suck at it
