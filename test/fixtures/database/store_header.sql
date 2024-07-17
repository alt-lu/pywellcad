EnableTrace(true)

Include('database_definition.sql')


######################################################################
# if the version already exist, delete it

# get our WellID from the document header
$RSET = Select Value 
+ From Header 
+ Where Name = 'WELL' 
+ Using $this
$WellID = $RSET.Value
close($RSET )

# get our Run Number from the document header
$RSET = Select Value
+ From Header
+ Where Name = 'RUN'
+ Using $this
$RunID = $RSET.Value
close($RSET)

# get our Version Number from the document header
$RSET = Select Value
+ From Header
+ Where Name = 'VERSION'
+ Using $this
$VersionID = $RSET.Value
close($RSET)

$VERSID = 75


######################################################################
# store header form for each version

$Store = Select HeaderForm, versID
+ From Versions
+ Where versID = $VERSID
StoreHeaderForm($Store)
close($Store)




######################################################################
# done
#




