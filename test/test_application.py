import unittest
import pathlib
import wellcad.com

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = wellcad.com.Application()
        self.fixture_path = pathlib.Path(__file__).parent / "fixtures"
    
    def tearDown(self):
        self.app.quit(False)
    
    def test_show_window(self):
        self.assertTrue(self.app.show_window())
    
    def test_minimize_window(self):
        self.app.minimize_window()
    
    def test_maximize_window(self):
        self.app.maximize_window()
    
    def test_new_borehole(self):
        self.app.new_borehole()
    
    def test_new_borehole_with_template(self):
        self.app.new_borehole(str(self.fixture_path / "Well1.wdt"))
    
    def test_new_borehole_with_bogus_template(self):
        with self.assertRaises(Exception):
            self.app.new_borehole("NonExistentFile.wdt")
    
    def test_close_borehole_without_saving(self):
        self.app.new_borehole()
        self.app.close_borehole(False)
    
    def test_open_existing_borehole(self):
        self.app.open_borehole(str(self.fixture_path / "Well1.wcl"))
    
    def test_open_bogus_borehole(self):
        with self.assertRaises(Exception):
            self.app.open_borehole("NonExistentFile.wcl")
    
    def test_open_borehole_count(self):
        self.assertGreaterEqual(self.app.borehole_count, 0)
    
    def test_get_active_borehole(self):
        self.app.new_borehole()
        self.assertIsInstance(self.app.get_active_borehole(), wellcad.com.Borehole)
    
    def test_get_borehole(self):
        self.app.new_borehole()
        self.assertIsInstance(self.app.get_borehole(0), wellcad.com.Borehole)
    
    def test_get_out_of_range_borehole(self):
        self.app.new_borehole()
        with self.assertRaises(Exception):
            self.app.get_borehole(1000)
    
    def test_file_import(self):
        borehole = self.app.file_import(str(self.fixture_path / "Well1.las"), False)
        self.assertIsInstance(borehole, wellcad.com.Borehole)
        self.app.close_borehole(False)
    
    def test_bogus_file_import(self):
        with self.assertRaises(Exception):
            self.app.file_import("NotAFile.las", False)
    
    def test_multi_file_import(self):
        files = ','.join(str(self.fixture_path / "Well1_Strata.waq") for _ in range(2))
        borehole = self.app.multi_file_import(files, False)
        self.assertIsInstance(borehole, wellcad.com.Borehole)
        self.app.close_borehole(False)
    
    def test_bogus_multi_file_import(self):
        with self.assertRaises(Exception):
            self.app.multi_file_import("NotAFile.waq,AnotherFakeFile.waq", False)


if __name__ == '__main__':
    unittest.main()
