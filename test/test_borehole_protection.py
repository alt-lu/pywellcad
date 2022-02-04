import pathlib
import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestBoreholeProtection(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Casing with cement quality issues.wcl"))
        cls.header = cls.borehole.header

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_allow_insert_log(self):
        nb_of_logs = self.borehole.nb_of_logs
        self.borehole.allow_insert_log(False, "Alt123")
        self.borehole.enable_protection(True, "Alt123")
        self.borehole.insert_new_log(7)
        self.assertAttrEqual(self.borehole, "nb_of_logs", nb_of_logs)
        self.borehole.allow_insert_log(True, "Alt123")
        self.borehole.insert_new_log(7)
        self.assertAttrEqual(self.borehole, "nb_of_logs", nb_of_logs + 1)

    def test_allow_modify_headers_content(self):
        self.borehole.allow_modify_headers_content(False, "Alt123")
        self.borehole.enable_protection(True, "Alt123")
        org_txt = self.header.get_item_text("Main_Title")
        self.header.set_item_text("Main_Title", "Nothing")
        self.assertEqual(org_txt, self.header.get_item_text("Main_Title"))
        self.borehole.allow_modify_headers_content(True, "Alt123")
        self.header.set_item_text("Main_Title", "Nothing")
        self.assertEqual("Nothing", self.header.get_item_text("Main_Title"))

    def test_allow_export_file(self):
        output_path = str(self.fixture_path / "output.jpg")
        self.borehole.allow_export_file(False, "Alt123")
        self.borehole.enable_protection(True, "Alt123")
        self.assertFalse(self.borehole.file_export(output_path), False)
        self.borehole.allow_export_file(False, "Alt123")
        self.assertTrue(self.borehole.file_export(output_path), False)


if __name__ == '__main__':
    unittest.main()
