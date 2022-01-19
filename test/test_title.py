import unittest
import wellcad.com
from ._sample_path import SamplePath
from ._extra_asserts import ExtraAsserts


class TestTitle(unittest.TestCase, SamplePath, ExtraAsserts):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.title = cls.borehole.title("GR")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_position(self):
        self.assertAttrEqual(self.title, "left_position", 0.08062253892421722)
        self.assertAttrEqual(self.title, "right_position", 0.14869199693202972)
        self.assertAttrAlmostChange(self.title, "left_position", 0.1, 3)
        self.assertAttrAlmostChange(self.title, "right_position", 0.4, 3)

    def test_swap_left_right(self):
        right = self.title.right_position
        left = self.title.left_position
        self.title.left_position = right + 0.01  # left_position becomes right_position if set to a value greater than current right_position
        self.assertAlmostEqual(self.title.left_position, right, 3)
        self.assertAlmostEqual(self.title.right_position, right + 0.01, 3)
        self.title.left_position = left

    def test_out_of_bounds_position(self):
        left = self.title.left_position
        right = self.title.right_position
        self.title.left_position = -0.1
        self.assertEqual(self.title.left_position, 0.0)
        self.title.right_position = 1.1
        self.assertEqual(self.title.right_position, 1.0)
        self.title.left_position = left
        self.title.right_position = right

    def test_box_height(self):
        self.assertAttrEqual(self.title, "box_height", 200.0)
        self.assertAttrChange(self.title, "box_height", 300.0)

    def test_box_height_clamp(self):
        height = self.title.box_height
        self.title.box_height = 5.0
        self.assertAttrEqual(self.title, "box_height", 10.0)
        self.title.box_height = height

    def test_display_frame(self):
        self.assertAttrEqual(self.title, "display_frame", True)
        self.assertAttrChange(self.title, "display_frame", False)

    def test_display_properties(self):
        self.assertAttrEqual(self.title, "display_properties", True)
        self.assertAttrChange(self.title, "display_properties", False)

    def test_display_title(self):
        self.assertAttrEqual(self.title, "display_title", True)
        self.assertAttrChange(self.title, "display_title", False)

    def test_display_comment(self):
        self.assertAttrEqual(self.title, "display_comment", False)
        self.assertAttrChange(self.title, "display_comment", True)

    def test_use_colored_background(self):
        self.assertAttrEqual(self.title, "use_colored_background", False)
        self.assertAttrChange(self.title, "use_colored_background", True)

    def test_frame_color(self):
        self.assertAttrEqual(self.title, "frame_color", 0)
        self.assertAttrChange(self.title, "frame_color", 150)

    def test_background_color(self):
        self.assertAttrEqual(self.title, "background_color", 16777215)
        self.assertAttrChange(self.title, "background_color", 150)

    def test_frame_width(self):
        self.assertAttrEqual(self.title, "frame_width", 1)
        self.assertAttrChange(self.title, "frame_width", 5)

    def test_frame_style(self):
        self.assertAttrEqual(self.title, "frame_style", 0)
        self.assertAttrChange(self.title, "frame_style", 0)
        self.assertAttrChange(self.title, "frame_style", 1)
        self.assertAttrChange(self.title, "frame_style", 2)
        self.assertAttrChange(self.title, "frame_style", 3)
        self.assertAttrChange(self.title, "frame_style", 4)

    def test_frame_style_out_of_bounds(self):
        self.assertAttrNotChanged(self.title, "frame_style", 9999)

    def test_title_top_bottom(self):
        self.assertAttrEqual(self.title, "title_top", 0.0)
        self.assertAttrEqual(self.title, "title_bottom", 0.4099999666213989)
        self.assertAttrAlmostChange(self.title, "title_top", 0.1, 3)
        self.assertAttrAlmostChange(self.title, "title_bottom", 0.4, 3)

    def test_swap_title_top_bottom(self):
        bottom = self.title.title_bottom
        top = self.title.title_top
        self.title.title_top = bottom + 0.01  # title_top becomes title_bottom if set to a value greater than current title_bottom
        self.assertAlmostEqual(self.title.title_top, bottom, 3)
        self.assertAlmostEqual(self.title.title_bottom, bottom + 0.01, 3)
        self.title.title_top = top

    def test_out_of_bounds_title_position(self):
        top = self.title.title_top
        bottom = self.title.title_bottom
        self.title.title_top = -0.1
        self.assertEqual(self.title.title_top, 0.0)
        self.title.title_bottom = 1.1
        self.assertEqual(self.title.title_bottom, 1.0)
        self.title.title_top = top
        self.title.title_bottom = bottom
        self.assertAttrEqual(self.title, "title_top", top)
        self.assertAttrEqual(self.title, "title_bottom", bottom)

    def test_title_horizontal_position(self):
        self.assertAttrEqual(self.title, "title_horizontal_position", 1)
        self.assertAttrChange(self.title, "title_horizontal_position", 0)
        self.assertAttrChange(self.title, "title_horizontal_position", 1)
        self.assertAttrChange(self.title, "title_horizontal_position", 2)

    def test_title_vertical_position(self):
        self.assertAttrEqual(self.title, "title_vertical_position", 1)
        self.assertAttrChange(self.title, "title_vertical_position", 0)
        self.assertAttrChange(self.title, "title_vertical_position", 1)
        self.assertAttrChange(self.title, "title_vertical_position", 2)

    def test_title_orientation(self):
        self.assertAttrEqual(self.title, "title_orientation", 0)
        self.assertAttrChange(self.title, "title_orientation", 0)
        self.assertAttrChange(self.title, "title_orientation", 1)
        self.assertAttrChange(self.title, "title_orientation", 2)
        self.assertAttrChange(self.title, "title_orientation", 3)

    def test_title_color(self):
        self.assertAttrEqual(self.title, "title_color", 0)
        self.assertAttrChange(self.title, "title_color", 150)

    def test_comment_top_bottom(self):
        self.assertAttrEqual(self.title, "comment_top", 0.3999999761581421)
        self.assertAttrEqual(self.title, "comment_bottom", 0.3999999761581421)
        self.assertAttrAlmostChange(self.title, "comment_top", 0.1, 3)
        self.assertAttrAlmostChange(self.title, "comment_bottom", 0.4, 3)

    def test_swap_comment_top_bottom(self):
        bottom = self.title.comment_bottom
        top = self.title.comment_top
        self.title.comment_top = bottom + 0.01  # comment_top becomes comment_bottom if set to a value greater than current comment_bottom
        self.assertAlmostEqual(self.title.comment_top, bottom, 3)
        self.assertAlmostEqual(self.title.comment_bottom, bottom + 0.01, 3)
        self.title.comment_top = top

    def test_out_of_bounds_comment_position(self):
        top = self.title.comment_top
        bottom = self.title.comment_bottom
        self.title.comment_top = -0.1
        self.assertEqual(self.title.comment_top, 0.0)
        self.title.comment_bottom = 1.1
        self.assertEqual(self.title.comment_bottom, 1.0)
        self.title.comment_top = top
        self.title.comment_bottom = bottom

    def test_comment_horizontal_position(self):
        self.assertAttrEqual(self.title, "comment_horizontal_position", 1)
        self.assertAttrChange(self.title, "comment_horizontal_position", 0)
        self.assertAttrChange(self.title, "comment_horizontal_position", 1)
        self.assertAttrChange(self.title, "comment_horizontal_position", 2)

    def test_comment_vertical_position(self):
        self.assertAttrEqual(self.title, "comment_vertical_position", 1)
        self.assertAttrChange(self.title, "comment_vertical_position", 0)
        self.assertAttrChange(self.title, "comment_vertical_position", 1)
        self.assertAttrChange(self.title, "comment_vertical_position", 2)

    def test_comment_alignment(self):
        self.assertAttrEqual(self.title, "comment_alignment", 1)
        self.assertAttrChange(self.title, "comment_alignment", 0)
        self.assertAttrChange(self.title, "comment_alignment", 1)
        self.assertAttrChange(self.title, "comment_alignment", 2)

    def test_comment_orientation(self):
        self.assertAttrEqual(self.title, "comment_orientation", 0)
        self.assertAttrChange(self.title, "comment_orientation", 0)
        self.assertAttrChange(self.title, "comment_orientation", 1)
        self.assertAttrChange(self.title, "comment_orientation", 2)
        self.assertAttrChange(self.title, "comment_orientation", 3)

    def test_comment_color(self):
        self.assertAttrEqual(self.title, "comment_color", 0)
        self.assertAttrChange(self.title, "comment_color", 150)

    def test_properties_top_bottom(self):
        self.assertAttrEqual(self.title, "properties_top", 0.5999999642372131)
        self.assertAttrEqual(self.title, "properties_bottom", 1.0)
        self.assertAttrAlmostChange(self.title, "properties_top", 0.1, 3)
        self.assertAttrAlmostChange(self.title, "properties_bottom", 0.8, 3)

    def test_swap_properties_top_bottom(self):
        top = self.title.properties_top
        bottom = self.title.properties_bottom
        self.title.properties_bottom = top - 0.01  # properties_top becomes properties_top if set to a value greater than current properties_top
        self.assertAlmostEqual(self.title.properties_bottom , top, 3)
        self.assertAlmostEqual(self.title.properties_top, top - 0.01, 3)
        self.title.properties_bottom = bottom

    def test_out_of_bounds_properties_position(self):
        top = self.title.properties_top
        bottom = self.title.properties_bottom
        self.title.properties_top = -0.1
        self.assertEqual(self.title.properties_top, 0.0)
        self.title.properties_bottom = 1.1
        self.assertEqual(self.title.properties_bottom, 1.0)
        self.title.properties_top = top
        self.title.properties_bottom = bottom
        
    def test_properties_color(self):
        self.assertAttrEqual(self.title, "properties_color", 0)
        self.assertAttrChange(self.title, "properties_color", 150)

    def test_title_font(self):
        self.assertIsInstance(self.title.title_font, wellcad.com.Font)

    def test_comment_font(self):
        self.assertIsInstance(self.title.comment_font, wellcad.com.Font)
        
    def test_properties_font(self):
        self.assertIsInstance(self.title.properties_font, wellcad.com.Font)


if __name__ == '__main__':
    unittest.main()
