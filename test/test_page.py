import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestPage(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.page = cls.borehole.page

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_depth_range(self):
        self.assertAttrEqual(self.page, "depth_range", 0)
        self.assertAttrChange(self.page, "depth_range", 1)
        self.assertAttrNotChanged(self.page, "depth_range", 2)

    def test_nb_of_depth_range(self):
        self.assertEqual(self.page.nb_of_depth_range, 0)
        self.page.add_depth_range(50.0, 80.0)
        self.assertEqual(self.page.nb_of_depth_range, 1)
        self.page.remove_depth_range(0)
        self.assertEqual(self.page.nb_of_depth_range, 0)

    def test_document_height(self):
        self.assertEqual(self.page.document_height, 491)

    def test_document_width(self):
        self.assertAttrEqual(self.page, "document_width", 2826)
        self.assertAttrChange(self.page, "document_width", 200)

    def test_paper_mode(self):
        self.assertAttrEqual(self.page, "paper_mode", 0)
        self.assertAttrChange(self.page, "paper_mode", 1)
        self.assertAttrNotChanged(self.page, "paper_mode", 2)

    def test_print_titles_on_top(self):
        self.assertAttrEqual(self.page, "print_titles_on_top", True)
        self.assertAttrChange(self.page, "print_titles_on_top", False)

    def test_print_titles_on_bottom(self):
        self.assertAttrEqual(self.page, "print_titles_on_bottom", True)
        self.assertAttrChange(self.page, "print_titles_on_bottom", False)

    def test_print_titles_on_top_on_each_page(self):
        self.assertAttrEqual(self.page, "print_titles_on_top_on_each_page", False)
        self.assertAttrChange(self.page, "print_titles_on_top_on_each_page", True)

    def test_print_titles_on_bottom_on_each_page(self):
        self.assertAttrEqual(self.page, "print_titles_on_bottom_on_each_page", False)
        self.assertAttrChange(self.page, "print_titles_on_bottom_on_each_page", True)

    def test_margin(self):
        self.assertAttrEqual(self.page, "top_margin", 5)
        self.assertAttrChange(self.page, "top_margin", 6)
        self.assertAttrEqual(self.page, "bottom_margin", 5)
        self.assertAttrChange(self.page, "bottom_margin", 6)
        self.assertAttrEqual(self.page, "left_margin", 10)
        self.assertAttrChange(self.page, "left_margin", 6)
        self.assertAttrEqual(self.page, "right_margin", 10)
        self.assertAttrChange(self.page, "right_margin", 6)

    def test_numbering(self):
        self.assertAttrEqual(self.page, "numbering", 3)
        self.assertAttrChange(self.page, "numbering", 0)
        self.assertAttrChange(self.page, "numbering", 1)
        self.assertAttrChange(self.page, "numbering", 2)
        self.assertAttrChange(self.page, "numbering", 3)
        self.assertAttrChange(self.page, "numbering", 4)

    def test_numbering_out_of_bounds(self):
        original = self.page.numbering
        self.page.numbering = 5  # out of bounds, should set value to 0 instead
        self.assertEqual(self.page.numbering, 0)
        self.page.numbering = original

    def test_print_header(self):
        self.assertAttrEqual(self.page, "print_header", True)
        self.assertAttrChange(self.page, "print_header", False)

    def test_add_remove_depth_range(self):
        self.page.add_depth_range(50.0, 80.0)
        self.page.add_depth_range(50.0, 80.0)
        self.page.add_depth_range(80.0, 50.0)
        self.page.add_depth_range(50.0, 50.0)
        self.page.remove_depth_range(0)
        self.page.remove_depth_range(0)
        self.page.remove_depth_range(0)
        self.page.remove_depth_range(0)

    def test_remove_non_existing_depth_range(self):
        self.assertEqual(self.page.nb_of_depth_range, 0)
        self.page.remove_depth_range(0)


if __name__ == '__main__':
    unittest.main()
