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

### application object testing ###
try:
	obj_wcad.show_window()
except:
	PrintException("ShowWindow")


try:
    obj_wcad.minimize_window()
except:
	PrintException("MinimizeWindow")
   
   
try:
    obj_wcad.maximize_window()
except:
	PrintException("MaximizeWindow")
   
   
try:
    obj_wcad.new_borehole()
except:
	PrintException("NewBorehole")
    
    
try:
    obj_wcad.new_borehole(r"C:\Temp\Well1.wdt")
except:
	PrintException("NewBorehole")
   
   
try:
    obj_wcad.close_borehole(False, 0)
except:
	PrintException("CloseBorehole")

    
try:
    obj_wcad.open_borehole(r"C:\Temp\Well1.wcl")
except:
	PrintException("OpenBorehole")
    
    
try:
    doc_count = obj_wcad.get_borehole_count()
except:
	PrintException("NbOfDocuments")
    
    
try:
    obj_bhole = obj_wcad.get_active_borehole()
    obj_bhole.set_name("Master Test 1")
except:
	PrintException("GetActiveBorehole")


try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_bhole.set_name("Master Test 2")
except:
	PrintException("GetBorehole")


try:
    obj_bhole = obj_wcad.file_import(("{}\Well1.las").format(path), False)
except:
	PrintException("FileImport")


try:
    obj_bhole = obj_wcad.multi_file_import(("{}\Well1.las,"\
                                            "{}\Well1_Strata.csv")\
                                            .format(path, path), False)
except:
	PrintException("MultiFileImport")
    

### borehole object testing ###

# General document handling
try:
    obj_bhole = obj_wcad.get_active_borehole()
    doc_name = obj_bhole.get_name()
except:
	PrintException("GetName")


try:
    obj_bhole = obj_wcad.get_active_borehole()
    obj_bhole.enable_auto_update(False)
    auto_update = obj_bhole.is_auto_update_enabled()
    obj_bhole.enable_auto_update(True)
except:
	PrintException("AutoUpdate")
    
    
try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_bhole.refresh_window()
except:
	PrintException("RefreshWindow")
    

try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_bhole.set_draft_mode(2)
except:
	PrintException("SetDraftMode")
    
    
try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_bhole.minimize_window()
except:
	PrintException("MinimizeWindow")
    
    
try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_bhole.maximize_window()
except:
	PrintException("MaximizeWindow")
    
    
try:
    obj_bhole = obj_wcad.get_borehole(0)
    bot_depth = obj_bhole.get_bottom_depth()
except:
	PrintException("GetBottomDepth")
    

try:
    obj_bhole = obj_wcad.get_borehole(0)
    top_depth = obj_bhole.get_top_depth()
except:
	PrintException("GetTopDepth")
    

try:
    obj_bhole = obj_wcad.get_borehole(2)
    obj_bhole.set_visible_depth_range(100.0, 150.0)
except:
	PrintException("SetVisibleDepthRange")
    
    
try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_depth = obj_bhole.get_depth()
except:
	PrintException("GetDepth")


try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_page = obj_bhole.get_page()
except:
	PrintException("GetPage")
 
 
try:
    obj_bhole = obj_wcad.get_borehole(2)
    obj_title = obj_bhole.get_title(0)
except:
	PrintException("GetPage")
 
 
try:
    obj_bhole = obj_wcad.get_borehole(0)
    obj_page = obj_bhole.get_page()
except:
	PrintException("GetPage") 
    
    
# General log handling

# Common log edition

# end of the script
try:
    ctypes.windll.user32.MessageBoxW(0, "Proceed to remove docs and close", "End of script", 0)
    # remove all open docs
    for index in range(obj_wcad.get_borehole_count(),0,-1):
        obj_wcad.close_borehole(False, index-1)
        
    obj_wcad.quit(False)
except:
	PrintException("Quit")   
