import unittest
import pathlib

import pywintypes

import wellcad.com
from ._sample_path import SamplePath


class TestHeader(unittest.TestCase, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.header = cls.borehole.header
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.header_name = str(cls.fixture_path / "Default.wch")
        cls.trailer_name = str(cls.fixture_path / "API default.wch")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_nb_of_items(self):
        self.assertGreater(self.header.nb_of_items, 0)

    def test_get_wrong_item_text(self):
        self.assertEqual(self.header.get_item_text("wrong name"), '')

    def test_get_item_text(self):
        self.assertEqual(self.header.get_item_text("COMPANY"), 'Advanced Logic Technology')

    def test_case_get_item_text(self):
        self.assertEqual(self.header.get_item_text("company"), '')

    def test_set_item_text(self):
        self.header.set_item_text("COMPANY", "ALT")

    def test_get_wrong_item_name(self):
        self.assertEqual(self.header.item_name(-1), '')

    def test_get_item_name(self):
        self.assertEqual(self.header.item_name(5), 'email')

    def test_allow_export_header(self):
        self.header.allow_export_header(0, False, "Alt123")

    def test_invalid_allow_export_trailer(self):
        with self.assertRaises(pywintypes.com_error):
            self.header.allow_export_trailer(0, False, "Alt123")  # Doesn't raise an exception

    def test_nb_of_header_forms(self):
        self.assertGreater(self.header.nb_of_header_forms, 0)

    def test_nb_of_trailer_forms(self):
        self.assertGreater(self.header.nb_of_trailer_forms, 0)

    def test_add_header_form(self):
        nb_init = self.header.nb_of_header_forms
        self.header.add_header_form(self.header_name)
        nb_final = self.header.nb_of_header_forms
        self.assertGreater(nb_final, nb_init)

    def test_add_trailer_form(self):
        nb_init = self.header.nb_of_trailer_forms
        self.header.add_trailer_form(self.trailer_name)
        nb_final = self.header.nb_of_trailer_forms
        self.assertGreater(nb_final, nb_init)

    def tests_delete_header_forms(self):
        # delete one header form
        nb_init = self.header.nb_of_header_forms
        self.header.delete_header_form(0)
        self.assertGreater(nb_init, self.header.nb_of_header_forms)

        # delete all header forms
        self.header.add_header_form(self.header_name)
        self.assertGreater(self.header.nb_of_header_forms, 0)
        self.header.delete_all_header_forms()
        self.assertEqual(self.header.nb_of_header_forms, 0)

    def tests_delete_trailer_forms(self):
        # delete one trailer forms
        nb_init = self.header.nb_of_trailer_forms
        self.header.delete_trailer_form(0)
        self.assertGreater(nb_init, self.header.nb_of_trailer_forms)

        # delete all trailer forms
        self.header.add_trailer_form(self.trailer_name)
        self.assertGreater(self.header.nb_of_trailer_forms, 0)
        self.header.delete_all_trailer_forms()
        self.assertEqual(self.header.nb_of_trailer_forms, 0)

if __name__ == '__main__':
    unittest.main()
