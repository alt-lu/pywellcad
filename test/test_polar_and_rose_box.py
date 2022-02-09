import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestPolarAndRoseBox(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.new_borehole()
        cls.fmi_net_sand_estimation_borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.polar_log = cls.fmi_net_sand_estimation_borehole.get_log("Polar Projection")
        cls.polar_item = cls.polar_log.schmit_box(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAlmostEqual(self.polar_item.top_depth, 2118.838, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.polar_item.bottom_depth, 2148.989, 3)

    def test_text(self):
        self.assertAttrEqual(self.polar_item, "text", '')
        self.assertAttrChange(self.polar_item, "text", 'Any Comment')


if __name__ == '__main__':
    unittest.main()
