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
obj_wcad.show_window()
obj_bhole = obj_wcad.open_borehole(r"C:\Users\micha\Documents\Projects\pywellcad\master_test_scripts\Well1.wcl")
obj_log = obj_bhole.get_log("GR")

### log object testing ###
"""
try:
    obj_log.file_export(r"C:\Temp\Well1.wcl", False, r"C:\Temp\Well1.ini", "LAS")
except:
	PrintException("ShowWindow")

try:
    obj_log.nb_of_data()
except:
	PrintException("ShowWindow")

try:
    obj_log.set_name("blabla")
except:
	PrintException("ShowWindow")

try:
    obj_log.get_title_comment()
except:
    PrintException("ShowWindow")

try:
    obj_log.get_title_comment()
except:
    PrintException("ShowWindow")

try:
    obj_log.top_depth()
except:
	PrintException("ShowWindow")

try:
    obj_log.bottom_depth()
except:
	PrintException("ShowWindow")

try:
    obj_log.do_settings_dlg()
except:
	PrintException("ShowWindow")

try:
    obj_log.get_data_table()
except:
	PrintException("ShowWindow")

# PROBLEME !!!!!!!!
try:
    obj_log.set_data_table()
except:
	PrintException("ShowWindow")

try:
    obj_log.set_position(3, 4)
except:
	PrintException("ShowWindow")


try:
    obj_log.data_min()
except:
	PrintException("ShowWindow")

try:
    obj_log.data_max()
except:
	PrintException("ShowWindow")


try:
    obj_log.set_log_unit("csv")
except:
	PrintException("ShowWindow")

try:
    obj_log.get_log_unit()
except:
	PrintException("ShowWindow")


try:
    obj_log.set_left_position(0.3)
except:
	PrintException("ShowWindow")

try:
    obj_log.get_left_position()
except:
	PrintException("ShowWindow")
	


try:
    obj_log.set_right_position(0.3)
except:
	PrintException("ShowWindow")

try:
    obj_log.get_right_position()
except:
	PrintException("ShowWindow")

try:
    obj_log.set_position(0,0.1)
except:
	PrintException("ShowWindow")
	
try:
    obj_log.type()
except:
	PrintException("ShowWindow")



try:
    obj_log.hide_log_title()
except:
	PrintException("ShowWindow")

try:
    obj_log.set_border_style(1)
except:
	PrintException("ShowWindow")

try:
    obj_log.get_border_style()
except:
	PrintException("ShowWindow")
	
try:
    obj_log.hide_log_data()
except:
	PrintException("ShowWindow")


try:
    obj_log.display_border()
except:
	PrintException("ShowWindow")

try:
    obj_log.clear_history()
except:
	PrintException("ShowWindow")

try:
    obj_log.nb_of_history_item()
except:
	PrintException("ShowWindow")
	


try:
    obj_log.history_item_date(1)
except:
	PrintException("ShowWindow")

try:
    obj_log.history_item_description(1)
except:
    PrintException("ShowWindow")

try:
    obj_log.get_null_value()
except:
    PrintException("ShowWindow")
    

try:
    obj_log.set_null_value(1.1)
except:
    PrintException("ShowWindow")

try:
    obj_log.mask_contacts()
except:
    PrintException("ShowWindow")

try:
    obj_log.mask_horizontal_grid()
except:
    PrintException("ShowWindow")


try:
    obj_log.get_sample_rate()
except:
    PrintException("ShowWindow")

try:
    obj_log.set_sample_rate(0.1)
except:
    PrintException("ShowWindow")

try:
    obj_log.scale_low(1.1)
except:
    PrintException("ShowWindow")

try:
    obj_log.scale_high(1.1)
except:
    PrintException("ShowWindow")
    


try:
    obj_log.get_scale_mode()
except:
    PrintException("ShowWindow")

try:
    obj_log.set_scale_mode(0)
except:
    PrintException("ShowWindow")


try:
    obj_log.scale_reversed()
except:
    PrintException("ShowWindow")

try:
    obj_log.use_log_colored_background()
except:
    PrintException("ShowWindow")

try:
    obj_log.grid_enable()
except:
    PrintException("ShowWindow")

try:
    obj_log.maj_grid_spacing(0.2)
except:
    PrintException("ShowWindow")

try:
    obj_log.min_grid_spacing(0.2)
except:
    PrintException("ShowWindow")
    

try:
    obj_log.lock_log_data()
except:
    PrintException("ShowWindow")

try:
    obj_log.data(0)
except:
    PrintException("ShowWindow")

try:
    obj_log.data_depth(0)
except:
    PrintException("ShowWindow")

try:
    obj_log.data_at_depth(1.2)
except:
    PrintException("ShowWindow")


try:
    obj_log.insert_data_at_depth(1.2, 0.2)
except:
    PrintException("ShowWindow")

try:
    obj_log.insert_data(0, 1.1)
except:
    PrintException("ShowWindow")

#try:
#    obj_log.get_formula()
#except:
#    PrintException("ShowWindow")

#try:
#    obj_log.set_formula("GR*2")
#except:
#    PrintException("ShowWindow")

try:
    obj_log.get_filter()
except:
    PrintException("ShowWindow")

try:
    obj_log.set_filter(3)
except:
    PrintException("ShowWindow")
"""
#try:
#    obj_log.log_background_color(3, 4, 255)
#except:
#	PrintException("ShowWindow")


# end of the script
try:
    ctypes.windll.user32.MessageBoxW(0, "Proceed to remove docs and close", "End of script", 0)
    # remove all open docs
    for index in range(obj_wcad.get_borehole_count(),0,-1):
        obj_wcad.close_borehole(False, index-1)
        
    obj_wcad.quit(False)
except:
	PrintException("Quit")