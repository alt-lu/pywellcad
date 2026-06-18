import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestContact(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.litho_log = cls.borehole.get_log("lithology")
        cls.litho_log.attach_contact_dictionary("C:\Program Files\Advanced Logic Technology\WellCAD\Dictionaries\Bedding contacts.ctd")
        cls.dict = cls.litho_log.contact_dictionary
        cls.contact = cls.dict.contact(1)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_code(self):
        self.assertEqual(self.contact.code, "393")

    def test_description(self):
        # verify that the property is initially set to "scoured", then set it to "new descr"
        self.assertEqual(self.contact.description, "scoured")
        self.contact.description = "new descr"
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.description, "scoured")
        self.contact.description = "scoured"

    def test_cross_document(self):
        # verify that the property is initially set to False, then set it to True
        self.assertEqual(self.contact.cross_document, False)
        self.contact.cross_document = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.cross_document, False)
        self.contact.cross_document = False

    def test_scale_factor(self):
        # verify that the property is initially set to 100%, then set it to 150%
        self.assertEqual(self.contact.scale_factor, 1.0)
        self.contact.scale_factor = 1.5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.scale_factor, 1.0)
        self.contact.scale_factor = 1.0

    def test_width(self):
        # verify that the property is initially set to 2 (0.2 mm), then set it to 5 (0.5 mm)
        self.assertEqual(self.contact.width, 2)
        self.contact.width = 5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.width, 2)
        self.contact.width = 2

    def test_style(self):
        # verify that the property is initially set to 5 (small wave line), then set it to 2 (dot line)
        self.assertEqual(self.contact.style, 5)
        self.contact.style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.style, 5)
        self.contact.style = 5

    def test_color(self):
        # verify that the property is initially set to 0 (black), then set it to red
        self.assertEqual(self.contact.color, 0)
        self.contact.color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.contact.color, 0)
        self.contact.color = 0


if __name__ == '__main__':
    unittest.main()
