import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeNmr(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.sample_path / "BMR Water Well Example.wcl"))
        cls.borehole_proc = cls.app.open_borehole(str(cls.fixture_path / "nmr/nmr.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_process_nmrsa_data(self):
        nb_logs = self.borehole_proc.nb_of_logs
        config = "UseDefautOuputs=yes"
        self.borehole_proc.process_nmrsa_data("NMR", False, config)
        self.assertGreater(self.borehole_proc.nb_of_logs, nb_logs)

    def test_nmr_total_porosity(self):
        config = "MaxCutoffValue=-1, UseTimeMaxCutoff=yes"
        output_log = self.borehole.nmr_total_porosity("T2DIST", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_nmr_total_porosity_documentation(self):
        self.fail("NMRTotalPorosity missing in the chm documentation")

    def test_nmr_permeability(self):
        config = "T2DistributionTraceUnit=seconds,UseTimeMaxCutoff=true,MaxCutoffValue=0, \
        DisplayTIMModel=true,VariableCforTIMModel=1,ExponentMforTIMModel=4,BFVCutoffForTIMModel=2, \
        BFVCutoffForTIMModel=0.3,FFVCutoffForTIMModel=0,DisplaySDRModel=true,VariableCforSDRModel=4, \
        ExponentMforSDRModel=4,ExponentNforSDRModel=2,DisplayT2LogMean=false"
        output_log = self.borehole.nmr_permeability("T2DIST", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_nmr_permeability_documentation(self):
        self.fail("NMRPermeability missing in the chm documentation")

    def test_nmr_fluid_volumes(self):
        config = "UseLithoDatabaseAssociatedColor=yes,Components=Bound Water,Moveable Water,\
        Cutoff=3,5"
        output_log = self.borehole.nmr_fluid_volumes("T2DIST", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_nmr_fluid_volumes_missing_doc(self):
        self.fail("NMRFluidVolumes missing in the chm documentation")


if __name__ == '__main__':
    unittest.main()