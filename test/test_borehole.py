import unittest
import pathlib
import wellcad.com
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBorehole(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.sample_path = cls._find_sample_path()
        cls.borehole = cls.app.open_borehole(str(cls.fixture_path / "borehole/Well1.wcl"))
        cls.elog_borehole = cls.app.open_borehole(str(cls.fixture_path / "borehole/ElogCorrection.wcl"))
        cls.classic_borehole = cls.app.open_borehole(str(cls.sample_path / "Classic Sample.wcl"))


    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)
    
    def test_invalid_borehole(self):
        self.assertIsNone(wellcad.com.Borehole(None))
    
    def test_name(self):
        self.assertAttrEqual(self.borehole, "name", "Well1.wcl")
        self.assertAttrChange(self.borehole, "name", "Holey McHoleface")
    
    def test_borehole_version(self):
        self.assertIsInstance(self.borehole.version_major, int)
        self.assertIsInstance(self.borehole.version_minor, int)
        self.assertIsInstance(self.borehole.version_build, int)

    def test_extents(self):
        self.assertIsInstance(self.borehole.bottom_depth, float)
        self.assertIsInstance(self.borehole.top_depth, float)

    def test_log_count(self):
        self.assertGreaterEqual(self.borehole.nb_of_logs, 0)
    
    def test_auto_update(self):
        self.borehole.auto_update = False
        self.assertEqual(self.borehole.auto_update, False)
        self.borehole.auto_update = True
        self.assertEqual(self.borehole.auto_update, True)
        self.assertAttrChange(self.borehole, "auto_update", False)
    
    def test_refresh_window(self):
        self.borehole.refresh_window()

    def test_show_window(self):
        self.borehole.show_window()

    def test_set_draft_mode(self):
        self.borehole.set_draft_mode(0)
        self.borehole.set_draft_mode(1)
        self.borehole.set_draft_mode(2)

    def test_set_draft_mode_wrong(self):
        self.borehole.set_draft_mode(4)
    
    def test_minimize_window(self):
        self.borehole.minimize_window()
    
    def test_maximize_window(self):
        self.borehole.maximize_window()

    def test_read_database(self):
        script = str(self.fixture_path / "database/load_header.sql")
        success = self.borehole.read_database(script)
        self.assertEqual(success, True)

    def test_write_database(self):
        script = str(self.fixture_path / "database/store_header.sql")
        success = self.borehole.write_database(script)
        self.assertEqual(success, True)

    def test_set_visible_depth_range(self):
        self.borehole.set_visible_depth_range(10, 20)

    def test_get_depth(self):
        self.assertIsInstance(self.borehole.depth, wellcad.com.Depth)

    def test_get_header(self):
        self.assertIsInstance(self.borehole.header, wellcad.com.Header)

    def test_get_page(self):
        self.assertIsInstance(self.borehole.page, wellcad.com.Page)

    def test_workspace(self):
        config = str(self.fixture_path / "borehole/workspace_settings.ini")
        self.assertIsInstance(self.borehole.create_new_workspace(2, config), wellcad.com.Workspace)
        self.assertIsInstance(self.borehole.workspace(0), wellcad.com.Workspace)

    def test_check_formula(self):
        self.assertEqual(self.borehole.check_formula("({GR}-min({GR}))/(max({GR})- min({GR}))"), True)
        self.assertEqual(self.borehole.check_formula("bad formula"), False)

    def test_get_odbc(self):
        self.assertIsInstance(self.borehole.odbc, wellcad.com.Odbc)

    def test_connect_to(self):
        self.fail("test_connect_to not implemented")

    def test_disconnect_from(self):
        self.fail("test_disconnect_from not implemented")

    def test_save_as(self):
        output = str(self.fixture_path / "borehole/trashme.wcl")
        self.assertTrue(self.borehole.save_as(output))

    def test_file_export(self):
        output = str(self.fixture_path / "borehole/trashme.las")
        ini = str(self.fixture_path / "borehole/file_export.ini")
        self.assertTrue(self.borehole.file_export(output, False, ini))

    def test_do_print(self):
        self.fail("test_do_print not implemented")

    def test_log_by_name(self):
        self.assertIsInstance(self.borehole.get_log("GR"), wellcad.com.Log)

    def test_log_by_index(self):
        self.assertIsInstance(self.borehole.get_log(0), wellcad.com.Log)

    def test_get_log_by_name(self):
        self.assertIsInstance(self.borehole.get_log("GR"), wellcad.com.Log)
    
    def test_get_log_by_index(self):
        self.assertIsInstance(self.borehole.get_log(0), wellcad.com.Log)

    def test_get_title(self):
        self.assertIsInstance(self.borehole.title("GR"), wellcad.com.Title)

    def test_insert_new_log(self):
        self.assertIsInstance(self.borehole.insert_new_log(1), wellcad.com.Log)

    def test_convert_log_to(self):
        self.assertIsInstance(self.borehole.convert_log_to("GR", 3), wellcad.com.Log)

    def test_add_log(self):
        log = self.borehole.get_log("GR")
        duplicate = self.borehole.add_log(log)
        self.assertIsInstance(duplicate, wellcad.com.Log)

    def test_remove_log(self):
        log = self.borehole.get_log("GR")
        log_b = self.borehole.add_log(log)
        nb_of_logs = self.borehole.nb_of_logs
        self.borehole.remove_log(log_b.name)
        self.assertGreater(nb_of_logs, self.borehole.nb_of_logs)

    def test_clear_log_contents(self):
        log = self.borehole.get_log("GR")
        log_b = self.borehole.add_log(log)
        self.assertIsInstance(log_b, wellcad.com.Log)
        nb_of_data = log_b.nb_of_data
        self.borehole.clear_log_contents(log_b.name)
        self.assertGreater(nb_of_data, log_b.nb_of_data)

    def test_apply_template(self):
        self.assertTrue(self.borehole.apply_template(str(self.fixture_path / "borehole/Well1.wdt"), False, True))

    def test_slice_logs(self):
        nb_of_logs = self.borehole.nb_of_logs
        self.borehole.slice_log("GR", 10.0, True, True, True)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_merge_logs(self):
        nb_of_logs = self.borehole.nb_of_logs
        self.borehole.merge_logs("GR#1", "GR#2", True, True)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_merge_same_log_items(self):
        log = self.borehole.get_log("Litho")
        nb_of_data = log.nb_of_data
        self.borehole.merge_same_log_items(log.name)
        self.assertGreater(nb_of_data, log.nb_of_data)

    def test_extend_log(self):
        log = self.borehole.get_log("GR")
        nb_of_data = log.nb_of_data
        self.borehole.extend_log(log.name, top_depth=log.top_depth, bottom_depth=30.0)
        self.assertGreater(log.nb_of_data, nb_of_data)

    def test_depth_shift_log(self):
        self.borehole.depth_shift_log("GR", 2.0)

    def test_depth_match_log(self):
        self.borehole.depth_match_log("Litho", "DepthMatchLog")

    def test_fill_log(self):
        log = self.borehole.get_log("XSection")
        nb_of_data = log.nb_of_data
        self.borehole.fill_log("XSection", 0, 10, 2, 1)
        self.assertGreater(log.nb_of_data, nb_of_data)

    def test_filter_log(self):
        config = "FilterType=Median, FilterWidth=5, CircularData=false"
        self.assertIsInstance(self.borehole.filter_log("GR", False, config), wellcad.com.Log)

    def test_block_log(self):
        self.borehole.block_log("GR", False, "Average=yes, OutputLogAsText=yes")

    def test_extract_well_log_statistics(self):
        nb_of_logs = self.borehole.nb_of_logs
        self.borehole.extract_well_log_statistics("GR", False, "Average=yes")
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_normalize(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "NormalizeAt100=yes,  CreateNewLog=yes, ComponentsToDelete=VCLA"
        self.borehole.normalize("Volume", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)
        self.fail("NormalizeAt100 should be changed in the documentation")

    def test_unit_conversion(self):
        self.assertEqual(self.elog_borehole.get_log("Diam").log_unit, "in")
        config = "Category=Length, FromUnit=in, ToUnit=mm, CreateNewLogs=False"
        self.elog_borehole.unit_conversion("Diam", False, config)
        self.assertEqual(self.elog_borehole.get_log("Diam").log_unit, "mm")
        config = "Category=Length, FromUnit=mm, ToUnit=in, CreateNewLogs=False"
        self.elog_borehole.unit_conversion("Diam", False, config)  # Undo changes
        self.assertEqual(self.elog_borehole.get_log("Diam").log_unit, "in")

    def test_zonation_single_log(self):
        nb_of_logs = self.classic_borehole.nb_of_logs
        logs = "GR"
        config = "NbOutputIntervals=2,IntervalMinThickness=1,UseIntervalThickness=false,UseLithoLogAsOutput=true"
        self.classic_borehole.zonation(logs, False, config)
        self.assertGreater(self.classic_borehole.nb_of_logs, nb_of_logs)

    def test_zonation_multiple_log(self):
        nb_of_logs = self.classic_borehole.nb_of_logs
        logs = ["GR", ]
        config = "NbOutputIntervals=2,IntervalMinThickness=1,UseIntervalThickness=false,UseLithoLogAsOutput=true"
        self.classic_borehole.zonation(logs, False, config)  # TODO figure out why it doesn't work with lists
        self.assertGreater(self.classic_borehole.nb_of_logs, nb_of_logs)

    def test_resample_log(self):
        config = "SamplingRate=0.05"
        self.assertIsInstance(self.borehole.resample_log("GR", False, config), wellcad.com.Log)

    def test_interpolate_log(self):
        config = "MaximumGap=0.25"
        self.assertIsInstance(self.borehole.interpolate_log("GR", False, config), wellcad.com.Log)

    def test_calculate_borehole_deviation(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "MagX=MX, MagY=MY, MagZ=MZ, InclX=AX, InclY=AY, InclZ=AZ, IsAccelerometer=yes,\
                 MagXPositive=yes,MagYPositive=yes,MagZPositive=yes,InclXPositive=yes,InclYPositive=yes,\
                 InclZPositive=yes,MarkerPosition=182.5"
        self.borehole.calculate_borehole_deviation(False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_calculate_borehole_coordinates(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "Method = Classic Tangential, Unit = m, AzimuthLog=Azimuth,TiltLog=Tilt"
        self.borehole.calculate_borehole_coordinates(False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_calculate_borehole_closure(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "AzimuthLog=Azimuth,TiltLog=Tilt,NorthingLog=Northing,EastingLog=Easting"
        self.borehole.calculate_borehole_closure(False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_calculate_borehole_volume(self):
        nb_of_logs = self.elog_borehole.nb_of_logs
        config = "InnerDiam = Diam, InnerDiamUnit = in, AnnularVolume = False"
        self.elog_borehole.calculate_borehole_volume(False, config)
        self.assertGreater(self.elog_borehole.nb_of_logs, nb_of_logs)

    def test_elog_correction(self):
        config = str(self.fixture_path / "borehole/AutoElogCorrection.ini")
        self.assertIsInstance(self.elog_borehole.elog_correction(False, config), wellcad.com.Log)


if __name__ == '__main__':
    unittest.main()
