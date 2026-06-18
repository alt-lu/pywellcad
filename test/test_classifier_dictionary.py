import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestClassifierDictionary(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.log = cls.borehole.get_log("Lithology from GR Classification")
        cls.dict = cls.log.classifier_dictionary
        cls.log.classifier_dictionary = cls.dict

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.dict, "name", '(Untitled)')
        self.assertAttrChange(self.dict, 'name', 'wrong_name')

    def test_nb_of_classifiers(self):
        self.assertAttrEqual(self.dict, "nb_of_classifiers", 9)

    def test_classifier_item(self):
        self.assertIsInstance(self.dict.classifier_item(0), wellcad.com.ClassifierItem)
        self.assertIsNotNone(self.dict.classifier_item(0))
        self.assertIsInstance(self.dict.classifier_item('claystone'), wellcad.com.ClassifierItem)
        self.assertIsNotNone(self.dict.classifier_item('claystone'))
        self.assertIsNone(self.dict.classifier_item(self.dict.nb_of_classifiers))
        self.assertIsNone(self.dict.classifier_item('code_not_present'))

    def test_add_classifier(self):
        # get the number of classifiers in the dictionary
        nb_init = self.dict.nb_of_classifiers

        # add the new classifier item
        new_item = self.dict.add_classifier()

        # verify that the new classifier item has been created, is a ClassifierItem object and has been added to the dictionary
        self.assertIsNotNone(new_item)
        self.assertIsInstance(new_item, wellcad.com.ClassifierItem)
        self.assertGreater(self.dict.nb_of_classifiers, nb_init)

        # remove it from the dictionary
        self.dict.remove_classifier(self.dict.nb_of_classifiers - 1);

    def test_remove_classifier(self):
        # add a new classifier item
        new_classifier = self.dict.add_classifier

        # get the number of classifiers in the dictionary
        nb_init = self.dict.nb_of_classifiers

        # remove the newly created classifier (last position in the dictionary)
        removed = self.dict.remove_classifier(self.dict.nb_of_classifiers - 1)
        self.assertEqual(removed, True)
        # verify that the size of the dictionary decreased
        self.assertGreater(nb_init, self.dict.nb_of_classifiers)


if __name__ == '__main__':
    unittest.main()
