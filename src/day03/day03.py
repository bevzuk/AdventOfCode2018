from src.day03.Fabric import Fabric
from src.day03.Piece import Piece


def solve_part_1():
    text_file = open("day03.input.txt", "r")
    pieces = list(map(lambda x: Piece(x), text_file.readlines()))
    text_file.close()

    max_width = 0
    max_height = 0
    for piece in pieces:
        if piece.left_offset + piece.width > max_width:
            max_width = piece.left_offset + piece.width
        if piece.top_offset + piece.height > max_height:
            max_height = piece.top_offset + piece.height

    fabric = Fabric(max_width, max_height)
    for piece in pieces:
        fabric.claim(piece)

    print("1. Number of overlapping inches: ", fabric.overlapping_inches)

    out_file = open("day03.out.txt", "w")
    out_file.write(fabric.area())
    out_file.close()


def solve_part_2():
    text_file = open("day03.input.txt", "r")
    pieces = list(map(lambda x: Piece(x), text_file.readlines()))
    text_file.close()

    for piece1 in pieces:
        overlaps = False
        for piece2 in pieces:
            if piece1 == piece2:
                continue
            if piece1.overlaps(piece2):
                overlaps = True
                continue
        if not overlaps:
            print("2. Non-overlapping piece:", piece1.number)


solve_part_1()
solve_part_2()
