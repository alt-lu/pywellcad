import unittest
import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestCommentBox(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.borehole = cls.app.new_borehole()
        cls.log = cls.borehole.insert_new_log(8)
        cls.top_depth = 10.0
        cls.bottom_depth = 15.0
        cls.box = cls.log.insert_new_comment_box(cls.top_depth, cls.bottom_depth, 'mytext')

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_text(self):
        self.box.text = 'mytext'

    def test_get_text(self):
        self.assertAttrEqual(self.box, "text", "mytext")
        self.assertAttrChange(self.box, "text", "myothertext")

    def test_get_top_depth(self):
        self.assertEqual(self.box.top_depth, self.top_depth)

    def test_get_bottom_depth(self):
        self.assertEqual(self.box.bottom_depth, self.bottom_depth)


if __name__ == '__main__':
    unittest.main()
