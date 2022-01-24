import unittest
import pathlib

import pywintypes

import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestStructure(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.log = cls.borehole.log("Structure")
        cls.struct = cls.log.structure(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_depth(self):
        self.assertAlmostEqual(self.struct.depth, 2119.46, 2)

    def test_feature_depth(self):
        self.assertAlmostEqual(self.struct.feature_depth, 2119.46, 2)  #TODO is there an example to test this with a partial structure?

    def test_azimuth(self):
        self.assertAlmostEqual(self.struct.azimuth, 307.58, 2)
        self.assertAttrAlmostChange(self.struct, 'azimuth', 25.0, 2)

    def test_tilt(self):
        self.assertAlmostEqual(self.struct.tilt, 37.59, 2)
        self.assertAttrAlmostChange(self.struct, 'tilt', 25.0, 2)

    def test_aperture(self):
        self.assertAlmostEqual(self.struct.aperture, 0.0, 2)
        self.assertAttrAlmostChange(self.struct, 'aperture', 1.5, 2)

    def test_get_attribute_value(self):
        self.assertEqual(self.struct.get_attribute_value("Type"), "2 - Bed / Lamina")
        self.assertEqual(self.struct.get_attribute_value("attribute that doesn't exit"), "")

    def test_set_attribute_value(self):
        self.struct.set_attribute_value("Type", "random string")

    def test_visible_azimuth_ranges(self):
        self.assertEqual(self.struct.visible_azimuth_ranges, "")  #TODO is there an example to test this with a partial structure?


if __name__ == '__main__':
    unittest.main()
