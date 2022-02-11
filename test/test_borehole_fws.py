import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeFws(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "FWS  4RX Transit Time.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_correct_bad_traces(self):
        self.borehole.correct_bad_traces("RX1")

    def test_stack_traces(self):
        output_log = self.borehole.stack_traces(False, "RX1", False, "NumberOfStacks = 5")
        self.assertIsInstance(output_log, wellcad.com.Log)
        output_log = self.borehole.stack_traces(False, "", False, "NumberOfStacks = 5")
        self.assertIsNone(output_log, wellcad.com.Log)

    def test_reverse_amplitude(self):
        self.borehole.reverse_amplitude("RX1")

    def test_filter_fws_log(self):
        output_log = self.borehole.average_filter_fws_log("RX1", filter_width=8, filter_type=0)
        self.assertIsInstance(output_log, wellcad.com.Log)
        output_log = self.borehole.average_filter_fws_log("RX1", filter_width=14, filter_type=1)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_freq_filter_fws_log(self):
        output_log = self.borehole.freq_filter_fws_log("RX1", 5, 10, 15, 20)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_apply_stand_off_correction(self):
        config = "LogUnit=us,ToolSpacing=0.6,ToolSpacingUnit=m,ToolDiameter=50,ToolDiameterUnit=m,HoleDiameter=100,\
        HoleDiameterUnit=mm,FluidVelocity=1500,FluidVelocityUnit=m/s"
        output_log = self.borehole.apply_stand_off_correction("RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_compensated_velocity(self):
        config = "RX1Log=RX1 - dt,RX1LogUnit=us,RX2Log=RX2 - dt,RX1LogUnit=us,Spacing=0.6,SpacingUnit=m,\
        VelocityUnit=us/m"
        output_log = self.borehole.compensated_velocity("RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_apply_semblance_processing(self):
        config = str(self.fixture_path / "ApplySemblanceProcessing.ini")
        output_log = self.borehole.apply_semblance_processing(False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_process_reflected_tube_wave(self):
        config = "Side=both,Offset=25,Blanking=25,FluidSlowness=696,TxFrequency=15000"
        output_log = self.borehole.process_reflected_tube_wave("RX1", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_pick_first_arrival(self):
        config_file = "file=" + str(self.fixture_path / "FwsFirstArrival.ini")
        config = "Method=Standard Threshold Pickup Algorithm," + config_file
        output_log = self.borehole.pick_first_arrival("RX1", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)
        config = "Method=Advanced Threshold Pickup Algorithm," + config_file
        output_log = self.borehole.pick_first_arrival("RX1", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_pick_first_arrival_documentation(self):
        self.fail("pick_first_arrival chm documentation : [Advanced Threshold Pickup Algorithm] section \
         missing in the config file ")

    def test_cement_bond(self):
        config = "Logs=RX1,AreRadiiSectors=false,EnableT0Gate=true,T0GateStart=100,T0GateLength=25,\
        EnableTXGate=false,TXGateBlanking=0,TXGateThreshold=15,TXGateLength=25,EnableCalibration=false,\
        FreePipeTargetAmplitude=0,FreePipeTargetAmplitudeUnits=mV,BLGateStart=100,BLGateLength=25"
        nb_logs = self.borehole.nb_of_logs
        self.borehole.cement_bond("RX1", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_logs)

    def test_pick_e1_arrival(self):
        config = "PickPositivPolarity=false,FilterWidth=5"
        output_log = self.borehole.pick_e1_arrival("RX1", "RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_adjust_pick_to_extremum(self):
        config = "PickPositivPolarity=false,FilterWidth=5"
        output_log = self.borehole.adjust_pick_to_extremum("RX1", "RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_extract_e1_amplitude(self):
        output_log = self.borehole.extract_e1_amplitude("RX1", "RX1 - dt", False)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_extract_window_peak_amplitude(self):
        config = "WindowStart=100,WindowLength=40,PickMax=true,PickPos=true,EnableResampling=true"
        output_log = self.borehole.extract_window_peak_amplitude("RX1", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_calculate_mechanical_properties(self):
        nb_logs = self.borehole.nb_of_logs
        self.borehole.calculate_mechanical_properties("RX1 - dt", "RX1 - dt")
        self.assertGreater(self.borehole.nb_of_logs, nb_logs)

    def test_integrated_travel_time(self):
        nb_logs = self.borehole.nb_of_logs
        config = "TWT=no,TimeOffset=100"
        self.borehole.integrated_travel_time("RX1 - dt", False, config)
        self.assertGreater(self.borehole.nb_of_logs, nb_logs)

    def test_bond_index(self):
        config = "CementAmplitude=5,FreePipeAmplitude=62.2"
        output_log = self.borehole.bond_index("RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_compressive_strength(self):
        config = "CasingOD=7,CasingWeight=23"
        output_log = self.borehole.compressive_strength("RX1 - dt", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)


if __name__ == '__main__':
    unittest.main()
