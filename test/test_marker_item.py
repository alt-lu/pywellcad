import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestMarkerItem(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.borehole = cls.app.new_borehole()
        cls.log = cls.borehole.insert_new_log(24)
        cls.marker = cls.log.insert_new_marker(10.5, 'myname', 'mycomment', 'mycontact')

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.marker, "name", 'myname')
        self.assertAttrChange(self.marker, "name", 'mynewname')

    def test_comment(self):
        self.assertAttrEqual(self.marker, "comment", 'mycomment')
        self.assertAttrChange(self.marker, "comment", 'mynewcomment')

    def test_contact(self):
        self.assertAttrEqual(self.marker, "contact", 'mycontact')
        self.assertAttrChange(self.marker, "contact", 'mynewcontact')

    def test_depth(self):
        self.assertAlmostEqual(self.marker.depth, 10.5, 3)


if __name__ == '__main__':
    unittest.main()
