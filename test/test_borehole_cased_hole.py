import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeCasedHole(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.fixture_path / "borehole-casedhole/cased_hole.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_correct_dead_sensor(self):
        config = "Method=Automatic, ReplaceBy=Average, WindowHeight=1.2, MinDataHeight=1.0, Discrimination=0.125"
        output_log = self.borehole.correct_dead_sensor("TravelTime", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_shift_correction(self):
        config = "Zone1=ref1, 24.5, 26.0, 93, Zone2=ref2, 44.5, 45.1, 90,\
                 OutputCorrections = yes, ExtendTrends = yes"
        output_log = self.borehole.shift_correction("TravelTime", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_calculate_fluid_velocity(self):
        config = "TravelTimeUnit = 0.1, ToolRadius = 19, TimeWindow = WndTime, CalibrationPoint1 = 20.44, 96,\
                 CalibrationPoint2 = 36.85, 96, ExtendTrends = yes"
        output_log = self.borehole.calculate_fluid_velocity("TravelTime", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_centralize(self):
        config = "UseRange=no, OutputEccentricity=yes"
        output_log = self.borehole.centralize("TravelTime", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_calculate_acoustic_caliper(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "TravelTimeUnit = 1, CaliperUnit=mm, ToolRadius = 19, TimeWindow = WndTime,\
                 FluidVelocity = 1480, FluidVelocityUnit= m/s, CurveOutput=no, ImageOutput=yes"
        output_log = self.borehole.calculate_acoustic_caliper("TravelTime", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_calculate_casing_thickness(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "TravelTimeUnit = 1, ThicknessUnit=mm, SteelVelocity=5850, SteelVelocityUnit=m/s,\
                 CurveOutput=no, ImageOutput=yes"
        output_log = self.borehole.calculate_casing_thickness("ThicknessTTime", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

    def test_calculate_apparent_metal_loss(self):
        config = "InternalPipeRadius=78, ExternalPipeRadius=100"
        output_log = self.borehole.calculate_apparent_metal_loss("IR", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_radius_to_from_diameter(self):
        config = "Method = TwoTimesRadius"
        output_log = self.borehole.radius_to_from_diameter("IR", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_outer_inner_radius_diameter(self):
        config = "Thickness = THK, InputType = InnerRadius, OutputType = OuterDiameter"
        output_log = self.borehole.outer_inner_radius_diameter("IR", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_cased_hole_normalization(self):
        config = "Method=Median, Value=10.5"
        output_log = self.borehole.cased_hole_normalization("IR", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_cased_hole_ultrasonics(self):
        nb_of_logs = self.borehole.nb_of_logs
        config = "Thickness=yes, Cadi=yes, Score=yes"
        self.borehole.cased_hole_ultrasonics("Wavelet", "Zones", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_of_logs)

if __name__ == '__main__':
    unittest.main()