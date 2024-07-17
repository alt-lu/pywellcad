EnableTrace(true)

Include('database_open.sql')

$VERSID = 75

$Form = select HeaderForm, versID 
+ from Versions
+ where versID = $VERSID
LoadHeaderForm($Form, TRUE)
close($Form)