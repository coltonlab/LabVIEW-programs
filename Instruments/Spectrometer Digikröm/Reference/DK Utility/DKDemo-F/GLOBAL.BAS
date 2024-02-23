Attribute VB_Name = "GLOBAL"
'****************************************************************************
'*                                                                          *
'*   DkSeries Visual Basic Library software, for use with DK240, DK242, or  *
'*   DK480 CVI monochromators.                                              *
'*   Written in Microsoft Visual Basic 4.0 16-bit version for Windows.      *
'*                                                                          *
'****************************************************************************
'
'  Filename:  DK-Vb.BAS
'  Development Filename:  CM11XV2.BAS
'  Other Required Files:  All forms and other modules
'  Compiled Filename:  N/A (contents included to make exe based on 8-2049-A
'  File Rev: b
'
'  Copyright CVI Laser Corporation, 1997
'
'
'  Revision History:
'
'     Date      Rev  By     Desc. of Change/Modification
'     --------  ---  ---    --------------------------------------
'     07-21-97  1    TT     Created in VB 4.0 16-bit version.
'     11-23-98  1    TT     Changed all timeout% a bit longer.
'     07-26-02  2.0a TT     Upgraded to VB 6.0
'
'
'
'****************************************************************************



Option Explicit

' Softwave information
Global Const VERSION = "2"
Global Const REVISION = "1"
Global Const HelpFile = "Dk.hlp"    '"CM11x.hlp" '"Dk.hlp"

' Configuration information.
Global Const DefPort = 0    'The default port is com1; 2: com2 ...
Global Const DefBaud = 0    'The default baudrate is 9600;

' File Open/Save Dialog Flags
Global Const OFN_OVERWRITEPROMPT = &H2&
Global Const OFN_HIDEREADONLY = &H4&
Global Const OFN_FILEMUSTEXIST = &H1000&

' MsgBox parameters
Global Const MB_YESNO = 4
Global Const MB_RETRYCANCEL = 5        ' Retry and Cancel buttons
Global Const MB_ICONSTOP = 16          ' Critical message
Global Const MB_ICONQUESTION = 32      ' Warning query
Global Const MB_ICONEXCLAMATION = 48   ' Warning message
Global Const MB_ICONINFORMATION = 64   ' Information message

' Show parameters
Global Const MODAL = 1
Global Const MODELESS = 0

' MsgBox return values
Global Const IDOK = 1                  ' OK button pressed
Global Const IDCANCEL = 2              ' Cancel button pressed
Global Const IDABORT = 3               ' Abort button pressed
Global Const IDRETRY = 4               ' Retry button pressed
Global Const IDIGNORE = 5              ' Ignore button pressed
Global Const IDYES = 6                 ' Yes button pressed
Global Const IDNO = 7                  ' No button pressed
Global Const IDCONTINUE = 8            ' Continue button pressed

' Commands to pass WinHelp()
Global Const HELP_CONTEXT = &H1 '  Display topic in ulTopic
Global Const HELP_QUIT = &H2    '  Terminate help
Global Const HELP_INDEX = &H3   '  Display index
Global Const HELP_HELPONHELP = &H4      '  Display help on using help
Global Const HELP_SETINDEX = &H5        '  Set the current Index for multi index help
Global Const HELP_KEY = &H101           '  Display topic for keyword in offabData
Global Const HELP_MULTIKEY = &H201

' Window 3.1 commands to pass WinHelp()
Global Const HELP_CONTENTS = &H3     ' Display Help for a particular topic
Global Const HELP_SETCONTENTS = &H5  ' Display Help contents topic
Global Const HELP_CONTEXTPOPUP = &H8 ' Display Help topic in popup window
Global Const HELP_FORCEFILE = &H9    ' Ensure correct Help file is displayed
Global Const HELP_COMMAND = &H102    ' Execute Help macro
Global Const HELP_PARTIALKEY = &H105 ' Display topic found in keyword list
Global Const HELP_SETWINPOS = &H203  ' Display and position Help window

' Win Constants
Global Const WF_CPU286 = &H2&
Global Const WF_CPU386 = &H4&
Global Const WF_CPU486 = &H8&
Global Const WF_STANDARD = &H10&
Global Const WF_ENHANCED = &H20&
Global Const WF_80x87 = &H400&

' Win32
Public Const PROCESSOR_INTEL_386 = 386
Public Const PROCESSOR_INTEL_486 = 486
Public Const PROCESSOR_INTEL_PENTIUM = 586
Public Const PROCESSOR_MIPS_R4000 = 4000
Public Const PROCESSOR_ALPHA_21064 = 21064

' Global varables
Global gblCancel%   'True or False
Global gblSerial$
Global gblInitCom%
Global gblOkCancel%, gblContinueCancel%
Global gblOrder%, gblUnitToNm!, gblUnitsN%
Global gblNGrtInstd%    'Number of gratings installed on turret#1
Global gblNGrtSelted&   'Number of grating selected.
Global gblCurWL&, gblCurGr&, gblCurBl&
Global gblBaud%, gblPortNo%
Global gblSSpeed%, gblCurSize%
Global gblType% '0: single, 1: Additive dispersion, 254: Subtractive dps.
Global gblIniExist% 'True: if DkSeries.ini exists.
Global gblAddr%, gblOVal&, gblNVal&
Global gblS1%, gblS2%, gblS3%   'S1: Entrance slit, S2: Exit, S3: Middle.
Global gblNovAdd29&     ' Dk configuration byte.


Global gblFilter%

'Global modNovContents&(64)

'Global modNovContents&(127)

Type MEMORYSTATUS   '  32 Bytes
        dwLength As Long
        dwMemoryLoad As Long
        dwTotalPhys As Long
        dwAvailPhys As Long
        dwTotalPageFile As Long
        dwAvailPageFile As Long
        dwTotalVirtual As Long
        dwAvailVirtual As Long
End Type

Type SYSTEM_INFO  '  36  Bytes
        dwOemID As Long
        dwPageSize As Long
        lpMinimumApplicationAddress As Long
        lpMaximumApplicationAddress As Long
        dwActiveProcessorMask As Long
        dwNumberOrfProcessors As Long
        dwProcessorType As Long
        dwAllocationGranularity As Long
        wProcessorLevel As Integer
        wProcessorRevision As Integer
End Type

' DLL's declarations
Declare Function WinHelp Lib "user32" Alias "WinHelpA" (ByVal hwnd As Long, ByVal lpHelpFile As String, ByVal wCommand As Long, ByVal dwData As Long) As Long
Declare Function GetPrivateProfileInt& Lib "kernel32" Alias "GetPrivateProfileIntA" (ByVal lpApplicationName As String, ByVal lpKeyName As String, ByVal nDefault As Long, ByVal lpFileName As String)
Declare Function WritePrivateProfileString& Lib "kernel32" Alias "WritePrivateProfileStringA" (ByVal lpApplicationName As String, ByVal lpKeyName As Any, ByVal lpString As String, ByVal lpFileName As String)
Declare Sub GlobalMemoryStatus Lib "kernel32" (lpBuffer As MEMORYSTATUS)
Declare Sub GetSystemInfo Lib "kernel32" (lpSystemInfo As SYSTEM_INFO)

Sub Centerform(X As Form)
  X.Top = Screen.Height / 2 - X.Height / 2
  X.Left = Screen.Width / 2 - X.Width / 2
End Sub

Function COMInit%(PortNo%, Baudrate%)
 'Returns true if success; otherwise this function returns false.
  Dim Status%, BaudLocal%, PortLocal%
  ' Remember: will get portnumber, and baudrate.
  On Error GoTo COMInitErr
  PortLocal% = PortNo% + 1
  BaudLocal% = 9600 / 2 ^ Baudrate%
  Status% = DKInitComPort%(PortLocal%, BaudLocal%, frmDK.comComm1)
  If Status% > 127 Then
    'An error has occurred.
    COMInit% = False
  Else
    COMInit% = COMTest%()
  End If
COMInitResume:
  Exit Function

COMInitErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "Init. Comm. Port Error"
  Resume COMInitResume

End Function

Function COMTest%()
  'Returns true if success; otherwise this function returns false.
  Dim Status%
  On Error GoTo COMTestErr
  'MsgBox "Sending :  27 ", MB_ICONINFORMATION, "Init. Comm. Port"
  Status% = DKEcho%(frmDK.comComm1, 1)   '1: is Timeout% in seconds
  If Status% > 127 Then
    MsgBox "The monochromator is not responding ", MB_ICONQUESTION, "Init. Comm. Port"
    gblInitCom% = False
    COMTest% = False
  Else
    gblInitCom% = True
    COMTest% = True
  End If

COMTestResume:
  Exit Function

COMTestErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "Init. Comm. Port Error"
  Resume COMTestResume

End Function

Function GetDkInit%()
' If DkSeries.ini doesn't exist, then this function will return False;
' otherwise, it will return true.
  Dim subPort%, subBaud%
  Dim Ret%
  
  subPort% = GetPrivateProfileInt&("DkSeries", "Port", -1, "DkSeries.ini")
  If subPort% = -1 Then
    GetDkInit% = False
  Else
    GetDkInit% = True
    subBaud% = GetPrivateProfileInt&("DkSeries", "Baud", -1, "DkSeries.ini")
    gblPortNo% = subPort%
    gblBaud% = subBaud%
  End If

End Function

Sub InitQueries()
  Dim DataL&, DataS$, Status%, Timeout%
  Dim AData%(5), Data1I%, Data2I%, Data3I%
  Timeout% = 5
  ' Query current wavelength
  Status% = DKWaveQ%(DataL&, frmDK.comComm1, Timeout%)
  If Status% > 127 Then GoTo ErrMessage
    gblCurWL& = DataL&
    
  ' Query the Novram location 29
  Status% = DKNovramRead%(29, DataL&, frmDK.comComm1, Timeout%)
  If Status% > 127 Then GoTo ErrMessage
    gblNovAdd29& = DataL&
  ' Query the slit widths
  If (gblNovAdd29& And &H2) Then
    Status% = DKSlit242Q%(Data1I%, Data2I%, Data3I%, frmDK.comComm1, Timeout%)
    If Status% > 127 Then GoTo ErrMessage
      gblS1% = Data1I%
      gblS2% = Data2I%
      gblS3% = Data3I%
  Else
    Status% = DKSlit240Q%(Data1I%, Data2I%, frmDK.comComm1, Timeout%)
    If Status% > 127 Then GoTo ErrMessage
      gblS1% = Data1I%
      gblS2% = Data2I%
      gblS3% = 0
  End If
    
  ' Query the machine serial number.
  Status% = DKSerialQ%(DataS$, frmDK.comComm1, Timeout%)
  If Status% > 127 Then GoTo ErrMessage
  gblSerial$ = DataS$
  
  ' Query the type of the machine
  ' 0: single, 1: Additive dispersion, 254: Subtractive dps.
  'Status% = DKQuery%(1, DataL&, frmDK.comComm1, Timeout%)
  'If Status% > 127 Then GoTo ErrMessage
  'gblType% = DataL&
  
  ' Execute the Grtid? command
  Status% = DKGrtidQ%(AData%(), frmDK.comComm1, Timeout%)
  If Status% > 127 Then GoTo ErrMessage
  gblNGrtInstd% = AData%(0)    'Number of gratings installed on turret#1
  gblNGrtSelted& = AData%(1)   'Number of grating selected.
  gblCurGr& = AData%(2) * 256 + AData%(3)
  gblCurBl& = AData%(4) * 256 + AData%(5)
  
  'Extract the current order from bit 3 of Status% byte
  'gblOrder% = (Status% And 8) \ 8
  'Query the current scan speed.
  Status% = DKSpeedQ%(DataL&, frmDK.comComm1, Timeout%)
  If Status% > 127 Then GoTo ErrMessage
  gblSSpeed% = DataL&
  'Query the current size.
  'Status% = DKQuery%(6, DataL&, frmDK.comComm1, Timeout%)

  'If Status% > 127 Then GoTo ErrMessage
  'gblCurSize% = DataL&
  Exit Sub

ErrMessage:
  MsgBox "An error has occurred !", MB_ICONSTOP

End Sub

Function SaveCmInit%()
' This function returns true if it is succeful.
' Otherwise, it is false.
  Dim subPort%, subBaud%
  Dim Ret1%, Ret2%
  subPort% = gblPortNo%
  subBaud% = gblBaud%
  Ret1% = WritePrivateProfileString&("DkSeries", ByVal "Port", Str$(subPort%), "DkSeries.ini")
  Ret2% = WritePrivateProfileString&("DkSeries", ByVal "Baud", Str$(subBaud%), "DkSeries.ini")
  If Ret1% = 0 Or Ret2% = 0 Then
    SaveCmInit% = False
  Else
    SaveCmInit% = True
  End If

End Function

Sub SaveConfig()
  Dim Baud$
  If gblInitCom% Then
    If SaveCmInit%() Then
      Baud$ = Str$(9600 / (2 ^ gblBaud%))
      MsgBox "COM " & gblPortNo% + 1 & " and " & Baud$ & " Baud rate have been saved. "
    Else
      MsgBox "An error has occurred. The current configuration cannot be saved. "
    End If
  Else
    MsgBox "Did you initialize a serial port ? "
  End If

End Sub

Sub TopLeftform(X As Form)
  X.Top = 0
  X.Left = 0

End Sub

