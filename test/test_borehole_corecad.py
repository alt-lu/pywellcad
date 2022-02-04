import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeCoreCAD(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole_sorting = cls.app.open_borehole(str(cls.fixture_path / "corecad/grain_size_sorting.wcl"))
        cls.borehole_stats = cls.app.open_borehole(str(cls.fixture_path / "corecad/grain_size_statistics.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_extract_grain_size_statistics(self):
        nb_of_logs = self.borehole_stats.nb_of_logs
        config = "Method=0,Mean=true,Median=false,Sorting=false,Skewness=false,Kurtosis=false,Histo=false"
        self.borehole_stats.extract_grain_size_statistics("Grain Size WellLog", False, config)
        self.assertGreater(self.borehole_stats.nb_of_logs, nb_of_logs)

    def test_grain_size_sorting(self):
        config = "BlockedAverage=true"
        output_log = self.borehole_sorting.grain_size_sorting("Minimum", "Maximum",False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)


if __name__ == '__main__':
    unittest.main()
