from unittest import TestCase

import numpy as np


def volume(*args):
    dimension = len(args) - 1
    for arg in args:
        if dimension != len(arg) - 1:
            raise ValueError("Tuple not expected size")
    # np.matrix([np.subtract()])


class SampleTest(TestCase):
    def test_invalid_input(self):
        self.assertRaises(ValueError, volume((1, 1, 1), (4, 4, 1)))

    def test_triangle_volume1(self):
        self.assertEqual(3, volume((1, 1), (4, 1), (0, 3)))

    def test_triangle_volume2(self):
        self.assertEqual(6, volume((0, 0), (4, 0), (0, 3)))

    def test_tetrahedron1(self):
        self.assertEqual(3 * 3, volume((1, 1, 0), (4, 1, 0), (0, 3, 0), (1, 1, 3)))

    def test_tetrahedron2(self):
        self.assertEqual(6, volume((0, 0, 0), (4, 0, 0), (0, 3, 0), (0, 0, 3)))
