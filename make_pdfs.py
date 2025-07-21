import argparse
import os
from itertools import permutations
from menace import Board
from latex import preamb, postamb

parser = argparse.ArgumentParser(description="Make MENACE pdfs")
parser.add_argument(
    "destination",
    metavar="destination",
    nargs="?",
    default=None,
    help="Destination of pdf files.",
)
parser.add_argument(
    "--with-indices", action="store_true", help="Include index numbers on boxes."
)

args = parser.parse_args()
include_indices = args.with_indices
if include_indices:
    dir = "output-with-indices"
else:
    dir = "output-no-indices"
if args.destination is not None:
    while dir.endswith("/"):
        dir = dir[:-1]
    dir = args.destination

positions = [[Board()], [], [], []]

for o1, x1 in permutations(range(9), 2):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    if board.is_max() and not board.in_set(positions[1]):
        positions[1].append(board)

for o1, x1, o2, x2 in permutations(range(9), 4):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    if board.is_max() and not board.in_set(positions[2]):
        positions[2].append(board)

for o1, x1, o2, x2, o3, x3 in permutations(range(9), 6):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    board[o3] = 1
    board[x3] = 2
    if board.has_winner():
        continue
    if board.is_max() and not board.in_set(positions[3]):
        positions[3].append(board)


assert len(positions[0]) == 1
assert len(positions[1]) == 12
assert sum([len(p) for p in positions]) == 304

index = 1
for i, boards in enumerate(positions):
    latex = preamb
    for j, board in enumerate(boards):
        if include_indices:
            latex += board.as_latex(index=index)
        else:
            latex += board.as_latex()
        latex += "\n"
        if (j + 1) % 5 == 0:
            latex += "\n\\noindent"
        index += 1
    latex += postamb
    print(latex)
    with open(f"{dir}/boxes{i}.tex", "w") as f:
        f.write(latex)
    assert os.system(
        f"pdflatex -output-directory {dir} {dir}/boxes{i}.tex") == 0
