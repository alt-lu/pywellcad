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

    def test_add_pattern(self):
        # get the initial number of patterns in the dictionary
        nb_init = self.dict.nb_of_patterns

        # add a new pattern to the dictionary
        new_pattern = self.dict.add_pattern()
        # verify that it exists, that it's a LithoPattern object and that it has been added to the dictionary
        self.assertIsNotNone(new_pattern)
        self.assertIsInstance(new_pattern, wellcad.com.LithoPattern)
        self.assertGreater(self.dict.nb_of_patterns, nb_init)

        # remove it from the dictionary
        self.dict.remove_pattern(new_pattern.code)

    def test_remove_pattern(self):
        # add a new pattern
        new_pattern = self.dict.add_pattern()

        # get the initial number of pattern
        nb_init = self.dict.nb_of_patterns
        # remove the newly created pattern
        removed = self.dict.remove_pattern(new_pattern.code)

        # verify that it has been removed, and that the size of the dictionary decreased
        self.assertEqual(removed, True)
        self.assertGreater(nb_init, self.dict.nb_of_patterns)


if __name__ == '__main__':
    unittest.main()
