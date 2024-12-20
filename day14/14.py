import math
import re
import sys

def safey_score(robots: list[tuple[int]]) -> int:
    q = [0] * 4
    for xf, yf in robots:
        midw, midh = width // 2, height // 2
        if xf < midw:
            if yf < midh:
                q[0] += 1
            if yf > midh:
                q[1] += 1
        elif xf > midw:
            if yf < midh:
                q[2] += 1
            if yf > midh:
                q[3] += 1
    return math.prod(q)

# Set the file path directly
file_path = 'D:/Advent of code/day14/input.txt'

# Set width and height based on the file path or other conditions
width, height = 101, 103  # You can adjust these values as needed

with open(file_path, "r") as f:
    lines = list(map(str.strip, f.readlines()))

robots = []
for line in lines:
    # p=0,4 v=3,-3
    x, y, dx, dy = tuple(map(int, re.findall(r"-?\d+", line)))
    robots.append((x, y, dx, dy))

part1_robots = []
for x, y, dx, dy in robots:
    xf = (x + (dx * 100)) % width
    yf = (y + (dy * 100)) % height
    part1_robots.append((xf, yf))

part1 = safey_score(part1_robots)
print(f"Part 1: {part1}")

t = []
ss = []
min_score = 1e10
for i in range(10000):
    snap = []
    for x, y, dx, dy in robots:
        xf = (x + (dx * i)) % width
        yf = (y + (dy * i)) % height
        snap.append((xf, yf))
    t.append(i)
    sss = safey_score(snap)
    ss.append(sss)
    if sss < min_score:
        best_snap = snap[:]
        min_score = sss
        best_frame = i

part2 = best_frame
print(f"Part 2: {part2}")