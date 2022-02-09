import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestFont(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.log = cls.borehole.get_log("Description")
        cls.font = cls.log.font

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_name(self):
        self.assertAttrEqual(self.font, "name", "Arial Narrow")
        self.assertAttrChange(self.font, "name", "Calibri")

    def test_size(self):
        self.assertAttrEqual(self.font, "size", -21)
        self.assertAttrChange(self.font, "size", -8)  # actually sets it to -7
        self.assertAttrChange(self.font, "size", 15)  # actually sets it to -20

    def test_weight(self):
        self.assertAttrEqual(self.font, "weight", 400)
        self.assertAttrChange(self.font, "weight", 700)

    def test_italic(self):
        self.assertAttrEqual(self.font, "italic", False)
        self.assertAttrChange(self.font, "italic", True)

    def test_underline(self):
        self.assertAttrEqual(self.font, "underline", False)
        self.assertAttrChange(self.font, "underline", True)

    def test_bold(self):
        self.assertAttrEqual(self.font, "bold", False)
        self.assertAttrChange(self.font, "bold", True)

    def test_strikethrough(self):
        self.assertAttrEqual(self.font, "strikethrough", False)
        self.assertAttrChange(self.font, "strikethrough", True)


    def test_charset(self):
        self.assertAttrEqual(self.font, "charset", 0)
        self.assertAttrChange(self.font, "charset", 1)


if __name__ == '__main__':
    unittest.main()
