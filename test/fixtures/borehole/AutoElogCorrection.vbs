'==============================================

'Define constants
Set FSO = CreateObject("Scripting.FileSystemObject")
PATH = FSO.GetParentFolderName(wscript.ScriptFullName) & "\"
CONFIGFILE = PATH & "AutoElogCorrection.ini"

'Start WellCAD
Set obWCAD = CreateObject("WellCAD.Application")
obWCAD.ShowWindow()

'Get the document
Set obBHDoc = obWCAD.GetActiveBorehole()
obBHDoc.AutoUpdate = FALSE

Set obLog = obBHDoc.ElogCorrection(FALSE, CONFIGFILE)

obBHDoc.AutoUpdate = TRUE
obBHDoc.RefreshWindow


'don
bOk = MsgBox("Done", vbOkOnly + vbInformation, "AutoElogCorrection")