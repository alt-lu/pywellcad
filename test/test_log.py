import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from datetime import datetime, timezone, timedelta
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLog(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"

        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.gr_log = cls.borehole.log("GR")
        cls.sonic_e1_mud_log = cls.borehole.log("Sonic - E1 - Mud")
        cls.gr_litho_interval_log = cls.borehole.log("Lithology from GR Classification")
        cls.ole_log = cls.borehole.insert_new_log(22)
        cls.polar_and_rose_log = cls.borehole.insert_new_log(20)

        cls.geotech_borehole = cls.app.open_borehole(str(cls.sample_path / "Geotech Plot.WCL"))
        cls.depth_log = cls.geotech_borehole.log("Elev.")

        cls.volume_analysis_borehole = cls.app.open_borehole(str(cls.sample_path / "Volume Analysis.wcl"))
        cls.formula_log = cls.volume_analysis_borehole.log("GR percent")

        cls.fmi_borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.structure_log = cls.fmi_borehole.log("Structure")

        cls.breakout_borehole = cls.app.open_borehole(str(cls.fixture_path / "Breakout Picking.WCL"))
        cls.breakout_log = cls.breakout_borehole.log("Breakouts")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_file_export_to_csv(self):
        self.assertTrue(self.gr_log.file_export(r"C:\Temp", "Test Export", "csv"))

    def test_nb_of_data(self):
        number = self.gr_log.nb_of_data
        self.assertGreater(number, 0)
        self.assertIsInstance(number, int)
        self.assertAttrChangeRaises(self.gr_log, "nb_of_data", 0)

    def test_name(self):
        self.assertAttrEqual(self.gr_log, "name", "GR")
        self.assertAttrChange(self.gr_log, "name", "GRA")

    def test_title_comment(self):
        self.assertAttrEqual(self.gr_log, "title_comment", "")
        self.assertAttrChange(self.gr_log, "title_comment", "This is a gamma log")

    def test_depths(self):
        top_depth = self.gr_log.top_depth
        bottom_depth = self.gr_log.bottom_depth
        self.assertIsInstance(top_depth, float)
        self.assertIsInstance(bottom_depth, float)
        self.assertGreaterEqual(bottom_depth, top_depth)
        self.assertAttrChangeRaises(self.gr_log, "top_depth", 0)
        self.assertAttrChangeRaises(self.gr_log, "bottom_depth", 0)

    def test_data_table(self):
        original_data = self.gr_log.data_table
        self.assertIsInstance(original_data, tuple)
        new_data = tuple([original_data[0]] + [(row[0], random.random() * 200.0) for row in original_data[1:]])
        self.gr_log.data_table = new_data
        for a, b in zip(self.gr_log.data_table[1:], new_data[1:]):
            self.assertEqual(a[0], b[0])
            # Test we're equal to 7 significant figures (WellCAD uses 32 bit floats, so that's the best we can expect)
            self.assertAlmostEqual(a[1] / b[1], 1.0, delta=1e-7)
        self.gr_log.data_table = original_data

    def test_data_extents(self):
        maximum = self.gr_log.data_max
        minimum = self.gr_log.data_min
        self.assertIsInstance(maximum, float)
        self.assertIsInstance(minimum, float)
        self.assertGreaterEqual(maximum, minimum)
        self.assertAttrChangeRaises(self.gr_log, "data_max", 10.0)
        self.assertAttrChangeRaises(self.gr_log, "data_min", 0.0)

    def test_log_unit(self):
        self.assertAttrEqual(self.gr_log, "log_unit", "API")
        self.assertAttrChange(self.gr_log, "log_unit", "cps")
        self.assertAttrChangeRaises(self.gr_log, "log_unit", 25)

    def test_position(self):
        left = self.gr_log.left_position
        right = self.gr_log.right_position
        self.assertIsInstance(left, float)
        self.assertIsInstance(right, float)
        self.assertGreaterEqual(right, left)
        new_left = left + 0.1
        new_right = right + 0.15
        self.gr_log.set_position(new_left, new_right)
        self.assertAlmostEqual(new_left, self.gr_log.left_position)
        self.assertAlmostEqual(new_right, self.gr_log.right_position)
        self.gr_log.left_position = left
        self.gr_log.right_position = right
        self.assertEqual(left, self.gr_log.left_position)
        self.assertEqual(right, self.gr_log.right_position)

    def test_swapped_position(self):
        left = self.gr_log.left_position
        right = self.gr_log.right_position

        # Check that positions are swapped if we set left greater than
        # right
        self.gr_log.set_position(0.5, 0.2)
        self.assertAlmostEqual(self.gr_log.left_position, 0.2)
        self.assertAlmostEqual(self.gr_log.right_position, 0.5)

        self.gr_log.set_position(left, right)

    def test_confusing_swap(self):
        left = self.gr_log.left_position
        right = self.gr_log.right_position

        # This is very confusing behaviour
        self.gr_log.left_position = 0.5
        self.gr_log.right_position = 0.7
        self.assertAlmostEqual(self.gr_log.left_position, 0.5)
        self.assertAlmostEqual(self.gr_log.right_position, 0.7)

        self.gr_log.left_position = left
        self.gr_log.right_position = right

    def test_out_of_bounds_position(self):
        left = self.gr_log.left_position
        right = self.gr_log.right_position

        # Make sure we can't set positions outside 0.0 to 1.0. Behaviour
        # here is to clamp
        self.gr_log.left_position = -0.1
        self.assertEqual(self.gr_log.left_position, 0.0)
        self.gr_log.right_position = 1.1
        self.assertEqual(self.gr_log.right_position, 1.0)

        self.gr_log.set_position(left, right)

    def test_type(self):
        self.assertAttrEqual(self.gr_log, "type", 1)
        self.assertAttrChangeRaises(self.gr_log, "type", 2)

    def test_hide_log_title(self):
        self.assertAttrEqual(self.gr_log, "hide_log_title", False)
        self.assertAttrChange(self.gr_log, "hide_log_title", True)

    def test_hide_log_data(self):
        self.assertAttrEqual(self.gr_log, "hide_log_data", False)
        self.assertAttrChange(self.gr_log, "hide_log_data", True)

    def test_log_background_color(self):
        self.assertAttrEqual(self.gr_log, "log_background_color", 0xffffff)
        self.assertAttrChange(self.gr_log, "log_background_color", 0x0000ff)

    def test_border_style(self):
        self.assertAttrEqual(self.gr_log, "border_style", 0)
        self.assertAttrChange(self.gr_log, "border_style", 1)
        self.assertAttrNotChanged(self.gr_log, "border_style", 5)

    def test_border_color(self):
        self.assertAttrEqual(self.gr_log, "border_color", 0x000000)
        self.assertAttrChange(self.gr_log, "border_color", 0x0000ff)
        self.assertAttrNotChanged(self.gr_log, "border_color", -1)

    def test_display_border(self):
        self.assertAttrEqual(self.gr_log, "display_border", True)
        self.assertAttrChange(self.gr_log, "display_border", False)

    def test_history(self):
        # Make a change of some sort.
        self.assertAttrChange(self.gr_log, "name", "GRA")
        now = datetime.now(timezone.utc)
        change_count = self.gr_log.nb_of_history_item
        self.assertGreater(change_count, 0)
        change_date = self.gr_log.history_item_date(change_count - 1)
        self.assertAlmostEqual(now, change_date, delta=timedelta(seconds=1))
        change_description = self.gr_log.history_item_description(change_count - 1)
        self.assertEqual(change_description, "'GRA' has been renamed as 'GR'")
        self.gr_log.clear_history()
        self.assertEqual(self.gr_log.nb_of_history_item, 0)
        self.assertAttrChangeRaises(self.gr_log, "nb_of_history_item", 0)

    def test_null_value(self):
        self.assertAttrEqual(self.gr_log, "null_value", -999)
        self.assertAttrChange(self.gr_log, "null_value", -999.25)

    def test_mask_contacts(self):
        self.assertAttrEqual(self.gr_log, "mask_contacts", False)
        self.assertAttrChange(self.gr_log, "mask_contacts", True)

    def test_mask_horizontal_grid(self):
        self.assertAttrEqual(self.gr_log, "mask_horizontal_grid", True)
        self.assertAttrChange(self.gr_log, "mask_horizontal_grid", False)

    def test_sample_rate(self):
        self.assertAlmostEqual(self.gr_log.sample_rate, 0.05)
        top = self.gr_log.top_depth
        bottom = self.gr_log.bottom_depth
        self.gr_log.sample_rate = 0.1
        self.assertEqual(bottom, self.gr_log.bottom_depth)
        self.assertAlmostEqual(bottom + (top - bottom) * 2, self.gr_log.top_depth)
        self.gr_log.sample_rate = 0.05

    def test_scale_low(self):
        self.assertAttrEqual(self.gr_log, "scale_low", 0.0)
        self.assertAttrChange(self.gr_log, "scale_low", 2.0)

    def test_scale_high(self):
        self.assertAttrEqual(self.gr_log, "scale_high", 200.0)
        self.assertAttrChange(self.gr_log, "scale_high", 100.0)

    def test_scale_mode(self):
        self.assertAttrEqual(self.gr_log, "scale_mode", 0)
        self.assertAttrChange(self.gr_log, "scale_mode", 1)
        self.assertAttrNotChanged(self.gr_log, "scale_mode", 2)

    def test_scale_reversed(self):
        self.assertAttrEqual(self.gr_log, "scale_reversed", True)
        self.assertAttrChange(self.gr_log, "scale_reversed", False)
        self.assertAttrChangeRaises(self.gr_log, "scale_reversed", "Test")

    def test_use_log_colored_background(self):
        self.assertAttrEqual(self.gr_log, "use_log_colored_background", False)
        self.assertAttrChange(self.gr_log, "use_log_colored_background", True)

    def test_grid_enable(self):
        self.assertAttrEqual(self.gr_log, "maj_grid_enable", False)
        self.assertAttrChange(self.gr_log, "maj_grid_enable", True)
        self.assertAttrEqual(self.gr_log, "min_grid_enable", False)
        self.assertAttrChange(self.gr_log, "min_grid_enable", True)

    def test_grid_spacing(self):
        self.assertAttrEqual(self.gr_log, "maj_grid_spacing", 40.0)
        self.assertAttrChange(self.gr_log, "maj_grid_spacing", 30.0)
        self.assertAttrEqual(self.gr_log, "min_grid_spacing", 0.0)
        self.assertAttrChange(self.gr_log, "min_grid_spacing", 10.0)

        # Make sure we can't set min grid spacing larger than maj and vice
        # versa. The behaviour here is one of clamping.
        self.gr_log.min_grid_spacing = 50.0
        self.assertEqual(self.gr_log.min_grid_spacing, 40.0)
        self.gr_log.maj_grid_spacing = 30.0
        self.assertEqual(self.gr_log.maj_grid_spacing, 40.0)
        self.gr_log.min_grid_spacing = 0.0

    def test_lock_log_data(self):
        self.assertFalse(self.gr_log.lock_log_data)
        self.gr_log.lock_log_data = True
        self.assertTrue(self.gr_log.lock_log_data)
        original_data = self.gr_log.data_table
        new_data = tuple([original_data[0]] + [(row[0], random.random() * 200.0) for row in original_data[1:]])
        self.gr_log.data_table = new_data
        self.assertEqual(self.gr_log.data_table, original_data)
        self.gr_log.lock_log_data = False
    
    def test_data(self):
        self.assertEqual(self.gr_log.data(0), 97.86750030517578)
        self.assertEqual(self.gr_log.data(-1), self.gr_log.null_value)
    
    def test_data_at_depth(self):
        self.assertEqual(self.gr_log.data_at_depth(88.0), 97.86750030517578)
        self.assertEqual(self.gr_log.data_at_depth(90.0), self.gr_log.null_value)
        self.assertEqual(self.gr_log.data_at_depth(87.0), 98.1874008178711)
    
    def test_data_depth(self):
        self.assertEqual(self.gr_log.data_depth(0), 88.0)
        self.assertIsNone(self.gr_log.data_depth(-1), "What is the behaviour of data_depth() with out-of-bound indices?")
    
    def test_insert_remove_data(self):
        self.gr_log.insert_data(0, 10.0)
        self.assertEqual(self.gr_log.data(0), 10.0)
        self.gr_log.remove_data(0)
        self.assertEqual(self.gr_log.data(0), 97.86750030517578)
    
    def test_insert_oob_data(self):
        with self.assertRaises(pywintypes.com_error):
            self.gr_log.insert_data(-1, 11.0)
    
    def test_insert_remove_data_at_depth(self):
        original = self.gr_log.data_at_depth(87.05)
        self.gr_log.insert_data_at_depth(87.05, 11.0)
        self.assertAlmostEqual(self.gr_log.data_at_depth(87.05), 11.0)
        self.gr_log.remove_data_at_depth(87.05)
        self.assertAlmostEqual(self.gr_log.data_at_depth(87.05), original)
    
    def test_insert_data_at_depth_documentation(self):
        self.fail("It isn't clear which direction data gets pushed when a new data point is inserted.")
    
    def test_remove_data_at_depth_documentation(self):
        self.fail("Behaviour isn't the same as in documentation. remove_data_at_depth() in a Well Log actually removes it, it doesn't just set it to NULL")
    
    def test_insert_data_between_samples(self):
        original = self.gr_log.data_at_depth(87.05)
        self.gr_log.insert_data_at_depth(87.06, 12.0)
        self.assertNotAlmostEqual(self.gr_log.data_at_depth(87.06), 12.0, msg="No data should have been inserted (off sample spacing).")
        self.assertAlmostEqual(self.gr_log.data_at_depth(87.05), original)
    
    def test_setting_data(self):
        self.fail("There are no methods for setting data by index or depth.")

    def test_formula(self):
        self.assertAttrEqual(self.formula_log, "formula", "{GR}/100")
        self.assertAttrChange(self.formula_log, "formula", "{GR}/1000")
        self.assertAttrNotChanged(self.formula_log, "formula", "InvalidFormula")
    
    def test_filter(self):
        self.assertAttrEqual(self.gr_log, "filter", 0)
        self.assertAttrChange(self.gr_log, "filter", 2)
        self.assertAttrNotChanged(self.gr_log, "filter", -1)
    
    def test_fixed_bar_width(self):
        self.assertAttrEqual(self.sonic_e1_mud_log, "fixed_bar_width", 15)
        self.assertAttrChange(self.sonic_e1_mud_log, "fixed_bar_width", 10)
        self.assertAttrNotChanged(self.sonic_e1_mud_log, "fixed_bar_width", -1)
    
    def test_new_interval_item_at_depth(self):
        item = self.gr_litho_interval_log.insert_new_interval_item(20.0, 22.0, 78.8)
        self.assertIsInstance(item, wellcad.com.IntervalItem)
        query = self.gr_litho_interval_log.interval_item_at_depth(21.0)
        self.assertIsNotNone(query)
        self.gr_litho_interval_log.remove_interval_item_at_depth(21.0)
    
    def test_insert_interval_item_remove_by_depth(self):
        item = self.gr_litho_interval_log.insert_new_interval_item(80.0, 82.0, 23.0)
        self.assertIsInstance(item, wellcad.com.IntervalItem)
        self.gr_litho_interval_log.remove_interval_item_at_depth(81.0)
        item = self.gr_litho_interval_log.interval_item_at_depth(81.0)
        self.assertNotAlmostEqual(item.value, 23.0)
    
    def test_insert_interval_item_remove_by_index(self):
        item = self.gr_litho_interval_log.insert_new_interval_item(20.0, 22.0, 78.8)
        self.assertIsInstance(item, wellcad.com.IntervalItem)
        self.gr_litho_interval_log.remove_interval_item(0)
        self.assertIsNone(self.gr_litho_interval_log.interval_item_at_depth(21.0))

    def test_interval_item(self):
        item = self.gr_litho_interval_log.interval_item(1)
        self.assertIsInstance(item, wellcad.com.IntervalItem)
        self.assertAlmostEqual(item.value, 72.5)
        item = self.gr_litho_interval_log.interval_item(-1)
        self.assertIsNone(item)
    
    def test_interval_item_at_depth(self):
        item = self.gr_litho_interval_log.interval_item_at_depth(90.0)
        self.assertIsNone(item)
        item = self.gr_litho_interval_log.interval_item_at_depth(84.0)
        self.assertAlmostEqual(item.value, 95.0)
    
    def test_pen_color(self):
        self.assertAttrEqual(self.gr_log, "pen_color", 0x00ffffff)
        self.assertAttrChange(self.gr_log, "pen_color", 0x00ff0000)
        self.assertAttrNotChanged(self.gr_log, "pen_color", -10)
    
    def test_pen_style(self):
        self.assertAttrEqual(self.gr_log, "pen_style", 0)
        self.assertAttrChange(self.gr_log, "pen_style", 1)
        self.assertAttrNotChanged(self.gr_log, "pen_style", 5)
    
    def test_pen_width(self):
        self.assertAttrEqual(self.gr_log, "pen_width", 3)
        self.assertAttrChange(self.gr_log, "pen_width", 5)
        self.assertAttrNotChanged(self.gr_log, "pen_width", -1)
    
    def test_shading(self):
        self.assertAttrEqual(self.gr_log, "shading", 1)
        self.assertAttrChange(self.gr_log, "shading", 0)
        self.assertAttrNotChanged(self.gr_log, "shading", 3)
    
    def test_style_mud_log(self):
        self.assertAttrEqual(self.sonic_e1_mud_log, "style", 1)
        self.assertAttrChange(self.sonic_e1_mud_log, "style", 3)
        self.assertAttrNotChanged(self.sonic_e1_mud_log, "style", 0)
    
    def test_insert_new_ole_box_from_file(self):
        self.ole_log.insert_new_ole_box_from_file(str(pathlib.Path(__file__).parent / "fixtures" / "test_img.jpg"),
                                                  True, 0, 10)

    def test_used_as_depth_scale(self):
        self.assertAttrEqual(self.depth_log, "used_as_depth_scale", False)
        self.assertAttrChange(self.depth_log, "used_as_depth_scale", True)

    def test_insert_and_remove_new_schmit_box(self):
        box = self.polar_and_rose_log.insert_new_schmit_box(10.5, 22.5, "No comment")
        self.assertAttrEqual(self.polar_and_rose_log, "nb_of_data", 1)
        self.assertIsInstance(box, wellcad.com.PolarAndRoseBox)
        self.polar_and_rose_log.remove_schmit_box(0)
        self.assertAttrEqual(self.polar_and_rose_log, "nb_of_data", 0)

    def test_schmit_box_at_depth(self):
        self.polar_and_rose_log.insert_new_schmit_box(10.5, 22.5, "No comment")
        box = self.polar_and_rose_log.schmit_box_at_depth(15)
        self.assertIsInstance(box, wellcad.com.PolarAndRoseBox)
        self.polar_and_rose_log.remove_schmit_box_at_depth(15)
        self.assertAttrEqual(self.polar_and_rose_log, "nb_of_data", 0)

    def test_schmit_box(self):
        self.polar_and_rose_log.insert_new_schmit_box(10.5, 22.5, "No comment")
        box = self.polar_and_rose_log.schmit_box(0)
        self.assertIsInstance(box, wellcad.com.PolarAndRoseBox)
        self.polar_and_rose_log.remove_schmit_box(0)

    def test_non_existing_schmit_box_at_depth(self):  # inconsistent with schmit_box(index)
        self.assertAttrEqual(self.polar_and_rose_log, "nb_of_data", 0)
        box = self.polar_and_rose_log.schmit_box_at_depth(15)
        self.assertIsNone(box)

    def test_inconsistent_behaviour_remove_schmit_box(self):  # same thing applies to schmit_box_at_depth and schmit_box
        self.assertAttrEqual(self.polar_and_rose_log, "nb_of_data", 0)
        self.polar_and_rose_log.remove_schmit_box_at_depth(0)  # success
        self.polar_and_rose_log.remove_schmit_box(0)  # fail

    def test_aperture_unit(self):
        self.assertAlmostEqual(self.structure_log.aperture_unit, 0.00254, 3)
        self.assertAttrAlmostChange(self.structure_log, "aperture_unit", 0.001, 3)

    def test_caliper_unit(self):
        self.assertAlmostEqual(self.structure_log.caliper_unit, 0.001, 3)
        self.assertAttrAlmostChange(self.structure_log, "caliper_unit", 0.0254, 3)

    def test_length_unit(self):
        self.assertAlmostEqual(self.breakout_log.length_unit, 0.001, 3)
        self.assertAttrAlmostChange(self.breakout_log, "length_unit", 0.0254, 3)

    def test_attribute_name(self):
        self.assertEqual(self.structure_log.get_attribute_name(0), "Type")
        self.structure_log.set_attribute_name(0, "new_name")
        self.assertEqual(self.structure_log.get_attribute_name(0), "new_name")
        self.structure_log.set_attribute_name(0, "Type")

    def test_insert_new_attribute(self):
        with self.assertRaises(pywintypes.com_error):
            self.structure_log.get_attribute_name(1)
        self.structure_log.insert_new_attribute("my_new_attribute")
        self.assertEqual(self.structure_log.get_attribute_name(1), "my_new_attribute")

    def test_attach_attribute_dictionary(self):
        attribute_dictionary = str(self.fixture_path / "DefaultStructure.tad")
        self.structure_log.attach_attribute_dictionary("new_attribute", attribute_dictionary)

    def test_insert_delete_structure(self):
        self.structure_log.insert_new_structure_ex(depth=10.0, azimuth=20.0, dip=3.0, aperture=0.0)
        self.structure_log.insert_new_structure_ex(depth=15.0, azimuth=50.0, dip=1.0, aperture=0.0)
        struct1 = self.structure_log.structure(0)
        struct2 = self.structure_log.structure_at_depth(15.0)
        self.assertAttrEqual(struct1, "azimuth", 20.0)
        self.assertAttrEqual(struct2, "azimuth", 50.0)
        self.structure_log.remove_structure(0)
        self.structure_log.remove_structure_at_depth(15.0)

    def test_insert_delete_breakout(self):
        self.breakout_log.insert_new_breakout_ex(depth=10.0, azimuth=20.0, tilt=3.0, length=1.0, opening=5.0)
        self.breakout_log.insert_new_breakout_ex(depth=15.0, azimuth=50.0, tilt=3.0, length=1.0, opening=5.0)
        breakout1 = self.breakout_log.breakout(0)
        breakout2 = self.breakout_log.breakout_at_depth(15.0)
        self.assertAttrEqual(breakout1, "azimuth", 20.0)
        self.assertAttrEqual(breakout2, "azimuth", 50.0)  #TODO fails, breakout_at_depth does not work as intended
        self.breakout_log.remove_breakout(0)
        self.breakout_log.remove_breakout_at_depth(15.0)


if __name__ == '__main__':
    unittest.main()
