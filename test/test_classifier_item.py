import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath

class TestClassifierItem(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.log = cls.borehole.get_log("Lithology from GR Classification")
        cls.dict = cls.log.classifier_dictionary
        cls.item = cls.dict.classifier_item("sandstone")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.item, "name", 'sandstone')

    def test_color(self):
        # verify that the property is initially set to X, then set it to red
        init_color = 15020032
        self.assertEqual(self.item.color, init_color)
        self.item.color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.item.color, init_color)
        self.item.color = init_color

    def test_low_value(self):
        # verify that the property is initially set to 0, then set it to 10
        self.assertEqual(self.item.low_value, 0)
        self.item.low_value = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.item.low_value, 0)
        self.item.low_value = 0

    def test_high_value(self):
        # verify that the property is initially set to 45, then set it to 35
        self.assertEqual(self.item.high_value, 45)
        self.item.high_value = 35
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.item.high_value, 45)
        self.item.high_value = 45

if __name__ == '__main__':
    unittest.main()
