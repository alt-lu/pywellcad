import unittest
import pathlib

import pywintypes

import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestBreakout(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.fixture_path / "Breakout Picking.WCL"))
        cls.log = cls.borehole.log("Breakouts")
        cls.breakout = cls.log.breakout(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_depth(self):
        self.assertAlmostEqual(self.breakout.depth, 106.88, 2)

    def test_azimuth(self):
        self.assertAlmostEqual(self.breakout.azimuth, 285.81, 2)
        self.assertAttrAlmostChange(self.breakout, 'azimuth', 25.0, 2)

    def test_tilt(self):
        self.assertAlmostEqual(self.breakout.tilt, 0.585, 2)
        self.assertAttrAlmostChange(self.breakout, 'tilt', 25.0, 2)

    def test_aperture(self):
        self.assertAlmostEqual(self.breakout.aperture, 16.86, 2)
        self.assertAttrAlmostChange(self.breakout, 'aperture', 1.5, 2)

    def test_get_attribute_value(self):
        self.assertEqual(self.breakout.get_attribute_value("Type"), "0")
        self.assertEqual(self.breakout.get_attribute_value("attribute that doesn't exit"), "")

    def test_set_attribute_value(self):
        self.breakout.set_attribute_value("Type", "random string")


if __name__ == '__main__':
    unittest.main()
