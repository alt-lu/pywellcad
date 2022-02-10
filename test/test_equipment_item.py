import unittest
import pywintypes
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestEquipmentItem(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Engineering Log and Borehole Volume.wcl"))
        cls.engineering_log = cls.borehole.get_log("Well Sketch")
        cls.eqp_item = cls.engineering_log.eqp_item(10)
        cls.liquid_eqp_item = cls.engineering_log.eqp_item(16)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_top_bottom(self):
        top = self.eqp_item.top_depth  # 50
        bottom = self.eqp_item.bottom_depth  # 60
        self.assertIsInstance(top, float)
        self.assertIsInstance(bottom, float)
        self.assertGreaterEqual(bottom, top)
        self.assertAttrAlmostChange(self.eqp_item, 'top_depth', top + 5, 3)
        self.assertAttrAlmostChange(self.eqp_item, 'bottom_depth', bottom + 5, 3)

    def test_swapped_top_bottom(self):
        top = self.eqp_item.top_depth  # 50
        bottom = self.eqp_item.bottom_depth  # 60
        self.eqp_item.top_depth = bottom + 10
        self.eqp_item.bottom_depth = top - 10
        self.assertAlmostEqual(self.eqp_item.top_depth, top, 3)  # no change because greater than bottom
        self.assertAlmostEqual(self.eqp_item.bottom_depth, bottom, 3)  # no change because smaller than top

    def test_axis_position(self):
        self.assertAlmostEqual(self.eqp_item.axis_position, 0.0, 3)
        self.assertAttrAlmostChange(self.eqp_item, 'axis_position', 0.2, 3)

    def test_diameter(self):
        inner = self.eqp_item.internal_diameter  # 90
        outer = self.eqp_item.external_diameter  # 100
        self.assertIsInstance(inner, float)
        self.assertIsInstance(outer, float)
        self.assertGreaterEqual(outer, inner)
        self.assertAttrAlmostChange(self.eqp_item, 'internal_diameter', inner + 5, 3)
        self.assertAttrAlmostChange(self.eqp_item, 'external_diameter', outer + 5, 3)

    def test_swapped_diameter(self):
        inner = self.eqp_item.internal_diameter  # 90
        outer = self.eqp_item.external_diameter  # 100
        self.eqp_item.top_depth = outer + 10
        self.eqp_item.bottom_depth = inner - 10
        self.assertAlmostEqual(self.eqp_item.internal_diameter, inner, 3)  # no change because greater than outer
        self.assertAlmostEqual(self.eqp_item.external_diameter, outer, 3)  # no change because smaller than inner

    def test_type(self):
        self.assertAttrEqual(self.eqp_item, "type", 2)

    def test_name(self):
        self.assertAttrEqual(self.eqp_item, "name", "PlainCasing")

    def test_description(self):
        self.assertAttrEqual(self.eqp_item, "description", "Plain casing")

    def test_comment(self):
        self.assertAttrEqual(self.eqp_item, "comment", "")
        self.assertAttrChange(self.eqp_item, "comment", "a fresh comment")

    def test_axis_position_fail_on_non_solid(self):
        with self.assertRaises(pywintypes.com_error):
            self.liquid_eqp_item.axis_position

    def test_int_diameter_fail_on_non_solid(self):
        with self.assertRaises(pywintypes.com_error):
            self.liquid_eqp_item.internal_diameter

    def test_ext_diameter_fail_on_non_solid(self):
        with self.assertRaises(pywintypes.com_error):
            self.liquid_eqp_item.external_diameter

    def test_set_injection_position(self):
        self.assertAttrEqual(self.liquid_eqp_item, 'injection_position', 0.0)
        self.assertAttrAlmostChange(self.liquid_eqp_item, 'injection_position', 0.5, 3)

    def test_set_injection_depth(self):
        self.assertAttrEqual(self.liquid_eqp_item, 'injection_depth', 0.0)  # initial value is 0
        self.assertAttrAlmostChange(self.liquid_eqp_item, 'injection_depth', 70.0, 3)
        self.assertAttrAlmostChange(self.liquid_eqp_item, 'injection_depth', 0.0, 3)  # Cannot set it back to a value outside the range top_depth - bottom_depth

    def test_weight(self):
        self.assertAttrEqual(self.eqp_item, 'weight', -1.0)  # default value is -1 ?
        self.assertAttrAlmostChange(self.eqp_item, 'weight', 0.5, 3)
        
    def test_thickness(self):
        self.assertAttrEqual(self.eqp_item, 'thickness', 5.0)
        self.assertAttrAlmostChange(self.eqp_item, 'thickness', 7.0, 3)

    def test_thickness_and_diameter(self):
        self.assertAttrEqual(self.eqp_item, 'thickness', 5.0)
        self.assertAttrEqual(self.eqp_item, 'external_diameter', 100.0)
        self.assertAttrEqual(self.eqp_item, 'internal_diameter', 90.0)
        self.eqp_item.thickness = 10.0
        self.assertAttrEqual(self.eqp_item, 'thickness', 10.0)
        self.assertAttrEqual(self.eqp_item, 'external_diameter', 100.0)
        self.assertAttrEqual(self.eqp_item, 'internal_diameter', 80.0)
        self.eqp_item.thickness = 5.0
        self.assertAttrEqual(self.eqp_item, 'thickness', 5.0)
        self.assertAttrEqual(self.eqp_item, 'external_diameter', 100.0)
        self.assertAttrEqual(self.eqp_item, 'internal_diameter', 90.0)

    def test_grade(self):
        self.assertAttrEqual(self.eqp_item, 'grade', "")
        self.assertAttrChange(self.eqp_item, 'grade', "good casing")
        


if __name__ == '__main__':
    unittest.main()
