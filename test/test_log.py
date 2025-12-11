import pathlib
import unittest
import pywintypes
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
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"

        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.gr_log = cls.borehole.get_log("GR")
        cls.sonic_e1_mud_log = cls.borehole.get_log("Sonic - E1 - Mud")
        cls.gr_litho_interval_log = cls.borehole.get_log("Lithology from GR Classification")
        cls.ole_log = cls.borehole.insert_new_log(22)
        cls.polar_and_rose_log = cls.borehole.insert_new_log(20)
        cls.comment_log = cls.borehole.get_log("Description")
        cls.fws_log = cls.borehole.get_log("Sonic")

        cls.geotech_borehole = cls.app.open_borehole(str(cls.sample_path / "Geotech Plot.WCL"))
        cls.depth_log = cls.geotech_borehole.get_log("Elev.")
        cls.marker_log = cls.geotech_borehole.get_log("Sample No.")

        cls.engineering_borehole = cls.app.open_borehole(
            str(cls.sample_path / "Engineering Log and Borehole Volume.wcl"))
        cls.engineering_log = cls.engineering_borehole.get_log("Well Sketch")

        cls.volume_analysis_borehole = cls.app.open_borehole(str(cls.sample_path / "Volume Analysis.wcl"))
        cls.formula_log = cls.volume_analysis_borehole.get_log("GR percent")
        cls.analysis_log = cls.volume_analysis_borehole.get_log("Volume")
        cls.shading_log = cls.volume_analysis_borehole.get_log("#1")

        cls.fmi_borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.structure_log = cls.fmi_borehole.get_log("Structure")
        cls.structure_true_log = cls.fmi_borehole.get_log("True Dip")
        cls.image_log = cls.fmi_borehole.get_log("FMI Image")
        cls.log_3d = cls.fmi_borehole.get_log("FMI")
        cls.caliper_log = cls.fmi_borehole.get_log("C1")
        cls.fmi_mean = cls.fmi_borehole.get_log("FMI Mean")

        cls.breakout_borehole = cls.app.open_borehole(str(cls.fixture_path / "Breakout Picking.WCL"))
        cls.breakout_log = cls.breakout_borehole.get_log("Breakouts")

        cls.lineation_borehole = cls.app.open_borehole(str(cls.fixture_path / "Lineation Example.WCL"))
        cls.lineation_log = cls.lineation_borehole.get_log("Lineations")
        cls.rgb_log = cls.lineation_borehole.get_log("OPTV (High side)")
        cls.log_3d_lin = cls.lineation_borehole.get_log("3D Log")

        cls.litho_borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.core_desc_log = cls.litho_borehole.get_log("Bio qualifier")
        cls.strata_log = cls.litho_borehole.get_log("Depo")
        cls.stacking_pattern_log = cls.litho_borehole.get_log("Stacking")
        cls.litho_log = cls.litho_borehole.get_log("lithology")
        cls.litho_sed_log = cls.litho_borehole.get_log("sedimentary structure")
        cls.litho_dict = str(cls.fixture_path / "litho_dict.LTH")
        cls.contact_dict = str(cls.fixture_path / "Bedding contacts.ctd")

        cls.corrosion_borehole = cls.app.open_borehole(str(cls.sample_path / "ABI 43 Corrosion Plot.wcl"))
        cls.cross_section_log = cls.corrosion_borehole.get_log("Cross Section")

        cls.nmr_borehole = cls.app.open_borehole(str(cls.sample_path / "NMR Demo.WCL"))
        cls.percentage_log = cls.nmr_borehole.get_log("Fluid Volumes")

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

    def test_left_position_greater_than_right(self):
        left = self.gr_log.left_position
        right = self.gr_log.right_position

        self.gr_log.left_position = 0.5
        self.assertAlmostEqual(self.gr_log.left_position, right)
        self.assertAlmostEqual(self.gr_log.right_position, 0.5)

        self.gr_log.set_position(left, right)

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
        self.assertAttrNotChanged(self.gr_log, "log_background_color", -10)

    def test_border_style(self):
        self.assertAttrEqual(self.gr_log, "border_style", 0)
        self.assertAttrChange(self.gr_log, "border_style", 1)
        self.assertAttrNotChanged(self.gr_log, "border_style", 5)

    def test_border_width(self):
        self.assertAttrEqual(self.gr_log, "border_width", 1)
        self.assertAttrChange(self.gr_log, "border_width", 2)
        self.assertAttrNotChanged(self.gr_log, "border_width", -1)

    def test_border_color(self):
        self.assertAttrEqual(self.gr_log, "border_color", 0x000000)
        self.assertAttrChange(self.gr_log, "border_color", 0x0000ff)
        self.assertAttrNotChanged(self.gr_log, "border_color", -10)

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
        self.assertEqual(change_description, "'GRA' has been renamed as 'GR'.")
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
        self.assertEqual(self.gr_log.data_table, original_data)  # Fails, LockLogData does not work
        self.gr_log.lock_log_data = False

    def test_data(self):
        self.assertEqual(self.gr_log.get_data(0), 97.86750030517578)
        self.gr_log.set_data(0, 100.0)
        self.assertEqual(self.gr_log.get_data(0), 100.0)
        self.gr_log.set_data(0, 97.86750030517578)
        self.assertEqual(self.gr_log.get_data(0), 97.86750030517578)
        self.assertEqual(self.gr_log.get_data(-1), self.gr_log.null_value)

    def test_data_at_depth(self):
        self.assertEqual(self.gr_log.get_data_at_depth(88.0), 97.86750030517578)
        self.assertEqual(self.gr_log.get_data_at_depth(87.0), 98.1874008178711)
        self.gr_log.set_data_at_depth(88.0, 100.0)
        self.assertEqual(self.gr_log.get_data_at_depth(88.0), 100.0)
        self.gr_log.set_data_at_depth(88.0, 97.86750030517578)
        self.assertEqual(self.gr_log.get_data_at_depth(88.0), 97.86750030517578)
        self.assertEqual(self.gr_log.get_data_at_depth(90.0), self.gr_log.null_value)

    def test_data_depth(self):
        self.assertEqual(self.gr_log.data_depth(0), 88.0)
    
    def test_insert_remove_data(self):
        self.gr_log.insert_data(0, 10.0)
        self.assertEqual(self.gr_log.get_data(0), 10.0)
        self.gr_log.remove_data(0)
        self.assertEqual(self.gr_log.get_data(0), 97.86750030517578)

    def test_insert_oob_data(self):
        with self.assertRaises(pywintypes.com_error):
            self.gr_log.insert_data(-1, 11.0)

    def test_insert_remove_data_at_depth(self):
        original = self.gr_log.get_data_at_depth(87.05)
        self.gr_log.insert_data_at_depth(87.05, 11.0)
        self.assertAlmostEqual(self.gr_log.get_data_at_depth(87.05), 11.0)
        self.gr_log.remove_data_at_depth(87.05)
        self.assertAlmostEqual(self.gr_log.get_data_at_depth(87.05), original)

    def test_insert_data_between_samples(self):
        self.gr_log.insert_data_at_depth(87.06, 12.0)
        self.assertAlmostEqual(self.gr_log.get_data_at_depth(87.05), 12.0)
        self.gr_log.remove_data_at_depth(87.05)

    def test_formula(self):
        self.assertAttrEqual(self.formula_log, "formula", "{GR}/100")
        self.assertAttrChange(self.formula_log, "formula", "{GR}/1000")
        self.assertAttrChangeRaises(self.formula_log, "formula", "InvalidFormula", pywintypes.com_error)

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
        self.assertAttrNotChanged(self.gr_log, "shading", 4)

    def test_style_mud_log(self):
        self.assertAttrEqual(self.sonic_e1_mud_log, "style", 1)
        self.assertAttrChange(self.sonic_e1_mud_log, "style", 3)
        self.assertAttrNotChanged(self.sonic_e1_mud_log, "style", 0)

    def test_litho_dictionary(self):
        # Copy the original litho log.
        copied_litho_log = self.litho_borehole.add_log(self.litho_log)

        # Make sure we can get a litho dictionary.
        self.assertIsInstance(self.litho_log.litho_dictionary, wellcad.com.LithoDictionary)

        # Update the litho dictionary.
        new_dict = self.litho_log.attach_litho_dictionary(self.litho_dict)
        self.assertIsInstance(new_dict, wellcad.com.LithoDictionary)

        # Revert it back and delete the copied litho log.
        self.litho_log.litho_dictionary = copied_litho_log.litho_dictionary
        self.litho_borehole.remove_log(copied_litho_log.name)
    
    def test_litho_dictionary_scope(self):
        copied_litho_log = self.litho_borehole.add_log(self.litho_log)
        litho_dictionary = copied_litho_log.litho_dictionary
        copied_litho_log.attach_litho_dictionary(self.litho_dict)

        # The below will fail, because the litho dictionary went out of scope
        # and was destroyed by WellCAD (when the new one was attached). Should
        # it? Is this the correct behaviour?
        copied_litho_log.litho_dictionary = litho_dictionary

    def test_component_name(self):
        self.assertEqual(self.analysis_log.get_component_name(0), "VXBW.ELA")
        self.analysis_log.set_component_name(0, "test")
        self.assertEqual(self.analysis_log.get_component_name(0), "test")
        self.analysis_log.set_component_name(0, "VXBW.ELA")
        self.assertEqual(self.analysis_log.get_component_name(0), "VXBW.ELA")

    def test_insert_delete_fossil_item(self):
        self.core_desc_log.insert_new_fossil_item(top_depth=10.0, bottom_depth=11.0, litho_code="a cool litho code",
                                                  abundance=5.0, dominance=0, position=0.5)
        self.core_desc_log.insert_new_fossil_item(top_depth=14.0, bottom_depth=15.0, litho_code="a nice litho code",
                                                  abundance=5.0, dominance=0, position=0.5)
        fossil_item1 = self.core_desc_log.fossil_item(0)
        fossil_item2 = self.core_desc_log.fossil_item_at_depth(15.0)
        self.assertAttrEqual(fossil_item1, "symbol_code", "a cool litho code")
        self.assertAttrEqual(fossil_item2, "symbol_code", "a nice litho code")
        self.core_desc_log.remove_fossil_item(0)
        self.core_desc_log.remove_fossil_item_at_depth(15.0)

    def test_insert_delete_litho_bed(self):
        self.litho_log.insert_new_litho_bed(top_depth=10.0, bottom_depth=12.0, litho_code="a cool litho code",
                                            value=0.2, position=0.5)
        self.litho_log.insert_new_litho_bed(top_depth=14.0, bottom_depth=16.0, litho_code="a nice litho code",
                                            value=0.2, position=0.5)
        litho_bed1 = self.litho_log.get_litho_bed(0)
        litho_bed2 = self.litho_log.get_litho_bed_at_depth(15.0)
        self.assertAttrEqual(litho_bed1, "litho_code", "a cool litho code")
        self.assertAttrEqual(litho_bed2, "litho_code", "a nice litho code")
        self.litho_log.remove_litho_bed(0)
        self.litho_log.remove_litho_bed_at_depth(15.0)

    def test_set_litho_bed(self):
        # The methods set_litho_bed and set_litho_bed_at_depth do not exist. Is it an error ? There's already the insert_new_litho_bed for this task.
        litho_bed_1 = self.litho_log.get_litho_bed(0)
        litho_bed_2 = self.litho_log.get_litho_bed(1)
        self.assertIsInstance(litho_bed_1, wellcad.com.LithoBed)
        self.assertIsInstance(litho_bed_2, wellcad.com.LithoBed)
        self.litho_log.set_litho_bed(0, litho_bed_2)
        self.litho_log.set_litho_bed_at_depth(10522, litho_bed_2)

    def test_insert_delete_trace(self):
        """For each log that has an insert_trace methode, we test the following:
            - adding a trace at the beginning or end
            - check the No-data value
            - removing the first or last trace
            - removing a trace in the middle (has different behaviour depending on the log)
            - if removing doesn't really remove the trace, what is the value that is set instead"""

        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.analysis_log.insert_trace(1869)
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1870)
        self.assertEqual(self.analysis_log.get_trace_data(1869, 0), -999.25)
        self.analysis_log.remove_trace(1869)
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.analysis_log.remove_trace(10)  # trace is not really removed but values are set to No-data
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.assertEqual(self.analysis_log.get_trace_data(10, 0), -999.25)

        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.image_log.insert_trace(1026)
        self.assertAttrEqual(self.image_log, "nb_of_data", 1027)
        self.assertEqual(self.image_log.get_trace_data(1869, 0), 65535)
        self.image_log.remove_trace(1026)
        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.image_log.remove_trace(10)  # trace is not really removed but values are set to No-data
        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.assertEqual(self.image_log.get_trace_data(10, 0), 65535)

        self.assertAttrEqual(self.fws_log, "nb_of_data", 381)
        self.fws_log.insert_trace(10)
        self.assertAttrEqual(self.fws_log, "nb_of_data", 382)
        self.assertEqual(self.fws_log.get_trace_data(10, 0), -999.0)
        self.fws_log.remove_trace(10)  # trace should be entirely removed (not the case for image log traces and others)
        self.assertAttrEqual(self.fws_log, "nb_of_data", 381)

    def test_trace_at_depth(self):
        """For each log that has an insert_trace_at_depth methode, we test the following:
            - adding a trace at the beginning or end
            - check the No-data value
            - removing the first or last trace
            - removing a trace in the middle (has different behaviour depending on the log)
            - if removing doesn't really remove the trace, what is the value that is set instead"""
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.analysis_log.insert_trace_at_depth(13.87)
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1870)
        self.assertEqual(self.analysis_log.get_trace_data_at_depth(13.8, 0), -999.25)
        self.analysis_log.remove_trace_at_depth(13.87)
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.analysis_log.remove_trace_at_depth(50.0)  # trace is not really removed but values are set to No-data
        self.assertAttrEqual(self.analysis_log, "nb_of_data", 1869)
        self.assertEqual(self.analysis_log.get_trace_data_at_depth(50.0, 0), -999.25)

        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.image_log.insert_trace_at_depth(2118.1)
        self.assertAttrEqual(self.image_log, "nb_of_data", 1027)
        self.assertEqual(self.image_log.get_trace_data_at_depth(2118.8, 0), 65535)
        self.image_log.remove_trace_at_depth(2118.05)
        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.image_log.remove_trace_at_depth(2119.0)  # trace is not really removed but values are set to No-data
        self.assertAttrEqual(self.image_log, "nb_of_data", 1026)
        self.assertEqual(self.image_log.get_trace_data_at_depth(2119.0, 0), 65535)

        self.assertAttrEqual(self.fws_log, "nb_of_data", 381)
        self.fws_log.insert_trace_at_depth(52.0)  # replaces existing trace
        self.assertAttrEqual(self.fws_log, "nb_of_data", 381)
        self.fws_log.insert_trace_at_depth(52.05)  # adds a new trace
        self.assertAttrEqual(self.fws_log, "nb_of_data", 382)
        self.assertEqual(self.fws_log.get_trace_data_at_depth(52.0, 0), -999.0)
        self.fws_log.remove_trace_at_depth(52.0)  # trace should be entirely removed (not the case for image log traces and others)
        self.assertAttrEqual(self.fws_log, "nb_of_data", 381)

        self.assertAttrEqual(self.percentage_log, "nb_of_data", 289)
        self.percentage_log.insert_trace_at_depth(18.10)  # adds a new trace
        self.assertAttrEqual(self.percentage_log, "nb_of_data", 290)
        self.percentage_log.insert_trace_at_depth(18.10)  # replaces existing trace
        self.assertAttrEqual(self.percentage_log, "nb_of_data", 290)
        self.assertEqual(self.percentage_log.get_trace_data_at_depth(18.10, 0), -999.0)
        self.percentage_log.remove_trace_at_depth(18.10)  # trace should be entirely removed (not the case for image log traces and others)
        self.assertAttrEqual(self.percentage_log, "nb_of_data", 289)

    def test_trace_for_percentage_logs(self):
        self.percentage_log.insert_trace(0)  # ERROR
        # there's no insert_trace(index) function for the percentage log
        self.percentage_log.insert_trace_at_depth(0)  # ok
        self.percentage_log.get_trace_data(0, 0)  # ok
        self.percentage_log.get_trace_data_at_depth(0, 0)  # ok
        self.percentage_log.remove_trace(0)  # ok
        self.percentage_log.remove_trace_at_depth(0)  # ok

    def test_trace_for_rgb_logs(self):
        # The RGB log have no insert_trace or remove_trace functions
        self.rgb_log.insert_trace(0)  # ERROR
        self.rgb_log.insert_trace_at_depth(0)  # ERROR
        self.rgb_log.get_trace_data(0, 0)  # ok
        self.rgb_log.get_trace_data_at_depth(0, 0)  # ok
        self.rgb_log.remove_trace(0)  # ERROR
        self.rgb_log.remove_trace_at_depth(0)  # ERROR

    def test_trace_data(self):
        self.assertEqual(self.percentage_log.get_trace_data(0, 0), 0.14799758791923523)
        self.percentage_log.set_trace_data(0, 0, 0.25)
        self.assertEqual(self.percentage_log.get_trace_data(0, 0), 0.25)
        self.percentage_log.set_trace_data(0, 0, 0.14799758791923523)

    def test_trace_data_at_depth(self):
        self.assertEqual(self.fws_log.get_trace_data_at_depth(50.0, 0), 0.146484375)
        self.fws_log.set_trace_data_at_depth(50.0, 0, 0.25)
        self.assertEqual(self.fws_log.get_trace_data_at_depth(50.0, 0), 0.25)
        self.fws_log.set_trace_data_at_depth(50.0, 0, 0.146484375)

    def test_trace_sample_rate(self):
        self.assertAttrEqual(self.fws_log, "trace_sample_rate", 3.5)
        self.assertAttrChange(self.fws_log, "trace_sample_rate", 10)

    def test_trace_offset(self):
        self.assertAttrEqual(self.fws_log, "trace_offset", 0.0)
        self.assertAttrChange(self.fws_log, "trace_offset", 5)

    def test_trace_length(self):
        self.assertAttrEqual(self.percentage_log, "trace_length", 3)
        self.assertAttrEqual(self.analysis_log, "trace_length", 7)
        self.assertAttrEqual(self.fws_log, "trace_length", 255)
        self.assertAttrEqual(self.image_log, "trace_length", 360)
        self.assertAttrEqual(self.rgb_log, "trace_length", 360)

        self.assertAttrChange(self.percentage_log, "trace_length", 5)
        self.assertAttrChange(self.analysis_log, "trace_length", 10)
        self.assertAttrChange(self.fws_log, "trace_length", 300)
        # self.assertAttrChange(self.image_log, "trace_length", 360)
        # self.assertAttrChange(self.rgb_log, "trace_length", 360)

    def test_insert_new_ole_box_from_file(self):
        self.ole_log.insert_new_ole_box_from_file(str(pathlib.Path(__file__).parent / "fixtures" / "test_img.jpg"),
                                                  True, 0, 10)

    def test_background_color(self):
        self.assertAttrEqual(self.engineering_log, "background_color", 4227327)
        self.assertAttrChange(self.engineering_log, "background_color", 4227300)

    def test_background_hatch_style(self):
        self.assertAttrEqual(self.engineering_log, "background_hatch_style", 5)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 0)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 1)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 2)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 3)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 4)
        self.assertAttrChange(self.engineering_log, "background_hatch_style", 5)
        self.assertAttrNotChanged(self.engineering_log, "background_hatch_style", 7)

    def background_hatch_style_is_wrong(self):
        self.fail("background_hatch_style 6 should not be in the documentation and 4 should be")

    def test_background_style(self):
        self.assertAttrEqual(self.engineering_log, "background_style", 0)
        self.assertAttrChange(self.engineering_log, "background_style", 0)
        self.assertAttrChange(self.engineering_log, "background_style", 1)
        self.assertAttrChange(self.engineering_log, "background_style", 2)
        self.assertAttrNotChanged(self.engineering_log, "background_style", 3)

    def test_drill_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)
        drill_item_1 = self.engineering_log.drill_item(0)
        drill_item_2 = self.engineering_log.drill_item(1)
        drill_item_3 = self.engineering_log.drill_item(2)
        self.assertIsInstance(drill_item_1, wellcad.com.DrillItem)
        self.assertIsInstance(drill_item_2, wellcad.com.DrillItem)
        self.assertIsInstance(drill_item_3, wellcad.com.DrillItem)

    def test_drill_item_at_depth(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)
        drill_item_index_0 = self.engineering_log.drill_item(0)
        drill_item_index_1 = self.engineering_log.drill_item(1)
        drill_item_index_2 = self.engineering_log.drill_item(2)
        depth0 = drill_item_index_0.bottom_depth  # 15
        depth1 = drill_item_index_1.bottom_depth  # 50
        depth2 = drill_item_index_2.bottom_depth  # 90
        self.assertNotEqual(depth0, depth1)
        self.assertNotEqual(depth1, depth2)
        self.assertNotEqual(depth0, depth2)
        drill_item_at_depth_0 = self.engineering_log.drill_item_at_depth(depth0)
        depth0_ = drill_item_at_depth_0.bottom_depth
        self.assertEqual(depth0_, depth0)

    def test_remove_drill_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)
        self.engineering_log.insert_new_drill_item(100, 96.0)
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 4)
        self.engineering_log.remove_drill_item(3)
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)

    def test_insert_new_drill_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)
        self.engineering_log.insert_new_drill_item(70, 96.0)  # log should have a 15m, 50m, 70m and 90m drill
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 4)
        depth = self.engineering_log.drill_item(2).bottom_depth
        self.assertEqual(depth, 70)
        self.engineering_log.remove_drill_item(2)
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)

    def test_insert_bigger_drill_below_smaller_drill(self):
        top_drill = self.engineering_log.drill_item(0)
        self.assertAttrEqual(top_drill, "bottom_depth", 15.0)
        self.assertAttrEqual(top_drill, "diameter", 300.0)
        self.engineering_log.insert_new_drill_item(20, 400.0)  # drill at 20m, diameter = 400
        self.assertAttrEqual(top_drill, "diameter", 300.0)
        self.engineering_log.remove_drill_item(1)
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)

    def test_nb_of_drill_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_drill_item", 3)

    def test_nb_of_eqp_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_eqp_item", 20)

    def test_eqp_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_eqp_item", 20)
        eqp_item = self.engineering_log.eqp_item(0)
        self.assertIsInstance(eqp_item, wellcad.com.EquipmentItem)

    def test_insert_and_remove_new_eqp_item(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_eqp_item", 20)
        self.assertIsNone(self.engineering_log.eqp_item(20))
        self.assertAttrEqual(self.engineering_log.eqp_item(19), "name", "PVC")  # last item is PVC
        self.engineering_log.insert_new_eqp_item(10.0, 15.0, "Water")  # item is put at the end of the list
        self.assertAttrEqual(self.engineering_log.eqp_item(20), "name", "Water")  # new last item is water
        self.engineering_log.remove_eqp_item(20)
        self.assertIsNone(self.engineering_log.eqp_item(20))

    def test_no_insert_if_invalid_eqp_name(self):
        self.assertAttrEqual(self.engineering_log, "nb_of_eqp_item", 20)
        self.engineering_log.insert_new_eqp_item(10.0, 15.0, "invalid name")
        self.assertAttrEqual(self.engineering_log, "nb_of_eqp_item", 20)

    def test_comment_style(self):
        self.assertAttrEqual(self.engineering_log, "comment_style", 2)
        self.assertAttrChange(self.engineering_log, "comment_style", 0)
        self.assertAttrChange(self.engineering_log, "comment_style", 1)

    def test_diameter_high(self):
        self.assertAttrEqual(self.engineering_log, "diameter_high", 400.0)
        self.assertAttrChange(self.engineering_log, "diameter_high", 500.0)

    def test_ground_depth(self):
        self.assertAttrEqual(self.engineering_log, "ground_depth", 0.0)
        self.assertAttrChange(self.engineering_log, "ground_depth", 1.0)

    def test_style_engineering_log(self):
        self.assertAttrEqual(self.engineering_log, "style", 0)
        self.assertAttrChange(self.engineering_log, "style", 0)
        self.assertAttrChange(self.engineering_log, "style", 1)
        self.assertAttrChange(self.engineering_log, "style", 2)

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

    def test_insert_remove_attribute(self):
        with self.assertRaises(pywintypes.com_error):
            self.structure_log.get_attribute_name(1)
        self.structure_log.insert_new_attribute("my_new_attribute")
        self.assertEqual(self.structure_log.get_attribute_name(1), "my_new_attribute")

        # get the number of attributes linked to the log (2)
        nb_attribs = self.structure_log.nb_of_attributes
        # remove the newly added attribute
        self.structure_log.remove_attribute("my_new_attribute")

        # get the number of attributes and verify that it is lower than the previous number now that one of them has been eliminated
        self.assertGreater(nb_attribs, self.structure_log.nb_of_attributes)

    def test_attach_attribute_dictionary(self):
        attribute_dictionary = str(self.fixture_path / "DefaultStructure.tad")
        self.structure_log.attach_attribute_dictionary("Type", attribute_dictionary)

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
        self.assertAttrEqual(breakout2, "azimuth", 50.0)
        self.breakout_log.remove_breakout(0)
        self.breakout_log.remove_breakout_at_depth(15.0)

    def test_insert_delete_lineation(self):
        self.lineation_log.insert_new_lineation_ex(depth=10.0, trend=20.0, plunge=3.0, eccentricity=0.0)
        self.lineation_log.insert_new_lineation_ex(depth=15.0, trend=20.0, plunge=3.0, eccentricity=-0.8)
        lineation1 = self.lineation_log.lineation(0)
        lineation2 = self.lineation_log.lineation_at_depth(15.0)
        self.assertAttrEqual(lineation1, "eccentricity", 0.0)
        self.assertAttrEqual(lineation2, "eccentricity", -0.800000011920929)
        self.lineation_log.remove_lineation(0)
        self.lineation_log.remove_lineation_at_depth(15.0)

    def test_column_name(self):
        self.assertEqual(self.strata_log.get_column_name(0), "Depo")
        self.strata_log.set_column_name(0, "new column name")
        self.assertEqual(self.strata_log.get_column_name(0), "new column name")
        self.strata_log.set_column_name(0, "Depo")

    def test_strata_column(self):
        column = self.strata_log.strata_column(0)
        comment_box = column.comment_box(0)
        self.assertEqual(comment_box.text, "Distributary Mouth Bar")
        self.assertIsInstance(column, wellcad.com.Log)

    def test_insert_remove_strata_column(self):
        # Insert a new column into the Strata Log
        self.strata_log.insert_new_strata_column("new_col")

        # Get the number of columns in the Strata Log
        nb_columns_init = self.strata_log.nb_of_columns

        # Remove the last column of the Strata Log (the one we just added)
        self.strata_log.remove_strata_column(nb_columns_init - 1)

        # Verify that the number of column decreased
        self.assertGreater(nb_columns_init, self.strata_log.nb_of_columns)

    def test_insert_delete_comment_box(self):
        self.comment_log.insert_new_comment_box(top_depth=10.0, bottom_depth=12.0, text="kind text")
        self.comment_log.insert_new_comment_box(top_depth=14.0, bottom_depth=16.0, text="mean text")
        comment_box1 = self.comment_log.comment_box(0)
        comment_box2 = self.comment_log.comment_box_at_depth(15.0)
        self.assertAttrEqual(comment_box1, "text", "kind text")
        self.assertAttrEqual(comment_box2, "text", "mean text")
        self.comment_log.remove_comment_box(0)
        self.comment_log.remove_comment_box_at_depth(15.0)

    def test_insert_delete_marker(self):
        self.marker_log.insert_new_marker(depth=10.0, name="a name", comment="a comment", contact="a contact style")
        self.marker_log.insert_new_marker(depth=15.0, name="an other name", comment="an other comment",
                                          contact="an other contact style")
        marker1 = self.marker_log.marker(3)
        marker2 = self.marker_log.marker_by_name("an other name")
        self.assertAttrEqual(marker1, "comment", "a comment")
        self.assertAttrEqual(marker2, "comment", "an other comment")
        self.marker_log.remove_marker(3)
        self.marker_log.remove_marker(3)

    def test_font(self):
        font = self.comment_log.font
        self.assertIsInstance(font, wellcad.com.Font)
        self.assertEqual(font.italic, False)
        new_comment_log = self.borehole.insert_new_log(8)
        new_comment_log.font.italic = True
        new_comment_log.font = font
        self.assertEqual(new_comment_log.font.italic, False)

    def test_insert_delete_cross_box(self):
        self.cross_section_log.insert_new_cross_box(top_depth=10.0, bottom_depth=12.0)
        self.cross_section_log.insert_new_cross_box(top_depth=14.0, bottom_depth=16.0)
        cross_box1 = self.cross_section_log.cross_box(0)
        cross_box2 = self.cross_section_log.cross_box_at_depth(15.0)
        self.assertAttrEqual(cross_box1, "top_depth", 10.0)
        self.assertAttrEqual(cross_box2, "top_depth", 14.0)
        self.cross_section_log.remove_cross_box(0)
        self.cross_section_log.remove_cross_box_at_depth(15.0)

    def test_insert_delete_stack_item(self):
        self.stacking_pattern_log.insert_new_stack_item(top_depth=10.0, bottom_depth=12.0, top_width=0.1,
                                                        bottom_width=0.9)
        self.stacking_pattern_log.insert_new_stack_item(top_depth=14.0, bottom_depth=16.0, top_width=0.1,
                                                        bottom_width=0.9)
        stack_item1 = self.stacking_pattern_log.stack_item(0)
        stack_item2 = self.stacking_pattern_log.stack_item_at_depth(15.0)
        self.assertAttrEqual(stack_item1, "top_depth", 10.0)
        self.assertAttrEqual(stack_item2, "top_depth", 14.0)
        self.stacking_pattern_log.remove_stack_item(0)
        self.stacking_pattern_log.remove_stack_item_at_depth(15.0)

    def test_grid_width(self):
        # verify the initial widths of the vertical grids, then verify that they can be changed
        self.assertAttrEqual(self.gr_log, "maj_grid_width", 1)
        self.assertAttrChange(self.gr_log, "maj_grid_width", 4)
        self.assertAttrEqual(self.gr_log, "min_grid_width", 1)
        self.assertAttrChange(self.gr_log, "min_grid_width", 2)

    def test_grid_color(self):
        # verify the initial colors of the vertical grids, then verify that they can be changed
        # reset the boolean since the grids are activated by modifying their color

        # major grid
        is_enabled_maj = self.gr_log.maj_grid_enable
        self.assertAttrEqual(self.gr_log, "maj_grid_color", 0)
        self.assertAttrChange(self.gr_log, "maj_grid_color", 0x0000ff)
        self.gr_log.maj_grid_enable = is_enabled_maj
        # minor grid
        is_enabled_min = self.gr_log.min_grid_enable
        self.assertAttrEqual(self.gr_log, "min_grid_color", 0)
        self.assertAttrChange(self.gr_log, "min_grid_color", 0x0000ff)
        self.gr_log.min_grid_enable = is_enabled_min

    def test_grid_style(self):
        # verify the initial styles of the vertical grids, then verify that they can be changed
        self.assertAttrEqual(self.gr_log, "maj_grid_style", 0)
        self.assertAttrChange(self.gr_log, "maj_grid_style", 1)
        self.assertAttrEqual(self.gr_log, "min_grid_style", 2)
        self.assertAttrChange(self.gr_log, "min_grid_style", 3)

    def test_overwrite_depth_grid(self):
        # verify that the property is initially enabled, then disable it
        self.assertEqual(self.gr_log.overwrite_depth_grids, True)
        self.gr_log.overwrite_depth_grids = False
        # verify that the property has been changed and turn back to the original value
        self.assertNotEqual(self.gr_log.overwrite_depth_grids, True)
        self.gr_log.overwrite_depth_grids = True

    def test_overflow_type(self):
        # verify that the property is initially set to 2, then set it to 1
        self.assertEqual(self.gr_log.overflow_type, 2)
        self.gr_log.overflow_type = 1
        # verify that the property has been changed and turn back to the original value
        self.assertNotEqual(self.gr_log.overflow_type, 2)
        self.gr_log.overflow_type = 2

    def test_decades(self):
        # verify that the property is initially set to 1, then set it to 3
        self.assertEqual(self.gr_log.decades, 1)
        self.gr_log.decades = 3
        # verify that the property has been changed and turn back to the original value
        self.assertNotEqual(self.gr_log.decades, 1)
        self.gr_log.decades = 1

    def test_cardinal_points_color(self):
        # verify that the color is initially set to no color, then set it to red
        self.assertEqual(self.image_log.cardinal_points_color, 0)
        self.image_log.cardinal_points_color = 0x0000ff
        # verify that the property has been changed and turn back to the original color
        self.assertNotEqual(self.image_log.cardinal_points_color, 0)
        self.image_log.cardinal_points_color = 0

    def test_left_shading_color(self):
        # verify that the color is initially undefined, then set it to red
        self.assertEqual(self.image_log.left_shading_color, -1)
        self.image_log.left_shading_color = 0x0000ff
        # verify that the property has been changed and turn back to the original color
        self.assertNotEqual(self.image_log.left_shading_color, -1)
        self.image_log.left_shading_color = -1

    def test_right_shading_color(self):
        # verify that the color is initially undefined, then set it to red
        self.assertEqual(self.image_log.right_shading_color, -1)
        self.image_log.right_shading_color = 0x0000ff
        # verify that the property has been changed and turn back to the original color
        self.assertNotEqual(self.image_log.right_shading_color, -1)
        self.image_log.right_shading_color = -1

    def test_curves_count(self):
        # verify that the property is initially set to 1, then set it to 3
        self.assertEqual(self.image_log.curves_count, 1)
        self.image_log.curves_count = 3
        # verify that the property has been changed and turn back to the original value
        self.assertNotEqual(self.image_log.curves_count, 1)
        self.image_log.curves_count = 1

    def test_shading_type(self):
        # verify that the property is initially set to 0 (opaque), then set it to 1 (transparent)
        self.assertEqual(self.gr_log.shading_type, 0)
        self.gr_log.shading_type = 1
        # verify that the property has been changed and turn back to the original value
        self.assertNotEqual(self.gr_log.shading_type, 0)
        self.gr_log.shading_type = 0

    def test_set_caliper_component(self):
        # use a well log as a caliper component of a 3D log
        self.log_3d.set_caliper_component(str(self.caliper_log._dispatch))

    def test_set_amplitude_component(self):
        # use a well log as an amplitude component of a 3D log
        self.log_3d.set_amplitude_component(str(self.fmi_mean._dispatch))

    def test_set_structure_component(self):
        # use a structure log as a structure component of a 3D log
        self.log_3d.set_structure_component(str(self.structure_true_log._dispatch))

    def test_set_lineation_component(self):
        # use a lineation log as the lineation component of a 3D log
        self.log_3d_lin.set_lineation_component(str(self.lineation_log._dispatch))

    def test_get_attribute_dictionary(self):
        attrib_name = self.structure_log.get_attribute_name(0)
        self.structure_log.get_attribute_dictionary(attrib_name)

    def test_text_format(self):
        # verify that the property is initially set to 0 (plain text), then set it to 1 (rich text)
        self.assertEqual(self.comment_log.text_format, 0)
        self.comment_log.text_format = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.text_format, 0)
        self.comment_log.text_format = 0

    def test_horz_text_align(self):
        # for comment logs
        # verify that the property is initially set to 1 (center), then set it to 0 (left)
        self.assertEqual(self.comment_log.horz_text_align, 1)
        self.comment_log.horz_text_align = 0
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.horz_text_align, 1)
        self.comment_log.horz_text_align = 1

        # for marker logs
        # verify that the property is initially set to 0 (left), then set it to 1 (center)
        self.assertEqual(self.marker_log.horz_text_align, 0)
        self.marker_log.horz_text_align = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.horz_text_align, 0)
        self.marker_log.horz_text_align = 0

    def test_vert_text_align(self):
        # verify that the property is initially set to 1 (center), then set it to 2 (bottom)
        self.assertEqual(self.comment_log.vert_text_align, 1)
        self.comment_log.vert_text_align = 0
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.vert_text_align, 1)
        self.comment_log.vert_text_align = 1

    def test_text_orientation(self):
        # verify that the property is initially set to 0 (normal), then set it to 1 (left)
        self.assertEqual(self.comment_log.text_orientation, 0)
        self.comment_log.text_orientation = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.text_orientation, 0)
        self.comment_log.text_orientation = 0

    def test_repeat_text(self):
        # verify that the property is initially set to false, then set it to true
        self.assertEqual(self.comment_log.repeat_text, False)
        self.comment_log.repeat_text = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.repeat_text, False)
        self.comment_log.repeat_text = False

    def test_repeat_text_spacing(self):
        # verify that the property is initially set to 100mm, then set it to 50mm
        self.assertEqual(self.comment_log.repeat_text_spacing, 1000)
        self.comment_log.repeat_text_spacing = 500
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.repeat_text_spacing, 1000)
        self.comment_log.repeat_text_spacing = 1000

    def test_top_depth_indicator(self):
        # verify that the property is initially set to 1 (left), then set it to 2 (center)
        self.assertEqual(self.comment_log.top_depth_indicator, 1)
        self.comment_log.top_depth_indicator = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.top_depth_indicator, 1)
        self.comment_log.top_depth_indicator = 1

    def test_bottom_depth_indicator(self):
        # verify that the property is initially set to 0 (None), then set it to 1 (left)
        self.assertEqual(self.comment_log.bottom_depth_indicator, 0)
        self.comment_log.bottom_depth_indicator = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.bottom_depth_indicator, 0)
        self.comment_log.bottom_depth_indicator = 0

    def test_depth_font(self):
        font = self.comment_log.depth_font
        self.assertIsInstance(font, wellcad.com.Font)
        self.assertEqual(font.italic, False)
        new_comment_log = self.borehole.insert_new_log(8)
        new_comment_log.depth_font.italic = True
        new_comment_log.depth_font = font
        self.assertEqual(new_comment_log.depth_font.italic, False)

    def test_depth_digits(self):
        # for comment logs
        # verify that the property is initially set to 2, then set it to 3
        self.assertEqual(self.comment_log.depth_digits, 2)
        self.comment_log.depth_digits = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.depth_digits, 2)
        self.comment_log.depth_digits = 2

        # for marker logs
        # verify that the property is initially set to 2, then set it to 3
        self.assertEqual(self.marker_log.depth_digits, 2)
        self.marker_log.depth_digits = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.depth_digits, 2)
        self.marker_log.depth_digits = 2

    def test_pinches_position(self):
        # for comment logs
        # verify that the property is initially set to 1 (left), then set it to 2 (right)
        self.assertEqual(self.comment_log.pinches_position, 1)
        self.comment_log.pinches_position = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.pinches_position, 1)
        self.comment_log.pinches_position = 1

        # for marker logs
        # verify that the property is initially set to 1 (left), then set it to 2 (right)
        self.assertEqual(self.marker_log.pinches_position, 1)
        self.marker_log.pinches_position = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.pinches_position, 1)
        self.marker_log.pinches_position = 1

    def test_allow_pinches(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.comment_log.allow_pinches, True)
        self.comment_log.allow_pinches = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.comment_log.allow_pinches, True)
        self.comment_log.allow_pinches = True

    def test_classifier_dictionary(self):
        # Get the classifier dictionary of the interval log
        classif_dict = self.gr_litho_interval_log.classifier_dictionary
        self.assertIsInstance(classif_dict, wellcad.com.ClassifierDictionary)

        # Make a copy of a well log and assign the same dictionary
        copy_gr_log = self.borehole.add_log(self.gr_log)
        copy_gr_log.classifier_dictionary = classif_dict #doesn't work, same issue as with the "test_litho_dictionary_scope"

        # Get the classifier dictionary of the new well log to verify that it has been correctly affected
        classif_dict_well = self.gr_log.classifier_dictionary
        self.assertIsInstance(classif_dict_well, wellcad.com.ClassifierDictionary)

        # Remove the new well log
        self.borehole.remove_log(copy_gr_log)

    def test_display_depth(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.marker_log.display_depth, True)
        self.marker_log.display_depth = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.display_depth, True)
        self.marker_log.display_depth = True

    def test_display_name(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.marker_log.display_name, True)
        self.marker_log.display_name = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.display_name, True)
        self.marker_log.display_name = True

    def test_display_comment(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.marker_log.display_comment, False)
        self.marker_log.display_comment = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.marker_log.display_comment, False)
        self.marker_log.display_comment = False

    def test_name_font(self):
        font = self.marker_log.name_font
        self.assertIsInstance(font, wellcad.com.Font)
        self.assertEqual(font.italic, False)
        new_marker_log = self.borehole.insert_new_log(8)
        new_marker_log.font.italic = True
        new_marker_log.font = font
        self.assertEqual(new_marker_log.font.italic, False)

    def test_shading_up_down(self):
        # for the upper values
        # verify that the color is initially undefined, then set it to red
        self.assertEqual(self.fws_log.shading_color_up, 0)
        self.fws_log.shading_color_up = 0x0000ff
        # verify that the property has been changed and turn back to the original color
        self.assertNotEqual(self.fws_log.shading_color_up, 0)
        self.fws_log.shading_color_up = 0

        # for the lower values
        # verify that the color is initially undefined, then set it to green
        self.assertEqual(self.fws_log.shading_color_down, 0)
        self.fws_log.shading_color_down = 0x00ff00
        # verify that the property has been changed and turn back to the original color
        self.assertNotEqual(self.fws_log.shading_color_down, 0)
        self.fws_log.shading_color_down = 0

    def test_zero_line(self):
        # verify that the property is initially set to 0, then set it to 5
        self.assertEqual(self.fws_log.zero_line, 0)
        self.fws_log.zero_line = 5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.fws_log.zero_line, 0)
        self.fws_log.zero_line = 0

    def test_scale_factor(self):
        # verify that the property is initially set to 1, then set it to 1.5
        self.assertEqual(self.fws_log.scale_factor, 1)
        self.fws_log.scale_factor = 1.5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.fws_log.scale_factor, 1)
        self.fws_log.scale_factor = 1

    def test_associated_color(self):
        # verify that the property is initially set to false, then set it to  true
        self.assertEqual(self.litho_log.use_associated_color, True)
        self.litho_log.use_associated_color = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.use_associated_color, True)
        self.litho_log.use_associated_color = True

    def test_hide_symbol_background(self):
        # verify that the property is initially set to false, then set it to  true
        self.assertEqual(self.litho_log.hide_symbol_background, True)
        self.litho_log.hide_symbol_background = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.hide_symbol_background, True)
        self.litho_log.hide_symbol_background = True

    def test_symbol_scale(self):
        # verify that the property is initially set to 1 (100%), then set it to 1.5 (150%)
        self.assertEqual(self.litho_log.symbol_scale, 1)
        self.litho_log.symbol_scale = 1.5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.symbol_scale, 1)
        self.litho_log.symbol_scale = 1

    def test_display_contact(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.litho_log.display_contact, False)
        self.litho_log.display_contact = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.display_contact, False)
        self.litho_log.display_contact = False

    def test_display_text(self):
        # verify that the property is initially set to true, then set it to  false
        self.assertEqual(self.litho_log.display_text, False)
        self.litho_log.display_text = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.display_text, False)
        self.litho_log.display_text = False

    def test_label_mode(self):
        # verify that the property is initially set to 1 (description), then set it to 2 (code and description)
        self.assertEqual(self.litho_log.label_mode, 1)
        self.litho_log.label_mode = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.litho_log.label_mode, 1)
        self.litho_log.label_mode = 1

    def test_drawing_mode(self):
        # verify that the property is initially set to 1 (average slice), then set it to 0 (slices superimposed)
        self.assertEqual(self.cross_section_log.drawing_mode, 1)
        self.cross_section_log.drawing_mode = 0
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.drawing_mode, 1)
        self.cross_section_log.drawing_mode = 1

    def test_display_internal_circle(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.cross_section_log.display_internal_circle, True)
        self.cross_section_log.display_internal_circle = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.display_internal_circle, True)
        self.cross_section_log.display_internal_circle = True

    def test_internal_radius(self):
        # verify that the property is initially set to 4.37, then set it to 5
        radius = self.cross_section_log.internal_radius
        self.assertEqual(self.cross_section_log.internal_radius, radius)
        self.cross_section_log.internal_radius = 5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.internal_radius, radius)
        self.cross_section_log.internal_radius = radius

    def test_internal_shading_position(self):
        # verify that the property is initially set to 2 (Outside), then set it to 3 (Both)
        self.assertEqual(self.cross_section_log.internal_shading_position, 2)
        self.cross_section_log.internal_shading_position = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.internal_shading_position, 2)
        self.cross_section_log.internal_shading_position = 2

    def test_internal_shading_color(self):
        # verify that the property is initially set to pink, then set it to red
        color = 9020344
        self.assertEqual(self.cross_section_log.internal_shading_color, color)
        self.cross_section_log.internal_shading_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.internal_shading_color, color)
        self.cross_section_log.internal_shading_color = color

    def test_internal_shading_style(self):
        # verify that the property is initially 1 (Solid), then set it to 3 (Vertical Hatch)
        self.assertEqual(self.cross_section_log.internal_shading_style, 1)
        self.cross_section_log.internal_shading_style = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.internal_shading_style, 1)
        self.cross_section_log.internal_shading_style = 1

    def test_display_external_circle(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.cross_section_log.display_external_circle, True)
        self.cross_section_log.display_external_circle = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.display_external_circle, True)
        self.cross_section_log.display_external_circle = True

    def test_external_radius(self):
        # verify that the property is initially set to 8.75, then set it to 10
        self.assertEqual(self.cross_section_log.external_radius, 8.75)
        self.cross_section_log.external_radius = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.external_radius, 8.75)
        self.cross_section_log.external_radius = 8.75

    def test_external_shading_position(self):
        # verify that the property is initially set to 1 (Inside), then set it to 3 (Both)
        self.assertEqual(self.cross_section_log.external_shading_position, 1)
        self.cross_section_log.external_shading_position = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.external_shading_position, 1)
        self.cross_section_log.external_shading_position = 1

    def test_external_shading_color(self):
        # verify that the property is initially set to grey, then set it to green
        color = 8355711
        self.assertEqual(self.cross_section_log.external_shading_color, color)
        self.cross_section_log.external_shading_color = 0x00ff00
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.external_shading_color, color)
        self.cross_section_log.external_shading_color = color

    def test_external_shading_style(self):
        # verify that the property is initially 7 (Diagonal Cross Hatch), then set it to 2 (Horizontal Hatch)
        self.assertEqual(self.cross_section_log.external_shading_style, 7)
        self.cross_section_log.external_shading_style = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.external_shading_style, 7)
        self.cross_section_log.external_shading_style = 7

    def test_display_azimuth(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.cross_section_log.display_azimuth, True)
        self.cross_section_log.display_azimuth = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.display_azimuth, True)
        self.cross_section_log.display_azimuth = True

    def test_azimuth_spacing(self):
        # verify that the property is initially set to 30, then set it to 20
        self.assertEqual(self.cross_section_log.azimuth_spacing, 30)
        self.cross_section_log.azimuth_spacing = 20
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.azimuth_spacing, 30)
        self.cross_section_log.azimuth_spacing = 30

    def test_display_caliper(self):
        # verify that the property is initially set to False, then set it to True
        self.assertEqual(self.cross_section_log.display_caliper, False)
        self.cross_section_log.display_caliper = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.display_caliper, False)
        self.cross_section_log.display_caliper = False

    def test_caliper_spacing(self):
        # verify that the property is initially set to 2, then set it to 3
        self.assertEqual(self.cross_section_log.caliper_spacing, 2)
        self.cross_section_log.caliper_spacing = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.caliper_spacing, 2)
        self.cross_section_log.caliper_spacing = 2

    def test_display_labels(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.cross_section_log.display_labels, True)
        self.cross_section_log.display_labels = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.cross_section_log.display_labels, True)
        self.cross_section_log.display_labels = True

    def test_retrogradation_color(self):
        # verify that the property is initially set to red, then set it to green
        color = 16711680
        self.assertEqual(self.stacking_pattern_log.retrogradation_color, color)
        self.stacking_pattern_log.retrogradation_color = 0x00ff00
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.stacking_pattern_log.retrogradation_color, color)
        self.stacking_pattern_log.retrogradation_color = color

    def test_progradation_color(self):
        # verify that the property is initially set to blue, then set it to green
        color = 255
        self.assertEqual(self.stacking_pattern_log.progradation_color, color)
        self.stacking_pattern_log.progradation_color = 0x00ff00
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.stacking_pattern_log.progradation_color, color)
        self.stacking_pattern_log.progradation_color = color

    def test_aggradation_color(self):
        # verify that the property is initially set to yellow, then set it to green
        color = 65535
        self.assertEqual(self.stacking_pattern_log.aggradation_color, color)
        self.stacking_pattern_log.aggradation_color = 0x00ff00
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.stacking_pattern_log.aggradation_color, color)
        self.stacking_pattern_log.aggradation_color = color

    def test_display_limits(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.stacking_pattern_log.display_limits, False)
        self.stacking_pattern_log.display_limits = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.stacking_pattern_log.display_limits, False)
        self.stacking_pattern_log.display_limits = False

    def test_display_structure_aperture(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.log_3d.display_structure_aperture, True)
        self.log_3d.display_structure_aperture = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.display_structure_aperture, True)
        self.log_3d.display_structure_aperture = True

    def test_projection_type(self):
        # verify that the property is initially set to 2 (None), then set it to 1 (3rd Angle)
        self.assertEqual(self.log_3d.projection_type, 2)
        self.log_3d.projection_type = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.projection_type, 2)
        self.log_3d.projection_type = 2

    def test_frame_type(self):
        # verify that the property is initially set to 0 (No Frame), then set it to 1 (Frame Only)
        self.assertEqual(self.log_3d.frame_type, 0)
        self.log_3d.frame_type = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.frame_type, 0)
        self.log_3d.frame_type = 0

    def test_min_cylinder_faces(self):
        # verify that the property is initially set to 36, then set it to 72
        self.assertEqual(self.log_3d.min_cylinder_faces, 36)
        self.log_3d.min_cylinder_faces = 72
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.min_cylinder_faces, 36)
        self.log_3d.min_cylinder_faces = 36

    def test_ambient_intensity(self):
        # verify that the property is initially set to 0.2, then set it to 0.5
        intensity = self.log_3d.ambient_intensity
        self.assertEqual(self.log_3d.ambient_intensity, intensity)
        self.log_3d.ambient_intensity = 0.5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.ambient_intensity, intensity)
        self.log_3d.ambient_intensity = intensity

    def test_spot_intensity(self):
        # verify that the property is initially set to 1, then set it to 0.7
        self.assertEqual(self.log_3d.spot_intensity, 1)
        self.log_3d.spot_intensity = 0.7
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.spot_intensity, 1)
        self.log_3d.spot_intensity = 1

    def test_spot_vert_pos(self):
        # verify that the property is initially set to 106.0, then set it to 130
        self.assertEqual(self.log_3d.spot_vert_pos, 106)
        self.log_3d.spot_vert_pos = 130
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.spot_vert_pos, 106)
        self.log_3d.spot_vert_pos = 106

    def test_view_angle(self):
        # verify that the property is initially set to 343, then set it to 200
        angle = self.log_3d.view_angle
        self.assertEqual(self.log_3d.view_angle, angle)
        self.log_3d.view_angle = 200
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.view_angle, angle)
        self.log_3d.view_angle = angle

    def test_caliper_low(self):
        # verify that the property is initially set to 0, then set it to 5
        self.assertEqual(self.log_3d.caliper_low, 0)
        self.log_3d.caliper_low = 5
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.caliper_low, 0)
        self.log_3d.caliper_low = 0

    def test_caliper_high(self):
        # verify that the property is initially set to 20, then set it to 15
        self.assertEqual(self.log_3d.caliper_high, 20)
        self.log_3d.caliper_high = 15
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.log_3d.caliper_high, 20)
        self.log_3d.caliper_high = 20


    def test_set_caliper_log(self):
        self.structure_log.set_caliper_log("C1")

    def test_set_depth_of_img_log(self):
        self.structure_log.set_depth_of_img_log("C2")

    def test_caliper_from_log(self):
        # verify that the property is initially set to False, then set it to True
        self.assertEqual(self.structure_log.caliper_from_log, False)
        self.structure_log.caliper_from_log = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.caliper_from_log, False)
        self.structure_log.caliper_from_log = False

    def test_depth_of_img_from_log(self):
        # verify that the property is initially set to False, then set it to True
        self.assertEqual(self.structure_log.depth_of_img_from_log, False)
        self.structure_log.depth_of_img_from_log = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.depth_of_img_from_log, False)
        self.structure_log.depth_of_img_from_log = False

    def test_caliper_value(self):
        # verify that the property is initially set to 228.6, then set it to 300
        original_value = self.structure_log.caliper_value
        self.assertEqual(self.structure_log.caliper_value, original_value)
        self.structure_log.caliper_value = 0.30
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.caliper_value, original_value)
        self.structure_log.caliper_value = original_value

    def test_depth_of_img_value(self):
        # verify that the property is initially set to 0, then set it to 50
        self.assertEqual(self.structure_log.depth_of_img_value, 0)
        self.structure_log.depth_of_img_value = 50
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.depth_of_img_value, 0)
        self.structure_log.depth_of_img_value = 0

    def test_slabcore_azimuth(self):
        # verify that the property is initially set to 0, then set it to 60
        self.assertEqual(self.structure_log.slabcore_azimuth, 0)
        self.structure_log.slabcore_azimuth = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.slabcore_azimuth, 0)
        self.structure_log.slabcore_azimuth = 0

    def test_slabcore_style(self):
        # verify that the property is initially set to 0 (Full Size), then set it to 1 (Fixed Size)
        self.assertEqual(self.structure_log.slabcore_style, 0)
        self.structure_log.slabcore_style = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.slabcore_style, 0)
        self.structure_log.slabcore_style = 0

    def test_display_full_partial_picks(self):
        # verify that the property is initially set to 20, then set it to 15
        self.assertEqual(self.structure_log.display_full_partial_picks, True)
        self.structure_log.display_full_partial_picks = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.display_full_partial_picks, True)
        self.structure_log.display_full_partial_picks = True

    def test_display_nodes(self):
        # verify that the property is initially set to 20, then set it to 15
        self.assertEqual(self.structure_log.display_nodes, True)
        self.structure_log.display_nodes = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.structure_log.display_nodes, True)
        self.structure_log.display_nodes = True

    def test_display_opening(self):
        # verify that the property is initially set to False, then set it to True
        self.assertEqual(self.breakout_log.display_opening, False)
        self.breakout_log.display_opening = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.breakout_log.display_opening, False)
        self.breakout_log.display_opening = False

    def test_shading_style(self):
        # verify that the property is initially set to 1 (Solid), then set it to 4 (Downward Diagonal Batch)
        self.assertEqual(self.shading_log.shading_style, 1)
        self.shading_log.shading_style = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.shading_log.shading_style, 1)
        self.shading_log.shading_style = 1

    def test_shading_color(self):
        # verify that the property is initially set to Lime (green), then set it to red
        original_color = 65280
        self.assertEqual(self.shading_log.shading_color, original_color)
        self.shading_log.shading_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.shading_log.shading_color, original_color)
        self.shading_log.shading_color = original_color

    def test_opacity(self):
        # verify that the property is initially set to 100%, then set it to 60%
        self.assertEqual(self.shading_log.opacity, 100)
        self.shading_log.opacity = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.shading_log.opacity, 100)
        self.shading_log.opacity = 100

    def test_top_arrow_shape(self):
        # verify that the property is initially set to 0 (None), then set it to 8 (Full Triangle)
        self.assertEqual(self.gr_litho_interval_log.top_arrow_shape, 0)
        self.gr_litho_interval_log.top_arrow_shape = 8
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.top_arrow_shape, 0)
        self.gr_litho_interval_log.top_arrow_shape = 0

    def test_bottom_arrow_shape(self):
        # verify that the property is initially set to 0 (None), then set it to 8 (Full Triangle)
        self.assertEqual(self.gr_litho_interval_log.bottom_arrow_shape, 0)
        self.gr_litho_interval_log.bottom_arrow_shape = 8
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.bottom_arrow_shape, 0)
        self.gr_litho_interval_log.bottom_arrow_shape = 0

    def test_top_arrow_width(self):
        # verify that the property is initially set to 30, then set it to 60
        self.assertEqual(self.gr_litho_interval_log.top_arrow_width, 30)
        self.gr_litho_interval_log.top_arrow_width = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.top_arrow_width, 30)
        self.gr_litho_interval_log.top_arrow_width = 30

    def test_bottom_arrow_width(self):
        # verify that the property is initially set to 30, then set it to 60
        self.assertEqual(self.gr_litho_interval_log.bottom_arrow_width, 30)
        self.gr_litho_interval_log.bottom_arrow_width = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.bottom_arrow_width, 30)
        self.gr_litho_interval_log.bottom_arrow_width = 30

    def test_top_arrow_height(self):
        # verify that the property is initially set to 30, then set it to 60
        self.assertEqual(self.gr_litho_interval_log.top_arrow_height, 30)
        self.gr_litho_interval_log.top_arrow_height = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.top_arrow_height, 30)
        self.gr_litho_interval_log.top_arrow_height = 30

    def test_bottom_arrow_height(self):
        # verify that the property is initially set to 30, then set it to 60
        self.assertEqual(self.gr_litho_interval_log.bottom_arrow_height, 30)
        self.gr_litho_interval_log.bottom_arrow_height = 60
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.bottom_arrow_height, 30)
        self.gr_litho_interval_log.bottom_arrow_height = 30

    def test_classified(self):
        # verify that the property is initially set to True, then set it to False
        self.assertEqual(self.gr_litho_interval_log.classified, True)
        self.gr_litho_interval_log.classified = False
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.gr_litho_interval_log.classified, True)
        self.gr_litho_interval_log.classified = True

    def test_symbol_style(self):
        # verify that the property is initially set to 0 (None), then set it to 3 (Square)
        self.assertEqual(self.sonic_e1_mud_log.symbol_style, 0)
        self.sonic_e1_mud_log.symbol_style = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.sonic_e1_mud_log.symbol_style, 0)
        self.sonic_e1_mud_log.symbol_style = 0

    def test_symbol_color(self):
        # verify that the property is initially set to blue, then set it to red
        original_value = 16711680
        self.assertEqual(self.sonic_e1_mud_log.symbol_color, original_value)
        self.sonic_e1_mud_log.symbol_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.sonic_e1_mud_log.symbol_color, original_value)
        self.sonic_e1_mud_log.symbol_color = original_value

    def test_symbol_size(self):
        # verify that the property is initially set to 20 (2.0mm), then set it to  40 (4.0mm)
        self.assertEqual(self.sonic_e1_mud_log.symbol_size, 20)
        self.sonic_e1_mud_log.symbol_size = 40
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.sonic_e1_mud_log.symbol_size, 20)
        self.sonic_e1_mud_log.symbol_size = 20

    def test_attach_depth_to(self):
        # verify that the property is initially set to "Middle of Bar" (2), then set it to "Top of Bar" (1)
        self.assertEqual(self.sonic_e1_mud_log.attach_depth_to, 2)
        self.sonic_e1_mud_log.attach_depth_to = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.sonic_e1_mud_log.attach_depth_to, 2)
        self.sonic_e1_mud_log.attach_depth_to = 2

    def test_digits(self):
        # verify that the property is initially set to 2, then set it to  4
        self.assertEqual(self.sonic_e1_mud_log.digits, 2)
        self.sonic_e1_mud_log.digits = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.sonic_e1_mud_log.digits, 2)
        self.sonic_e1_mud_log.digits = 2

    def test_scale(self):
        # disable master scale
        self.depth_log.used_as_depth_scale = False
        # select date/time scale
        self.depth_log.log_unit = "Date/Time"

        # verify that the scale is initially set to 1:20, then set it to  1:30
        self.assertEqual(self.depth_log.scale, 20)
        self.depth_log.scale = 30
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.scale, 20)
        self.depth_log.scale = 20

        # verify that the paper scale unit is set to 1 (foot), then set it to 0 (meter)
        self.assertEqual(self.depth_log.paper_scale_unit, 0)
        self.depth_log.paper_scale_unit = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.paper_scale_unit, 0)
        self.depth_log.paper_scale_unit = 0

        # verify that the data scale unit when using Date/Time is set to 8 (seconds), then set it to 7 (minutes)
        self.assertEqual(self.depth_log.data_scale_unit, 8)
        self.depth_log.data_scale_unit = 7
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.data_scale_unit, 8)
        self.depth_log.data_scale_unit = 8

        # enable master scale
        self.depth_log.used_as_depth_scale = False
        # select depth scale (meters)
        self.depth_log.log_unit = "meters"

    def test_date_time_scale(self):
        # select date/time scale
        self.depth_log.log_unit = "Date/Time"

        # verify that the date format is initially set to 1 (DD/MM/YY), then set it to 4 (DD/MMM/YYYY)
        self.assertEqual(self.depth_log.date_format, 1)
        self.depth_log.date_format = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.date_format, 1)
        self.depth_log.date_format = 1

        # verify that the date frequence (date stamp) is initially set to 0, then set it to 1
        self.assertEqual(self.depth_log.date_stamp, 0)
        self.depth_log.date_stamp = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.date_stamp, 0)
        self.depth_log.date_stamp = 0

        # verify that the date format is initially set to 1 (HH:MM:SS), then set it to 4 (MM:SS.0)
        self.assertEqual(self.depth_log.time_format, 1)
        self.depth_log.time_format = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.time_format, 1)
        self.depth_log.time_format = 1

        # verify that the GMTOffset is initially set to 0, then set it to 10
        self.assertEqual(self.depth_log.gmt_offset, 0)
        self.depth_log.gmt_offset = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.gmt_offset, 0)
        self.depth_log.gmt_offset = 0

        # verify that the starting time is set to 0 second (01/01/1970 at 00:00:00), then set it to 90130 (02/01/1970 at 01:02:10)
        self.assertEqual(self.depth_log.time_zero, 0)
        self.depth_log.time_zero = 90130
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.time_zero, 0)
        self.depth_log.time_zero = 0

        # verify that the horizontal text alignment is initially set to 1 (center), then set it to 0 (left)
        self.assertEqual(self.depth_log.horz_text_align, 1)
        self.depth_log.horz_text_align = 0
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.horz_text_align, 1)
        self.depth_log.horz_text_align = 1

        # verify that the text orientation is initially set to 0 (normal), then set it to 1 (left)
        self.assertEqual(self.depth_log.text_orientation, 0)
        self.depth_log.text_orientation = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.text_orientation, 0)
        self.depth_log.text_orientation = 0

        # select depth scale (meters)
        self.depth_log.log_unit = "meters"

    def test_indicators_per_spacing(self):
        # verify that the property is initially set to 1, then set it to 2
        self.assertEqual(self.depth_log.indicators_per_spacing, 1)
        self.depth_log.indicators_per_spacing = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.indicators_per_spacing, 1)
        self.depth_log.indicators_per_spacing = 1

    def test_ticks_position(self):
        # verify that the property is initially set to 3 (Both), then set it to 2 (Right)
        self.assertEqual(self.depth_log.ticks_position, 3)
        self.depth_log.ticks_position = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.ticks_position, 3)
        self.depth_log.ticks_position = 3

    def test_min_grid_number(self):
        # verify that the property is initially set to 2, then set it to 3
        self.assertEqual(self.depth_log.min_grid_number, 2)
        self.depth_log.min_grid_number = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.min_grid_number, 2)
        self.depth_log.min_grid_number = 2

    def test_maj_grid_number(self):
        # verify that the property is initially set to 1, then set it to 2 (Right)
        self.assertEqual(self.depth_log.maj_grid_number, 1)
        self.depth_log.maj_grid_number = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.maj_grid_number, 1)
        self.depth_log.maj_grid_number = 1

    def test_min_grid_tick_style(self):
        # verify that the property is initially set to 0 (small line), then set it to 2 (small triangle)
        self.assertEqual(self.depth_log.min_grid_tick_style, 0)
        self.depth_log.min_grid_tick_style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.min_grid_tick_style, 0)
        self.depth_log.min_grid_tick_style = 0

    def test_maj_grid_tick_style(self):
        # verify that the property is initially set to 0 (small line), then set it to 2 (small triangle)
        self.assertEqual(self.depth_log.maj_grid_tick_style, 0)
        self.depth_log.maj_grid_tick_style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth_log.maj_grid_tick_style, 0)
        self.depth_log.maj_grid_tick_style = 0

    def test_attach_palette(self):
        self.gr_log.attach_palette("Palette1")

    def test_attach_contact_dictionary(self):
        # Copy the original litho log.
        copied_litho_log = self.litho_borehole.add_log(self.litho_log)

        # Update the litho dictionary.
        new_dict = self.litho_log.attach_contact_dictionary(self.contact_dict)
        self.assertIsInstance(new_dict, wellcad.com.ContactDictionary)

        # Delete the copied litho log.
        self.litho_borehole.remove_log(copied_litho_log.name)

    def test_contact_dictionary(self):
        # Attach a new contact dictionary to the lithological log
        new_dict = self.litho_log.attach_contact_dictionary(self.contact_dict)
        self.assertIsInstance(new_dict, wellcad.com.ContactDictionary)

        # Get the contact dictionary of this log
        dict = self.litho_log.contact_dictionary
        self.assertIsInstance(dict, wellcad.com.ContactDictionary)

        # Create a new lithological log
        new_litho_log = self.litho_borehole.insert_new_log(7)

        # Use the dictionary for this log
        new_litho_log.contact_dictionary = dict
        self.assertEqual(dict.name, new_litho_log.contact_dictionary.name)

    def test_nb_attributes(self):
        # verify that the structure log contains only 1 attribute
        self.assertEqual(self.structure_log.nb_of_attributes, 1)

    def test_left_right_border(self):
        # verify that the left border is the "RHOB" and that the right border is the "NPHI" log
        self.assertEqual(self.shading_log.get_left_border, "RHOB")
        self.assertEqual(self.shading_log.get_right_border, "NPHI")

        # change the left border to "- log border -" and the right border to "RHOB"
        self.shading_log.set_left_right_border("-log border-", "RHOB")

        # verify that the properties has been changed and turn it back to the original value
        self.assertNotEqual(self.shading_log.get_left_border, "RHOB")
        self.assertNotEqual(self.shading_log.get_right_border, "NPHI")
        self.shading_log.set_left_right_border("RHOB", "NPHI")

    def test_remove_component(self):
        # add a new component to an analysis log
        self.analysis_log.trace_length = self.analysis_log.trace_length + 1

        # get the number of components
        nb_comps = self.analysis_log.trace_length
        # remove the newly added attribute
        self.analysis_log.remove_component(nb_comps - 1)

        # get the number of attributes and verify that it is lower than the previous number now that an attribute has been eliminated
        self.assertGreater(nb_comps, self.analysis_log.trace_length)


if __name__ == '__main__':
    unittest.main()
