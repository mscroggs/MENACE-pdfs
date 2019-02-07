from itertools import permutations

from menace import Board

positions = [[],[],[]]

for o1 in range(9):
    board = Board()
    board[o1] = 1
    if board.is_max() and not board.in_set(positions[0]):
        positions[0].append(board)
    for x1 in range(9):
        if x1 not in [o1]:
            for o2 in range(o1):
                if o2 not in [o1,x1]:
                    board = Board()
                    board[o1] = 1
                    board[x1] = 2
                    board[o2] = 1
                    if board.is_max() and not board.in_set(positions[1]):
                        positions[1].append(board)
                    for x2 in range(x1):
                        if x2 not in [o1,x1,o2]:
                            for o3 in range(o1):
                                if o3 not in [o1,x1,o2,x2]:
                                    board = Board()
                                    board[o1] = 1
                                    board[x1] = 2
                                    board[o2] = 1
                                    board[x2] = 2
                                    board[o3] = 1
                                    if board.has_winner():
                                        break
                                    if board.is_max() and not board.in_set(positions[2]):
                                       positions[2].append(board)


print("==")
print([len(p) for p in positions])
print(sum([len(p) for p in positions]))
print("==")

preamb = "\\documentclass{article}\n\\usepackage{tikz}\n\\begin{document}\n\\noindent\n"
postamb = "\\end{document}"

import os
for i,boards in enumerate(positions):
    latex = preamb
    for board in boards:
        latex += board.as_latex()
        latex += "\n"
    latex += postamb
    print(latex)
    with open("output/second_boxes"+str(i)+".tex","w") as f:
        f.write(latex)
    os.system("pdflatex -output-directory output output/second_boxes"+str(i)+".tex")
