# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
# From type library 'WellCAD.tlb'
# On Fri Dec  3 13:46:20 2021
'WellCAD Object Library'
makepy_version = '0.5.01'
python_version = 0x30806f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{7235A6E1-ADF3-11CE-BCC2-444553540000}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class Borehole(DispatchBaseClass):
	'Borehole Object'
	CLSID = IID('{7235A6E2-ADF3-11CE-BCC2-444553540000}')
	coclass_clsid = IID('{7235A6E0-ADF3-11CE-BCC2-444553540000}')

	def AddLog(self, Log=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((9, 0),),Log
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddLog', None)
		return ret

	def AdjustImageBrightnessAndContrast(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((12, 16), (12, 16)),vLog
			, vPromptUser)

	def AdjustPickToExtremum(self, vFWSLog=defaultNamedOptArg, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(58, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vFWSLog
			, vLog, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'AdjustPickToExtremum', None)
		return ret

	def AllowExportFile(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(93, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowInsertAnnotation(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(96, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowInsertLog(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(91, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowModifyAnnotation(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(97, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowModifyHeadersContent(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(95, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowSaveTemplate(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(92, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def ApplyConditionalTesting(self, vLog1=defaultNamedOptArg, vLog2=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(36, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vLog1
			, vLog2, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyConditionalTesting', None)
		return ret

	def ApplyNaturalGammaBoreholeCorrection(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(67, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyNaturalGammaBoreholeCorrection', None)
		return ret

	def ApplySemblanceProcessing(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(60, LCID, 1, (9, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplySemblanceProcessing', None)
		return ret

	def ApplyStandOffCorrection(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(55, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyStandOffCorrection', None)
		return ret

	def ApplyStructureApparentToTrueCorrection(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(33, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyStructureApparentToTrueCorrection', None)
		return ret

	def ApplyStructureTrueToApparentCorrection(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyStructureTrueToApparentCorrection', None)
		return ret

	def ApplyTemplate(self, szPath=defaultNamedNotOptArg, vPromptIfNotFound=defaultNamedOptArg, vCreateNewLogs=defaultNamedOptArg, vCreateNewLayers=defaultNamedOptArg
			, vApplySettingsToAnnotations=defaultNamedOptArg, vReplaceHeader=defaultNamedOptArg, vKeepExistingCharts=defaultNamedOptArg, vCreateNewCharts=defaultNamedOptArg, vKeepExistingWS=defaultNamedOptArg
			, vCreateNewWS=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (11, 0), ((8, 0), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16), (12, 16)),szPath
			, vPromptIfNotFound, vCreateNewLogs, vCreateNewLayers, vApplySettingsToAnnotations, vReplaceHeader
			, vKeepExistingCharts, vCreateNewCharts, vKeepExistingWS, vCreateNewWS, vConfigFilename
			)

	def ApplyTotalGammaCalibration(self, vLog=defaultNamedNotOptArg, vPromptUser=defaultNamedNotOptArg, vConfigFilename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(74, LCID, 1, (9, 0), ((12, 0), (12, 0), (12, 0)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ApplyTotalGammaCalibration', None)
		return ret

	def BlockLog(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def CalculateAcousticCaliper(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def CalculateApparentMetalLoss(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(37, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CalculateApparentMetalLoss', None)
		return ret

	def CalculateBoreholeClosure(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(65, LCID, 1, (24, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)

	def CalculateBoreholeCoordinates(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(64, LCID, 1, (24, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)

	def CalculateBoreholeDeviation(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(63, LCID, 1, (24, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)

	def CalculateBoreholeVolume(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)

	def CalculateCasingThickness(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def CalculateFluidVelocity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(38, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CalculateFluidVelocity', None)
		return ret

	def CalculateMechanicalProperties(self, vLogP=defaultNamedOptArg, vLogS=defaultNamedOptArg, vLogDens=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLogP
			, vLogS, vLogDens)

	def CalculateSpectrumTotalCount(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(66, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def CasedHoleNormalization(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(111, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CasedHoleNormalization', None)
		return ret

	def CementBond(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._ApplyTypes_(131, 1, (16408, 0), ((12, 16), (12, 16), (12, 16)), 'CementBond', None,vLog
			, vPromptUser, vConfigFilename)

	def Centralize(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'Centralize', None)
		return ret

	def CentralizeImageData(self, vLog=defaultNamedOptArg, vCaliperLow=defaultNamedOptArg, vCaliperHigh=defaultNamedOptArg, vPromptUser=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(40, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vLog
			, vCaliperLow, vCaliperHigh, vPromptUser)
		if ret is not None:
			ret = Dispatch(ret, 'CentralizeImageData', None)
		return ret

	def CheckFormula(self, szFormula=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 0),),szFormula
			)

	def ClearLogContents(self, vLog=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(87, LCID, 1, (24, 0), ((12, 0),),vLog
			)

	def ColorClassification(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(115, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ColorClassification', None)
		return ret

	def CompensatedVelocity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(132, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CompensatedVelocity', None)
		return ret

	def ComputeGR(self, vLog1=defaultNamedOptArg, vLog2=defaultNamedOptArg, vLog3=defaultNamedOptArg, vPromptUser=defaultNamedOptArg
			, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(125, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)),vLog1
			, vLog2, vLog3, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ComputeGR', None)
		return ret

	def ConnectTo(self, szServerType=defaultNamedNotOptArg, szServerAddress=defaultNamedNotOptArg, nPort=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(76, LCID, 1, (11, 0), ((8, 0), (8, 0), (3, 0)),szServerType
			, szServerAddress, nPort)

	def ConvertLogTo(self, vLogToConvert=defaultNamedNotOptArg, viLogType=defaultNamedNotOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(72, LCID, 1, (9, 0), ((12, 0), (12, 0), (12, 16), (12, 16)),vLogToConvert
			, viLogType, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertLogTo', None)
		return ret

	def CorrectBadTraces(self, vLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((12, 16),),vLog
			)

	def CorrectDeadSensor(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(86, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def CreateNewWorkspace(self, iWSType=defaultNamedNotOptArg, vConfigFilename=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(99, LCID, 1, (9, 0), ((2, 0), (12, 0)),iWSType
			, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CreateNewWorkspace', None)
		return ret

	def CrossCorrelate(self, vLogReference=defaultNamedOptArg, vLogTarget=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(104, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vLogReference
			, vLogTarget, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'CrossCorrelate', None)
		return ret

	def DepthMatchLog(self, LogToMatch=defaultNamedOptArg, DepthLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(73, LCID, 1, (24, 0), ((12, 16), (12, 16)),LogToMatch
			, DepthLog)

	def DepthShiftLog(self, vLog=defaultNamedNotOptArg, fDepthShift=defaultNamedNotOptArg, vTopDepth=defaultNamedOptArg, vBotDepth=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(81, LCID, 1, (24, 0), ((12, 0), (4, 0), (12, 16), (12, 16)),vLog
			, fDepthShift, vTopDepth, vBotDepth)

	def DisconnectFrom(self, szServerType=defaultNamedNotOptArg, szServerAddress=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(77, LCID, 1, (11, 0), ((8, 0), (8, 0)),szServerType
			, szServerAddress)

	def DoPrint(self, vPrintDlg=defaultNamedOptArg, vStartDepth=defaultNamedOptArg, vEndDepth=defaultNamedOptArg, vNbOfCopies=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vPrintDlg
			, vStartDepth, vEndDepth, vNbOfCopies)

	def ElogCorrection(self, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(114, LCID, 1, (9, 0), ((12, 16), (12, 16)),vPromptUser
			, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ElogCorrection', None)
		return ret

	def EnableProtection(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(94, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def ExtendLog(self, vLog=defaultNamedNotOptArg, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(70, LCID, 1, (24, 0), ((12, 0), (4, 0), (4, 0)),vLog
			, fTopDepth, fBottomDepth)

	def ExtractColorComponents(self, vLog=defaultNamedOptArg, vMethod=defaultNamedOptArg, vColorModel=defaultNamedOptArg, vPromptUser=defaultNamedOptArg
			, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(98, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)),vLog
			, vMethod, vColorModel, vPromptUser, vConfigFilename)

	def ExtractE1Amplitude(self, vFWSLog=defaultNamedOptArg, vE1Log=defaultNamedOptArg, vPromptUser=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(57, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vFWSLog
			, vE1Log, vPromptUser)
		if ret is not None:
			ret = Dispatch(ret, 'ExtractE1Amplitude', None)
		return ret

	def ExtractGrainSizeStatistics(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._ApplyTypes_(126, 1, (16408, 0), ((12, 16), (12, 16), (12, 16)), 'ExtractGrainSizeStatistics', None,vLog
			, vPromptUser, vConfigFilename)

	def ExtractImageLogStatistics(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def ExtractRGBValues(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(85, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def ExtractStructureIntervalStatistic(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ExtractStructureIntervalStatistic', None)
		return ret

	def ExtractWellLogStatistics(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(89, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def ExtractWindowPeakAmplitude(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(52, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ExtractWindowPeakAmplitude', None)
		return ret

	def FileExport(self, vDataFilename=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg, vLogFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vDataFilename
			, vPromptUser, vConfigFilename, vLogFilename)

	def FillLog(self, vLog=defaultNamedNotOptArg, fTopDepth=defaultNamedNotOptArg, fBotDepth=defaultNamedNotOptArg, fStep=defaultNamedNotOptArg
			, fThickness=defaultNamedNotOptArg, vIntervalUserDefined=defaultNamedOptArg, vIntervalLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(88, LCID, 1, (24, 0), ((12, 0), (4, 0), (4, 0), (4, 0), (4, 0), (12, 16), (12, 16)),vLog
			, fTopDepth, fBotDepth, fStep, fThickness, vIntervalUserDefined
			, vIntervalLog)

	def FilterFWSLog(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(50, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'FilterFWSLog', None)
		return ret

	def FilterImageLog(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'FilterImageLog', None)
		return ret

	def FilterLog(self, vLog=defaultNamedNotOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(26, LCID, 1, (9, 0), ((12, 0), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'FilterLog', None)
		return ret

	def GrainSizeSorting(self, vLog1=defaultNamedOptArg, vLog2=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(129, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vLog1
			, vLog2, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'GrainSizeSorting', None)
		return ret

	def HydraulicConductivity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(117, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'HydraulicConductivity', None)
		return ret

	def InsertNewLog(self, iLogType=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((2, 0),),iLogType
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewLog', None)
		return ret

	def IntegratedTravelTime(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(128, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'IntegratedTravelTime', None)
		return ret

	def InterpolateLog(self, vLog=defaultNamedNotOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(83, LCID, 1, (9, 0), ((12, 0), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'InterpolateLog', None)
		return ret

	# The method Log is actually a property, but must be used as a method to correctly pass the arguments
	def Log(self, vLog=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(75, LCID, 2, (9, 0), ((12, 0),),vLog
			)
		if ret is not None:
			ret = Dispatch(ret, 'Log', None)
		return ret

	def MaximizeWindow(self):
		return self._oleobj_.InvokeTypes(78, LCID, 1, (24, 0), (),)

	def MergeLogs(self, vLog1=defaultNamedNotOptArg, vLog2=defaultNamedNotOptArg, vAverageOverlap=defaultNamedOptArg, vCreateNewLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((12, 0), (12, 0), (12, 16), (12, 16)),vLog1
			, vLog2, vAverageOverlap, vCreateNewLog)

	def MergeSameLogItems(self, vLog=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(69, LCID, 1, (24, 0), ((12, 0),),vLog
			)

	def MinimizeWindow(self):
		return self._oleobj_.InvokeTypes(79, LCID, 1, (24, 0), (),)

	def MirrorImage(self, vLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), ((12, 16),),vLog
			)

	def NMRFluidVolumes(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(108, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'NMRFluidVolumes', None)
		return ret

	def NMRPermeability(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(107, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def NMRTotalPorosity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(106, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'NMRTotalPorosity', None)
		return ret

	def NormalizeImage(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(31, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'NormalizeImage', None)
		return ret

	def OrientImageToHighside(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def OrientImageToNorth(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def OuterInnerRadiusDiameter(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(110, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'OuterInnerRadiusDiameter', None)
		return ret

	def Permeability(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(123, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'Permeability', None)
		return ret

	def PickE1Arrival(self, vFWSLog=defaultNamedOptArg, vDTLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(56, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vFWSLog
			, vDTLog, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PickE1Arrival', None)
		return ret

	def PickFirstArrival(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(51, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PickFirstArrival', None)
		return ret

	def PorosityArchie(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(122, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PorosityArchie', None)
		return ret

	def PorosityDensity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(120, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PorosityDensity', None)
		return ret

	def PorosityNeutron(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(119, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PorosityNeutron', None)
		return ret

	def PorositySonic(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(121, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'PorositySonic', None)
		return ret

	def ProcessMedusaSpectrumData(self, vLog1=defaultNamedOptArg, vLog2=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(90, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vLog1
			, vLog2, vPromptUser, vConfigFilename)

	def ProcessNMRSAData(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def ProcessReflectedTubeWave(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(59, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ProcessReflectedTubeWave', None)
		return ret

	def ProcessSpectrumData(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(68, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def RQD(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(101, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'RQD', None)
		return ret

	def RadiusToFromDiameter(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(109, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'RadiusToFromDiameter', None)
		return ret

	def ReadDatabase(self, szScriptPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((8, 0),),szScriptPath
			)

	def RecalculateStructureAzimuth(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def RecalculateStructureDip(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def RefreshWindow(self):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def RemoveLog(self, vLog=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((12, 0),),vLog
			)

	def RemoveStructuralDip(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(47, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'RemoveStructuralDip', None)
		return ret

	def Resample(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(130, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'Resample', None)
		return ret

	def ResampleLog(self, vLog=defaultNamedNotOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(27, LCID, 1, (9, 0), ((12, 0), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ResampleLog', None)
		return ret

	def ReverseAmplitude(self, vLog=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), ((12, 16),),vLog
			)

	def RotateImage(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(45, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def SaveAs(self, szFileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((8, 0),),szFileName
			)

	def SetDraftMode(self, vViewDraft=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(80, LCID, 1, (24, 0), ((12, 16),),vViewDraft
			)

	# The method SetLog is actually a property, but must be used as a method to correctly pass the arguments
	def SetLog(self, vLog=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(75, LCID, 4, (24, 0), ((12, 0), (9, 0)),vLog
			, arg1)

	def SetVisibleDepthRange(self, vTopDepth=defaultNamedOptArg, vBottomDepth=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(71, LCID, 1, (24, 0), ((12, 16), (12, 16)),vTopDepth
			, vBottomDepth)

	def ShaleVolume(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(118, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ShaleVolume', None)
		return ret

	def ShiftCorrection(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(112, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'ShiftCorrection', None)
		return ret

	def ShowWindow(self):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def SliceLog(self, vLog=defaultNamedNotOptArg, fSliceDepth=defaultNamedNotOptArg, vCreateTop=defaultNamedOptArg, vCreateBot=defaultNamedOptArg
			, vKeepOrig=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(82, LCID, 1, (24, 0), ((12, 0), (4, 0), (12, 16), (12, 16), (12, 16)),vLog
			, fSliceDepth, vCreateTop, vCreateBot, vKeepOrig)

	def SpectrometricRatios(self, vLog1=defaultNamedOptArg, vLog2=defaultNamedOptArg, vLog3=defaultNamedOptArg, vPromptUser=defaultNamedOptArg
			, vConfigFilename=defaultNamedOptArg):
		return self._ApplyTypes_(127, 1, (16408, 0), ((12, 16), (12, 16), (12, 16), (12, 16), (12, 16)), 'SpectrometricRatios', None,vLog1
			, vLog2, vLog3, vPromptUser, vConfigFilename)

	def StackTraces(self, vIsSpectrum=defaultNamedOptArg, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(61, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vIsSpectrum
			, vLog, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'StackTraces', None)
		return ret

	# The method Title is actually a property, but must be used as a method to correctly pass the arguments
	def Title(self, szTitle=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(84, LCID, 2, (9, 0), ((8, 0),),szTitle
			)
		if ret is not None:
			ret = Dispatch(ret, 'Title', None)
		return ret

	def UnitConversion(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	def WaterResistivity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(124, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'WaterResistivity', None)
		return ret

	def WaterSalinity(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(116, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)
		if ret is not None:
			ret = Dispatch(ret, 'WaterSalinity', None)
		return ret

	# The method Workspace is actually a property, but must be used as a method to correctly pass the arguments
	def Workspace(self, vWorkspace=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(100, LCID, 2, (9, 0), ((12, 0),),vWorkspace
			)
		if ret is not None:
			ret = Dispatch(ret, 'Workspace', None)
		return ret

	def WriteDatabase(self, szScriptPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (11, 0), ((8, 0),),szScriptPath
			)

	def Zonation(self, vLog=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((12, 16), (12, 16), (12, 16)),vLog
			, vPromptUser, vConfigFilename)

	_prop_map_get_ = {
		"AutoUpdate": (8, 2, (11, 0), (), "AutoUpdate", None),
		"BottomDepth": (3, 2, (4, 0), (), "BottomDepth", None),
		"Depth": (7, 2, (9, 0), (), "Depth", None),
		"Header": (5, 2, (9, 0), (), "Header", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NbOfLogs": (4, 2, (2, 0), (), "NbOfLogs", None),
		"ODBC": (12, 2, (9, 0), (), "ODBC", None),
		"Page": (6, 2, (9, 0), (), "Page", None),
		"TopDepth": (2, 2, (4, 0), (), "TopDepth", None),
		"VersionBuild": (11, 2, (2, 0), (), "VersionBuild", None),
		"VersionMajor": (9, 2, (2, 0), (), "VersionMajor", None),
		"VersionMinor": (10, 2, (2, 0), (), "VersionMinor", None),
	}
	_prop_map_put_ = {
		"AutoUpdate" : ((8, LCID, 4, 0),()),
		"BottomDepth" : ((3, LCID, 4, 0),()),
		"Depth" : ((7, LCID, 4, 0),()),
		"Header" : ((5, LCID, 4, 0),()),
		"Name" : ((1, LCID, 4, 0),()),
		"NbOfLogs" : ((4, LCID, 4, 0),()),
		"ODBC" : ((12, LCID, 4, 0),()),
		"Page" : ((6, LCID, 4, 0),()),
		"TopDepth" : ((2, LCID, 4, 0),()),
		"VersionBuild" : ((11, LCID, 4, 0),()),
		"VersionMajor" : ((9, LCID, 4, 0),()),
		"VersionMinor" : ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class CommentBox(DispatchBaseClass):
	'Borehole.Log.CommentBox Object'
	CLSID = IID('{985E0B97-295D-11CF-B80B-08002BE503AF}')
	coclass_clsid = IID('{985E0B98-295D-11CF-B80B-08002BE503AF}')

	_prop_map_get_ = {
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"Text": (3, 2, (8, 0), (), "Text", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
		"_Text": (0, 2, (8, 0), (), "_Text", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"Text" : ((3, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
		"_Text" : ((0, LCID, 4, 0),()),
	}
	# Default property for this class is '_Text'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "_Text", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class CrossPlot(DispatchBaseClass):
	'CrossPlot Object'
	CLSID = IID('{7235A6E3-ADF3-11CE-BCC2-444553540000}')
	coclass_clsid = IID('{7235A6E4-ADF3-11CE-BCC2-444553540000}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Depth(DispatchBaseClass):
	'Borehole.Depth Object'
	CLSID = IID('{F11EFBA2-1545-11CF-85CD-D0F803C10000}')
	coclass_clsid = IID('{F11EFBA3-1545-11CF-85CD-D0F803C10000}')

	def SetPosition(self, fLeft=defaultNamedNotOptArg, fRight=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((4, 0), (4, 0)),fLeft
			, fRight)

	_prop_map_get_ = {
		"Decimals": (4, 2, (2, 0), (), "Decimals", None),
		"HorizontalGrid": (6, 2, (2, 0), (), "HorizontalGrid", None),
		"HorizontalGridSpacing": (7, 2, (4, 0), (), "HorizontalGridSpacing", None),
		"LeftPosition": (2, 2, (4, 0), (), "LeftPosition", None),
		"RightPosition": (3, 2, (4, 0), (), "RightPosition", None),
		"Scale": (1, 2, (4, 0), (), "Scale", None),
		"Unit": (5, 2, (2, 0), (), "Unit", None),
		"UsedAsDepthScale": (9, 2, (11, 0), (), "UsedAsDepthScale", None),
	}
	_prop_map_put_ = {
		"Decimals" : ((4, LCID, 4, 0),()),
		"HorizontalGrid" : ((6, LCID, 4, 0),()),
		"HorizontalGridSpacing" : ((7, LCID, 4, 0),()),
		"LeftPosition" : ((2, LCID, 4, 0),()),
		"RightPosition" : ((3, LCID, 4, 0),()),
		"Scale" : ((1, LCID, 4, 0),()),
		"Unit" : ((5, LCID, 4, 0),()),
		"UsedAsDepthScale" : ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class DrillItem(DispatchBaseClass):
	'Borehole.Log.DrillItem Object'
	CLSID = IID('{9F5988D1-235E-11D1-B625-0000E829D655}')
	coclass_clsid = IID('{9F5988D2-235E-11D1-B625-0000E829D655}')

	_prop_map_get_ = {
		"BottomDepth": (1, 2, (4, 0), (), "BottomDepth", None),
		"Comment": (3, 2, (8, 0), (), "Comment", None),
		"Diameter": (2, 2, (4, 0), (), "Diameter", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((1, LCID, 4, 0),()),
		"Comment" : ((3, LCID, 4, 0),()),
		"Diameter" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class EqpItem(DispatchBaseClass):
	'Borehole.Log.EqpItem Object'
	CLSID = IID('{35381521-24F2-11D1-B629-0000E829D655}')
	coclass_clsid = IID('{35381522-24F2-11D1-B629-0000E829D655}')

	_prop_map_get_ = {
		"AxisPosition": (3, 2, (4, 0), (), "AxisPosition", None),
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"Comment": (11, 2, (8, 0), (), "Comment", None),
		"Description": (10, 2, (8, 0), (), "Description", None),
		"ExternalDiameter": (4, 2, (4, 0), (), "ExternalDiameter", None),
		"InjectionDepth": (7, 2, (4, 0), (), "InjectionDepth", None),
		"InjectionPosition": (6, 2, (4, 0), (), "InjectionPosition", None),
		"InternalDiameter": (5, 2, (4, 0), (), "InternalDiameter", None),
		"Name": (9, 2, (8, 0), (), "Name", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
		"Type": (8, 2, (2, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"AxisPosition" : ((3, LCID, 4, 0),()),
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"Comment" : ((11, LCID, 4, 0),()),
		"Description" : ((10, LCID, 4, 0),()),
		"ExternalDiameter" : ((4, LCID, 4, 0),()),
		"InjectionDepth" : ((7, LCID, 4, 0),()),
		"InjectionPosition" : ((6, LCID, 4, 0),()),
		"InternalDiameter" : ((5, LCID, 4, 0),()),
		"Name" : ((9, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
		"Type" : ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class FieldDoc(DispatchBaseClass):
	'Field Object'
	# This class is creatable by the name 'WellCAD.Field'
	CLSID = IID('{6D772C0E-334A-11D1-82F9-0000F8238C96}')
	coclass_clsid = IID('{6D772C10-334A-11D1-82F9-0000F8238C96}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Font(DispatchBaseClass):
	'Font Object'
	CLSID = IID('{657302AC-2A60-11CF-B80D-08002BE503AF}')
	coclass_clsid = IID('{657302AB-2A60-11CF-B80D-08002BE503AF}')

	_prop_map_get_ = {
		"Bold": (3, 2, (11, 0), (), "Bold", None),
		"Charset": (8, 2, (2, 0), (), "Charset", None),
		"Italic": (4, 2, (11, 0), (), "Italic", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"Size": (2, 2, (6, 0), (), "Size", None),
		"Strikethrought": (6, 2, (11, 0), (), "Strikethrought", None),
		"Underline": (5, 2, (11, 0), (), "Underline", None),
		"Weight": (7, 2, (2, 0), (), "Weight", None),
	}
	_prop_map_put_ = {
		"Bold" : ((3, LCID, 4, 0),()),
		"Charset" : ((8, LCID, 4, 0),()),
		"Italic" : ((4, LCID, 4, 0),()),
		"Name" : ((1, LCID, 4, 0),()),
		"Size" : ((2, LCID, 4, 0),()),
		"Strikethrought" : ((6, LCID, 4, 0),()),
		"Underline" : ((5, LCID, 4, 0),()),
		"Weight" : ((7, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Header(DispatchBaseClass):
	'Borehole.Header Object'
	CLSID = IID('{8C807380-137A-11CF-85CD-D0F803C10000}')
	coclass_clsid = IID('{8C807381-137A-11CF-85CD-D0F803C10000}')

	def AllowExportHeader(self, lIndex=defaultNamedNotOptArg, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((3, 0), (11, 0), (8, 0)),lIndex
			, bEnable, lpszPassword)

	def AllowExportTrailer(self, lIndex=defaultNamedNotOptArg, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 0), (11, 0), (8, 0)),lIndex
			, bEnable, lpszPassword)

	# The method ItemName is actually a property, but must be used as a method to correctly pass the arguments
	def ItemName(self, iItem=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 2, (8, 0), ((2, 0),),iItem
			)

	# The method ItemText is actually a property, but must be used as a method to correctly pass the arguments
	def ItemText(self, szItemName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(2, LCID, 2, (8, 0), ((8, 0),),szItemName
			)

	# The method SetItemText is actually a property, but must be used as a method to correctly pass the arguments
	def SetItemText(self, szItemName=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(2, LCID, 4, (24, 0), ((8, 0), (8, 0)),szItemName
			, arg1)

	_prop_map_get_ = {
		"NbOfItems": (1, 2, (2, 0), (), "NbOfItems", None),
	}
	_prop_map_put_ = {
		"NbOfItems" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoCrossBox(DispatchBaseClass):
	CLSID = IID('{3FA5F098-AB5C-486B-9827-0AA90955394F}')
	coclass_clsid = IID('{A56DA3E3-BADE-4D0D-83F9-C7E2B1369F78}')

	_prop_map_get_ = {
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoFossilItem(DispatchBaseClass):
	CLSID = IID('{22B5C0D9-E2B4-447B-99A0-C9D42809CEC1}')
	coclass_clsid = IID('{E4C2BA2C-03A2-4C35-A095-3DB558BA3346}')

	_prop_map_get_ = {
		"Abundance": (5, 2, (4, 0), (), "Abundance", None),
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"Dominance": (4, 2, (2, 0), (), "Dominance", None),
		"SymbolCode": (3, 2, (8, 0), (), "SymbolCode", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
	}
	_prop_map_put_ = {
		"Abundance" : ((5, LCID, 4, 0),()),
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"Dominance" : ((4, LCID, 4, 0),()),
		"SymbolCode" : ((3, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoIntervaltem(DispatchBaseClass):
	CLSID = IID('{D41945F6-59D1-49ED-A8AE-769F8F0E1F7D}')
	coclass_clsid = IID('{EA359274-BBFF-4148-B147-4FCB4B07D0E6}')

	_prop_map_get_ = {
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
		"Value": (3, 2, (4, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
		"Value": ((3, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(3, 2, (4, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoMarkerBox(DispatchBaseClass):
	CLSID = IID('{A181D990-A557-4131-A3E7-25E57FFD9D74}')
	coclass_clsid = IID('{E7D11EF3-FB3E-482F-BC45-7165D8D13A6B}')

	_prop_map_get_ = {
		"Comment": (3, 2, (8, 0), (), "Comment", None),
		"Contact": (4, 2, (8, 0), (), "Contact", None),
		"Depth": (1, 2, (4, 0), (), "Depth", None),
		"Name": (2, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"Comment" : ((3, LCID, 4, 0),()),
		"Contact" : ((4, LCID, 4, 0),()),
		"Depth" : ((1, LCID, 4, 0),()),
		"Name" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoODBC(DispatchBaseClass):
	CLSID = IID('{16BA375D-558D-436B-B514-0BB9A862A252}')
	coclass_clsid = IID('{CC85AC09-4589-42A6-960E-0C5620533E9D}')

	def InterpretSQLStatement(self, szStatement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), ((8, 0),),szStatement
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoSchmitBox(DispatchBaseClass):
	CLSID = IID('{F517449C-EA45-445F-A92A-A791A4C5E27F}')
	coclass_clsid = IID('{3AEACF71-920A-48F0-8A96-486A98483EB3}')

	_prop_map_get_ = {
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"Text": (3, 2, (8, 0), (), "Text", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"Text" : ((3, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoStackItem(DispatchBaseClass):
	CLSID = IID('{330DD4AC-402D-4EFF-81D0-34E110E53D05}')
	coclass_clsid = IID('{032FE6D0-27B3-4A4F-8EB6-17DD9836CD62}')

	_prop_map_get_ = {
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"BottomWidth": (4, 2, (4, 0), (), "BottomWidth", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
		"TopWidth": (3, 2, (4, 0), (), "TopWidth", None),
	}
	_prop_map_put_ = {
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"BottomWidth" : ((4, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
		"TopWidth" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBHAutoTitle(DispatchBaseClass):
	CLSID = IID('{A985F426-E8C8-4E40-AB81-CF87FDD167BE}')
	coclass_clsid = IID('{FE043ACE-23DF-4FAF-9D77-B763CD2293C1}')

	_prop_map_get_ = {
		"BackgroundColor": (31, 2, (3, 0), (), "BackgroundColor", None),
		"BoxHeight": (29, 2, (4, 0), (), "BoxHeight", None),
		"CommentAlignment": (17, 2, (2, 0), (), "CommentAlignment", None),
		"CommentBottom": (11, 2, (4, 0), (), "CommentBottom", None),
		"CommentColor": (12, 2, (3, 0), (), "CommentColor", None),
		"CommentFont": (13, 2, (9, 0), (), "CommentFont", None),
		"CommentHorizontalPosition": (14, 2, (2, 0), (), "CommentHorizontalPosition", None),
		"CommentOrientation": (16, 2, (2, 0), (), "CommentOrientation", None),
		"CommentText": (33, 2, (8, 0), (), "CommentText", None),
		"CommentTop": (10, 2, (4, 0), (), "CommentTop", None),
		"CommentVerticalPosition": (15, 2, (2, 0), (), "CommentVerticalPosition", None),
		"DisplayComment": (9, 2, (11, 0), (), "DisplayComment", None),
		"DisplayFrame": (25, 2, (11, 0), (), "DisplayFrame", None),
		"DisplayProperties": (18, 2, (11, 0), (), "DisplayProperties", None),
		"DisplayTitle": (1, 2, (11, 0), (), "DisplayTitle", None),
		"FrameColor": (26, 2, (3, 0), (), "FrameColor", None),
		"FrameStyle": (27, 2, (2, 0), (), "FrameStyle", None),
		"FrameWidth": (28, 2, (2, 0), (), "FrameWidth", None),
		"LeftPosition": (23, 2, (4, 0), (), "LeftPosition", None),
		"PropertiesBottom": (20, 2, (4, 0), (), "PropertiesBottom", None),
		"PropertiesColor": (21, 2, (3, 0), (), "PropertiesColor", None),
		"PropertiesFont": (22, 2, (9, 0), (), "PropertiesFont", None),
		"PropertiesTop": (19, 2, (4, 0), (), "PropertiesTop", None),
		"RightPosition": (24, 2, (4, 0), (), "RightPosition", None),
		"TitleBottom": (3, 2, (4, 0), (), "TitleBottom", None),
		"TitleColor": (4, 2, (3, 0), (), "TitleColor", None),
		"TitleFont": (5, 2, (9, 0), (), "TitleFont", None),
		"TitleHorizontalPosition": (6, 2, (2, 0), (), "TitleHorizontalPosition", None),
		"TitleOrientation": (8, 2, (2, 0), (), "TitleOrientation", None),
		"TitleText": (32, 2, (8, 0), (), "TitleText", None),
		"TitleTop": (2, 2, (4, 0), (), "TitleTop", None),
		"TitleVerticalPosition": (7, 2, (2, 0), (), "TitleVerticalPosition", None),
		"UseColoredBackground": (30, 2, (11, 0), (), "UseColoredBackground", None),
	}
	_prop_map_put_ = {
		"BackgroundColor" : ((31, LCID, 4, 0),()),
		"BoxHeight" : ((29, LCID, 4, 0),()),
		"CommentAlignment" : ((17, LCID, 4, 0),()),
		"CommentBottom" : ((11, LCID, 4, 0),()),
		"CommentColor" : ((12, LCID, 4, 0),()),
		"CommentFont" : ((13, LCID, 4, 0),()),
		"CommentHorizontalPosition" : ((14, LCID, 4, 0),()),
		"CommentOrientation" : ((16, LCID, 4, 0),()),
		"CommentText" : ((33, LCID, 4, 0),()),
		"CommentTop" : ((10, LCID, 4, 0),()),
		"CommentVerticalPosition" : ((15, LCID, 4, 0),()),
		"DisplayComment" : ((9, LCID, 4, 0),()),
		"DisplayFrame" : ((25, LCID, 4, 0),()),
		"DisplayProperties" : ((18, LCID, 4, 0),()),
		"DisplayTitle" : ((1, LCID, 4, 0),()),
		"FrameColor" : ((26, LCID, 4, 0),()),
		"FrameStyle" : ((27, LCID, 4, 0),()),
		"FrameWidth" : ((28, LCID, 4, 0),()),
		"LeftPosition" : ((23, LCID, 4, 0),()),
		"PropertiesBottom" : ((20, LCID, 4, 0),()),
		"PropertiesColor" : ((21, LCID, 4, 0),()),
		"PropertiesFont" : ((22, LCID, 4, 0),()),
		"PropertiesTop" : ((19, LCID, 4, 0),()),
		"RightPosition" : ((24, LCID, 4, 0),()),
		"TitleBottom" : ((3, LCID, 4, 0),()),
		"TitleColor" : ((4, LCID, 4, 0),()),
		"TitleFont" : ((5, LCID, 4, 0),()),
		"TitleHorizontalPosition" : ((6, LCID, 4, 0),()),
		"TitleOrientation" : ((8, LCID, 4, 0),()),
		"TitleText" : ((32, LCID, 4, 0),()),
		"TitleTop" : ((2, LCID, 4, 0),()),
		"TitleVerticalPosition" : ((7, LCID, 4, 0),()),
		"UseColoredBackground" : ((30, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMaxisDoc(DispatchBaseClass):
	CLSID = IID('{B8BE06A0-92B7-11D4-AE48-0000F8757500}')
	coclass_clsid = IID('{B8BE06A2-92B7-11D4-AE48-0000F8757500}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWellCADAutoApp(DispatchBaseClass):
	'Application Object'
	CLSID = IID('{96EB6D7A-E133-4659-B436-7395B6A3C68C}')
	coclass_clsid = IID('{54091291-1F61-4D78-AE38-9CDD620A0078}')

	def Cascade(self):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def CloseBorehole(self, vPromptUser=defaultNamedOptArg, vDocumentIndex=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((12, 16), (12, 16)),vPromptUser
			, vDocumentIndex)

	def FileImport(self, vDataFilename=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg, vLogFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vDataFilename
			, vPromptUser, vConfigFilename, vLogFilename)
		if ret is not None:
			ret = Dispatch(ret, 'FileImport', None)
		return ret

	def GetActiveBorehole(self):
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetActiveBorehole', None)
		return ret

	def GetBorehole(self, vDocumentIndex=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((12, 16),),vDocumentIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetBorehole', None)
		return ret

	def MaximizeWindow(self):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def MinimizeWindow(self):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def MultiFileImport(self, vDataFilenames=defaultNamedOptArg, vPromptUser=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg, vLogFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(9, LCID, 1, (9, 0), ((12, 16), (12, 16), (12, 16), (12, 16)),vDataFilenames
			, vPromptUser, vConfigFilename, vLogFilename)
		if ret is not None:
			ret = Dispatch(ret, 'MultiFileImport', None)
		return ret

	def NewBorehole(self, vDocumentFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(2, LCID, 1, (9, 0), ((12, 16),),vDocumentFilename
			)
		if ret is not None:
			ret = Dispatch(ret, 'NewBorehole', None)
		return ret

	def OpenBorehole(self, vDocumentFilename=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((12, 16),),vDocumentFilename
			)
		if ret is not None:
			ret = Dispatch(ret, 'OpenBorehole', None)
		return ret

	def Quit(self, vPromptUser=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((12, 16),),vPromptUser
			)

	def ShowWindow(self):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (11, 0), (),)

	def TileHorizontally(self):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def TileVertically(self):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"NbOfDocuments": (8, 2, (3, 0), (), "NbOfDocuments", None),
	}
	_prop_map_put_ = {
		"NbOfDocuments" : ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWorkspaceAuto(DispatchBaseClass):
	CLSID = IID('{42FBAC96-ADEE-46E7-8E67-5282E780C159}')
	coclass_clsid = IID('{A84D4613-C1F3-434C-B0EA-57ACF6E966F2}')

	def AddEnginLogFromDrillerCasingTableToBHole(self):
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def AddEnginLogFromLoggerCasingTableToBHole(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def AddJointLogToBHole(self):
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def ApplyTemplate(self, szPath=defaultNamedNotOptArg, vPromptIfNotFound=defaultNamedOptArg, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((8, 0), (12, 16), (12, 16)),szPath
			, vPromptIfNotFound, vConfigFilename)

	def AutoDetectZones(self):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def AutoJointDetection(self, vConfigFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((12, 0),),vConfigFilename
			)

	def AutomaticPicking(self, vConfigFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((12, 0),),vConfigFilename
			)

	def PickSimilarFeatures(self, vConfigFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((12, 0),),vConfigFilename
			)

	def QuickPick(self, vConfigFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((12, 0),),vConfigFilename
			)

	def RepresentativePicks(self, vConfigFilename=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((12, 0),),vConfigFilename
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class LithoBed(DispatchBaseClass):
	'Borehole.Log.LithoBed Object'
	CLSID = IID('{0220C64B-28B9-11CF-B80A-08002BE503AF}')
	coclass_clsid = IID('{0220C64C-28B9-11CF-B80A-08002BE503AF}')

	_prop_map_get_ = {
		"BottomContact": (6, 2, (8, 0), (), "BottomContact", None),
		"BottomDepth": (2, 2, (4, 0), (), "BottomDepth", None),
		"LithoCode": (4, 2, (8, 0), (), "LithoCode", None),
		"TopContact": (5, 2, (8, 0), (), "TopContact", None),
		"TopDepth": (1, 2, (4, 0), (), "TopDepth", None),
		"Value": (3, 2, (4, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"BottomContact" : ((6, LCID, 4, 0),()),
		"BottomDepth" : ((2, LCID, 4, 0),()),
		"LithoCode" : ((4, LCID, 4, 0),()),
		"TopContact" : ((5, LCID, 4, 0),()),
		"TopDepth" : ((1, LCID, 4, 0),()),
		"Value" : ((3, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(3, 2, (4, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class LithoDictionary(DispatchBaseClass):
	'LithoDictionary Object'
	CLSID = IID('{985E0B94-295D-11CF-B80B-08002BE503AF}')
	coclass_clsid = IID('{985E0B92-295D-11CF-B80B-08002BE503AF}')

	def IsPattern(self, szCode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), ((8, 0),),szCode
			)

	# The method LithoPattern is actually a property, but must be used as a method to correctly pass the arguments
	def LithoPattern(self, vPattern=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 2, (9, 0), ((12, 0),),vPattern
			)
		if ret is not None:
			ret = Dispatch(ret, 'LithoPattern', None)
		return ret

	_prop_map_get_ = {
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NbOfPatterns": (2, 2, (2, 0), (), "NbOfPatterns", None),
		"_Name": (0, 2, (8, 0), (), "_Name", None),
	}
	_prop_map_put_ = {
		"Name" : ((1, LCID, 4, 0),()),
		"NbOfPatterns" : ((2, LCID, 4, 0),()),
		"_Name" : ((0, LCID, 4, 0),()),
	}
	# Default property for this class is '_Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "_Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class LithoPattern(DispatchBaseClass):
	'LithoDictionary.LithoPattern Object'
	CLSID = IID('{985E0B95-295D-11CF-B80B-08002BE503AF}')
	coclass_clsid = IID('{985E0B96-295D-11CF-B80B-08002BE503AF}')

	_prop_map_get_ = {
		"Code": (1, 2, (8, 0), (), "Code", None),
		"Description": (2, 2, (8, 0), (), "Description", None),
		"Height": (4, 2, (3, 0), (), "Height", None),
		"Repeatable": (3, 2, (11, 0), (), "Repeatable", None),
		"Width": (5, 2, (3, 0), (), "Width", None),
		"_Code": (0, 2, (8, 0), (), "_Code", None),
	}
	_prop_map_put_ = {
		"Code" : ((1, LCID, 4, 0),()),
		"Description" : ((2, LCID, 4, 0),()),
		"Height" : ((4, LCID, 4, 0),()),
		"Repeatable" : ((3, LCID, 4, 0),()),
		"Width" : ((5, LCID, 4, 0),()),
		"_Code" : ((0, LCID, 4, 0),()),
	}
	# Default property for this class is '_Code'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "_Code", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Log(DispatchBaseClass):
	'Borehole.Log Object'
	CLSID = IID('{C99E26A0-13BF-11CF-85CD-D0F803C10000}')
	coclass_clsid = IID('{C99E26A1-13BF-11CF-85CD-D0F803C10000}')

	def AllowExportAttributeDictionary(self, lAttribute=defaultNamedNotOptArg, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(151, LCID, 1, (24, 0), ((3, 0), (11, 0), (8, 0)),lAttribute
			, bEnable, lpszPassword)

	def AllowExportLithoDictionary(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowModifyLogData(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(147, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowModifyLogSettings(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(148, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowUseFormula(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(146, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowViewFormula(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(145, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AllowViewLogHistory(self, bEnable=defaultNamedNotOptArg, lpszPassword=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(149, LCID, 1, (24, 0), ((11, 0), (8, 0)),bEnable
			, lpszPassword)

	def AttachAttributeDictionary(self, AttributeName=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(77, LCID, 1, (3, 0), ((8, 0), (8, 0)),AttributeName
			, FileName)

	def AttachLithoDictionary(self, szFileName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(55, LCID, 1, (9, 0), ((8, 0),),szFileName
			)
		if ret is not None:
			ret = Dispatch(ret, 'AttachLithoDictionary', None)
		return ret

	# The method AttributeName is actually a property, but must be used as a method to correctly pass the arguments
	def AttributeName(self, lAttribute=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(129, LCID, 2, (8, 0), ((3, 0),),lAttribute
			)

	# The method Breakout is actually a property, but must be used as a method to correctly pass the arguments
	def Breakout(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(124, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Breakout', None)
		return ret

	# The method BreakoutAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def BreakoutAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(125, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'BreakoutAtDepth', None)
		return ret

	def ClearHistory(self):
		return self._oleobj_.InvokeTypes(133, LCID, 1, (24, 0), (),)

	# The method ColumnName is actually a property, but must be used as a method to correctly pass the arguments
	def ColumnName(self, lColumn=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(128, LCID, 2, (8, 0), ((3, 0),),lColumn
			)

	# The method CommentBox is actually a property, but must be used as a method to correctly pass the arguments
	def CommentBox(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(89, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'CommentBox', None)
		return ret

	# The method CommentBoxAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def CommentBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(90, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'CommentBoxAtDepth', None)
		return ret

	# The method ComponentName is actually a property, but must be used as a method to correctly pass the arguments
	def ComponentName(self, Column=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(107, LCID, 2, (8, 0), ((3, 0),),Column
			)

	# The method CrossBox is actually a property, but must be used as a method to correctly pass the arguments
	def CrossBox(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(99, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'CrossBox', None)
		return ret

	# The method CrossBoxAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def CrossBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(100, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'CrossBoxAtDepth', None)
		return ret

	# The method Data is actually a property, but must be used as a method to correctly pass the arguments
	def Data(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(83, LCID, 2, (4, 0), ((3, 0),),lIndex
			)

	# The method DataAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def DataAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(84, LCID, 2, (4, 0), ((4, 0),),fDepth
			)

	# The method DataDepth is actually a property, but must be used as a method to correctly pass the arguments
	def DataDepth(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(118, LCID, 2, (4, 0), ((3, 0),),lIndex
			)

	def DoSettingsDlg(self):
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), (),)

	# The method DrillItem is actually a property, but must be used as a method to correctly pass the arguments
	def DrillItem(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(94, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'DrillItem', None)
		return ret

	# The method DrillItemAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def DrillItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(95, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'DrillItemAtDepth', None)
		return ret

	# The method EqpItem is actually a property, but must be used as a method to correctly pass the arguments
	def EqpItem(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(96, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'EqpItem', None)
		return ret

	def FileExport(self, Directory=defaultNamedNotOptArg, vFileTitle=defaultNamedOptArg, vExtension=defaultNamedOptArg, vPromptUser=defaultNamedOptArg
			, vConfigFilename=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(80, LCID, 1, (11, 0), ((8, 0), (12, 16), (12, 16), (12, 16), (12, 16)),Directory
			, vFileTitle, vExtension, vPromptUser, vConfigFilename)

	# The method FossilItem is actually a property, but must be used as a method to correctly pass the arguments
	def FossilItem(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(87, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'FossilItem', None)
		return ret

	# The method FossilItemAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def FossilItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(88, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'FossilItemAtDepth', None)
		return ret

	# The method HistoryItemDate is actually a property, but must be used as a method to correctly pass the arguments
	def HistoryItemDate(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(131, LCID, 2, (7, 0), ((3, 0),),lIndex
			)

	# The method HistoryItemDescription is actually a property, but must be used as a method to correctly pass the arguments
	def HistoryItemDescription(self, lIndex=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(132, LCID, 2, (8, 0), ((3, 0),),lIndex
			)

	def InsertData(self, lIndex=defaultNamedNotOptArg, newValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(60, LCID, 1, (24, 0), ((3, 0), (4, 0)),lIndex
			, newValue)

	def InsertDataAtDepth(self, fDepth=defaultNamedNotOptArg, newValue=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(62, LCID, 1, (24, 0), ((4, 0), (4, 0)),fDepth
			, newValue)

	def InsertNewAttribute(self, AttributeName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(76, LCID, 1, (24, 0), ((8, 0),),AttributeName
			)

	def InsertNewBreakout(self, fDepth=defaultNamedNotOptArg, fAzimuth=defaultNamedNotOptArg, fTilt=defaultNamedNotOptArg, fLength=defaultNamedNotOptArg
			, iCategory=defaultNamedNotOptArg, szDescription=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(121, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0), (4, 0), (2, 0), (8, 0)),fDepth
			, fAzimuth, fTilt, fLength, iCategory, szDescription
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewBreakout', None)
		return ret

	def InsertNewBreakoutEx(self, fDepth=defaultNamedNotOptArg, fAzimuth=defaultNamedNotOptArg, fTilt=defaultNamedNotOptArg, fLength=defaultNamedNotOptArg
			, fOpening=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(122, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0), (4, 0), (4, 0)),fDepth
			, fAzimuth, fTilt, fLength, fOpening)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewBreakoutEx', None)
		return ret

	def InsertNewCommentBox(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szText=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(48, LCID, 1, (9, 0), ((4, 0), (4, 0), (8, 0)),fTopDepth
			, fBottomDepth, szText)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewCommentBox', None)
		return ret

	def InsertNewCrossBox(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(68, LCID, 1, (9, 0), ((4, 0), (4, 0)),fTopDepth
			, fBottomDepth)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewCrossBox', None)
		return ret

	def InsertNewDrillItem(self, fBottomDepth=defaultNamedNotOptArg, fDiameter=defaultNamedNotOptArg, szComment=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(56, LCID, 1, (9, 0), ((4, 0), (4, 0), (12, 16)),fBottomDepth
			, fDiameter, szComment)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewDrillItem', None)
		return ret

	def InsertNewEqpItem(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szName=defaultNamedNotOptArg, szComment=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(58, LCID, 1, (9, 0), ((4, 0), (4, 0), (8, 0), (12, 16)),fTopDepth
			, fBottomDepth, szName, szComment)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewEqpItem', None)
		return ret

	def InsertNewFossilItem(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szLithoCode=defaultNamedNotOptArg, fAbundance=defaultNamedNotOptArg
			, lDominance=defaultNamedNotOptArg, fPosition=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(47, LCID, 1, (9, 0), ((4, 0), (4, 0), (8, 0), (4, 0), (3, 0), (4, 0)),fTopDepth
			, fBottomDepth, szLithoCode, fAbundance, lDominance, fPosition
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewFossilItem', None)
		return ret

	def InsertNewIntervalItem(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(66, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0)),fTopDepth
			, fBottomDepth, fValue)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewIntervalItem', None)
		return ret

	def InsertNewLithoBed(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szLithoCode=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg
			, fPosition=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), ((4, 0), (4, 0), (8, 0), (4, 0), (4, 0)),fTopDepth
			, fBottomDepth, szLithoCode, fValue, fPosition)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewLithoBed', None)
		return ret

	def InsertNewMarker(self, fDepth=defaultNamedNotOptArg, szName=defaultNamedNotOptArg, szComment=defaultNamedNotOptArg, szContact=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(81, LCID, 1, (9, 0), ((4, 0), (8, 0), (8, 0), (8, 0)),fDepth
			, szName, szComment, szContact)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewMarker', None)
		return ret

	def InsertNewOleBoxFromFile(self, FileName=defaultNamedNotOptArg, bAllowPicture=defaultNamedNotOptArg, fTopDepth=defaultNamedNotOptArg, fBotDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(79, LCID, 1, (24, 0), ((8, 0), (12, 0), (4, 0), (4, 0)),FileName
			, bAllowPicture, fTopDepth, fBotDepth)

	def InsertNewSchmitBox(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szText=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(70, LCID, 1, (9, 0), ((4, 0), (4, 0), (8, 0)),fTopDepth
			, fBottomDepth, szText)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewSchmitBox', None)
		return ret

	def InsertNewStackItem(self, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, fTopWidth=defaultNamedNotOptArg, fBotWidth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(72, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0), (4, 0)),fTopDepth
			, fBottomDepth, fTopWidth, fBotWidth)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewStackItem', None)
		return ret

	def InsertNewStrataBox(self, iColumn=defaultNamedNotOptArg, fTopDepth=defaultNamedNotOptArg, fBottomDepth=defaultNamedNotOptArg, szText=defaultNamedNotOptArg
			, szTopContact=defaultNamedOptArg, szBotContact=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(52, LCID, 1, (9, 0), ((3, 0), (4, 0), (4, 0), (8, 0), (12, 16), (12, 16)),iColumn
			, fTopDepth, fBottomDepth, szText, szTopContact, szBotContact
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewStrataBox', None)
		return ret

	def InsertNewStrataColumn(self, szText=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(50, LCID, 1, (9, 0), ((8, 0),),szText
			)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewStrataColumn', None)
		return ret

	def InsertNewStructure(self, fDepth=defaultNamedNotOptArg, fAzimuth=defaultNamedNotOptArg, fDip=defaultNamedNotOptArg, iCategory=defaultNamedNotOptArg
			, szDescription=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(53, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0), (2, 0), (8, 0)),fDepth
			, fAzimuth, fDip, iCategory, szDescription)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewStructure', None)
		return ret

	def InsertNewStructureEx(self, Depth=defaultNamedNotOptArg, Azimuth=defaultNamedNotOptArg, Dip=defaultNamedNotOptArg, Aperture=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(78, LCID, 1, (9, 0), ((4, 0), (4, 0), (4, 0), (4, 0)),Depth
			, Azimuth, Dip, Aperture)
		if ret is not None:
			ret = Dispatch(ret, 'InsertNewStructureEx', None)
		return ret

	def InsertTrace(self, lDepthIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(64, LCID, 1, (24, 0), ((3, 0),),lDepthIndex
			)

	def InsertTraceAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(65, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	# The method IntervalItem is actually a property, but must be used as a method to correctly pass the arguments
	def IntervalItem(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(97, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'IntervalItem', None)
		return ret

	# The method IntervalItemAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def IntervalItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(98, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'IntervalItemAtDepth', None)
		return ret

	# The method LithoBed is actually a property, but must be used as a method to correctly pass the arguments
	def LithoBed(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(85, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'LithoBed', None)
		return ret

	# The method LithoBedAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def LithoBedAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(86, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'LithoBedAtDepth', None)
		return ret

	# The method Marker is actually a property, but must be used as a method to correctly pass the arguments
	def Marker(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(108, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Marker', None)
		return ret

	# The method MarkerByName is actually a property, but must be used as a method to correctly pass the arguments
	def MarkerByName(self, szName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(109, LCID, 2, (9, 0), ((8, 0),),szName
			)
		if ret is not None:
			ret = Dispatch(ret, 'MarkerByName', None)
		return ret

	def RemoveBreakout(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(119, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveBreakoutAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(120, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveCommentBox(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveCommentBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(116, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveCrossBox(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(69, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveCrossBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(113, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveData(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(61, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveDataAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(63, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveDrillItem(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(57, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveEqpItem(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(59, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveFossilItem(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveFossilItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveIntervalItem(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(67, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveIntervalItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(114, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveLithoBed(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveLithoBedAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(117, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveMarker(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(82, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveSchmitBox(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(71, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveSchmitBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(112, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveStackItem(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(73, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveStackItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveStrataColumn(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveStructure(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	def RemoveStructureAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(115, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	def RemoveTrace(self, lDepthIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(74, LCID, 1, (24, 0), ((3, 0),),lDepthIndex
			)

	def RemoveTraceAtDepth(self, fDepth=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(75, LCID, 1, (24, 0), ((4, 0),),fDepth
			)

	# The method SchmitBox is actually a property, but must be used as a method to correctly pass the arguments
	def SchmitBox(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(101, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'SchmitBox', None)
		return ret

	# The method SchmitBoxAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def SchmitBoxAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(102, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'SchmitBoxAtDepth', None)
		return ret

	# The method SetAttributeName is actually a property, but must be used as a method to correctly pass the arguments
	def SetAttributeName(self, lAttribute=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(129, LCID, 4, (24, 0), ((3, 0), (8, 0)),lAttribute
			, arg1)

	# The method SetColumnName is actually a property, but must be used as a method to correctly pass the arguments
	def SetColumnName(self, lColumn=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(128, LCID, 4, (24, 0), ((3, 0), (8, 0)),lColumn
			, arg1)

	# The method SetComponentName is actually a property, but must be used as a method to correctly pass the arguments
	def SetComponentName(self, Column=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(107, LCID, 4, (24, 0), ((3, 0), (8, 0)),Column
			, arg1)

	# The method SetData is actually a property, but must be used as a method to correctly pass the arguments
	def SetData(self, lIndex=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(83, LCID, 4, (24, 0), ((3, 0), (4, 0)),lIndex
			, arg1)

	# The method SetDataAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def SetDataAtDepth(self, fDepth=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(84, LCID, 4, (24, 0), ((4, 0), (4, 0)),fDepth
			, arg1)

	# The method SetLithoBed is actually a property, but must be used as a method to correctly pass the arguments
	def SetLithoBed(self, lIndex=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(85, LCID, 4, (24, 0), ((3, 0), (9, 0)),lIndex
			, arg1)

	# The method SetLithoBedAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def SetLithoBedAtDepth(self, fDepth=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(86, LCID, 4, (24, 0), ((4, 0), (9, 0)),fDepth
			, arg1)

	def SetPosition(self, fLeft=defaultNamedNotOptArg, fRight=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((4, 0), (4, 0)),fLeft
			, fRight)

	# The method SetTraceData is actually a property, but must be used as a method to correctly pass the arguments
	def SetTraceData(self, lDepthIndex=defaultNamedNotOptArg, lTraceIndex=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(105, LCID, 4, (24, 0), ((3, 0), (3, 0), (4, 0)),lDepthIndex
			, lTraceIndex, arg2)

	# The method SetTraceDataAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def SetTraceDataAtDepth(self, fDepth=defaultNamedNotOptArg, fTracePosition=defaultNamedNotOptArg, arg2=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(106, LCID, 4, (24, 0), ((4, 0), (4, 0), (4, 0)),fDepth
			, fTracePosition, arg2)

	# The method StackItem is actually a property, but must be used as a method to correctly pass the arguments
	def StackItem(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(103, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'StackItem', None)
		return ret

	# The method StackItemAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def StackItemAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(104, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'StackItemAtDepth', None)
		return ret

	# The method StrataColumn is actually a property, but must be used as a method to correctly pass the arguments
	def StrataColumn(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(91, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'StrataColumn', None)
		return ret

	# The method Structure is actually a property, but must be used as a method to correctly pass the arguments
	def Structure(self, lIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(92, LCID, 2, (9, 0), ((3, 0),),lIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'Structure', None)
		return ret

	# The method StructureAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def StructureAtDepth(self, fDepth=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(93, LCID, 2, (9, 0), ((4, 0),),fDepth
			)
		if ret is not None:
			ret = Dispatch(ret, 'StructureAtDepth', None)
		return ret

	# The method TraceData is actually a property, but must be used as a method to correctly pass the arguments
	def TraceData(self, lDepthIndex=defaultNamedNotOptArg, lTraceIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(105, LCID, 2, (4, 0), ((3, 0), (3, 0)),lDepthIndex
			, lTraceIndex)

	# The method TraceDataAtDepth is actually a property, but must be used as a method to correctly pass the arguments
	def TraceDataAtDepth(self, fDepth=defaultNamedNotOptArg, fTracePosition=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(106, LCID, 2, (4, 0), ((4, 0), (4, 0)),fDepth
			, fTracePosition)

	_prop_map_get_ = {
		"ApertureUnit": (40, 2, (4, 0), (), "ApertureUnit", None),
		"BackgroundColor": (33, 2, (3, 0), (), "BackgroundColor", None),
		"BackgroundHatchStyle": (35, 2, (2, 0), (), "BackgroundHatchStyle", None),
		"BackgroundStyle": (34, 2, (2, 0), (), "BackgroundStyle", None),
		"BorderColor": (140, 2, (3, 0), (), "BorderColor", None),
		"BorderStyle": (141, 2, (2, 0), (), "BorderStyle", None),
		"BorderWidth": (142, 2, (2, 0), (), "BorderWidth", None),
		"BottomDepth": (8, 2, (4, 0), (), "BottomDepth", None),
		"CaliperUnit": (41, 2, (4, 0), (), "CaliperUnit", None),
		"CommentStyle": (152, 2, (2, 0), (), "CommentStyle", None),
		"DataMax": (10, 2, (4, 0), (), "DataMax", None),
		"DataMin": (9, 2, (4, 0), (), "DataMin", None),
		"DataTable": (127, 2, (12, 0), (), "DataTable", None),
		"DiameterHigh": (32, 2, (4, 0), (), "DiameterHigh", None),
		"DisplayBorder": (139, 2, (11, 0), (), "DisplayBorder", None),
		"Filter": (17, 2, (2, 0), (), "Filter", None),
		"FixedBarWidth": (25, 2, (2, 0), (), "FixedBarWidth", None),
		"Font": (27, 2, (9, 0), (), "Font", None),
		"Formula": (22, 2, (8, 0), (), "Formula", None),
		"GridEnable": (18, 2, (11, 0), (), "GridEnable", None),
		"GridSpacing": (20, 2, (4, 0), (), "GridSpacing", None),
		"GroundDepth": (30, 2, (4, 0), (), "GroundDepth", None),
		"HideLogData": (137, 2, (11, 0), (), "HideLogData", None),
		"HideLogTitle": (136, 2, (11, 0), (), "HideLogTitle", None),
		"LeftPosition": (5, 2, (4, 0), (), "LeftPosition", None),
		"LengthUnit": (123, 2, (4, 0), (), "LengthUnit", None),
		"LithoDictionary": (26, 2, (9, 0), (), "LithoDictionary", None),
		"LockLogData": (138, 2, (11, 0), (), "LockLogData", None),
		"LogBackgroundColor": (144, 2, (3, 0), (), "LogBackgroundColor", None),
		"LogUnit": (3, 2, (8, 0), (), "LogUnit", None),
		"MajGridEnable": (155, 2, (11, 0), (), "MajGridEnable", None),
		"MajGridSpacing": (153, 2, (4, 0), (), "MajGridSpacing", None),
		"MaskContacts": (135, 2, (11, 0), (), "MaskContacts", None),
		"MaskHorizontalGrid": (134, 2, (11, 0), (), "MaskHorizontalGrid", None),
		"MinGridEnable": (156, 2, (11, 0), (), "MinGridEnable", None),
		"MinGridSpacing": (154, 2, (4, 0), (), "MinGridSpacing", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NbOfData": (23, 2, (3, 0), (), "NbOfData", None),
		"NbOfDrillItem": (31, 2, (3, 0), (), "NbOfDrillItem", None),
		"NbOfEqpItem": (36, 2, (3, 0), (), "NbOfEqpItem", None),
		"NbOfHistoryItem": (130, 2, (3, 0), (), "NbOfHistoryItem", None),
		"NullValue": (28, 2, (4, 0), (), "NullValue", None),
		"PenColor": (14, 2, (3, 0), (), "PenColor", None),
		"PenStyle": (13, 2, (2, 0), (), "PenStyle", None),
		"PenWidth": (15, 2, (2, 0), (), "PenWidth", None),
		"RightPosition": (6, 2, (4, 0), (), "RightPosition", None),
		"SampleRate": (29, 2, (4, 0), (), "SampleRate", None),
		"ScaleHigh": (12, 2, (4, 0), (), "ScaleHigh", None),
		"ScaleLow": (11, 2, (4, 0), (), "ScaleLow", None),
		"ScaleMode": (19, 2, (2, 0), (), "ScaleMode", None),
		"ScaleReversed": (21, 2, (11, 0), (), "ScaleReversed", None),
		"Shading": (16, 2, (2, 0), (), "Shading", None),
		"Style": (24, 2, (2, 0), (), "Style", None),
		"TitleComment": (2, 2, (8, 0), (), "TitleComment", None),
		"TopDepth": (7, 2, (4, 0), (), "TopDepth", None),
		"TraceLength": (37, 2, (3, 0), (), "TraceLength", None),
		"TraceOffset": (39, 2, (4, 0), (), "TraceOffset", None),
		"TraceSampleRate": (38, 2, (4, 0), (), "TraceSampleRate", None),
		"Type": (4, 2, (2, 0), (), "Type", None),
		"UseLogColoredBackground": (143, 2, (11, 0), (), "UseLogColoredBackground", None),
		"UsedAsDepthScale": (126, 2, (11, 0), (), "UsedAsDepthScale", None),
	}
	_prop_map_put_ = {
		"ApertureUnit" : ((40, LCID, 4, 0),()),
		"BackgroundColor" : ((33, LCID, 4, 0),()),
		"BackgroundHatchStyle" : ((35, LCID, 4, 0),()),
		"BackgroundStyle" : ((34, LCID, 4, 0),()),
		"BorderColor" : ((140, LCID, 4, 0),()),
		"BorderStyle" : ((141, LCID, 4, 0),()),
		"BorderWidth" : ((142, LCID, 4, 0),()),
		"BottomDepth" : ((8, LCID, 4, 0),()),
		"CaliperUnit" : ((41, LCID, 4, 0),()),
		"CommentStyle" : ((152, LCID, 4, 0),()),
		"DataMax" : ((10, LCID, 4, 0),()),
		"DataMin" : ((9, LCID, 4, 0),()),
		"DataTable" : ((127, LCID, 4, 0),()),
		"DiameterHigh" : ((32, LCID, 4, 0),()),
		"DisplayBorder" : ((139, LCID, 4, 0),()),
		"Filter" : ((17, LCID, 4, 0),()),
		"FixedBarWidth" : ((25, LCID, 4, 0),()),
		"Font" : ((27, LCID, 4, 0),()),
		"Formula" : ((22, LCID, 4, 0),()),
		"GridEnable" : ((18, LCID, 4, 0),()),
		"GridSpacing" : ((20, LCID, 4, 0),()),
		"GroundDepth" : ((30, LCID, 4, 0),()),
		"HideLogData" : ((137, LCID, 4, 0),()),
		"HideLogTitle" : ((136, LCID, 4, 0),()),
		"LeftPosition" : ((5, LCID, 4, 0),()),
		"LengthUnit" : ((123, LCID, 4, 0),()),
		"LithoDictionary" : ((26, LCID, 4, 0),()),
		"LockLogData" : ((138, LCID, 4, 0),()),
		"LogBackgroundColor" : ((144, LCID, 4, 0),()),
		"LogUnit" : ((3, LCID, 4, 0),()),
		"MajGridEnable" : ((155, LCID, 4, 0),()),
		"MajGridSpacing" : ((153, LCID, 4, 0),()),
		"MaskContacts" : ((135, LCID, 4, 0),()),
		"MaskHorizontalGrid" : ((134, LCID, 4, 0),()),
		"MinGridEnable" : ((156, LCID, 4, 0),()),
		"MinGridSpacing" : ((154, LCID, 4, 0),()),
		"Name" : ((1, LCID, 4, 0),()),
		"NbOfData" : ((23, LCID, 4, 0),()),
		"NbOfDrillItem" : ((31, LCID, 4, 0),()),
		"NbOfEqpItem" : ((36, LCID, 4, 0),()),
		"NbOfHistoryItem" : ((130, LCID, 4, 0),()),
		"NullValue" : ((28, LCID, 4, 0),()),
		"PenColor" : ((14, LCID, 4, 0),()),
		"PenStyle" : ((13, LCID, 4, 0),()),
		"PenWidth" : ((15, LCID, 4, 0),()),
		"RightPosition" : ((6, LCID, 4, 0),()),
		"SampleRate" : ((29, LCID, 4, 0),()),
		"ScaleHigh" : ((12, LCID, 4, 0),()),
		"ScaleLow" : ((11, LCID, 4, 0),()),
		"ScaleMode" : ((19, LCID, 4, 0),()),
		"ScaleReversed" : ((21, LCID, 4, 0),()),
		"Shading" : ((16, LCID, 4, 0),()),
		"Style" : ((24, LCID, 4, 0),()),
		"TitleComment" : ((2, LCID, 4, 0),()),
		"TopDepth" : ((7, LCID, 4, 0),()),
		"TraceLength" : ((37, LCID, 4, 0),()),
		"TraceOffset" : ((39, LCID, 4, 0),()),
		"TraceSampleRate" : ((38, LCID, 4, 0),()),
		"Type" : ((4, LCID, 4, 0),()),
		"UseLogColoredBackground" : ((143, LCID, 4, 0),()),
		"UsedAsDepthScale" : ((126, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Page(DispatchBaseClass):
	'Borehole.Page Object'
	CLSID = IID('{F11EFBA0-1545-11CF-85CD-D0F803C10000}')
	coclass_clsid = IID('{F11EFBA1-1545-11CF-85CD-D0F803C10000}')

	def AddDepthRange(self, fTop=defaultNamedNotOptArg, fBot=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((4, 0), (4, 0)),fTop
			, fBot)

	def RemoveDepthRange(self, lIndex=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 0),),lIndex
			)

	_prop_map_get_ = {
		"BottomMargin": (4, 2, (2, 0), (), "BottomMargin", None),
		"DepthRange": (14, 2, (2, 0), (), "DepthRange", None),
		"DocumentHeight": (8, 2, (3, 0), (), "DocumentHeight", None),
		"DocumentWidth": (7, 2, (3, 0), (), "DocumentWidth", None),
		"LeftMargin": (1, 2, (2, 0), (), "LeftMargin", None),
		"NbOfDepthRange": (15, 2, (3, 0), (), "NbOfDepthRange", None),
		"Numbering": (6, 2, (2, 0), (), "Numbering", None),
		"PaperMode": (5, 2, (2, 0), (), "PaperMode", None),
		"PrintHeader": (9, 2, (11, 0), (), "PrintHeader", None),
		"PrintTitlesOnBottom": (12, 2, (11, 0), (), "PrintTitlesOnBottom", None),
		"PrintTitlesOnBottomOnEachPage": (13, 2, (11, 0), (), "PrintTitlesOnBottomOnEachPage", None),
		"PrintTitlesOnTop": (10, 2, (11, 0), (), "PrintTitlesOnTop", None),
		"PrintTitlesOnTopOnEachPage": (11, 2, (11, 0), (), "PrintTitlesOnTopOnEachPage", None),
		"RightMargin": (2, 2, (2, 0), (), "RightMargin", None),
		"TopMargin": (3, 2, (2, 0), (), "TopMargin", None),
	}
	_prop_map_put_ = {
		"BottomMargin" : ((4, LCID, 4, 0),()),
		"DepthRange" : ((14, LCID, 4, 0),()),
		"DocumentHeight" : ((8, LCID, 4, 0),()),
		"DocumentWidth" : ((7, LCID, 4, 0),()),
		"LeftMargin" : ((1, LCID, 4, 0),()),
		"NbOfDepthRange" : ((15, LCID, 4, 0),()),
		"Numbering" : ((6, LCID, 4, 0),()),
		"PaperMode" : ((5, LCID, 4, 0),()),
		"PrintHeader" : ((9, LCID, 4, 0),()),
		"PrintTitlesOnBottom" : ((12, LCID, 4, 0),()),
		"PrintTitlesOnBottomOnEachPage" : ((13, LCID, 4, 0),()),
		"PrintTitlesOnTop" : ((10, LCID, 4, 0),()),
		"PrintTitlesOnTopOnEachPage" : ((11, LCID, 4, 0),()),
		"RightMargin" : ((2, LCID, 4, 0),()),
		"TopMargin" : ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Structure(DispatchBaseClass):
	'Borehole.Log.Structure Object'
	CLSID = IID('{4EF06035-4510-11CF-B829-08002BE503AF}')
	coclass_clsid = IID('{4EF06036-4510-11CF-B829-08002BE503AF}')

	# The method AttributeValue is actually a property, but must be used as a method to correctly pass the arguments
	def AttributeValue(self, AttributeName=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(7, LCID, 2, (8, 0), ((8, 0),),AttributeName
			)

	# The method SetAttributeValue is actually a property, but must be used as a method to correctly pass the arguments
	def SetAttributeValue(self, AttributeName=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(7, LCID, 4, (24, 0), ((8, 0), (8, 0)),AttributeName
			, arg1)

	_prop_map_get_ = {
		"Aperture": (6, 2, (4, 0), (), "Aperture", None),
		"Azimuth": (1, 2, (4, 0), (), "Azimuth", None),
		"Category": (3, 2, (2, 0), (), "Category", None),
		"Depth": (5, 2, (4, 0), (), "Depth", None),
		"Description": (4, 2, (8, 0), (), "Description", None),
		"Length": (8, 2, (4, 0), (), "Length", None),
		"Tilt": (2, 2, (4, 0), (), "Tilt", None),
	}
	_prop_map_put_ = {
		"Aperture" : ((6, LCID, 4, 0),()),
		"Azimuth" : ((1, LCID, 4, 0),()),
		"Category" : ((3, LCID, 4, 0),()),
		"Depth" : ((5, LCID, 4, 0),()),
		"Description" : ((4, LCID, 4, 0),()),
		"Length" : ((8, LCID, 4, 0),()),
		"Tilt" : ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'WellCAD.Application'
class Application(CoClassBaseClass): # A CoClass
	CLSID = IID('{54091291-1F61-4D78-AE38-9CDD620A0078}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWellCADAutoApp,
	]
	default_interface = IWellCADAutoApp

class BHAutoCrossBox(CoClassBaseClass): # A CoClass
	CLSID = IID('{A56DA3E3-BADE-4D0D-83F9-C7E2B1369F78}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoCrossBox,
	]
	default_interface = IBHAutoCrossBox

class BHAutoFossilItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{E4C2BA2C-03A2-4C35-A095-3DB558BA3346}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoFossilItem,
	]
	default_interface = IBHAutoFossilItem

class BHAutoIntervalItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{EA359274-BBFF-4148-B147-4FCB4B07D0E6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoIntervaltem,
	]
	default_interface = IBHAutoIntervaltem

class BHAutoMarkerBox(CoClassBaseClass): # A CoClass
	CLSID = IID('{E7D11EF3-FB3E-482F-BC45-7165D8D13A6B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoMarkerBox,
	]
	default_interface = IBHAutoMarkerBox

class BHAutoODBC(CoClassBaseClass): # A CoClass
	CLSID = IID('{CC85AC09-4589-42A6-960E-0C5620533E9D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoODBC,
	]
	default_interface = IBHAutoODBC

class BHAutoSchmitBox(CoClassBaseClass): # A CoClass
	CLSID = IID('{3AEACF71-920A-48F0-8A96-486A98483EB3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoSchmitBox,
	]
	default_interface = IBHAutoSchmitBox

class BHAutoStackItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{032FE6D0-27B3-4A4F-8EB6-17DD9836CD62}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoStackItem,
	]
	default_interface = IBHAutoStackItem

class BHAutoTitle(CoClassBaseClass): # A CoClass
	CLSID = IID('{FE043ACE-23DF-4FAF-9D77-B763CD2293C1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBHAutoTitle,
	]
	default_interface = IBHAutoTitle

# This CoClass is known by the name 'WellCAD.Borehole'
class CBorehole(CoClassBaseClass): # A CoClass
	CLSID = IID('{7235A6E0-ADF3-11CE-BCC2-444553540000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Borehole,
	]
	default_interface = Borehole

class CCommentBox(CoClassBaseClass): # A CoClass
	CLSID = IID('{985E0B98-295D-11CF-B80B-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		CommentBox,
	]
	default_interface = CommentBox

# This CoClass is known by the name 'WellCAD.CrossPlot'
class CCrossPlot(CoClassBaseClass): # A CoClass
	CLSID = IID('{7235A6E4-ADF3-11CE-BCC2-444553540000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		CrossPlot,
	]
	default_interface = CrossPlot

class CDepth(CoClassBaseClass): # A CoClass
	CLSID = IID('{F11EFBA3-1545-11CF-85CD-D0F803C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Depth,
	]
	default_interface = Depth

class CDrillItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{9F5988D2-235E-11D1-B625-0000E829D655}')
	coclass_sources = [
	]
	coclass_interfaces = [
		DrillItem,
	]
	default_interface = DrillItem

class CEqpItem(CoClassBaseClass): # A CoClass
	CLSID = IID('{35381522-24F2-11D1-B629-0000E829D655}')
	coclass_sources = [
	]
	coclass_interfaces = [
		EqpItem,
	]
	default_interface = EqpItem

class CFieldDoc(CoClassBaseClass): # A CoClass
	CLSID = IID('{6D772C10-334A-11D1-82F9-0000F8238C96}')
	coclass_sources = [
	]
	coclass_interfaces = [
		FieldDoc,
	]
	default_interface = FieldDoc

# This CoClass is known by the name 'Font'
class CFont(CoClassBaseClass): # A CoClass
	CLSID = IID('{657302AB-2A60-11CF-B80D-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Font,
	]
	default_interface = Font

class CHeader(CoClassBaseClass): # A CoClass
	CLSID = IID('{8C807381-137A-11CF-85CD-D0F803C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Header,
	]
	default_interface = Header

class CLithoBed(CoClassBaseClass): # A CoClass
	CLSID = IID('{0220C64C-28B9-11CF-B80A-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		LithoBed,
	]
	default_interface = LithoBed

# This CoClass is known by the name 'LithoDictionary'
class CLithoDictionary(CoClassBaseClass): # A CoClass
	CLSID = IID('{985E0B92-295D-11CF-B80B-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		LithoDictionary,
	]
	default_interface = LithoDictionary

class CLithoPattern(CoClassBaseClass): # A CoClass
	CLSID = IID('{985E0B96-295D-11CF-B80B-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		LithoPattern,
	]
	default_interface = LithoPattern

class CLog(CoClassBaseClass): # A CoClass
	CLSID = IID('{C99E26A1-13BF-11CF-85CD-D0F803C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Log,
	]
	default_interface = Log

class CPage(CoClassBaseClass): # A CoClass
	CLSID = IID('{F11EFBA1-1545-11CF-85CD-D0F803C10000}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Page,
	]
	default_interface = Page

class CStructure(CoClassBaseClass): # A CoClass
	CLSID = IID('{4EF06036-4510-11CF-B829-08002BE503AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		Structure,
	]
	default_interface = Structure

class MaxisDoc(CoClassBaseClass): # A CoClass
	CLSID = IID('{B8BE06A2-92B7-11D4-AE48-0000F8757500}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMaxisDoc,
	]
	default_interface = IMaxisDoc

class Workspace(CoClassBaseClass): # A CoClass
	CLSID = IID('{A84D4613-C1F3-434C-B0EA-57ACF6E966F2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IWorkspaceAuto,
	]
	default_interface = IWorkspaceAuto

RecordMap = {
}

CLSIDToClassMap = {
	'{96EB6D7A-E133-4659-B436-7395B6A3C68C}' : IWellCADAutoApp,
	'{54091291-1F61-4D78-AE38-9CDD620A0078}' : Application,
	'{7235A6E2-ADF3-11CE-BCC2-444553540000}' : Borehole,
	'{7235A6E0-ADF3-11CE-BCC2-444553540000}' : CBorehole,
	'{7235A6E3-ADF3-11CE-BCC2-444553540000}' : CrossPlot,
	'{7235A6E4-ADF3-11CE-BCC2-444553540000}' : CCrossPlot,
	'{8C807380-137A-11CF-85CD-D0F803C10000}' : Header,
	'{8C807381-137A-11CF-85CD-D0F803C10000}' : CHeader,
	'{C99E26A0-13BF-11CF-85CD-D0F803C10000}' : Log,
	'{C99E26A1-13BF-11CF-85CD-D0F803C10000}' : CLog,
	'{F11EFBA0-1545-11CF-85CD-D0F803C10000}' : Page,
	'{F11EFBA1-1545-11CF-85CD-D0F803C10000}' : CPage,
	'{F11EFBA2-1545-11CF-85CD-D0F803C10000}' : Depth,
	'{F11EFBA3-1545-11CF-85CD-D0F803C10000}' : CDepth,
	'{0220C64B-28B9-11CF-B80A-08002BE503AF}' : LithoBed,
	'{0220C64C-28B9-11CF-B80A-08002BE503AF}' : CLithoBed,
	'{985E0B94-295D-11CF-B80B-08002BE503AF}' : LithoDictionary,
	'{985E0B92-295D-11CF-B80B-08002BE503AF}' : CLithoDictionary,
	'{985E0B95-295D-11CF-B80B-08002BE503AF}' : LithoPattern,
	'{985E0B96-295D-11CF-B80B-08002BE503AF}' : CLithoPattern,
	'{985E0B97-295D-11CF-B80B-08002BE503AF}' : CommentBox,
	'{985E0B98-295D-11CF-B80B-08002BE503AF}' : CCommentBox,
	'{657302AC-2A60-11CF-B80D-08002BE503AF}' : Font,
	'{657302AB-2A60-11CF-B80D-08002BE503AF}' : CFont,
	'{4EF06035-4510-11CF-B829-08002BE503AF}' : Structure,
	'{4EF06036-4510-11CF-B829-08002BE503AF}' : CStructure,
	'{9F5988D1-235E-11D1-B625-0000E829D655}' : DrillItem,
	'{9F5988D2-235E-11D1-B625-0000E829D655}' : CDrillItem,
	'{35381521-24F2-11D1-B629-0000E829D655}' : EqpItem,
	'{35381522-24F2-11D1-B629-0000E829D655}' : CEqpItem,
	'{6D772C0E-334A-11D1-82F9-0000F8238C96}' : FieldDoc,
	'{6D772C10-334A-11D1-82F9-0000F8238C96}' : CFieldDoc,
	'{B8BE06A0-92B7-11D4-AE48-0000F8757500}' : IMaxisDoc,
	'{B8BE06A2-92B7-11D4-AE48-0000F8757500}' : MaxisDoc,
	'{D41945F6-59D1-49ED-A8AE-769F8F0E1F7D}' : IBHAutoIntervaltem,
	'{EA359274-BBFF-4148-B147-4FCB4B07D0E6}' : BHAutoIntervalItem,
	'{3FA5F098-AB5C-486B-9827-0AA90955394F}' : IBHAutoCrossBox,
	'{A56DA3E3-BADE-4D0D-83F9-C7E2B1369F78}' : BHAutoCrossBox,
	'{F517449C-EA45-445F-A92A-A791A4C5E27F}' : IBHAutoSchmitBox,
	'{3AEACF71-920A-48F0-8A96-486A98483EB3}' : BHAutoSchmitBox,
	'{22B5C0D9-E2B4-447B-99A0-C9D42809CEC1}' : IBHAutoFossilItem,
	'{E4C2BA2C-03A2-4C35-A095-3DB558BA3346}' : BHAutoFossilItem,
	'{330DD4AC-402D-4EFF-81D0-34E110E53D05}' : IBHAutoStackItem,
	'{032FE6D0-27B3-4A4F-8EB6-17DD9836CD62}' : BHAutoStackItem,
	'{16BA375D-558D-436B-B514-0BB9A862A252}' : IBHAutoODBC,
	'{CC85AC09-4589-42A6-960E-0C5620533E9D}' : BHAutoODBC,
	'{A181D990-A557-4131-A3E7-25E57FFD9D74}' : IBHAutoMarkerBox,
	'{E7D11EF3-FB3E-482F-BC45-7165D8D13A6B}' : BHAutoMarkerBox,
	'{A985F426-E8C8-4E40-AB81-CF87FDD167BE}' : IBHAutoTitle,
	'{FE043ACE-23DF-4FAF-9D77-B763CD2293C1}' : BHAutoTitle,
	'{42FBAC96-ADEE-46E7-8E67-5282E780C159}' : IWorkspaceAuto,
	'{A84D4613-C1F3-434C-B0EA-57ACF6E966F2}' : Workspace,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'IWellCADAutoApp' : '{96EB6D7A-E133-4659-B436-7395B6A3C68C}',
	'Borehole' : '{7235A6E2-ADF3-11CE-BCC2-444553540000}',
	'CrossPlot' : '{7235A6E3-ADF3-11CE-BCC2-444553540000}',
	'Header' : '{8C807380-137A-11CF-85CD-D0F803C10000}',
	'Log' : '{C99E26A0-13BF-11CF-85CD-D0F803C10000}',
	'Page' : '{F11EFBA0-1545-11CF-85CD-D0F803C10000}',
	'Depth' : '{F11EFBA2-1545-11CF-85CD-D0F803C10000}',
	'LithoBed' : '{0220C64B-28B9-11CF-B80A-08002BE503AF}',
	'LithoDictionary' : '{985E0B94-295D-11CF-B80B-08002BE503AF}',
	'LithoPattern' : '{985E0B95-295D-11CF-B80B-08002BE503AF}',
	'CommentBox' : '{985E0B97-295D-11CF-B80B-08002BE503AF}',
	'Font' : '{657302AC-2A60-11CF-B80D-08002BE503AF}',
	'Structure' : '{4EF06035-4510-11CF-B829-08002BE503AF}',
	'DrillItem' : '{9F5988D1-235E-11D1-B625-0000E829D655}',
	'EqpItem' : '{35381521-24F2-11D1-B629-0000E829D655}',
	'FieldDoc' : '{6D772C0E-334A-11D1-82F9-0000F8238C96}',
	'IMaxisDoc' : '{B8BE06A0-92B7-11D4-AE48-0000F8757500}',
	'IBHAutoIntervaltem' : '{D41945F6-59D1-49ED-A8AE-769F8F0E1F7D}',
	'IBHAutoCrossBox' : '{3FA5F098-AB5C-486B-9827-0AA90955394F}',
	'IBHAutoSchmitBox' : '{F517449C-EA45-445F-A92A-A791A4C5E27F}',
	'IBHAutoFossilItem' : '{22B5C0D9-E2B4-447B-99A0-C9D42809CEC1}',
	'IBHAutoStackItem' : '{330DD4AC-402D-4EFF-81D0-34E110E53D05}',
	'IBHAutoODBC' : '{16BA375D-558D-436B-B514-0BB9A862A252}',
	'IBHAutoMarkerBox' : '{A181D990-A557-4131-A3E7-25E57FFD9D74}',
	'IBHAutoTitle' : '{A985F426-E8C8-4E40-AB81-CF87FDD167BE}',
	'IWorkspaceAuto' : '{42FBAC96-ADEE-46E7-8E67-5282E780C159}',
}


