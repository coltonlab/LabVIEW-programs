// **********************************************************************
// * wlmData.h                                                          *
// *   (header file for wlmData.dll)                                    *
// *                                                         2006-09-25 *
// **********************************************************************

// Data_EXPORTS must not be defined for any project using this dll.
	#ifdef Data_EXPORTS 
		#define DLL_IM_EXPORT dllexport 
	#else
		#define DLL_IM_EXPORT dllimport 
	#endif

	#define Data_API(ret) extern "C" __declspec(DLL_IM_EXPORT) ret __stdcall 


// **********************************************************************
	Data_API(long) Instantiate(long RFC, long Mode, long P1, long P2) ;
//	void CallbackProc(long Mode, long IntVal, double DblVal) ;
//	void CallbackProcEx(long Ver, long Mode, long IntVal, double DblVal, long Res1) ;
	Data_API(long) WaitForWLMEvent(long &Mode, long &IntVal, double &DblVal) ;
	Data_API(long) WaitForWLMEventEx(long &Ver, long &Mode, long &IntVal, double &DblVal, long &Res1) ;
	Data_API(long) ControlWLM(long Action, long App, long Res1) ;
	Data_API(long) SetMeasurementDelayMethod(long Mode, long Delay)	;
	Data_API(long) SetWLMPriority(long PPC, long Res1, long Res2) ;
	Data_API(long) PresetWLMIndex(long Ver) ;


// ***********  Get...-functions  ***************************************
	Data_API(long)           GetWLMVersion(long Ver) ;
	Data_API(long)           GetWLMIndex(long Ver) ;
	Data_API(long)           GetWLMCount(long V) ;

	Data_API(double)         GetFrequencyNum(long num, double F) ;
	Data_API(double)         GetFrequency(double F) ;
	Data_API(double)         GetFrequency2(double F2) ;
	Data_API(double)         GetWavelengthNum(long num, double WL) ;
	Data_API(double)         GetWavelength(double WL) ;
	Data_API(double)         GetWavelength2(double WL2) ;
	Data_API(double)         GetTemperature(double T) ;

	Data_API(unsigned short) GetExposure(unsigned short E) ;
	Data_API(unsigned short) GetExposure2(unsigned short E2) ;
	Data_API(long)           GetExposureNum(long num, long arr, long E) ;

	Data_API(bool)           GetExposureMode(bool EM) ;
	Data_API(long)           GetExposureRange(long ER) ;
	Data_API(unsigned short) GetResultMode(unsigned short RM) ;
	Data_API(unsigned short) GetRange(unsigned short R) ;
	Data_API(unsigned short) GetPulseMode(unsigned short PM) ;
	Data_API(unsigned short) GetWideMode(unsigned short WM) ;
	Data_API(bool)           GetFastMode(bool FM) ;
	Data_API(long)           GetDisplayMode(long DM) ;
	Data_API(bool)           GetReduced(bool R) ;
	Data_API(unsigned short) GetScale(unsigned short S) ;
	Data_API(bool)           GetLinkState(bool LS) ;
	Data_API(unsigned short) GetOperationState(unsigned short Op) ;

	Data_API(long)           GetPatternItemSize(long Index) ;
	Data_API(long)           GetPatternItemCount(long Index) ;
	Data_API(long)           GetPattern(long Index) ;
	Data_API(long)           GetPatternData(long Index, DWORD PArray) ;

	Data_API(long)           GetAnalysisItemSize(long Index) ;
	Data_API(long)           GetAnalysisItemCount(long Index) ;
	Data_API(long)           GetAnalysis(long Index) ;
	Data_API(long)           GetAnalysisData(long Index, DWORD PArray) ;
	Data_API(double)         GetLinewidth(long Index, double LW) ;

	Data_API(long)           GetMinPeak(long M1) ;
	Data_API(long)           GetMinPeak2(long M2) ;
	Data_API(long)           GetMaxPeak(long X1) ;
	Data_API(long)           GetMaxPeak2(long X2) ;
	Data_API(long)           GetAvgPeak(long A1) ;
	Data_API(long)           GetAvgPeak2(long A2) ;

	Data_API(long)           GetAmplitudeNum(long num, long Index, long A) ;
	Data_API(double)         GetIntensityNum(long num, double I) ;

	Data_API(unsigned short) GetDelay(unsigned short D) ;
	Data_API(unsigned short) GetShift(unsigned short S) ;
	Data_API(unsigned short) GetShift2(unsigned short S2) ;


// ***********  Set...-functions  ***************************************
	Data_API(long)           SetExposure(unsigned short E) ;
	Data_API(long)           SetExposure2(unsigned short E2) ;
	Data_API(long)           SetExposureNum(long num, long arr, long E) ;

	Data_API(long)           SetExposureMode(bool EM) ;
	Data_API(long)           SetResultMode(unsigned short RM) ;
	Data_API(long)           SetRange(unsigned short R) ;
	Data_API(long)           SetPulseMode(unsigned short PM) ;
	Data_API(long)           SetWideMode(unsigned short WM) ;
	Data_API(long)           SetFastMode(bool FM) ;
	Data_API(long)           SetDisplayMode(long DM) ;
	Data_API(long)           SetSwitcherMode(long SM) ;
	Data_API(long)           SetSwitcherSignal(long Signal, long Use, long Show) ;
	Data_API(long)           SetReduced(bool R) ;
	Data_API(long)           SetScale(unsigned short S) ;
	Data_API(long)           SetLinkState(bool LS) ;
	Data_API(long)           SetAvgPeak(long PA) ;

	Data_API(long)           Operation(unsigned short Op) ;
	Data_API(long)           Calibration(long Type, long Unit, double Value, long Channel) ;
	Data_API(long)           RaiseMeasurementEvent(long Mode) ;
	Data_API(long)           TriggerMeasurement(long Action) ;

	Data_API(long)           SetTemperature(double T) ;
	Data_API(long)           SetPattern(long Index, long iEnable) ;
	Data_API(long)           SetPatternData(long Index, DWORD PArray) ;
	Data_API(long)           SetAnalysis(long Index, long iEnable) ;

	Data_API(long)           SetDelay(unsigned short D) ;
	Data_API(long)           SetShift(unsigned short S) ;
	Data_API(long)           SetShift2(unsigned short S2) ;

	Data_API(void)           LinkSettingsDlg(void) ;


// ***********  Other...-functions  *************************************
	Data_API(double) ConvertUnit(double Val, long uFrom, long uTo) ;
	Data_API(double) ConvertDeltaUnit(double Base, double Delta, long uBase, long uFrom, long uTo) ;


// ***********  for future use ...  *************************************
	Data_API(bool)           GetAnalysisMode(bool AM) ;
	Data_API(long)           SetAnalysisMode(bool AM) ;
	Data_API(bool)           GetDeviationMode(bool DM) ;
	Data_API(long)           SetDeviationMode(bool DM) ;
	Data_API(double)         GetDeviationReference(double DR) ;
	Data_API(long)           SetDeviationReference(double DR) ;
	Data_API(long)           GetDeviationSensitivity(long DS) ;
	Data_API(long)           SetDeviationSensitivity(long DS) ;
	Data_API(double)         GetDeviationSignal(double DS) ;
	Data_API(double)         GetDeviationSignalNum(long Num, double DS) ;
	Data_API(long)           SetDeviationSignal(double DS) ;
	Data_API(long)           GetDeviationSetting(long DS, long iSet, double dSet) ;
	Data_API(long)           SetDeviationSetting(long DS, long iSet, double dSet) ;
	Data_API(double)         RaiseDeviationSignal(long iType, double dSignal) ;
	Data_API(double)         GetAnalogIn(double AI) ;
	Data_API(double)         GetDistance(double D) ;




// Instantiating Constants for 'RFC' parameter
	const	cInstCheckForWLM = -1;
	const	cInstResetCalc = 0;
	const	cInstReturnMode = cInstResetCalc;
	const	cInstNotification = 1;
	const	cInstCopyPattern = 2;
	const	cInstCopyAnalysis = cInstCopyPattern;
	const	cInstControlWLM = 3;
	const	cInstControlDelay = 4;
	const	cInstControlPriority = 5;

// Notification Constants for 'Mode' parameter
	const	cNotifyInstallCallback = 0;
	const	cNotifyRemoveCallback = 1;
	const	cNotifyInstallWaitEvent = 2;
	const	cNotifyRemoveWaitEvent = 3;
	const	cNotifyInstallCallbackEx = 4;
	const	cNotifyInstallWaitEventEx = 5;

// ResultError Constants of Set...-functions
	const	ResERR_NoErr = 0;
	const	ResERR_WlmMissing = -1;
	const	ResERR_CouldNotSet = -2;
	const	ResERR_ParmOutOfRange = -3;
	const	ResERR_WlmOutOfResources = -4;
	const	ResERR_WlmInternalError = -5;
	const	ResERR_NotAvailable = -6;
	const	ResERR_WlmBusy = -7;
	const	ResERR_NotInMeasurementMode = -8;
	const	ResERR_OnlyInMeasurementMode = -9;
	const	ResERR_ChannelNotAvailable = -10;
	const	ResERR_ChannelTemporarilyNotAvailable = -11;
	const	ResERR_CalOptionNotAvailable = -12;
	const	ResERR_CalWavelengthOutOfRange = -13;
	const	ResERR_BadCalibrationSignal = -14;
	const	ResERR_UnitNotAvailable = -15;

// Mode Constants for Callback-Export and WaitForWLMEvent-function
	const	cmiResultMode = 1;
	const	cmiRange = 2;
	const	cmiPulseMode = 3;
	const	cmiWideMode = 4;
	const	cmiFastMode = 5;
	const	cmiExposureMode = 6;
	const	cmiExposureValue1 = 7;
	const	cmiExposureValue2 = 8;
	const	cmiDelay = 9;
	const	cmiShift = 10;
	const	cmiShift2 = 11;
	const	cmiReduced = 12;
	const	cmiReduce = cmiReduced;
	const	cmiScale = 13;
	const	cmiTemperature = 14;
	const	cmiLink = 15;
	const	cmiOperation = 16;
	const	cmiDisplayMode = 17;
	const	cmiPattern1a = 18;
	const	cmiPattern1b = 19;
	const	cmiPattern2a = 20;
	const	cmiPattern2b = 21;
	const	cmiMin1 = 22;
	const	cmiMax1 = 23;
	const	cmiMin2 = 24;
	const	cmiMax2 = 25;
	const	cmiNowTick = 26;
	const	cmiCallback = 27;
	const	cmiFrequency1 = 28;
	const	cmiFrequency2 = 29;
	const	cmiDLLDetach = 30;
	const	cmiVersion = 31;
	const	cmiAnalysisMode = 32;
	const	cmiDeviationMode = 33;
	const	cmiDeviationReference = 34;
	const	cmiDeviationSensitivity = 35;
	const	cmiAppearance = 36;
	const	cmiWavelength1 = 42;
	const	cmiWavelength2 = 43;
	const	cmiLinewidth = 44;
	const	cmiLinkDlg = 56;
	const	cmiAnalysis = 57;
	const	cmiAnalogIn = 66;
	const	cmiAnalogOut = 67;
	const	cmiDistance = 69;
	const	cmiWavelength3 = 90;
	const	cmiWavelength4 = 91;
	const	cmiWavelength5 = 92;
	const	cmiWavelength6 = 93;
	const	cmiWavelength7 = 94;
	const	cmiWavelength8 = 95;
	const	cmiVersion0 = cmiVersion;
	const	cmiVersion1 = 96;
	const	cmiDLLAttach = 121;
	const	cmiSwitcherSignal = 123;
	const	cmiSwitcherMode = 124;
	const	cmiExposureValue11 = cmiExposureValue1;
	const	cmiExposureValue12 = 125;
	const	cmiExposureValue13 = 126;
	const	cmiExposureValue14 = 127;
	const	cmiExposureValue15 = 128;
	const	cmiExposureValue16 = 129;
	const	cmiExposureValue17 = 130;
	const	cmiExposureValue18 = 131;
	const	cmiExposureValue21 = cmiExposureValue2;
	const	cmiExposureValue22 = 132;
	const	cmiExposureValue23 = 133;
	const	cmiExposureValue24 = 134;
	const	cmiExposureValue25 = 135;
	const	cmiExposureValue26 = 136;
	const	cmiExposureValue27 = 137;
	const	cmiExposureValue28 = 138;
	const	cmiPatternAverage = 139;
	const	cmiPatternAvg1 = 140;
	const	cmiPatternAvg2 = 141;
	const	cmiAnalogOut1 = cmiAnalogOut;
	const	cmiAnalogOut2 = 142;
	const	cmiMin11 = cmiMin1;
	const	cmiMin12 = 146;
	const	cmiMin13 = 147;
	const	cmiMin14 = 148;
	const	cmiMin15 = 149;
	const	cmiMin16 = 150;
	const	cmiMin17 = 151;
	const	cmiMin18 = 152;
	const	cmiMin21 = cmiMin2;
	const	cmiMin22 = 153;
	const	cmiMin23 = 154;
	const	cmiMin24 = 155;
	const	cmiMin25 = 156;
	const	cmiMin26 = 157;
	const	cmiMin27 = 158;
	const	cmiMin28 = 159;
	const	cmiMax11 = cmiMax1;
	const	cmiMax12 = 160;
	const	cmiMax13 = 161;
	const	cmiMax14 = 162;
	const	cmiMax15 = 163;
	const	cmiMax16 = 164;
	const	cmiMax17 = 165;
	const	cmiMax18 = 166;
	const	cmiMax21 = cmiMax2;
	const	cmiMax22 = 167;
	const	cmiMax23 = 168;
	const	cmiMax24 = 169;
	const	cmiMax25 = 170;
	const	cmiMax26 = 171;
	const	cmiMax27 = 172;
	const	cmiMax28 = 173;
	const	cmiAvg11 = cmiPatternAvg1;
	const	cmiAvg12 = 174;
	const	cmiAvg13 = 175;
	const	cmiAvg14 = 176;
	const	cmiAvg15 = 177;
	const	cmiAvg16 = 178;
	const	cmiAvg17 = 179;
	const	cmiAvg18 = 180;
	const	cmiAvg21 = cmiPatternAvg2;
	const	cmiAvg22 = 181;
	const	cmiAvg23 = 182;
	const	cmiAvg24 = 183;
	const	cmiAvg25 = 184;
	const	cmiAvg26 = 185;
	const	cmiAvg27 = 186;
	const	cmiAvg28 = 187;

// WLM Control Mode Constants
	const	cCtrlWLMShow = 1;
	const	cCtrlWLMHide = 2;
	const	cCtrlWLMExit = 3;

// Measurement Control Mode Constants
	const	cCtrlMeasDelayRemove = 0;
	const	cCtrlMeasDelayGenerally = 1;
	const	cCtrlMeasDelayOnce = 2;
	const	cCtrlMeasDelayDenyUntil = 3;
	const	cCtrlMeasDelayIdleOnce = 4;
	const	cCtrlMeasDelayIdleEach = 5;
	const	cCtrlMeasDelayDefault = 6;

// Measurement Triggering Action Constants
	const	cCtrlMeasurementContinue = 0;
	const	cCtrlMeasurementInterrupt = 1;
	const	cCtrlMeasurementTriggerPoll = 2;
	const	cCtrlMeasurementTriggerSuccess = 3;

// ExposureRange Constants
	const	cExpoMin = 0;
	const	cExpoMax = 1;
	const	cExpo2Min = 2;
	const	cExpo2Max = 3;

// Amplitude Constants
	const	cMin1 = 0;
	const	cMin2 = 1;
	const	cMax1 = 2;
	const	cMax2 = 3;
	const	cAvg1 = 4;
	const	cAvg2 = 5;

// Measurement Range Constants
	const	cRange_250_410 = 4;
	const	cRange_250_425 = 0;
	const	cRange_300_410 = 3;
	const	cRange_350_500 = 5;
	const	cRange_400_725 = 1;
	const	cRange_700_1100 = 2;
	const	cRange_900_1500 = 6;
	const	cRange_1100_1700 = 7;

// Unit Constants for Get-/SetResultMode, GetLinewidth, Convert... and Calibration
	const	cReturnWavelengthVac = 0;
	const	cReturnWavelengthAir = 1;
	const	cReturnFrequency = 2;
	const	cReturnWavenumber = 3;
	const	cReturnPhotonEnergy = 4; // for Convert...-functions only

// Source Type Constants for Calibration
	const	cHeNe633 = 0;
	const	cHeNe1152 = 0;
	const	cNeL = 1;
	const	cOther = 2;

// Pattern- and Analysis Constants
	const	cPatternDisable = 0;
	const	cPatternEnable = 1;
	const	cAnalysisDisable = cPatternDisable;
	const	cAnalysisEnable = cPatternEnable;

	const	cSignal1Interferometers = 0;
	const	cSignal1WideInterferometer = 1;
	const	cSignal1Grating = 1;
	const	cSignal2Interferometers = 2;
	const	cSignal2WideInterferometer = 3;
	const	cSignalAnalysis = 4;
	const	cSignalAnalysisX = cSignalAnalysis;
	const	cSignalAnalysisY = cSignalAnalysis + 1;

// Return errorvalues of GetFrequency, GetWavelength and GetWLMVersion
	const	ErrNoValue = 0;
	const	ErrNoSignal = -1;
	const	ErrNoPulse = -8;
	const	ErrBadSignal = -2;
	const	ErrLowSignal = -3;
	const	ErrBigSignal = -4;
	const	ErrWlmMissing = -5;
	const	ErrNotAvailable = -6;
	const	InfNothingChanged = -7;
	const	ErrDiv0 = -13;
	const	ErrOutOfRange = -14;
	const	ErrUnitNotAvailable = -15;
	const	ErrMaxErr = ErrUnitNotAvailable;

// Return errorvalues of GetTemperature
	const	ErrTemperature = -1000;
	const	ErrTempNotMeasured = ErrTemperature + ErrNoValue;
	const	ErrTempNotAvailable = ErrTemperature + ErrNotAvailable;
	const	ErrTempWlmMissing = ErrTemperature + ErrWlmMissing;

// Return errorvalues of GetDistance
	// real errorvalues are ErrDistance combined with those of GetWavelength
	const	ErrDistance = -1000000000;
	const	ErrDistanceNotAvailable = ErrDistance + ErrNotAvailable;
	const	ErrDistanceWlmMissing = ErrDistance + ErrWlmMissing;

// *** end of wlmData.h