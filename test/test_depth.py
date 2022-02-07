import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestDepth(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.depth = cls.borehole.depth

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_decimals(self):
        self.assertAttrEqual(self.depth, "decimals", 0)
        self.assertAttrChange(self.depth, "decimals", 1)

    def test_horizontal_grid_spacing(self):
        self.assertAttrEqual(self.depth, "horizontal_grid_spacing", 4.0)
        self.assertAttrChange(self.depth, "horizontal_grid_spacing", 4.5)

    def test_scale(self):
        self.assertAttrEqual(self.depth, "scale", 150.0)
        self.assertAttrChange(self.depth, "scale", 100.0)

    def test_used_as_depth_scale(self):
        self.assertAttrEqual(self.depth, "used_as_depth_scale", True)
        new_depth_log = self.borehole.insert_new_log(17)  # new depth log
        new_depth_log.used_as_depth_scale = True   # Setting the new depth log as depth scale (True) changes the other ones to False
        self.assertAttrEqual(self.depth, "used_as_depth_scale", False)
        self.depth.used_as_depth_scale = True
        self.assertAttrEqual(self.depth, "used_as_depth_scale", True)
        self.assertAttrNotChanged(self.depth, "used_as_depth_scale", False)  # Setting fails because it is the main depth log


    def test_horizontal_grid(self):
        self.assertAttrEqual(self.depth, "horizontal_grid", 2)
        self.assertAttrChange(self.depth, "horizontal_grid", 0)
        self.assertAttrChange(self.depth, "horizontal_grid", 1)
        self.assertAttrChange(self.depth, "horizontal_grid", 2)
        self.assertAttrNotChanged(self.depth, "horizontal_grid", 3)  # out of bounds


    def test_position(self):
        left = self.depth.left_position
        right = self.depth.right_position
        self.assertIsInstance(left, float)
        self.assertIsInstance(right, float)
        self.assertGreaterEqual(right, left)
        new_left = left + 0.1
        new_right = right + 0.15
        self.depth.set_position(new_left, new_right)
        self.assertAlmostEqual(new_left, self.depth.left_position)
        self.assertAlmostEqual(new_right, self.depth.right_position)
        self.depth.left_position = left
        self.depth.right_position = right
        self.assertEqual(left, self.depth.left_position)
        self.assertEqual(right, self.depth.right_position)

    def test_swapped_position(self):
        left = self.depth.left_position
        right = self.depth.right_position

        # Check that positions are swapped if we set left greater than
        # right
        self.depth.set_position(0.5, 0.2)
        self.assertAlmostEqual(self.depth.left_position, 0.2)
        self.assertAlmostEqual(self.depth.right_position, 0.5)

        self.depth.set_position(left, right)

    def test_left_position_greater_than_right(self):
        left = self.depth.left_position
        right = self.depth.right_position

        self.depth.left_position = 0.5
        self.assertAlmostEqual(self.depth.left_position, right)
        self.assertAlmostEqual(self.depth.right_position, 0.5)

        self.depth.set_position(left, right)

    def test_out_of_bounds_position(self):
        left = self.depth.left_position
        right = self.depth.right_position

        # Make sure we can't set positions outside 0.0 to 1.0. Behaviour
        # here is to clamp
        self.depth.left_position = -0.1
        self.assertEqual(self.depth.left_position, 0.0)
        self.depth.right_position = 1.1
        self.assertEqual(self.depth.right_position, 1.0)

        self.depth.set_position(left, right)

    def test_unit(self):
        self.assertAttrEqual(self.depth, "unit", 0)
        self.assertAttrChange(self.depth, "unit", 0)
        self.assertAttrChange(self.depth, "unit", 1)
        self.assertAttrNotChanged(self.depth, "unit", 2)

    def test_set_position(self):
        self.depth.set_position(0.0, 0.15)

if __name__ == '__main__':
    unittest.main()
