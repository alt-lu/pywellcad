import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLithoPattern(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.litho_log = cls.borehole.get_log("lithology")
        cls.dict = cls.litho_log.litho_dictionary
        cls.pattern = cls.dict.litho_pattern(0)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_code(self):
        self.assertAttrEqual(self.pattern, "code", '#5')

    def test_description(self):
        # verify that the property is initially set to "Sand color", then set it to "new descr"
        self.assertEqual(self.pattern.description, "Sand Color")
        self.pattern.description = "new descr"
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.pattern.description, "Sand Color")
        self.pattern.description = "Sand Color"

    def test_width(self):
        # verify that the property is initially set to +-20, then set it to 10
        init_value = self.pattern.width
        self.assertAlmostEqual(init_value, 20, 3)
        self.pattern.width = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotAlmostEqual(self.pattern.width, 20, 3)
        self.pattern.width = init_value
        self.assertAlmostEqual(self.pattern.width, 20, 3)

    def test_height(self):
        # verify that the property is initially set to +-20, then set it to 10
        init_value = self.pattern.height
        self.assertAlmostEqual(init_value, 20, 3)
        self.pattern.height = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotAlmostEqual(self.pattern.height, 20, 3)
        self.pattern.height = init_value
        self.assertAlmostEqual(self.pattern.height, 20, 3)

    def test_repeatable(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.pattern.repeatable, True)
        self.pattern.repeatable = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.pattern.repeatable, True)
        self.pattern.repeatable = True

    def test_color(self):
        # verify that the property is initially set to X, then set it to red
        init_color = 8454143
        self.assertEqual(self.pattern.color, init_color)
        self.pattern.color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.pattern.color, init_color)
        self.pattern.color = init_color


if __name__ == '__main__':
    unittest.main()
