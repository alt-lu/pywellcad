import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestStructure(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.struct_borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.struct_log = cls.struct_borehole.log("Structure")
        cls.struct = cls.struct_log.structure(0)

        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.breakout_borehole = cls.app.open_borehole(str(cls.fixture_path / "Breakout Picking.WCL"))
        cls.breakout_log = cls.breakout_borehole.log("Breakouts")
        cls.breakout = cls.breakout_log.breakout(0)

        cls.lineation_borehole = cls.app.open_borehole(str(cls.fixture_path / "Lineation Example.WCL"))
        cls.lineation_log = cls.lineation_borehole.log("Lineations")
        cls.lineation = cls.lineation_log.lineation(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_depth(self):
        self.assertEqual(self.struct.depth, 2119.459716796875)
        self.assertEqual(self.breakout.depth, 106.87999725341797)
        self.assertEqual(self.lineation.depth, 54.13199996948242)

    def test_azimuth(self):
        self.assertAlmostEqual(self.struct.azimuth, 307.58, 2)
        self.assertAttrAlmostChange(self.struct, 'azimuth', 25.0, 2)
        self.assertAlmostEqual(self.breakout.azimuth, 285.81, 2)
        self.assertAttrAlmostChange(self.breakout, 'azimuth', 25.0, 2)
        self.assertAlmostEqual(self.lineation.azimuth, 209.62, 2)
        self.assertAttrAlmostChange(self.lineation, 'azimuth', 25.0, 2)

    def test_tilt(self):
        self.assertAlmostEqual(self.struct.tilt, 37.59, 2)
        self.assertAttrAlmostChange(self.struct, 'tilt', 25.0, 2)
        self.assertAlmostEqual(self.breakout.tilt, 0.585, 2)
        self.assertAttrAlmostChange(self.breakout, 'tilt', 25.0, 2)
        self.assertAlmostEqual(self.lineation.tilt, 29.82, 2)
        self.assertAttrAlmostChange(self.lineation, 'tilt', 25.0, 2)

    def test_aperture(self):
        self.assertAlmostEqual(self.struct.aperture, 0.0, 2)
        self.assertAttrAlmostChange(self.struct, 'aperture', 1.5, 2)
        self.assertAlmostEqual(self.breakout.aperture, 16.86, 2)
        self.assertAttrAlmostChange(self.breakout, 'aperture', 1.5, 2)

    def test_get_attribute_value(self):
        self.assertEqual(self.struct.get_attribute_value("Type"), "2 - Bed / Lamina")
        self.assertEqual(self.struct.get_attribute_value("attribute that doesn't exit"), "")
        self.assertEqual(self.breakout.get_attribute_value("Type"), "0")
        self.assertEqual(self.breakout.get_attribute_value("attribute that doesn't exit"), "")
        self.assertEqual(self.lineation.get_attribute_value("Type"), "FA")
        self.assertEqual(self.lineation.get_attribute_value("attribute that doesn't exit"), "")

    def test_set_attribute_value(self):
        self.struct.set_attribute_value("Type", "random string")
        self.breakout.set_attribute_value("Type", "random string")
        self.lineation.set_attribute_value("Type", "random string")

    def test_length(self):
        self.assertAttrEqual(self.breakout, "length", 0.1440047025680542)
        self.assertAttrAlmostChange(self.breakout, "length", 2.0, 2)

    def test_feature_depth(self):
        self.assertAlmostEqual(self.struct.feature_depth, 2119.46, 2)  #TODO is there an example to test this with a partial structure?

    def test_visible_azimuth_ranges(self):
        self.assertEqual(self.struct.visible_azimuth_ranges, "")  #TODO is there an example to test this with a partial structure?

    def test_eccentricity(self):
        self.assertEqual(self.lineation.eccentricity, 0.8725769519805908)


if __name__ == '__main__':
    unittest.main()
