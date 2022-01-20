import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestIntervalItem(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Geotech Plot.WCL"))
        cls.log = cls.borehole.log("Sampling")
        cls.item = cls.log.interval_item(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAttrEqual(self.item, "top_depth", 0.012770021334290504)

    def test_bottom_depth(self):
        self.assertAttrEqual(self.item, "bottom_depth", 2.014082670211792)

    def test_set_value(self):
        self.assertAttrEqual(self.item, "value", 1.6380952596664429)
        self.assertAttrAlmostChange(self.item, 'value', 30.4, 3)


if __name__ == '__main__':
    unittest.main()
