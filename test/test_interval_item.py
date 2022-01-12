import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts


class TestIntervalItem(unittest.TestCase, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.borehole = cls.app.new_borehole()
        cls.log = cls.borehole.insert_new_log(13)
        cls.item = cls.log.insert_new_interval_item(10.0, 12.0, 25.2)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_depth(self):
        self.assertAlmostEqual(self.item.top_depth, 10.0, 3)

    def test_bottom_depth(self):
        self.assertAlmostEqual(self.item.bottom_depth, 12.0, 3)

    def test_set_value(self):
        self.assertAlmostEqual(self.item.value, 25.2, 3)
        self.assertAttrAlmostChange(self.item, 'value', 30.4, 3)


if __name__ == '__main__':
    unittest.main()
