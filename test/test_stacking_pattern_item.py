import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestStackingPatternItem(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.borehole = cls.app.new_borehole()
        cls.log = cls.borehole.insert_new_log(19)
        cls.item = cls.log.insert_new_stack_item(10.5, 22.5, 0.1, 0.9)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAlmostEqual(self.item.top_depth, 10.5, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.item.bottom_depth, 22.5, 3)

    def test_set_top_width(self):
        self.assertAlmostEqual(self.item.top_width, 0.1, 3)
        self.assertAttrAlmostChange(self.item, 'top_width', 0.6, 3)

    def test_set_bottom_width(self):
        self.assertAlmostEqual(self.item.bottom_width, 0.9, 3)
        self.assertAttrAlmostChange(self.item, 'bottom_width', 0.2, 3)

    def test_set_bottom_width_out_of_bounds(self):
        self.assertAlmostEqual(self.item.bottom_width, 0.9, 3)
        self.item.bottom_width = 1.2
        self.assertAlmostEqual(self.item.bottom_width, 1.0, 3)


if __name__ == '__main__':
    unittest.main()
