import unittest
from src.day3 import Piece, FabricSolver

class WhenCreatePiece(unittest.TestCase):
    def test_that_it_populates_attributes(self):
        piece = Piece("#1 @ 906,735: 28x17");
        self.assertEqual(906, piece.top_offset)
        self.assertEqual(735, piece.left_offset);
        self.assertEqual(28, piece.width);
        self.assertEqual(17, piece.height);
