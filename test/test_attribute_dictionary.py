import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestAttributeDictionary(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.structure_log = cls.borehole.get_log("Structure")
        cls.attrib_name = cls.structure_log.get_attribute_name(0)
        cls.dict = cls.structure_log.get_attribute_dictionary(cls.attrib_name)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.dict, "name", 'Sort')
        self.assertAttrChange(self.dict, 'name', 'new_name')

    def test_nb_of_categories(self):
        self.assertAttrEqual(self.dict, "nb_of_categories", 4)
        # nb_categ = self.dict.nb_of_categories
        # self.assertEqual(nb_categ, 4)

    def test_is_category_not_present(self):
        self.assertAlmostEqual(self.dict.is_category('Wrong_Name'), False)

    def test_is_category(self):
        self.assertAlmostEqual(self.dict.is_category('3 - Parting'), True)

    def test_attribute_category(self):
        self.assertIsInstance(self.dict.attribute_category(0), wellcad.com.AttributeCategory)
        self.assertIsNotNone(self.dict.attribute_category(0))
        self.assertIsInstance(self.dict.attribute_category('3 - Parting'), wellcad.com.AttributeCategory)
        self.assertIsNotNone(self.dict.attribute_category('3 - Parting'))
        self.assertIsNone(self.dict.attribute_category(self.dict.nb_of_categories))
        self.assertIsNone(self.dict.attribute_category('code_not_present'))

    def test_add_category(self):
        # get the number of categories in the dictionary
        nb_init = self.dict.nb_of_categories

        # add the new category
        new_category = self.dict.add_category()

        # verify that the new category has been created, is a AttributeCategory object and has been added to the dictionary
        self.assertIsNotNone(new_category)
        self.assertIsInstance(new_category, wellcad.com.AttributeCategory)
        self.assertGreater(self.dict.nb_of_categories, nb_init)

        # remove it from the dictionary
        self.dict.remove_category(new_category.code);

    def test_remove_category(self):
        # add a new category
        new_category = self.dict.add_category

        # get the number of categories in the dictionary
        nb_init = self.dict.nb_of_categories

        # remove the newly created category (last position in the dictionary)
        removed = self.dict.remove_category(self.dict.nb_of_categories - 1)
        self.assertEqual(removed, True)
        # verify that the size of the dictionary decreased
        self.assertGreater(nb_init, self.dict.nb_of_categories)

if __name__ == '__main__':
    unittest.main()