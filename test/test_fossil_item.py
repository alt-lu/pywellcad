import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestFossilItem(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.borehole = cls.app.new_borehole()
        cls.log = cls.borehole.insert_new_log(16)
        cls.fossil = cls.log.insert_new_fossil_item(10.0, 12.0, 'mycode', 5.0, 1.0, 0.50)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAlmostEqual(self.fossil.top_depth, 10.0, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.fossil.bottom_depth, 12.0, 3)

    def test_symbol_code(self):
        self.assertAttrEqual(self.fossil, "symbol_code", 'mycode')
        self.assertAttrChange(self.fossil, "symbol_code", 'mycode2')

    def test_set_abundance(self):
        self.assertAlmostEqual(self.fossil.abundance, 5.0, 3)
        self.assertAttrAlmostChange(self.fossil, 'abundance', 6.0, 3)

    def test_set_dominance(self):
        self.assertAlmostEqual(self.fossil.dominance, 1.0, 3)
        self.assertAttrAlmostChange(self.fossil, 'dominance', 2.0, 3)

    def test_set_dominance_out_of_bounds(self):
        self.assertAlmostEqual(self.fossil.dominance, 1.0, 3)
        self.fossil.dominance = 3
        self.assertAlmostEqual(self.fossil.dominance, 1.0, 3)


if __name__ == '__main__':
    unittest.main()
