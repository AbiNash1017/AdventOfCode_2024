# Import necessary module
import sys

# Define the input file path
input_file_path = r"D:\Advent of code\day15\input.txt"

# Read the grid and moves from the input file
with open(input_file_path, "r") as f:
    grid_str, moves = f.read().split("\n\n")

# Create the grid from the string
grid = [list(row) for row in grid_str.split("\n")]
moves = moves.replace("\n", "")

# Find the initial position of the player represented by "@"
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

# Define the movement mapping
move_map = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

# Process the moves for Part 1
for move in moves:
    dr, dc = move_map[move]
    rr, cc = r + dr, c + dc
    do_move = True
    while True:
        if grid[rr][cc] == "#":
            do_move = False
            break
        if grid[rr][cc] == ".":
            break
        if grid[rr][cc] == "O":
            rr, cc = rr + dr, cc + dc
        else:
            assert False

    if not do_move:
        continue
    grid[r][c] = "."
    r, c = r + dr, c + dc
    if grid[r][c] == "O":
        grid[rr][cc] = "O"
    grid[r][c] = "@"

# Calculate the result for Part 1
part1 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "O"
)
print(f"Part 1: {part1}")

# Define the grid mapping for Part 2
grid_map = {"#": "##", "O": "[]", ".": "..", "@": "@."}

# Read the grid again from the input file for Part 2
with open(input_file_path, "r") as f:
    grid_str, moves = f.read().split("\n\n")
grid = []
for row in grid_str.splitlines():
    new_row = []
    for val in row:
        new_row.extend(grid_map[val])
    grid.append(new_row)
moves = moves.replace("\n", "")

# Find the initial position of the player represented by "@"
for r, row in enumerate(grid):
    for c, val in enumerate(row):
        if val == "@":
            break
    else:
        continue
    break

# Process the moves for Part 2
for move in moves:
    dr, dc = move_map[move]
    do_move = True
    to_move = [(r, c)]
    i = 0
    while i < len(to_move):
        rr, cc = to_move[i]
        i += 1
        nr, nc = rr + dr, cc + dc
        if (nr, nc) in to_move:
            continue
        if grid[nr][nc] == "#":
            do_move = False
            break
        if grid[nr][nc] == ".":
            continue
        if grid[nr][nc] == "[":
            to_move.extend([(nr, nc), (nr, nc + 1)])
        elif grid[nr][nc] == "]":
            to_move.extend([(nr, nc), (nr, nc - 1)])
        else:
            assert False

    if not do_move:
        continue
    grid_copy = [list(row) for row in grid]
    r, c = r + dr, c + dc
    for rr, cc in to_move:
        grid[rr][cc] = "."
    for rr, cc in to_move:
        grid[rr + dr][cc + dc] = grid_copy[rr][cc]

# Calculate the result for Part 2
part2 = sum(
    r * 100 + c for r, row in enumerate(grid) for c, val in enumerate(row) if val == "["
)
print(f"Part 2: {part2}")