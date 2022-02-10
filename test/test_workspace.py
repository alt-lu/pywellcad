import unittest
import wellcad.com
import pathlib
from ._sample_path import SamplePath


class TestWorkspace(unittest.TestCase, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.template = str(cls.fixture_path / "Getting Started FMI.ist")
        cls.config_file = str(cls.fixture_path / "workspace_config.ini")
        cls.sample_path = cls._find_sample_path()

        cls.isi_borehole = cls.app.open_borehole(str(cls.fixture_path / "ISI Workspace Sample.wcl"))
        cls.isi_workspace = cls.isi_borehole.workspace("ISI Test")

        cls.casing_borehole = cls.app.open_borehole(str(cls.fixture_path / "Cased Hole Demo.wcl"))
        cls.casing_workspace = cls.casing_borehole.workspace("Casing Integrity Workspace #1")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_auto_detect_zones(self):
        self.isi_workspace.auto_detect_zones()

    def test_pick_similar_features(self):
        self.isi_workspace.pick_similar_features(config_file_name=self.config_file)  # Should display a dialog because no feature was manually selected.

    def test_representative_picks(self):
        self.isi_workspace.representative_picks(config_file_name=self.config_file)

    def test_automatic_picking(self):
        self.isi_workspace.automatic_picking(config_file_name=self.config_file)

    def test_quick_pick(self):
        self.isi_workspace.quick_pick(config_file_name=self.config_file)

    def test_apply_template(self):
        success = self.isi_workspace.apply_template(self.template, False)
        self.assertEqual(success, True)
        self.fail("ApplyTemplate always display a dialog box, making it impossible to write a fully automatic test")

    def test_auto_joint_detection(self):
        self.casing_workspace.auto_joint_detection(self.config_file)

    def test_add_joint_log_to_b_hole(self):
        self.casing_workspace.add_joint_log_to_b_hole()
        self.assertIsInstance(self.casing_borehole.get_log("Joints"), wellcad.com.Log)
        self.casing_borehole.remove_log("Joints")

    def test_add_engin_log_from_driller_casing_table_to_b_hole(self):
        self.casing_workspace.add_engin_log_from_driller_casing_table_to_b_hole()
        self.assertIsInstance(self.casing_borehole.get_log("#1"), wellcad.com.Log)
        self.casing_borehole.remove_log("#1")

    def test_add_engin_log_from_logger_casing_table_to_b_hole(self):
        self.casing_workspace.add_engin_log_from_logger_casing_table_to_b_hole()
        self.assertIsInstance(self.casing_borehole.get_log("#1"), wellcad.com.Log)
        self.casing_borehole.remove_log("#1")


if __name__ == '__main__':
    unittest.main()
