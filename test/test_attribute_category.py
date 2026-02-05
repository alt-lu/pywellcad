import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestAttributeCategory(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.structure_log = cls.borehole.get_log("Structure")
        cls.dict = cls.structure_log.get_attribute_dictionary("Type")
        cls.category = cls.dict.attribute_category("0 - Joint")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_code(self):
        self.assertEqual(self.category.code, '0 - Joint')

    def test_description(self):
        # verify that the property is initially set to "Joint", then set it to "new descr"
        self.assertEqual(self.category.description, "Joint")
        self.category.description = "new descr"
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.description, "Joint")
        self.category.description = "Joint"

    def test_body_style(self):
        # verify that the property is initially set to 1 (Circle), then set it to 4 (Triangle)
        self.assertEqual(self.category.body_style, 1)
        self.category.body_style = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.body_style, 1)
        self.category.body_style = 1

    def test_body_size(self):
        # verify that the property is initially set to 0 (Small), then set it to 2 (Big)
        self.assertEqual(self.category.body_size, 0)
        self.category.body_size = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.body_size, 0)
        self.category.body_size = 0

    def test_tail_style(self):
        # verify that the property is initially set to 0 (Straight), then set it to 1 (Wiggle)
        self.assertEqual(self.category.tail_style, 0)
        self.category.tail_style = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.tail_style, 0)
        self.category.tail_style = 0

    def test_tail_size(self):
        # verify that the property is initially set to 3 (Big), then set it to 2 (Medium)
        self.assertEqual(self.category.tail_size, 3)
        self.category.tail_size = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.tail_size, 3)
        self.category.tail_size = 3

    def test_tail_color(self):
        # verify that the property is initially set to black (0), then set it to red
        self.assertEqual(self.category.tail_color, 0)
        self.category.tail_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.tail_color, 0)
        self.category.tail_color = 0

    def test_color(self):
        # verify that the property is initially set to X, then set it to green
        init_color = 16711680
        self.assertEqual(self.category.color, init_color)
        self.category.color = 0x00ff00
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.color, init_color)
        self.category.color = init_color

    def test_sine_style(self):
        # verify that the property is initially set to 0 (line), then set it to 2 (dot)
        self.assertEqual(self.category.sine_style, 0)
        self.category.sine_style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.sine_style, 0)
        self.category.sine_style = 0

    def test_sine_width(self):
        # verify that the property is initially set to 1 (0.1 mm), then set it to 5 (0.5 mm)
        self.assertEqual(self.category.sine_width, 1)
        self.category.sine_width = 5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.category.sine_width, 1)
        self.category.sine_width = 1


if __name__ == '__main__':
    unittest.main()
