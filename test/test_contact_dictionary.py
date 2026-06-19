import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestContactDictionary(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.litho_log = cls.borehole.get_log("lithology")
        cls.litho_log.attach_contact_dictionary("C:\Program Files\Advanced Logic Technology\WellCAD\Dictionaries\Bedding contacts.ctd")
        cls.dict = cls.litho_log.contact_dictionary

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.dict, "name", 'Bedding contacts')
        self.assertAttrChange(self.dict, 'name', 'new_name')

    def test_nb_of_contacts(self):
        self.assertAttrEqual(self.dict, "nb_of_contacts", 12)

    def test_contact(self):
        self.assertIsInstance(self.dict.contact(0), wellcad.com.Contact)
        self.assertIsNotNone(self.dict.contact(0))
        self.assertIsInstance(self.dict.contact('394'), wellcad.com.Contact)
        self.assertIsNotNone(self.dict.contact('394'))
        self.assertIsNone(self.dict.contact(self.dict.nb_of_contacts))
        self.assertIsNone(self.dict.contact('code_not_present'))

    def test_add_contact(self):
        # get the number of contacts in the dictionary
        nb_init = self.dict.nb_of_contacts

        # add the new contact
        new_contact = self.dict.add_contact()

        # verify that the new contact has been created, is a Contact object and has been added to the dictionary
        self.assertIsNotNone(new_contact)
        self.assertIsInstance(new_contact, wellcad.com.Contact)
        self.assertGreater(self.dict.nb_of_contacts, nb_init)

        # remove it from the dictionary
        self.dict.remove_contact(self.dict.nb_of_contacts - 1);

    def test_remove_contact(self):
        # add a new contact
        new_contact = self.dict.add_contact

        # get the number of contacts in the dictionary
        nb_init = self.dict.nb_of_contacts

        # remove the newly created contact (last position in the dictionary)
        removed = self.dict.remove_contact(self.dict.nb_of_contacts - 1)
        self.assertEqual(removed, True)
        # verify that the size of the dictionary decreased
        self.assertGreater(nb_init, self.dict.nb_of_contacts)


if __name__ == '__main__':
    unittest.main()