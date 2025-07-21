class Board:
    def __init__(self):
        self.board = [0] * 9

    def __getitem__(self, n):
        return self.board[n]

    def __setitem__(self, n, value):
        self.board[n] = value

    def __str__(self):
        return "\n".join([
            "".join([[" ", "o", "x"][j] for j in self.board[3*i:3*i+3]])
            for i in range(3)
        ])

    def in_set(self, set):
        set = [s.n() for s in set]
        for a in self.permutations():
            if a in set:
                return True
        return False

    def is_max(self):
        return self.n() == max(self.permutations())

    def permutations(self):
        out = []
        for rot in [
            (0, 1, 2, 3, 4, 5, 6, 7, 8), (2, 5, 8, 1, 4, 7, 0, 3, 6),
            (8, 7, 6, 5, 4, 3, 2, 1, 0), (6, 3, 0, 7, 4, 1, 8, 5, 2),
            (2, 1, 0, 5, 4, 3, 8, 7, 6), (8, 5, 2, 7, 4, 1, 6, 3, 0),
            (6, 7, 8, 3, 4, 5, 0, 1, 2), (0, 3, 6, 1, 4, 7, 2, 5, 8)
        ]:
            out.append(self.nrot(rot))
        return out

    def has_winner(self):
        for i, j, k in [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
            (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ]:
            if self[i] != 0 and self[i] == self[j] == self[k]:
                return True
        return False

    def n(self):
        return self.nrot(list(range(9)))

    def nrot(self, rot):
        out = 0
        for i in range(9):
            out += 3 ** i * self[rot[i]]
        return out

    def as_latex(self, index=None):
        out = "\\begin{tikzpicture}\n"
        out += "\\clip (3.75mm,-1mm) rectangle (40.25mm,25mm);\n"
        out += "\\draw[gray] (5mm,5mm) -- (39mm,5mm);\n"
        out += "\\draw[gray] (5mm,19mm) -- (39mm,19mm);\n"
        out += "\\draw[gray] (5mm,0mm) -- (5mm,24mm);\n"
        out += "\\draw[gray] (39mm,0mm) -- (39mm,24mm);\n"

        out += "\\draw (16mm,10mm) -- (28mm,10mm);\n"
        out += "\\draw (16mm,14mm) -- (28mm,14mm);\n"
        out += "\\draw (20mm,6mm) -- (20mm,18mm);\n"
        out += "\\draw (24mm,6mm) -- (24mm,18mm);\n"

        for i, c in enumerate([
            (16, 6), (20, 6), (24, 6),
            (16, 10), (20, 10), (24, 10),
            (16, 14), (20, 14), (24, 14)
        ]):
            if self[i] == 1:
                # o
                out += f"\\draw ({c[0]+2}mm,{c[1]+2}mm) circle (1mm);\n"
            if self[i] == 2:
                # x
                out += (f"\\draw ({c[0]+1}mm,{c[1]+1}mm)"
                        f" -- ({c[0]+3}mm,{c[1]+3}mm);\n"
                        f"\\draw ({c[0]+1}mm,{c[1]+3}mm)"
                        f" -- ({c[0]+3}mm,{c[1]+1}mm);\n")
        if index is not None:
            # Add index at bottom-right corner
            out += f"\\node[anchor=south east, font=\\small] at (39mm,6mm) {{{{ {index} }}}};\n"

        out += "\\end{tikzpicture}"
        return out
