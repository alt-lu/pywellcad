import unittest
import pathlib
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestCrossSectionBox(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "ABI 43 Corrosion Plot.wcl"))
        cls.log = cls.borehole.log("Cross Section")
        cls.item = cls.log.cross_box(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAlmostEqual(self.item.top_depth, 45.0622, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.item.bottom_depth, 45.0622, 3)


if __name__ == '__main__':
    unittest.main()
