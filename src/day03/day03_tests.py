import unittest

from parameterized import parameterized

from src.day03.Fabric import Fabric
from src.day03.Piece import Piece


class WhenCreatePiece(unittest.TestCase):
    def test_that_it_populates_attributes(self):
        piece = Piece("#1 @ 906,735: 28x17")
        self.assertEqual(1, piece.number)
        self.assertEqual(906, piece.left_offset)
        self.assertEqual(735, piece.top_offset)
        self.assertEqual(28, piece.width)
        self.assertEqual(17, piece.height)

    def test_that_it_has_corners(self):
        piece = Piece("#1 @ 1,1: 2x3")

        self.assertEqual([(1, 1), (2, 1), (2, 3), (1, 3)], piece.Corners)

    def test_that_piece_contains_point(self):
        piece = Piece("#1 @ 0,0: 2x2")

        self.assertEqual(True, piece.contains((0, 0)))

    @parameterized.expand([
        ["#1 @ 0,0: 2x2", "#1 @ 1,1: 2x3"],
        ["#2 @ 0,0: 2x2", "#1 @ 0,1: 2x3"],
        ["#3 @ 0,0: 2x2", "#1 @ 1,0: 2x3"],
        ["#4 @ 0,0: 2x2", "#1 @ 0,0: 2x3"],
        ["#5 @ 0,0: 5x5", "#1 @ 2,2: 1x1"],
        ["#6 @ 0,0: 5x5", "#1 @ 0,0: 1x1"],
        ["#7 @ 0,0: 5x5", "#1 @ 0,4: 1x1"],
        ["#8 @ 0,0: 5x5", "#1 @ 4,4: 1x1"],
        ["#9 @ 0,0: 5x5", "#1 @ 4,0: 1x1"],
        ["#10 @ 0,0: 1x1", "#1 @ 0,0: 1x1"],
        ["#11 @ 1,0: 1x3", "#1 @ 0,1: 3x1"],
    ])
    def test_that_piece_overlaps_with_another_piece(self, s1, s2):
        piece1 = Piece(s1)
        piece2 = Piece(s2)

        self.assertEqual(True, piece1.overlaps(piece2))
        self.assertEqual(True, piece2.overlaps(piece1))

    def test_that_piece_does_not_overlaps_with_another_piece_wtf(self):
        piece1 = Piece("#1 @ 1,2: 2x3")
        piece2 = Piece("#2 @ 1,0: 2x2")

        self.assertEqual(False, piece1.overlaps(piece2))

    @parameterized.expand([
        ["#1 @ 1,2: 2x3", "#1 @ 0,0: 1x2"],
        ["#2 @ 1,2: 2x3", "#2 @ 1,0: 2x2"],
        ["#3 @ 1,2: 2x3", "#2 @ 3,0: 1x10"],
        ["#4 @ 1,2: 2x3", "#2 @ 3,2: 2x3"],
        ["#5 @ 1,2: 2x3", "#2 @ 3,5: 1x1"],
        ["#6 @ 1,2: 2x3", "#2 @ 1,5: 10x10"],
        ["#7 @ 1,2: 2x3", "#2 @ 0,5: 10x10"],
        ["#8 @ 1,2: 2x3", "#2 @ 0,2: 1x3"],
    ])
    def test_that_piece_does_not_overlaps_with_another_piece(self, p1, p2):
        piece1 = Piece(p1)
        piece2 = Piece(p2)

        self.assertEqual(False, piece1.overlaps(piece2))
        self.assertEqual(False, piece2.overlaps(piece1))

    def test_that_piece_equals_to_itself(self):
        piece = Piece("#1 @ 2,2: 2x2")

        self.assertEqual(True, piece == piece)


class WhenClaimPiece(unittest.TestCase):
    def test_that_fabric_counts_single_piece_1x1(self):
        piece = Piece("#1 @ 0,0: 1x1")
        fabric = Fabric(2, 2)
        fabric.claim(piece)

        self.assertEqual("\n"
                         "1.\n"
                         "..\n", fabric.area())

    def test_that_fabric_counts_single_piece_2x2(self):
        piece = Piece("#1 @ 1,1: 2x2")
        fabric = Fabric(4, 4)
        fabric.claim(piece)

        self.assertEqual("\n"
                         "....\n"
                         ".11.\n"
                         ".11.\n"
                         "....\n", fabric.area())

    def test_that_fabric_counts_single_piece_2x2_asymmetrical(self):
        piece = Piece("#1 @ 2,1: 2x2")
        fabric = Fabric(4, 4)
        fabric.claim(piece)

        self.assertEqual("\n"
                         "....\n"
                         "..11\n"
                         "..11\n"
                         "....\n", fabric.area())

    def test_that_fabric_counts_overlapping_pieces_2x2(self):
        fabric = Fabric(4, 4)
        fabric.claim(Piece("#1 @ 0,0: 2x2"))
        fabric.claim(Piece("#1 @ 1,1: 2x2"))

        self.assertEqual("\n"
                         "11..\n"
                         "121.\n"
                         ".11.\n"
                         "....\n", fabric.area())

    @parameterized.expand([
        ["#1 @ 0,0: 2x2", "#1 @ 1,1: 2x2", 1],
        ["#2 @ 0,0: 2x2", "#2 @ 0,0: 2x2", 4],
    ])
    def test_that_fabric_counts_overlapping_inches_count(self, piece1, piece2, overlapping_inches):
        fabric = Fabric(4, 4)
        fabric.claim(Piece(piece1))
        fabric.claim(Piece(piece2))

        self.assertEqual(overlapping_inches, fabric.overlapping_inches)
