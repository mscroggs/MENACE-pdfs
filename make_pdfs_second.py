import os
from itertools import permutations
from menace import Board
from latex import preamb, postamb

positions = [[], [], [], []]

for o1 in range(9):
    board = Board()
    board[o1] = 1
    if board.is_max() and not board.in_set(positions[0]):
        positions[0].append(board)

for o1, x1, o2 in permutations(range(9), 3):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    if board.is_max() and not board.in_set(positions[1]):
        positions[1].append(board)

for o1, x1, o2, x2, o3 in permutations(range(9), 5):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    board[o3] = 1
    if board.has_winner():
        continue
    if board.is_max() and not board.in_set(positions[2]):
        positions[2].append(board)

for o1, x1, o2, x2, o3, x3, o4 in permutations(range(9), 7):
    board = Board()
    board[o1] = 1
    board[x1] = 2
    board[o2] = 1
    board[x2] = 2
    board[o3] = 1
    board[x3] = 2
    board[o4] = 1
    if board.has_winner():
        continue
    if board.is_max() and not board.in_set(positions[3]):
        positions[3].append(board)


assert sum([len(p) for p in positions]) == 289
assert len(positions[0]) == 3
assert len(positions[1]) == 38

index = 1
for i, boards in enumerate(positions):
    latex = preamb
    for j, board in enumerate(boards):
        latex += board.as_latex(index=index)
        latex += "\n"
        if (j + 1) % 5 == 0:
            latex += "\n\\noindent"
        index += 1
    latex += postamb
    with open(f"output/second_boxes{i}.tex", "w") as f:
        f.write(latex)
    assert os.system(
        f"pdflatex -output-directory output output/second_boxes{i}.tex") == 0
