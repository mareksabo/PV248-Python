from unittest import TestCase

import numpy as np


def volume(*args):
    dimension = len(args)

    if dimension < 3:
        raise ValueError("More params needed")

    for arg in args:
        if dimension - 1 != len(arg):
            print(arg)
            print(len(arg))
            raise ValueError("Tuple not expected size")

    first = args[0]
    others = args[1:]

    array = np.matrix([np.subtract(x, first) for x in others])
    return np.absolute(np.linalg.det(array.T) / np.math.factorial(dimension - 1))


class SampleTest(TestCase):
    def test_invalid_1(self):
        self.assertRaises(ValueError, volume, (1, 1, 1), (4, 4, 1))

    def test_invalid_2(self):
        self.assertRaises(ValueError, volume, (1, 1))

    def test_invalid_3(self):
        self.assertRaises(ValueError, volume, (2, 3), (5, 4, 0), (1, 4, 0), (2, 9, 1))

    def test_invalid_4(self):
        self.assertRaises(ValueError, volume, (2,), (5,))

    def test_invalid_5(self):
        self.assertRaises(ValueError, volume, (5, 4, 0), (1, 4), (2, 3, 9), (2, 9, 1))

    def test_2D_1(self):
        self.assertEqual(volume((1, 1), (4, 1), (0, 3)), 3)

    def test_2D_2(self):
        self.assertEqual(volume((0, 0), (4, 0), (0, 3)), 6)

    def test_2D_3(self):
        self.assertAlmostEqual(volume((1, 1), (5, 0), (5, 4)), 8)

    def test_2D_4(self):
        self.assertAlmostEqual(volume((1, 2), (3, 4), (6, 5)), 2)

    def test_2D_5(self):
        self.assertAlmostEqual(volume((1, 8), (2, 4), (0, 9)), 1.5)

    def test_3D_1(self):
        self.assertAlmostEqual(volume((0, 0, 0), (5, 0, 0), (5, 4, 0), (2, 0, 2)), 20 / 3)

    def test_3D_2(self):
        self.assertAlmostEqual(volume((0, 0, 0), (5, 0, 0), (5, 4, 0), (2, 0, -2)), 20 / 3)

    def test_3D_3(self):
        self.assertAlmostEqual(volume((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, 0)), 1 / 6)

    def test_3D_4(self):
        self.assertAlmostEqual(volume((0, 0, 1), (0, 0, 0), (5, 0, 0), (2, 3, 2)), 7.5 / 3)

    def test_3D_5(self):
        self.assertAlmostEqual(volume((0, 0, 0), (4, 0, 0), (0, 3, 0), (0, 0, 3)), 6)

    def test_3D_6(self):
        self.assertAlmostEqual(volume((1, 1, 0), (4, 1, 0), (0, 3, 0), (1, 1, 3)), 3)
