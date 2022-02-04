import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeGamma(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.fixture_path / "spectral_gamma/spectral_gamma.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_apply_natural_gamma_borehole_correction(self):
        config = "EnableDeadTime=true,DeadTime=5,EnableFactors=true,Top1=0,Bot1=100,\
        FactorName1=K1,Factor1-1=1,FactorName2=K2,Factor2-1=1.12"
        output_log = self.borehole.apply_natural_gamma_borehole_correction("Spectrum - Stabilized", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_apply_total_gamma_calibration(self):
        config = "K-Factor=2*0.00001028"
        output_log = self.borehole.apply_total_gamma_calibration("GR", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_apply_total_gamma_calibration_documentation(self):
        self.fail("chm documentation : should return a log")

    def test_calculate_spectrum_total_count(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "UseWindow=true,WinLow=25,WinHigh=200,Channel=true,Total=true,\
        Min=false,Max=false,Ave=false,Median=false"
        self.borehole.calculate_spectrum_total_count("Spectrum - Stabilized", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_spectrometric_ratios(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "A=K,B=U"
        self.borehole.spectrometric_ratios("K", "U", "Th", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_process_medusa_spectrum_data(self):
        nb_of_logs = self.borehole.nb_of_logs
        calib_file = str(self.fixture_path / "spectral_gamma/QL40-SGR-210304.mcf")
        config = "CalibrationFilePath=" + calib_file
        config = config + "WinHigh=5,EnableFittedSpectrum=true,EnableStabilizationFactor=true,"
        config = config + "EnableConcentrationErrors=true,HoleDiameter=100,"
        config = config + "CasingThickness=,CasingType=0,FluidDensity=1.1,FluidK=0,FluidU=0,FluidTh=0,ToolPosition=1"
        self.borehole.process_medusa_spectrum_data("Spectrum", "LiveTime", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_process_spectrum_data(self):
        nb_of_logs = self.borehole.nb_of_logs
        calib_file = str(self.fixture_path / "spectral_gamma/SpecG.sgm")
        config = "ProcessModel =" + calib_file
        self.borehole.process_spectrum_data("Spectrum", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_compute_gr(self):
        calib_file = str(self.fixture_path / "spectral_gamma/QL40-SGR-210304.mcf")
        config = "CalibrationFilePath=" + calib_file
        output_log = self.borehole.compute_gr("K", "U", "Th", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)


if __name__ == '__main__':
    unittest.main()
