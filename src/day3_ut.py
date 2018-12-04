import unittest
from parameterized import parameterized
from src.day3 import Piece, Fabric

class WhenCreatePiece(unittest.TestCase):
    def test_that_it_populates_attributes(self):
        piece = Piece("#1 @ 906,735: 28x17")
        self.assertEqual(906, piece.top_offset)
        self.assertEqual(735, piece.left_offset)
        self.assertEqual(28, piece.width)
        self.assertEqual(17, piece.height)

class WhenClaimPiece(unittest.TestCase):
    def test_that_fabric_counts_single_piece_1x1(self):
        piece = Piece("#1 @ 0,0: 1x1")
        fabric = Fabric(2, 2)
        fabric.Claim(piece)

        self.assertEqual("\n"
                         "1.\n"
                         "..\n", fabric.Area())

    def test_that_fabric_counts_single_piece_2x2(self):
        piece = Piece("#1 @ 1,1: 2x2")
        fabric = Fabric(4, 4)
        fabric.Claim(piece)

        self.assertEqual("\n"
                         "....\n"
                         ".11.\n"
                         ".11.\n"
                         "....\n", fabric.Area())

    def test_that_fabric_counts_overlapping_pieces_2x2(self):
        fabric = Fabric(4, 4)
        fabric.Claim(Piece("#1 @ 0,0: 2x2"))
        fabric.Claim(Piece("#1 @ 1,1: 2x2"))

        self.assertEqual("\n"
                         "11..\n"
                         "121.\n"
                         ".11.\n"
                         "....\n", fabric.Area())

    @parameterized.expand([
        ["#1 @ 0,0: 2x2", "#1 @ 1,1: 2x2", 1],
        ["#2 @ 0,0: 2x2", "#2 @ 0,0: 2x2", 4],
    ])
    def test_that_fabric_counts_overlapping_inches_count(self, piece1, piece2, overlappingInches):
        fabric = Fabric(4, 4)
        fabric.Claim(Piece(piece1))
        fabric.Claim(Piece(piece2))

        self.assertEqual(overlappingInches, fabric.OverlappingInches)

