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
        self.assertAttrEqual(self.pattern, "description", 'Sand Color')

    def test_width(self):
        self.assertAlmostEqual(self.pattern.width, 20, 3)

    def test_height(self):
        self.assertAlmostEqual(self.pattern.height, 20, 3)

    def test_repeatable(self):
        self.assertEqual(self.pattern.repeatable, True)


if __name__ == '__main__':
    unittest.main()
