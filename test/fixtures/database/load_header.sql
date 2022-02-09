# WellCAD ODBC connector script:
# This script loads a version from the database
#
#

######################################################################
# Global defines & switches

$MaxStringSize = 65535
$DepthUnit = m
$Server = Demo
$User = Admin
$Password = 

# Register and open the data source dynamically
$dsnname = DSN=Demo
$driver = Microsoft Access Driver (*.mdb, *.accdb)
$dbq = DBQ=C:\\Users\\arnaud\\source\\repos\\pywellcad\\test\\fixtures\\database\\Demo.mdb
REGISTERDATABASEDYN($driver, $dsnname,$dbq)


# open data source


$dsn = OpenDatabase($Server,$User,false,true,$Password)
EnableTrace(true)

$VERSID = 75

######################################################################
# Load header form
$Form = select HeaderForm, versID 
+ from Versions
+ where versID = $VERSID
LoadHeaderForm($Form, TRUE)
close($Form)



######################################################################
# done
#
