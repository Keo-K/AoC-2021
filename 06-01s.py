import sys
import numpy as np

with open("06-01.txt") as f:
    data = list(map(int, f.read().strip().split(",")))


def get_fish():
    fish = np.array(data)
    ret_val = np.zeros((9,), dtype=np.longlong)
    for i in range(9):
        ret_val[i] = np.count_nonzero(fish == i)
    return ret_val


def main():
    fish = get_fish()
    for i in range(256):
        reproducing_fish = fish[0]
        fish[0:8] = fish[1:9]
        fish[6] += reproducing_fish
        fish[8] = reproducing_fish
    print("Total number of fish:\t" + str(fish.sum()))


if __name__ == "__main__":
    main()
