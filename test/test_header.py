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
            self.header.allow_export_trailer(0, False, "Alt123")


if __name__ == '__main__':
    unittest.main()
