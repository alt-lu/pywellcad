import pathlib
import unittest
import wellcad.com
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestLogProtection(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"

        cls.litho_borehole = cls.app.open_borehole(str(cls.sample_path / "Core Description.wcl"))
        cls.litho_log = cls.litho_borehole.get_log("lithology")
        cls.volume_analysis_borehole = cls.app.open_borehole(str(cls.sample_path / "Volume Analysis.wcl"))
        cls.formula_log = cls.volume_analysis_borehole.get_log("GR percent")
        cls.classic_borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.gr_log = cls.classic_borehole.get_log("GR")
        cls.fmi_borehole = cls.app.open_borehole(str(cls.sample_path / "FMI and Net Sand Estimation.wcl"))
        cls.structure_log = cls.fmi_borehole.get_log("Structure")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_allow_modify_log_data(self):
        self.litho_log.allow_modify_log_data(False, "Alt123")  # enable protection
        self.litho_borehole.enable_protection(True, "Alt123")
        self.assertAttrNotChanged(self.litho_log.get_litho_bed(0), "litho_code", 'mylithocode')  # Should open a warning dialog and fail to change
        self.litho_borehole.enable_protection(False, "Alt123")  # disable protection
        self.litho_log.allow_modify_log_data(True, "Alt123")
        self.assertAttrChange(self.litho_log.get_litho_bed(0), "litho_code", 'mylithocode')  # Should work

    def test_allow_modify_log_settings(self):
        self.litho_log.allow_modify_log_settings(False, "Alt123")  # enable protection
        self.litho_borehole.enable_protection(True, "Alt123")
        self.assertAttrNotChanged(self.litho_log, "name", "test")  # Should open a warning dialog and fail to change
        self.litho_borehole.enable_protection(False, "Alt123")  # disable protection
        self.litho_log.allow_modify_log_settings(True, "Alt123")
        self.assertAttrChange(self.litho_log, "name", "test")  # Should work


    def test_allow_use_formula(self):
        self.formula_log.allow_use_formula(False, "Alt123")  # enable protection
        self.volume_analysis_borehole.enable_protection(True, "Alt123")
        self.assertAttrNotChanged(self.formula_log, "formula", "{GR}/1000")  # Should open a warning dialog and fail to change
        self.volume_analysis_borehole.enable_protection(False, "Alt123")  # disable protection
        self.formula_log.allow_use_formula(True, "Alt123")
        self.assertAttrChange(self.formula_log, "formula", "{GR}/1000")  # Should work

    def test_allow_view_formula(self):
        self.formula_log.allow_view_formula(False, "Alt123")  # enable protection
        self.volume_analysis_borehole.enable_protection(True, "Alt123")
        self.assertAttrNotChanged(self.formula_log, "formula", "{GR}/1000")  # Should open a warning dialog and fail to change
        self.volume_analysis_borehole.enable_protection(False, "Alt123")  # disable protection
        self.formula_log.allow_view_formula(True, "Alt123")
        self.assertAttrChange(self.formula_log, "formula", "{GR}/1000")  # Should work

    def test_allow_view_log_history(self):
        self.assertAttrChange(self.gr_log, "name", "GRA")
        self.gr_log.allow_view_log_history(False, "Alt123")
        self.classic_borehole.enable_protection(True, "Alt123")
        self.gr_log.history_item_date(0)  # Should open a warning dialog
        self.classic_borehole.enable_protection(False, "Alt123")
        self.gr_log.allow_view_log_history(True, "Alt123")
        self.fail("All method I could find related to history are not affected by allow_view_log_history")

    def test_allow_export_litho_dictionary(self):
        self.litho_log.allow_export_litho_dictionary(False, "Alt123")
        self.litho_log.allow_export_litho_dictionary(True, "Alt123")
        with self.assertRaises(pywintypes.com_error):
            self.structure_log.allow_export_litho_dictionary(True, "Alt123")  # Test on non litho log

    def test_allow_export_attribute_dictionary(self):
        self.structure_log.allow_export_attribute_dictionary(0, False, "Alt123")
        self.structure_log.allow_export_attribute_dictionary(0, True, "Alt123")
        with self.assertRaises(pywintypes.com_error):
            self.formula_log.allow_export_attribute_dictionary(0, True, "Alt123")  # Test on non structure log

    def test_no_export_attribute_dictionary(self):
        self.fail(
            "No way to test allow_export_attribute_dictionary because there is no way to export an attribute dictionary")


if __name__ == '__main__':
    unittest.main()
