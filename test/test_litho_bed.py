import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLithoBed(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Engineering Log and Borehole Volume.wcl"))
        cls.litho_log = cls.borehole.log("Lithology")
        cls.bed = cls.litho_log.get_litho_bed(60)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_litho_code(self):
        self.assertAttrEqual(self.bed, "litho_code", 'tst')
        self.assertAttrChange(self.bed, "litho_code", 'mylithocode')

    def test_top_contact(self):
        self.assertAttrEqual(self.bed, "top_contact", '')
        self.assertAttrChange(self.bed, "top_contact", 'mytopcontactcode')

    def test_bottom_contact(self):
        self.assertAttrEqual(self.bed, "bottom_contact", '')
        self.assertAttrChange(self.bed, "bottom_contact", 'mybottomcontactcode')

    def test_hardness(self):
        self.assertAlmostEqual(self.bed.value, 0.75, 3)
        self.assertAttrAlmostChange(self.bed, "value", 0.3, 3)

    def test_hardness_out_of_bounds(self):
        self.assertAlmostEqual(self.bed.value, 0.75, 3)
        self.bed.value = 1.2
        self.assertAlmostEqual(self.bed.value, 1.0, 3)
        self.bed.value = 0.75

    def test_top_depth(self):
        self.assertAlmostEqual(self.bed.top_depth, 49.2, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.bed.bottom_depth, 49.5, 3)


if __name__ == '__main__':
    unittest.main()
