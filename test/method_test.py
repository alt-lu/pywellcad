# imports
from pywellcad import *
import os

path = os.getcwd()

# create application object
obj_wcad = wellcad.Application()
obj_wcad.maximize_window()
obj_bhole = obj_wcad.open_borehole(r"C:\Temp\Well1.wcl")

#test method
obj_bhole = obj_wcad.get_active_borehole()
obj_bhole.reverse_fws_amplitude("RX1") 