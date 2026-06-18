import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestDepth(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.depth = cls.borehole.depth
        cls.comment_log = cls.borehole.get_log("Description")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_decimals(self):
        self.assertAttrEqual(self.depth, "decimals", 0)
        self.assertAttrChange(self.depth, "decimals", 1)

    def test_horizontal_grid_spacing(self):
        self.assertAttrEqual(self.depth, "horizontal_grid_spacing", 4.0)
        self.assertAttrChange(self.depth, "horizontal_grid_spacing", 4.5)

    def test_scale(self):
        self.assertAttrEqual(self.depth, "scale", 150.0)
        self.assertAttrChange(self.depth, "scale", 100.0)

    def test_used_as_depth_scale(self):
        self.assertAttrEqual(self.depth, "used_as_depth_scale", True)
        new_depth_log = self.borehole.insert_new_log(17)  # new depth log
        new_depth_log.used_as_depth_scale = True   # Setting the new depth log as depth scale (True) changes the other ones to False
        self.assertAttrEqual(self.depth, "used_as_depth_scale", False)
        self.depth.used_as_depth_scale = True
        self.assertAttrEqual(self.depth, "used_as_depth_scale", True)
        self.assertAttrNotChanged(self.depth, "used_as_depth_scale", False)  # Setting fails because it is the main depth log


    def test_horizontal_grid(self):
        self.assertAttrEqual(self.depth, "horizontal_grid", 2)
        self.assertAttrChange(self.depth, "horizontal_grid", 0)
        self.assertAttrChange(self.depth, "horizontal_grid", 1)
        self.assertAttrChange(self.depth, "horizontal_grid", 2)
        self.assertAttrNotChanged(self.depth, "horizontal_grid", 3)  # out of bounds


    def test_position(self):
        left = self.depth.left_position
        right = self.depth.right_position
        self.assertIsInstance(left, float)
        self.assertIsInstance(right, float)
        self.assertGreaterEqual(right, left)
        new_left = left + 0.1
        new_right = right + 0.15
        self.depth.set_position(new_left, new_right)
        self.assertAlmostEqual(new_left, self.depth.left_position)
        self.assertAlmostEqual(new_right, self.depth.right_position)
        self.depth.left_position = left
        self.depth.right_position = right
        self.assertEqual(left, self.depth.left_position)
        self.assertEqual(right, self.depth.right_position)

    def test_swapped_position(self):
        left = self.depth.left_position
        right = self.depth.right_position

        # Check that positions are swapped if we set left greater than
        # right
        self.depth.set_position(0.5, 0.2)
        self.assertAlmostEqual(self.depth.left_position, 0.2)
        self.assertAlmostEqual(self.depth.right_position, 0.5)

        self.depth.set_position(left, right)

    def test_left_position_greater_than_right(self):
        left = self.depth.left_position
        right = self.depth.right_position

        self.depth.left_position = 0.5
        self.assertAlmostEqual(self.depth.left_position, right)
        self.assertAlmostEqual(self.depth.right_position, 0.5)

        self.depth.set_position(left, right)

    def test_out_of_bounds_position(self):
        left = self.depth.left_position
        right = self.depth.right_position

        # Make sure we can't set positions outside 0.0 to 1.0. Behaviour
        # here is to clamp
        self.depth.left_position = -0.1
        self.assertEqual(self.depth.left_position, 0.0)
        self.depth.right_position = 1.1
        self.assertEqual(self.depth.right_position, 1.0)

        self.depth.set_position(left, right)

    def test_unit(self):
        self.assertAttrEqual(self.depth, "unit", 0)
        self.assertAttrChange(self.depth, "unit", 0)
        self.assertAttrChange(self.depth, "unit", 1)
        self.assertAttrNotChanged(self.depth, "unit", 2)

    def test_set_position(self):
        self.depth.set_position(0.0, 0.15)

    def test_reversed_scale(self):
        # verify that the property is set to False, then set it to True
        self.assertEqual(self.depth.scale_reversed, False)
        self.depth.scale_reversed = True
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.scale_reversed, False)
        self.depth.scale_reversed = False

    def test_paper_scale_unit(self):
        # verify that the paper scale unit is set to 0 (meter), then set it to 2 (inch)
        self.assertEqual(self.depth.paper_scale_unit, 0)
        self.depth.paper_scale_unit = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.paper_scale_unit, 0)
        self.depth.paper_scale_unit = 0

    def test_data_scale_unit(self):
        # verify that the data scale unit is equal to the log unit (meters)
        self.assertEqual(self.depth.data_scale_unit, 0)
        # try to change it and verify that it stays the same
        self.depth.data_scale_unit = 2
        self.assertEqual(self.depth.data_scale_unit, 0)

        # select date/time scale (4)
        self.depth.unit = 4
        # verify that the data scale unit is now 8 (seconds), then change it to 7 (minutes)
        self.assertEqual(self.depth.data_scale_unit, 8)
        self.depth.data_scale_unit = 7
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.data_scale_unit, 8)
        self.depth.data_scale_unit = 8

        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_background_style(self):
        # verify that the background style is set to 1 (Transparent), then set it to 0 (Opaque)
        self.assertEqual(self.depth.background_style, 1)
        self.depth.background_style = 0
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.background_style, 1)
        self.depth.background_style = 1

    def test_date_format(self):
        # select date/time scale (4)
        self.depth.log_unit = 4
        # verify that the date format index is set to 1 (DD/MM/YY), then set it to 4 (DD-MMM-YYYY)
        self.assertEqual(self.depth.date_format, 1)
        self.depth.date_format = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.date_format, 1)
        self.depth.date_format = 1
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_date_stamp(self):
        # select date/time scale (4)
        self.depth.unit = 4
        # verify that the date stamp is set to 0, then set it to 2
        self.assertEqual(self.depth.date_stamp, 0)
        self.depth.date_stamp = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.date_stamp, 0)
        self.depth.date_stamp = 0
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_time_format(self):
        # select date/time scale
        self.depth.unit = 4
        # verify that the time format index is set to 1 (HH:MM:SS), then set it to 4 (MM:SS.0)
        self.assertEqual(self.depth.time_format, 1)
        self.depth.time_format = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.time_format, 1)
        self.depth.time_format = 1
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_time_zero(self):
        # select date/time scale
        self.depth.unit = 4
        # verify that the starting time is set to 0 second (01/01/1970 at 00:00:00), then set it to 90130 (02/01/1970 at 01:02:10)
        self.assertEqual(self.depth.time_zero, 0)
        self.depth.time_zero = 90130
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.time_zero, 0)
        self.depth.time_zero = 0
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_gmt_offset(self):
        # select date/time scale
        self.depth.unit = 4
        # verify that the GMT offset is set to 0 minute, then set it to 10 minutes
        self.assertEqual(self.depth.gmt_offset, 0)
        self.depth.gmt_offset = 10
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.gmt_offset, 0)
        self.depth.gmt_offset = 0
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_horz_text_align(self):
        # select date/time scale
        self.depth.unit = 4
        # verify that the alignment is set to 1 (Center), then set it to 2 (Right)
        self.assertEqual(self.depth.horz_text_align, 1)
        self.depth.horz_text_align = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.horz_text_align, 1)
        self.depth.hor_text_align = 1
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_text_orientation(self):
        # select date/time scale
        self.depth.unit = 4
        # verify that the orientation is set to 0 (Normal), then set it to 2 (Right)
        self.assertEqual(self.depth.text_orientation, 0)
        self.depth.text_orientation = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.text_orientation, 0)
        self.depth.text_orientation = 0
        # return to the original depth scale by selecting the meter unit
        self.depth.unit = 0

    def test_indicators_per_spacing(self):
        # verify that the number of indicators per spacing is set to 1, then set it to 3
        self.assertEqual(self.depth.indicators_per_spacing, 1)
        self.depth.indicators_per_spacing = 3
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.indicators_per_spacing, 1)
        self.depth.indicators_per_spacing = 1

    def test_ticks_position(self):
        # verify that the tick position is set to 3 (Both), then set it to 2 (Right)
        self.assertEqual(self.depth.ticks_position, 3)
        self.depth.ticks_position = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.ticks_position, 3)
        self.depth.ticks_position = 3

    def test_maj_grid_number(self):
        # verify that the number of major grid lines per spacing is set to 1, then set it to 2
        self.assertEqual(self.depth.maj_grid_number, 1)
        self.depth.maj_grid_number = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.maj_grid_number, 1)
        self.depth.maj_grid_number = 1

    def test_min_grid_number(self):
        # verify that the number of minor grid lines per spacing is set to 2, then set it to 1
        self.assertEqual(self.depth.min_grid_number, 2)
        self.depth.min_grid_number = 1
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.min_grid_number, 2)
        self.depth.min_grid_number = 2

    def test_maj_grid_tick_style(self):
        # verify that the major grid tick style is set to 0 (Small Line), then set it to 2 (Small Triangle)
        self.assertEqual(self.depth.maj_grid_tick_style, 0)
        self.depth.maj_grid_tick_style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.maj_grid_tick_style, 0)
        self.depth.maj_grid_tick_style = 0

    def test_min_grid_tick_style(self):
        # verify that the minor grid tick style is set to 0 (Small Line), then set it to 2 (Small Triangle)
        self.assertEqual(self.depth.min_grid_tick_style, 0)
        self.depth.min_grid_tick_style = 2
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.min_grid_tick_style, 0)
        self.depth.min_grid_tick_style = 0

    def test_maj_grid_width(self):
        # verify that the pen width of the major grid lines is set to 1 (0.1 mm), then set it to 4 (0.4 mm)
        self.assertEqual(self.depth.maj_grid_width, 1)
        self.depth.maj_grid_width = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.maj_grid_width, 1)
        self.depth.maj_grid_width = 1

    def test_min_grid_width(self):
        # verify that the pen width of the minor grid lines is set to 1 (0.1 mm), then set it to 4 (0.4 mm)
        self.assertEqual(self.depth.min_grid_width, 1)
        self.depth.min_grid_width = 4
        # verify that the property has been changed and turn it back to the original value
        self.assertNotEqual(self.depth.min_grid_width, 1)
        self.depth.min_grid_width = 1

    def test_maj_grid_color(self):
        init_color = self.depth.maj_grid_color
        # set the color of the major grid lines to red
        self.depth.maj_grid_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value (Lavender)
        self.assertNotEqual(self.depth.maj_grid_color, init_color)
        self.depth.maj_grid_color = init_color

    def test_min_grid_color(self):
        init_color = self.depth.min_grid_color
        # set the color of the minor grid lines to red
        self.depth.min_grid_color = 0x0000ff
        # verify that the property has been changed and turn it back to the original value (Lavender)
        self.assertNotEqual(self.depth.min_grid_color, init_color)
        self.depth.min_grid_color = init_color

    def test_depth_font(self):
        # Get depth font
        font = self.depth.depth_font

        # Verify the font properties
        self.assertIsInstance(font, wellcad.com.Font)
        self.assertEqual(font.italic, False)

        # Get the font of the comment log
        comment_font = self.comment_log.font
        comment_font.italic = True
        self.assertIsInstance(font, wellcad.com.Font)

        # Assign this font to the depth column
        self.depth.depth_font = comment_font

        # Verify that the depth font of the depth column has changed
        self.assertEqual(self.depth.depth_font.italic, True)


if __name__ == '__main__':
    unittest.main()
