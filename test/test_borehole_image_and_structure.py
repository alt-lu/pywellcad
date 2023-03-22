import pathlib
import unittest
import wellcad.com
import random
from datetime import datetime, timezone, timedelta
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeImageAndStructure(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.config_file = str(cls.fixture_path / "Process.ini")
        cls.classic_borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))
        cls.structure_borehole = cls.app.open_borehole(str(cls.fixture_path / "Structure.wcl"))
        cls.obi_borehole = cls.app.open_borehole(str(cls.sample_path / "OBI vs. Core.WCL"))
        cls.atv_borehole = cls.app.open_borehole(str(cls.sample_path / "ATV Processing Example.wcl"))
        cls.orient_borehole = cls.app.open_borehole(str(cls.fixture_path / "Orient To Sample.WCL"))
        cls.app.show_window()

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_adjust_image_brightness_and_contrast_auto(self):
        self.obi_borehole.adjust_image_brightness_and_contrast(log="CORE", prompt_user=False)

    def test_apply_structure_true_to_apparent_correction(self):
        log = self.structure_borehole.apply_structure_true_to_apparent_correction("Structure", False, "AzimuthLog=Azimuth,TiltLog=Tilt,ReferenceIsNorth=yes")
        self.assertIsInstance(log, wellcad.com.Log)
        self.structure_borehole.remove_log("Structure#1")

    def test_apply_structure_apparent_to_true_correction(self):
        log = self.structure_borehole.apply_structure_apparent_to_true_correction(log="Structure", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.structure_borehole.remove_log("Structure#1")

    def test_recalculate_structure_azimuth(self):
        self.structure_borehole.recalculate_structure_azimuth(log="Structure", prompt_user=False, config=self.config_file)

    def test_recalculate_structure_dip(self):
        self.structure_borehole.recalculate_structure_dip(log="Structure", prompt_user=False, config=self.config_file)

    def test_remove_structural_dip(self):
        log = self.structure_borehole.remove_structural_dip(log="Structure", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.structure_borehole.remove_log("Structure#1")

    def test_extract_structure_interval_statistic(self):
        log = self.structure_borehole.extract_structure_interval_statistic(log="Structure", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.structure_borehole.remove_log("Ave (3D) Azimuth")
        self.structure_borehole.remove_log("Min Azimuth")

    def test_extract_color_components(self):
        self.obi_borehole.extract_color_components(log="CORE", prompt_user=False)
        self.assertIsInstance(self.obi_borehole.get_log("CORE-R"), wellcad.com.Log)
        self.assertIsInstance(self.obi_borehole.get_log("CORE-G"), wellcad.com.Log)
        self.assertIsInstance(self.obi_borehole.get_log("CORE-B"), wellcad.com.Log)
        self.obi_borehole.remove_log("CORE-R")
        self.obi_borehole.remove_log("CORE-G")
        self.obi_borehole.remove_log("CORE-B")

    def test_color_classification(self):
        self.obi_borehole.color_classification(log="CORE", prompt_user=False, config=self.config_file)
        self.assertIsInstance(self.obi_borehole.get_log("CORE - Classification - Analysis"), wellcad.com.Log)
        self.assertIsInstance(self.obi_borehole.get_log("CORE - Classification - RGB"), wellcad.com.Log)
        self.obi_borehole.remove_log("CORE - Classification - Analysis")
        self.obi_borehole.remove_log("CORE - Classification - RGB")


    def test_representative_picks(self):
        log = self.structure_borehole.representative_picks(log="Structure", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.structure_borehole.remove_log("Structure - Representative Picks")

    def test_image_complexity_map(self):
        self.classic_borehole.image_complexity_map(log="Reflec", prompt_user=False, config=self.config_file)
        self.assertIsInstance(self.classic_borehole.get_log("Reflec - ICM"), wellcad.com.Log)
        self.classic_borehole.remove_log("Reflec - ICM")

    def test_extract_image_log_statistics(self):
        self.classic_borehole.extract_image_log_statistics(log="Reflec", prompt_user=False, config=self.config_file)
        self.assertIsInstance(self.classic_borehole.get_log("Reflec - Max"), wellcad.com.Log)
        self.classic_borehole.remove_log("Reflec - Max")

    def test_normalize_image(self):
        log = self.classic_borehole.normalize_image(log="Reflec", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.classic_borehole.remove_log("Reflec#1")

    def test_orient_image_to_north(self):
        self.orient_borehole.orient_image_to_north(log="Amplitude", prompt_user=False)

    def test_orient_image_to_highside(self):
        self.orient_borehole.orient_image_to_highside(log="Amplitude", prompt_user=False)

    def test_rotate_image(self):
        self.obi_borehole.rotate_image(log="OPTICAL TELEVIEWER", prompt_user=False, config=self.config_file)

    def test_mirror_image(self):
        self.obi_borehole.mirror_image(log="OPTICAL TELEVIEWER")

    def test_filter_image_log(self):
        log = self.classic_borehole.filter_image_log(log="Reflec", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.classic_borehole.remove_log("Reflec - Despiking Filter")

    def test_apply_conditional_testing(self):
        log = self.classic_borehole.apply_conditional_testing(log_if="Reflec", log_then="Reflec", prompt_user=False, config=self.config_file)
        self.assertIsInstance(log, wellcad.com.Log)
        self.classic_borehole.remove_log("Reflec - Conditional testing")

    def test_correct_bad_traces(self):
        self.classic_borehole.correct_bad_traces(log="Reflec")

    def test_rqd(self):
        log = self.atv_borehole.rqd("True Dips", False, "AttributeName1=Type,AttributeValues1=1000,CorePieceLength=0.1,CoreLength=1")
        self.assertIsInstance(log, wellcad.com.Log)
        self.atv_borehole.remove_log("RQD")

    def test_retinex_filter_rgb_log(self):
        log = self.obi_borehole.retinex_filter_rgb_log(log="CORE", prompt_user=False, config="")
        self.assertIsInstance(log, wellcad.com.Log)

    def test_sharpen_rgb_log(self):
        log = self.obi_borehole.sharpen_rgb_log(log="CORE", prompt_user=False, config="")
        self.assertIsInstance(log, wellcad.com.Log)


if __name__ == '__main__':
    unittest.main()
