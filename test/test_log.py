import unittest
import wellcad.com
import random
from datetime import datetime, timezone, timedelta
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLog(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.gr_log = cls.borehole.log("GR")
    
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
    
    def test_do_settings_dlg(self):
        self.assertTrue(self.gr_log.do_settings_dlg())
        self.fail("Settings dialog boxes are not shown, only property bars.")
    
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
        

if __name__ == '__main__':
    unittest.main()