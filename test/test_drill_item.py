import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestDrillItem(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Engineering Log and Borehole Volume.wcl"))
        cls.engineering_log = cls.borehole.log("Well Sketch")
        cls.drill_item = cls.engineering_log.drill_item(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.drill_item.bottom_depth, 15.0, 3)

    def test_set_diameter(self):
        self.assertAlmostEqual(self.drill_item.diameter, 300.0, 3)
        self.assertAttrAlmostChange(self.drill_item, 'diameter', 112.2, 3)

    def test_get_comment(self):
        self.assertAttrEqual(self.drill_item, "comment", 'Drill\r\n0.00-15.00\r\ndiameter:300')

    def test_set_comment(self):
        self.assertAttrChange(self.drill_item, "comment", 'mycomment')


if __name__ == '__main__':
    unittest.main()
