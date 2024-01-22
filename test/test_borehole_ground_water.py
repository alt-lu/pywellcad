import pathlib
import unittest

import pywintypes

import wellcad.com
import random
import pywintypes
from ._extra_asserts import ExtraAsserts
from ._sample_path import SamplePath


class TestBoreholeGroundWater(unittest.TestCase, ExtraAsserts, SamplePath):
    @classmethod
    def setUpClass(cls):
        cls.app = wellcad.com.Application()
        cls.sample_path = cls._find_sample_path()
        cls.fixture_path = pathlib.Path(__file__).parent / "fixtures"
        cls.borehole = cls.app.open_borehole(str(cls.fixture_path / "groundwater/groundwater.wcl"))

    @classmethod
    def tearDownClass(cls):
        cls.app.quit(False)

    def test_water_salinity(self):
        config = "Temperature=Temperature (C),TemperatureUnit=degC"
        output_log = self.borehole.water_salinity("Conductivity", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_water_salinity_documentation(self):
        self.fail("water salinity chm documentation : input restricted to conductivity")

    def test_water_resistivity(self):
        config = "Temperature=25,TemperatureUnit=degC,RefTemperature=25,RefTemperatureUnit=degC,Method=0"
        output_log = self.borehole.water_resistivity("Fluid Resistivity", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_water_resistivity_documentation(self):
        self.fail("water_resistivity chm documentation : Method is missing")

    def test_shale_volume(self):
        config = "Equation=0,ShaleValueType=0,Shale=500,ShaleTopDepth=30,ShaleBotDepth=80,\
        SandstoneValueType=2,Sandstone=0,SandstoneTopDepth=160,SandstoneBotDepth=180"
        output_log = self.borehole.shale_volume("Gamma Ray", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_porosity_sonic(self):
        config = "Method=0,MatrixSlowness=50,MatrixSlownessUnit=us/m,FluidSlowness=189,\
        FluidSlownessUnit=us/m,C=0.67,Compaction=1"
        output_log = self.borehole.porosity_sonic("P-Slowness", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_porosity_archie(self):
        config = "Method=0,Rw=Rw,RwUnit=ohm.m,Vsh=0,Rsh=30,RshUnit=ohm.m,CementationFactor=1,\
        CementationExponent=2,Cs=1"
        output_log = self.borehole.porosity_archie("Normal Resistivity", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_porosity_density(self):
        config = "Method=0,MatrixDensity=2.7,MatrixDensityUnit=g/cc,FluidDensity=1.0,\
        FluidDensityUnit=g/cc,ShaleVolume=0,ShaleDensity=1.5,ShaleDensityUnit=g/cc"
        output_log = self.borehole.porosity_density("Bulk Density", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_porosity_neutron(self):
        config = "Vsh=Vsh,ShaleNPhi=50"
        output_log = self.borehole.porosity_neutron("NPhi (Sandstone)", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_permeability(self):
        config = "CementationFactor=1"
        output_log = self.borehole.permeability("DPhi (Sandstone)", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_hydraulic_conductivity(self):
        config = str(self.fixture_path / "groundwater/groundwater.ini")
        output_log = self.borehole.hydraulic_conductivity("Permeability", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

    def test_transmissivity(self):
        config = str(self.fixture_path / "groundwater/transmissivity.ini")
        output_log = self.borehole.transmissivity("Conductivity", False, config)
        self.assertIsInstance(output_log, wellcad.com.Log)

if __name__ == '__main__':
    unittest.main()
