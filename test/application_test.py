# imports
import sys
import os
import ctypes
from pywellcad import *

# path to working folder
path = os.getcwd()

# helper definitions
def PrintException(name = ""):   
    print (("EXCEPTION: {} line {}").format(name, sys.exc_info()[-1].tb_lineno)) 

# create application object
obj_wcad = wellcad.Application()

### borehole object testing ###
obj_bhole = obj_wcad.get_active_borehole()

# General document handling     

try:
    obj_bhole.set_draft_mode(2)
except:
    PrintException("SetDraftMode")
    
try:
    obj_bhole.set_visible_depth_range(1.0, 10.0)
except:
    PrintException("SetVisibleDepthRange")
    

try:
    obj_header = obj_bhole.get_header()
except:
    PrintException("GetHeader")
    

try:
    obj_depth = obj_bhole.get_depth()
except:
    PrintException("GetDepth")


try:
    obj_page = obj_bhole.get_page()
except:
    PrintException("GetPage")
 
 
try:
    obj_title = obj_bhole.get_title(0)
except:
    PrintException("Get Title")
 
 
try:
    obj_odbc = obj_bhole.get_odbc()
except:
    PrintException("Get ODBC")

    
    
# General log handling
try:
    obj_log = obj_bhole.convert_log_to("GR", 3, False)
except:
    PrintException("Convert Log To") 

try:
    obj_bhole.clear_log_contents(obj_bhole.nb_of_logs-1) 
except:
    PrintException("Clear Contents")  
    
    
try:
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Remove Log")


# Common log edition
try:
    obj_bhole.slice_log("GR",30.5) 
    obj_bhole.merge_logs("GR#1", "GR#2", True, False)
except:
    PrintException("Slice and Merge")


try:
    obj_bhole.merge_same_log_items("Litho") 
except:
    PrintException("Merge Same Log Items")      


try:
    obj_bhole.extend_log("GR", 0.0, 7.0) 
except:
    PrintException("Extend Log")


try:
    obj_bhole.depth_shift_log("GR", 0.5, 0.0, 5.0) 
except:
    PrintException("Depth Shift Log")


try:
    obj_bhole.depth_match_log("RES","Shift") 
except:
    PrintException("Depth Match Log")
    
    
try:
    obj_bhole.fill_log("Cross Section",
                       0.0,
                       5.0,
                       1.0,
                       False,
                       "Litho") 
except:
    PrintException("Fill Log")

# Common Processes
try:
    obj_log = obj_bhole.filter_log("GR",
                                   False,
                                   "FilterType=Median,\
                                   FilterWidth=15")
    obj_bhole.filter_log_average("Azimuth", 15, True, "degrees")
    obj_bhole.filter_log_median("GR", 15)
    obj_bhole.filter_log_weighted_ave("GR", 15)
except:
    PrintException("Filter Log")


try:
    obj_log = obj_bhole.block_log("GR",
                                   False,
                                   "ReferenceInterval=1,\
                                   Average=yes,\
                                   OutputLogAsText=no,\
                                   OutputLogAsGraphic=yes")
except:
    PrintException("Block Log")


try:
    obj_log = obj_bhole.normalize_perc_log("Compo", False)
except:
    PrintException("Normalize Perc Log")


try:
    obj_log = obj_bhole.normalize_perc_log("Compo", False)
except:
    PrintException("Extract Multi Log Statistics")


try:
    obj_log = obj_bhole.resample_log("GR", False, "SamplingRate=0.2")
except:
    PrintException("Resample Log")
    
    
try:
    obj_log = obj_bhole.interpolate_log("Dens", False, "MaximumGap = 1")
except:
    PrintException("Resample Log")
    

try:
    obj_bhole.borehole_deviation(False,
                                 "MagX=Hx,\
                                  MagY=Hy,\
                                  MagZ=Hz,\
                                  InclX=Gx,\
                                  InclY=Gy,\
                                  InclZ=Gz")  
except:
    PrintException("Borehole Deviation")
    
    
try:
    obj_log = obj_bhole.elog_correction(False, "LogN32=RES,\
                                        ElectrodeSpacingN32=32,\
                                        ElectrodeSpacingN32Unit=in,\
                                        ElectrodeDiameter=1.57,\
                                        ElectrodeDiameterUnit=inch,\
                                        BoreholeDiameter=2.20,\
                                        FluidResistivity=25")
except:
    PrintException("Elog Correction")  

    

# Image & structure logs processes

try:
    obj_bhole.correct_image_traces("AMP")
except:
    PrintException("Correct Bad Traces")


try:
    obj_bhole.conditional_testing("AMP", "AMP", False)
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Conditional Testing")


try:
    obj_bhole.filter_image("AMP", False, "FilterType = Average, FilterWidth = 3, FilterHeight = 3")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Filter Image Log")
    

try:
    obj_log = obj_bhole.mirror_image("AMP")
except:
    PrintException("Mirror Image")


try:
    obj_bhole.rotate_image("AMP", False, "RotateBy = 90, RotateClockwise = yes")
except:
    PrintException("Rotate Image")
    
    
try:
    obj_bhole.orient_image_highside("AMP", False, "MagX=Hx,\
                                    MagY=Hy,\
                                    MagZ=Hz,\
                                    InclX=Gx,\
                                    InclY=Gy,\
                                    InclZ=Gz")
except:
    PrintException("Rotate Image Highside")  
  
 
try:
    obj_bhole.orient_image_north("AMP", False,"MagX=Hx,\
                                 MagY=Hy,\
                                 MagZ=Hz,\
                                 InclX=Gx,\
                                 InclY=Gy,\
                                 InclZ=Gz")
except:
    PrintException("Rotate Image North")   
    

try:
    obj_bhole.normalize_image("AMP", False, "Mode=Static")
except:
    PrintException("Normalize Image")
    

try:
    obj_bhole.image_complexity_map("AMP", False, "LogType=2")
except:
    PrintException("Image Complexity")
    

try:
    obj_bhole.fluid_velocity("TT", False, "TravelTimeUnit=0.1,\
                             ToolRadius=19,\
                             CalibrationPoint1 = 1.0,96,\
                             CalibrationPoint2 = 5.0,96")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Estimate Fluid Velocity")
    

try:
    obj_bhole.acoustic_caliper("TT", False, "TravelTimeUnit=0.1,\
                                ToolRadius=19,\
                                FluidVelocity=1500,\
                                FluidVelocityUnit=m/s")
except:
    PrintException("Calculate Caliper")
    

try:
    obj_bhole.apparent_to_true("Structure", False, "AzimuthLog=Azimuth,\
                                TiltLog=Tilt,\
                                ReferenceIsNorth=yes")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Apparent to True")


try:
    obj_bhole.true_to_apparent("Structure", False, "AzimuthLog=Azimuth,\
                               TiltLog=Tilt,\
                               ReferenceIsNorth=yes")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("True to Apparent")


try:
    obj_bhole.recalculate_structure_azimuth("Structure", False, "Angle=45,\
                                            RotateClockwise=yes")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Recalculate Structure Azimuth")
    

try:
    obj_bhole.recalculate_structure_dip("Structure", False,
                                        "Caliper=150,\
                                        CaliperUnit=mm")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Recalculate Structure Dip")
    

try:
    obj_bhole.remove_structure_dip("Structure", False,
                                   "Azimuth=45,\
                                   Dip=10")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Structural Dip Removal")


try:
    obj_bhole.color_components("OBI", False,
                               "method=2,\
                                model=0")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Extract Color Component")
    

try:
    obj_bhole.brightness_and_contrast("OBI", False)
except:
    PrintException("Brightness and Contrast") 


try:
    obj_bhole.color_classification("OBI", False,f"{path}\ColorClassification.ini")
except:
    PrintException("Color Classification")    
    
    
try:
    obj_bhole.structure_statistics("Structure",False, "Reference=1,\
                                    OutputAverageAzimuth=yes")
except:
    PrintException("Structure Interval Statistics")
    

 try:
    obj_bhole.rqd("Structure",False, "AttributeName1=Type,\
                   AttributeValues1=0-Joint")
except:
    PrintException("RQD")


try:
    obj_bhole.representative_picks("Structure",False,"TiltWindow=5.0,\
                                    AzimuthWindow=15.0,\
                                    DepthWindow=0.5")
except:
    PrintException("Representative Picks")


try:
    obj_bhole.borehole_deviation(False,"MagX=HX, MagY=HY, MagZ=HZ, InclX=GX, InclY=GY, InclZ=GZ")
except:
    PrintException("Borehole Coordinates")
 

try:
    obj_bhole.borehole_coordinates(False,
                                   "AzimuthLog=Azimuth,\
                                   TiltLog=Tilt,\
                                   Method=MinimumCurvature ")
except:
    PrintException("Borehole Coordinates")
    

try:
    obj_bhole.borehole_closure(False,
                               "AzimuthLog=Azimuth,\
                                TiltLog=Tilt,\
                                NorthingLog=Northing,\
                                EastingLog=Easting")
except:
    PrintException("Borehole Closure")
    
    
# cased hole processes

try:
    obj_bhole.dead_sensor_correction("TT", False,
                                     "Method=Automatic,\
                                     ReplaceBy=median")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Dead Sensor Correction")
  
  
try:
    obj_bhole.shift_correction("TT", False,"Zone1 = 0.1,0.3,1144")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Shift Correction")

 
try:
    obj_bhole.centralize("TT", False)
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Centralize")

 
try:
    obj_bhole.casing_thickness("TT", False, "TravelTimeUnit = 0.1")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Casing Thickness")

    
try:
    obj_bhole.metal_loss("TT", False, "InternalPipeRadius = 1100,\
                         ExternalPipeRadius = 2000")

    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Metal Loss")
    

try:
    obj_bhole.radius_to_from_diameter("TT", False, "Method = HalfDiameter")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
    obj_bhole.radius_to_diameter("TT")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
    obj_bhole.diameter_to_radius("TT")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)
except:
    PrintException("Radius and Diameter")


try:
    obj_bhole.outer_inner_radius_diameter("TT", False, "Thickness=200,\
                                          InputType=InnerRadius,\
                                          OutputType=OuterRadius")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Outer Inner Radius Diameter")


try:
    obj_bhole.casing_normalization("TT", False, "Method=Mean")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Casing Normalization")
  

# fws processes

try:
    obj_bhole.correct_fws_traces("RX1")         
except:
    PrintException("Correct Bad Traces FWS")


try:
    obj_bhole.stack_fws_traces("RX1", False, "NumberOfStacks=5")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)    
except:
    PrintException("Stack Traces FWS")
    

try:
    obj_bhole.reverse_fws_amplitude("RX1")         
except:
    PrintException("Reverse Amplitude FWS")


# groundwater processes

try:
    obj_bhole.water_salinity("RES", False,
                             "Temperature=25,\
                             TemperatureUnit=degC")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Water Salinity")
    
    
try:
    obj_bhole.water_resistivity("RES", False,
                                "Temperature=50,\
                                TemperatureUnit=degC,\
                                RefTemperature=25,\
                                RefTemperatureUnit=degC") 
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Water Resistivity")


try:
    obj_log = obj_bhole.shale_volume("GR", False,
                                     "ShaleValueType=1,\
                                     SandstoneValueType=1,\
                                     Equation=0")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Shale Volume")
 
 
try:
    obj_log = obj_bhole.porosity_sonic("DTP", False,
                                       "Method=1,\
                                       MatrixSlowness=50,\
                                       MatrixSlownessUnit=us/ft,\
                                       FluidSlowness=189,\
                                       FluidSlownessUnit=us/ft")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Sonic Porosity")


try:
    obj_log = obj_bhole.porosity_archie("RES", False,
                                        "Method=0,Rw=5,\
                                        RwUnit=ohm.m")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Archie Porosity")
 
 
try:
    obj_log = obj_bhole.porosity_density("Dens", False,
                                         "Method=0,\
                                         MatrixDensity=2.7,\
                                         MatrixDensityUnit=g/cc,\
                                         FluidDensity=1.0,\
                                         FluidDensityUnit=g/cc")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Density Porosity")

    
try:
    obj_log = obj_bhole.porosity_neutron("NPHI", False,
                                         "Vsh=VSH,\
                                         ShaleNPhi=50")
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Neutron Porosity")
   

try:
    obj_log = obj_bhole.permeability("NPHI", False, "CementationFactor=2.0")  
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Permeability") 


try:
    obj_log = obj_bhole.hydraulic_conductivity("K", False,
                                               "Density=1000,\
                                               DensityUnit= kg/m3,\
                                               Viscosity=0.000890439,\
                                               ViscosityUnit=Pa.s")   
    obj_bhole.remove_log(obj_bhole.nb_of_logs-1)           
except:
    PrintException("Hydraulic Conductivity")    
    


# end of the script
try:
    ctypes.windll.user32.MessageBoxW(0, "Proceed to remove docs and close", "End of script", 0)
    # remove all open docs
    for index in range(obj_wcad.borehole_count,0,-1):
        obj_wcad.close_borehole(False, index-1)
        
    obj_wcad.quit(False)
except:
    PrintException("Quit")   
