import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLithoDictionary(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.litho_log = cls.borehole.get_log("lithology")
        cls.dict = cls.litho_log.litho_dictionary

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.dict, "name", 'lithology dominant')
        self.assertAttrChange(self.dict, 'name', 'my_new_name')

    def test_nb_of_patterns(self):
        self.assertAttrEqual(self.dict, "nb_of_patterns", 6)

    def test_is_pattern_not_present(self):
        self.assertAlmostEqual(self.dict.is_pattern('myself'), False)

    def test_is_pattern(self):
        self.assertAlmostEqual(self.dict.is_pattern('#5'), True)

    def test_litho_pattern(self):
        self.assertIsInstance(self.dict.litho_pattern(0), wellcad.com.LithoPattern)
        self.assertIsNotNone(self.dict.litho_pattern(0))
        self.assertIsInstance(self.dict.litho_pattern('#5'), wellcad.com.LithoPattern)
        self.assertIsNotNone(self.dict.litho_pattern('#5'))
        self.assertIsNone(self.dict.litho_pattern(self.dict.nb_of_patterns))
        self.assertIsNone(self.dict.litho_pattern('code_not_present'))


if __name__ == '__main__':
    unittest.main()
