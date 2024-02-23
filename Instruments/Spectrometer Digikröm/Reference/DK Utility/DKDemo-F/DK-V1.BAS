Attribute VB_Name = "DK_V1"
'****************************************************************************
'*                                                                          *
'*   DkSeries Visual Basic Library software, for use with DK240, DK242, or  *
'*   DK480 CVI monochromators.                                              *
'*   Written in Microsoft Visual Basic 4.0 16-bit version for Windows.      *
'*                                                                          *
'****************************************************************************
'
'  Filename:  DK-V1.BAS
'  Development Filename:  CM11XV2.BAS
'  Other Required Files:  All forms and other modules
'  Compiled Filename:  N/A (contents included to make exe based on 8-2049-A
'  File Rev: 1
'
'  Copyright CVI Laser Corporation, 1997
'
'
'  Revision History:
'
'     Date      Rev  By     Desc. of Change/Modification
'     --------  ---  ---    --------------------------------------
'     07-21-97  1b   TT     Created in VB 4.0 16-bit version
'     02-27-98  1c   TT     Added SlotWidth routine
'     11-23-98  1d   TT     Fixed the problem with DK242. It has error #5
'                           when the program starts initialization. See ~1d
'                           ~1d for changes.
'     03-13-2009 1e  NCT    Modified to adjust M1 or M2 independently when
'                           calibrating zero. ~1e for changes
'                           -added slot width for machine 2  ~1e_1
'                           -fixed width display for slit 3 (DK242)  ~1e_2
'
'****************************************************************************

Option Explicit
Const MB_ICONEXCLAMATION = 48   ' Warning message
Const MB_ICONSTOP = 16          ' Critical message

Dim ErrorStatus%    'Error: bit 7 is set; otherwise bit 7 is 0.
Dim StatusByte$     'status byte from DkSeries
Dim CancelByte$     'CancelByte$ is "24"
Dim HighByte%, MiddleByte%, LowByte%
Dim Echoed%         'Echoed byte
Dim Cmd%            'commands
Function DKBaud%(Baud%, PortNo%, dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKCalibrate%(Wavelength&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Ajusts the monochromator calibration factor so the current wavelength
' position is defined as the wavelength sent with the command.
'
' CAUTION!  DO NOT calibrate the monochromator at very short wavelengths
'           (less than 100 nm.)  Always calibrate to a known reference
'           in the working region of the grating, away from 0 nm.
'
' Command: To Instrument:   <18>
'          From Instrument: <18>
'          To Instrument:   <Wavelength High Byte><W.Mid.Byte><W.Low Byte>
'          From Instrument: <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter WaveLength& is a LONG INTEGER, and dkPort is a commnunication
' control.

'
' Wavelength& may range from 0 through 16777215, but acceptable values to
' the monochromator will depend on the ruling of the grating selected.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKCalibrateErr
  Cmd% = 18
  If (Wavelength& >= 0) And (Wavelength& <= 16777215) Then
    ' Calculate the 3 byte wavelength specifier to send in the command
    HighByte% = Int(Wavelength& / 65536!)
    MiddleByte% = Int((Wavelength& - 65536! * HighByte%) / 256)
    LowByte% = Int(Wavelength& - (65536! * HighByte% + 256! * MiddleByte%))
    ' Sending Calibrate command.
     dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKCalibrateResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKCalibrateErr
    ' Send out 3-byte wavelength.
    dkPort.Output = Chr$(HighByte%) + Chr$(MiddleByte%) + Chr$(LowByte%)
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)   'Timeout% in seconds
  Else
    ErrorStatus% = 128      'Error; set bit 7 of return value
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If

DKCalibrateResume:
  DKCalibrate% = ErrorStatus%
  Exit Function

DKCalibrateErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKCalibrateResume

End Function

Function DKDecM1%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <01>
'          From Instrument: <01>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 1
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err

  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKDecM1% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

Function DKDecM2%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M2 (Exit side grating turret in a
' DK242)
'
'
' Command: To Instrument:   <02>
'          From Instrument: <02>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM2Err
  Cmd% = 2
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM2Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM2Err
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM2Resume:
  DKDecM2% = ErrorStatus%
  Exit Function

DKDecM2Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM2Resume

End Function
Function DKReset%(dkPort As Control, Timeout%)

' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Verifies communication by sending a single byte and receiving that same
' byte back.
'
' Command: To Instrument:   <255><255><255>
'           Action: DK does resetting.
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a control, and Timeout% as an integer.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim DelayTime%, Byte1$, Minutes%
  Cmd% = 255
  On Error GoTo DKResetErr
  dkPort.Output = Chr$(Cmd%) + Chr$(Cmd%) + Chr$(Cmd%)
  ErrorStatus% = 0

DKResetResume:
  DKReset% = ErrorStatus%
  Exit Function

DKResetErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128          'Error; set bit 7
  Resume DKResetResume

End Function
Function DKEcho%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Verifies communication by sending a single byte and receiving that same
' byte back.
'
' Command: To Instrument:   <27>
'          From Instrument: <27>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a control, and Timeout% as an integer.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim DelayTime%, Byte1$, Minutes%  ' ~2CM
  Cmd% = 27
  On Error GoTo DKEchoErr
  dkPort.Output = Chr$(Cmd%)
  ' Get Echoed Byte
  If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKEchoResume
  End If
  ' ~2CM
  Byte1$ = dkPort.Input          'Read in byte
  If Asc(Byte1$) = Cmd% Then
    ErrorStatus% = 0            'no error
  Else
    ErrorStatus% = 128          'Error; set bit 7
  End If

DKEchoResume:
  DKEcho% = ErrorStatus%
  Exit Function

DKEchoErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128          'Error; set bit 7
  Resume DKEchoResume

End Function

Function DKGetStatusCancel%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Gets the status and cancel bytes sent back from the monochromator. This
' function is used by other monochromator library functions and is intended
' to be used elsewhere.
'
' This function returns an INTEGER that is value of the monochromator's
' status byte.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
'
  Dim DelayTime%, Minutes%, TimeoutErr%, Temp%
  On Error GoTo CMGetStatusCancelErr
  ' Get Status Byte
  If Timeout% > 0 Then
    TimeoutErr% = DKTimeout%(dkPort, Timeout%)
    If TimeoutErr% = 128 Then
      ErrorStatus% = TimeoutErr%
      GoTo CMGetStatusCancelResume
    End If
  End If
  
  StatusByte$ = dkPort.Input              'Read in status byte
  ErrorStatus% = Asc(StatusByte$)         'Convert from char to integer
  Temp% = ErrorStatus% And &H40
  If (Temp% = &H40) Then
    ErrorStatus% = ErrorStatus% And &H7F
  End If

  ' Get Cancel Byte
  If Timeout% > 0 Then
    TimeoutErr% = DKTimeout%(dkPort, Timeout%)
    If TimeoutErr% = 128 Then
      ErrorStatus% = TimeoutErr%
      GoTo CMGetStatusCancelResume
    End If
  End If
  CancelByte$ = dkPort.Input              'Read in final byte
  If Asc(CancelByte$) <> 24 Then ErrorStatus% = 128

CMGetStatusCancelResume:
  DKGetStatusCancel% = ErrorStatus%
  Exit Function

CMGetStatusCancelErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume CMGetStatusCancelResume

End Function

Function DKGoto%(Wavelength&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Moves the monochromator to a desired wavelength in tenths of Angstroms.
'
' Command: To Instrument:   <16>
'          From Instrument: <16>
'          To Instrument:   <Wavelength High Byte><W.Mid.Byte><W.Low Byte>
'          From Instrument: <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter WaveLength& is a LONG INTEGER and dkPort as commnunication
' control.
'
' Wavelength& may range from 0 through 16,777,215, but acceptable values to
' the monochromator will depend on the ruling of the grating selected and
' the current monochromator UNITS.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKGotoErr
  Cmd% = 16
  If (Wavelength& >= 0) And (Wavelength& <= 16777215) Then
    ' Calculate the 3 byte wavelength specifier to send in the command
    HighByte% = Int(Wavelength& / 65536!)
    MiddleByte% = Int((Wavelength& - 65536! * HighByte%) / 256)
    LowByte% = Int(Wavelength& - (65536! * HighByte% + 256! * MiddleByte%))
    dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKGotoResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKGotoErr
    ' Send out 3-byte wavelength.
    dkPort.Output = Chr$(HighByte%) + Chr$(MiddleByte%) + Chr$(LowByte%)
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)   'Timeout% in seconds
  Else
    ErrorStatus% = 128      'Error; set bit 7 of return value
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If

DKGotoResume:
  DKGoto% = ErrorStatus%
  Exit Function

DKGotoErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKGotoResume

End Function

Function DKGrtidQ%(AData%(), dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Returns the current grating information
'
' Command: To Instrument:   <19>
'          From Instrument: <19>
'                           <6 byte grating ruling identifier>
'                           <Status Byte><24>
'
' The six bytes are:
' Byte 1: Number of gratings installed in monochromator (1-3)
' Byte 2: Number of grating currently being used (1-3)
' Byte 3: High byte of current grating ruling (g/mm)
' Byte 4: Low byte of current grating ruling (g/mm)
' Byte 5: High byte of current grating blaze wavelength (nm)
' Byte 6: Low byte of current grating blaze wavelenght (nm)
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  AData% is a array of 6 INTEGERs.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim I%
  On Error GoTo DKGrtidQErr
  Cmd% = 19
  ' Sending the Grtid? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKGrtidQResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKGrtidQErr
  
  'Get returned query data
  For I% = 0 To 5
    AData%(I%) = Asc(dkPort.Input)
  Next I%

  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKGrtidQResume:
  DKGrtidQ% = ErrorStatus%
  Exit Function

DKGrtidQErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKGrtidQResume

End Function
Function DKStepUp%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the clockwise direction for M1 (Entrance side grating turret in a DK242,
' or the only turret in a DK240.)
'
' Command: To Instrument:   <07>
'          From Instrument: <07>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKStepUpErr
  Cmd% = 7
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKStepUpResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKStepUpErr
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKStepUpResume:
  DKStepUp% = ErrorStatus%
  Exit Function

DKStepUpErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKStepUpResume

End Function
Function DKStepDn%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the clockwise direction for M1 (Entrance side grating turret in a DK242,
' or the only turret in a DK240.)
'
' Command: To Instrument:   <01>
'          From Instrument: <01>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKStepDnErr
  Cmd% = 1
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKStepDnResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKStepDnErr
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKStepDnResume:
  DKStepDn% = ErrorStatus%
  Exit Function

DKStepDnErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKStepDnResume


End Function
Function DKScanUp%(dkPort As Control, TimeScan%, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the clockwise direction for M1 (Entrance side grating turret in a DK242,
' or the only turret in a DK240.)
'
' Command: To Instrument:   <09>
'          From Instrument: <09>
'                   Time to scan.....
'          To Instrument:   <24>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKScanUpErr
  Cmd% = 9
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKScanUpResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKScanUpErr
  
  'Stop scanning
  ErrorStatus% = DKTimeout%(dkPort, TimeScan%)
  dkPort.Output = Chr$(24)
  
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKScanUpResume:
  DKScanUp% = ErrorStatus%
  Exit Function

DKScanUpErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKScanUpResume

End Function
Function DKScanDn%(dkPort As Control, TimeScan%, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the counter-clockwise direction for M1 (Exit side grating turret in a DK242,
' or the only turret in a DK240.)
'
' Command: To Instrument:   <03>
'          From Instrument: <03>
'                   Time to scan.....
'          To Instrument:   <24>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKScanDnErr
  Cmd% = 3
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKScanDnResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKScanDnErr
  
  'Stop scanning
  ErrorStatus% = DKTimeout%(dkPort, TimeScan%)
  dkPort.Output = Chr$(24)
  
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKScanDnResume:
  DKScanDn% = ErrorStatus%
  Exit Function

DKScanDnErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKScanDnResume

End Function
Function DKIncM1%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the clockwise direction for M1 (Entrance side grating turret in a DK242,
' or the only turret in a DK240.)
'
' Command: To Instrument:   <07>
'          From Instrument: <07>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKIncM1Err
  Cmd% = 7
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKIncM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKIncM1Err
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKIncM1Resume:
  DKIncM1% = ErrorStatus%
  Exit Function

DKIncM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKIncM1Resume

End Function

Function DKIncM2%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Increments the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 deg/step (ustep mode)
' in the clockwise direction for M2 (Exit side grating turret in a DK242).
'
'
' Command: To Instrument:   <08>
'          From Instrument: <08>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKIncM2Err
  Cmd% = 8
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKIncM2Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKIncM2Err
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKIncM2Resume:
  DKIncM2% = ErrorStatus%
  Exit Function

DKIncM2Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKIncM2Resume

End Function

Function DKInitComPort%(PortNo%, Baud%, dkPort As Control)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Opens a RS232 com port to communicate with the monochromator.  8 data
' bits, 1 stop bit, and no parity are fixed.  Baud rate is selectable,
' as is the COM port to use.  The baud rate selected here must match the
' monochromator's baud rate (selected with the BAUD command.)
'
' This function must be run before any other monochromator library function
' calls.
'
' This function's return value is an INTEGER.  A value of zero indicates
' success.  Non-zero return values indicate an error has occured.
'
' The passed parameters PortNo%, and Baud% all INTEGERs. dkPort as a
' commnunications Control.
'
' Valid choices for PortNo% are 1 = COM1, 2 = COM2, 3 = COM3, 4 = COM4.
'
' Valid baud rates for CM110/112 are 9600, 4800, 2400, 1200, 600, 300, 150 and 75,
' but valid baud rates for Visual Basic are 9600, 4800, 2400, 1200, 600, 300.
'
  Dim InS$
  On Error GoTo DKInitComPortErr
  If dkPort.PortOpen Then
    dkPort.PortOpen = False
  End If
  dkPort.CommPort = PortNo%
  dkPort.Settings = Baud% & ",N,8,1"
  dkPort.RTSEnable = True             ' Enables the Request To Send line
  dkPort.InputLen = 1                 ' Read 1 character at the receive buffer. 0: entire contents.
  dkPort.PortOpen = True

  ErrorStatus% = 0                      ' No error

DKInitComPortResume:
  DKInitComPort% = ErrorStatus%
  Exit Function

DKInitComPortErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKInitComPortResume

End Function

Function DKNovramRead%(Address%, DataL&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Reads a word from the monochromator's non-volatile memory.
'
' Command: To Instrument:   <56>
'          From Instrument: <56>
'          To Instrument:   <Address Byte>
'          From Instrument: <Data High Byte><Data Low Byte>
'                           <Status Byte><24>
'
' dkPort as a communication control.
' The passed parameters Address%, Timeout% are intergers.
' DataByte% contains a returned byte.
'
' This function's returned value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' Valid choices for Address% are 1 through 64. If the number is bigger than
' 64, it will be cut off the bigger part in AND format. The status byte in
' this case will be > 127.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim High&, Low&
  On Error GoTo DKNovramReadErr
  Cmd% = 56
  If ((Address% >= 1) And (Address% <= 64)) Then
    ' Sending out Novram Read command
    dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKNovramReadResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKNovramReadErr
    ' Send out Address% byte
    dkPort.Output = Chr$(Address%)
    ' Check for returned data
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKNovramReadResume
    End If
    High& = Asc(dkPort.Input)         'Read the high byte.
    Low& = Asc(dkPort.Input)          'Read the low byte.
    DataL& = High& * 256 + Low&
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)
  Else
    ErrorStatus% = 128
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If

DKNovramReadResume:
  DKNovramRead% = ErrorStatus%
  Exit Function

DKNovramReadErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKNovramReadResume

End Function

Function DKNovramWrite%(Address%, DataWord&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Writes a word (2 bytes) to the monochromator's non-volatile memory.
'
' WARNING!!!  Improper use of this command may corrupt the configuration
'             and calibration information of the monochromator.  DO NOT
'             use this command if you are unsure of the implications!
'
' Command: To Instrument:   <59>
'          From Instrement: <59>
'          To Instrument:   <Address% 1-64>
'                           <Data High Byte><Data Low Byte><Checksum Byte>
'          From Instrument: <Status Byte><24>
'
' Checksum = Address% + Data High Byte + Data Low Byte
' The addition is operated in 1 byte method. Truncate the cary bit if existed.
' Therefore Checksum <=255.
'
' dkPort is a communication control.
' The passed parameters Address%, Timeout% are intergers.
' DataWord& contains a returned byte.
'
' This function's returned value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' Valid choices for Address% are 1 through 64.
' Valid values for DataWord& are 0 through 65535.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim CheckSum%
  On Error GoTo DKNovramWriteErr
  Cmd% = 59
  If ((Address% >= 1) And (Address% <= 64) And (DataWord& >= 0) And (DataWord& <= 65535)) Then
    ' Convert DataWord to two bytes.
    HighByte% = Int(DataWord& / 256!)
    LowByte% = Int(DataWord& - 256! * HighByte%)
    CheckSum% = Address% + HighByte% + LowByte%
    If CheckSum% > 255 Then
      CheckSum% = CheckSum% - 256     'truncate to 1 byte long
    End If
    If CheckSum% > 255 Then
      CheckSum% = CheckSum% - 256     'truncate to 1 byte long
    End If
    ' Sending out Novram Write command.
    dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKNovramWriteResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKNovramWriteErr
    ' Sending out Address% byte
    dkPort.Output = Chr$(Address%)
    ' Sending out two data bytes.
    dkPort.Output = Chr$(HighByte%) + Chr$(LowByte%) + Chr$(CheckSum%)
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)
  Else
    ErrorStatus% = 128      'Error; set bit 7 of return value
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If

DKNovramWriteResume:
  DKNovramWrite% = ErrorStatus%
  Exit Function

DKNovramWriteErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKNovramWriteResume

End Function

Function DKOrder%(Order%, dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKQuery%(QueryCode%, DataL&, dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKRtsCts%(dkPort As Control, RtsOutPc%, CtsInPc%)
' RtsOutPc% is true if the PC enables the RTS line, and vive-versa.
' ClsInPc% is true if CTS line is high, and vice-versa
  On Error GoTo CMRtsCtsErr
  ErrorStatus% = 0      ' No error.
  RtsOutPc% = dkPort.RTSEnable
  CtsInPc% = dkPort.CTSHolding

CMRtsCtsResume:
  DKRtsCts% = ErrorStatus%
  Exit Function

CMRtsCtsErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume CMRtsCtsResume



End Function

Function DKSlotWidth%(DataL&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the monochromator for current slot width.
'
' Command: To Instrument:   <37>
'          From Instrument: <37>
'                           <Data High Byte><Data Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  DataL& is a LONG INTEGER.
'
' DataL& = (Data High Byte) * 256 + (Data Low Byte)
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim High&, Low&
  On Error GoTo DKSlotWidthErr
  Cmd% = 37
  ' Sending the Speed? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSlotWidthResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSlotWidthErr
  
  'Get returned query data
  High& = Asc(dkPort.Input)         'Read the high byte.
  Low& = Asc(dkPort.Input)          'Read the low byte.
  
  DataL& = High& * 256 + Low&

  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSlotWidthResume:
  DKSlotWidth% = ErrorStatus%
  Exit Function

DKSlotWidthErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSlotWidthResume

End Function

'begin ~1e_1
Function DKSlotWidth2%(DataL&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the monochromator for current slot width.
'
' Command: To Instrument:   <38>
'          From Instrument: <38>
'                           <Data High Byte><Data Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  DataL& is a LONG INTEGER.
'
' DataL& = (Data High Byte) * 256 + (Data Low Byte)
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim High&, Low&
  On Error GoTo DKSlotWidthErr
  Cmd% = 38
  ' Sending the Speed? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSlotWidthResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSlotWidthErr
  
  'Get returned query data
  High& = Asc(dkPort.Input)         'Read the high byte.
  Low& = Asc(dkPort.Input)          'Read the low byte.
  
  DataL& = High& * 256 + Low&

  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSlotWidthResume:
  DKSlotWidth2% = ErrorStatus%
  Exit Function

DKSlotWidthErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSlotWidthResume
'end ~1e_1
End Function


Function DKSltAdjCal%(SlitByte%, SlitWidth%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Sets the monochromator's slit width of the entrance, exit, or middle slit
'(DK242 only).
' If SlitByte% = 14, all slits will be set.
' If SlitByte% = 31, entrance slit will be set.
' If SlitByte% = 32, exit slit will be set.
' If SlitByte% = 34, middle slit will be set (DK242 only).
'
' Allows for recalibration for entrance, exit, or middle slit(DK242 only).
' If SlitByte% = 22, for entrance slit.
' If SlitByte% = 23, for exit slit.
' If SlitByte% = 35, for middle slit (DK242 only).
'
' Command: To Instrument:   <SlitByte%>
'          From Instrument: <SlitByte%>
'          To Instrument:   <SW High Byte><SW Low Byte>
'          From Instrument: <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort is a communication control.
' The passed parameters SlitByte%, SlitWidth% and Timeout% are INTEGERs.
'
' SlitWidth% is always in microns.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
'  Calculate the 2 byte speed specifier to send in the command
'
  On Error GoTo DKSltAdjErr
  Cmd% = SlitByte%
  HighByte% = Int(SlitWidth% / 256!)
  LowByte% = Int(SlitWidth% - 256! * HighByte%)
  ' Sending out Slit adjustment command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSltAdjResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSltAdjErr
  ' Send out 2-byte speed.
  dkPort.Output = Chr$(HighByte%) + Chr$(LowByte%)
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSltAdjResume:
  DKSltAdjCal% = ErrorStatus%
  Exit Function

DKSltAdjErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSltAdjResume

End Function


Function DKScan%(EndWavelength&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Scans the monochromator between a present position and an end position at
' a rate determined by the SPEED command.  The present wavelength may be
' greater than the end wavelength or vice versa.
'
' Command: To Instrument:   <12>
'          From Instrument: <12>
'          To Instrument:   <End Wavelength High Byte>
'                           <End Wavelength Middle Byte>
'                           <End Wavelength Low Byte>
'          From Instrument: <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter EndWavelength& are LONG INTEGERs.
' dkPort is a communication control.
'
' Wavelengths may range from 0 through 16777215, but acceptable values to
' the monochromator will depend on the ruling of the grating selected.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKScanErr
  Cmd% = 12
  If (EndWavelength& >= 0) And (EndWavelength& <= 16777215) Then
    ' Calculate the 3 byte wavelength specifier to send in the command
    HighByte% = Int(EndWavelength& / 65536!)
    MiddleByte% = Int((EndWavelength& - 65536! * HighByte%) / 256)
    LowByte% = Int(EndWavelength& - (65536! * HighByte% + 256! * MiddleByte%))
    dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKScanResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKScanErr
    ' Send out 3-byte wavelength.
    dkPort.Output = Chr$(HighByte%) + Chr$(MiddleByte%) + Chr$(LowByte%)
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)
  Else
    ErrorStatus% = 128      'Error; set bit 7 of return value
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If


DKScanResume:
  DKScan% = ErrorStatus%
  Exit Function

DKScanErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKScanResume

End Function

Function DKGrtsel%(GratingNo%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Selects the grating that will be used.
' The monochromator will automatically reset after this command is performed.
' The cancel byte will be received after a look-up table created.
'
' Command: To Instrument:   <26>
'          From Instrument: <26>
'                           <Grating Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameters GratingNo% as INTEGER, and dkPort as commnunication
' control.
'
' Valid values for GratingNo% are 1 , 2 and 3.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKGrtselErr
  Cmd% = 26
  If (GratingNo% >= 1) And (GratingNo% <= 3) Then
    ' Send out Grtsel command.
    dkPort.Output = Chr$(Cmd%)
    ' Checking for echoed byte.
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKGrtselResume
    End If
    Echoed% = Asc(dkPort.Input)       'Read the echoed byte
    If Echoed% <> Cmd% Then GoTo DKGrtselErr
    ' Send out grating byte
    dkPort.Output = Chr$(GratingNo%)
    ' Get Status and Cancel Bytes
    ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)   'Timeout% in seconds
  Else
    ErrorStatus% = 128
    MsgBox "The entered number is out of range", MB_ICONEXCLAMATION, "DK.BAS"
  End If

DKGrtselResume:
  DKGrtsel% = ErrorStatus%
  Exit Function

DKGrtselErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKGrtselResume

End Function

Function DKSerialQ%(DataS$, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the monochromator for the machine serial number.
'
' Command: To Instrument:   <33>
'          From Instrument: <33>
'                           <5 Digit ASCII Serial Number>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  DataL& is a LONG INTEGER.
'
' DataS$ = 5 Digit ASCII Serial Number
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim I%
  On Error GoTo DKSerialQErr
  DataS$ = ""
  Cmd% = 33
  ' Sending the Serial? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSerialQResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSerialQErr
  ' Get returned serial number
  For I% = 1 To 5
    DataS$ = DataS$ & dkPort.Input
  Next I%
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSerialQResume:
  DKSerialQ% = ErrorStatus%
  Exit Function

DKSerialQErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSerialQResume

End Function






Function DKSize%(StepSize%, dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKSlit240Q%(S1Data%, S2Data%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the DK240 monochromator for current entrance and exit slit width.
'
' Command: To Instrument:   <30>
'          From Instrument: <30>
'                           <S1 High Byte><S1 Low Byte>
'                           <S2 High Byte><S2 Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  S1Data% and S2Data% are INTEGERs.
'
' S1Data% = (S1 High Byte) * 256 + (S1 Low Byte)
' S2Data% = (S2 High Byte) * 256 + (S2 Low Byte)

' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim Data%(3), I%
  On Error GoTo DKSlit240QErr
  Cmd% = 30
  ' Sending the Speed? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSlit240QResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSlit240QErr
    
  'Get returned query data
  For I% = 0 To 3
    If Timeout% > 0 Then
      ErrorStatus% = DKTimeout%(dkPort, Timeout%)
      If ErrorStatus% = 128 Then GoTo DKSlit240QResume
    End If
    Data(I%) = Asc(dkPort.Input)         'Read data.
  Next I%
  
  S1Data% = Data%(0) * 256 + Data%(1)
  S2Data% = Data%(2) * 256 + Data%(3)
  
  '  Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSlit240QResume:
  DKSlit240Q% = ErrorStatus%
  Exit Function

DKSlit240QErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume Next   'DKSlit240QResume
End Function


Function DKSlit242Q%(S1Data%, S2Data%, S3Data%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the DK240 monochromator for current entrance and exit slit width.
'
' Command: To Instrument:   <30>
'          From Instrument: <30>
'                           <S1 High Byte><S1 Low Byte>
'                           <S2 High Byte><S2 Low Byte>
'                           <S3 High Byte><S3 Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  S1Data%, S1Data% and S3Data% are INTEGERs.
'
' S1Data% = (S1 High Byte) * 256 + (S1 Low Byte)
' S2Data% = (S2 High Byte) * 256 + (S2 Low Byte)
' S2Data% = (S2 High Byte) * 256 + (S2 Low Byte)
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim Data%(5), I%
  On Error GoTo DKSlit242QErr
  Cmd% = 30
  ' Sending the Speed? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSlit242QResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSlit242QErr
      
  'Get returned query data
  For I% = 0 To 5
   'Checking for data bytes.
   If Timeout% > 0 Then     '~1d
     ErrorStatus% = DKTimeout%(dkPort, Timeout%)
     If ErrorStatus% = 128 Then GoTo DKSlit242QResume
   End If
   
   Data(I%) = Asc(dkPort.Input)         'Read data.
  Next I%
  
  S1Data% = Data%(0) * 256 + Data%(1)
  S2Data% = Data%(2) * 256 + Data%(3)
  S3Data% = Data%(4) * 256 + Data%(5)   ' ~1e_2
  
  '  Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSlit242QResume:
  DKSlit242Q% = ErrorStatus%
  Exit Function

DKSlit242QErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSlit242QResume

End Function
Function DKFilter%(Filter%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Sets the monochromator's filter wheel
'
' Command: To Instrument:   <15>
'          From Instrument: <15>
'          To Instrument:   <1 to 6>
'          From Instrument: <Status Byte><24>
'   Delay about 600 ms
'          To Instrument:   <24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort is a communication control.
' The passed parameters Filter% and Timeout% are both INTEGERs.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
'
  On Error GoTo DKFilterErr
  Cmd% = 15
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKFilterResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKFilterErr
  ' Send out 1-byte filter.
  dkPort.Output = Chr$(Filter%)
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)
  
  ErrorStatus% = DKTimeout%(dkPort, 1)
  dkPort.Output = Chr$(24)
  
  '24 back from instrument
  ErrorStatus% = DKTimeout%(dkPort, 1)
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte

DKFilterResume:
  DKFilter% = ErrorStatus%
  Exit Function

DKFilterErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKFilterResume

End Function
Function DKSpeed%(ScanSpeed%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Sets the monochromator's scan speed (for use with the SCAN command.)
'
' Command: To Instrument:   <13>
'          From Instrument: <13>
'          To Instrument:   <Speed High Byte><Speed Low Byte>
'          From Instrument: <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort is a communication control.
' The passed parameters ScanSpeed% and Timeout% are both INTEGERs.
'
' ScanSpeed% is always in Nanometers per minute.
'
' Valid values of ScanSpeed% depend on the ruling of the grating selected,
' per the following table:
'
'  Grating    Allowed Scan Speeds [Nanometers per minute]
'  [grv/mm]     Min.                    Max.
'  --------   ---------------------------------------------------
'   3600        1.......................199
'   2400        1.......................299
'   1800        1.......................399
'   1200        1.......................600
'    600        2, 4, 6,................1200
'    300        4, 8, 12,...............2400
'    150        8, 16, 24,..............4800
'     75        16, 32, 48,.............9600
'
'   Maximum scan speed = 600 * 1200 / Grmm, except grating grooves > 1200
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
'  Calculate the 2 byte speed specifier to send in the command
'
  On Error GoTo DKSpeedErr
  Cmd% = 13
  HighByte% = Int(ScanSpeed% / 256!)
  LowByte% = Int(ScanSpeed% - 256! * HighByte%)
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSpeedResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSpeedErr
  ' Send out 2-byte speed.
  dkPort.Output = Chr$(HighByte%) + Chr$(LowByte%)
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSpeedResume:
  DKSpeed% = ErrorStatus%
  Exit Function

DKSpeedErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSpeedResume

End Function


Function DKSpeedQ%(DataL&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the monochromator for current scan speed.
'
' Command: To Instrument:   <21>
'          From Instrument: <21>
'                           <Data High Byte><Data Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  DataL& is a LONG INTEGER.
'
' DataL& = (Data High Byte) * 256 + (Data Low Byte)
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim High&, Low&
  On Error GoTo DKSpeedQErr
  Cmd% = 21
  ' Sending the Speed? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKSpeedQResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKSpeedQErr
  
  'Get returned query data
  High& = Asc(dkPort.Input)         'Read the high byte.
  Low& = Asc(dkPort.Input)          'Read the low byte.
  
  DataL& = High& * 256 + Low&

  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKSpeedQResume:
  DKSpeedQ% = ErrorStatus%
  Exit Function

DKSpeedQErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKSpeedQResume

End Function



Function DKStep%(dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKTimeout%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' This function will return 128 (bit 7 sets 1) if during the time was set
' by Timeout% but no byte was received on the transmission line. Otherwise
' the return number is 0.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim Minutes%, DelayTime%
  If Timeout% > 0 Then
    If Timeout% > 3599 Then Timeout% = 3599
    Minutes% = Minute(Time$)
    DelayTime% = Second(Time$) + Timeout%     'Timeout% in seconds
    While (dkPort.InBufferCount = 0) And ((Minute(Time$) - Minutes%) * 60 + Second(Time$) < DelayTime%)
    Wend    'Wait until character present or waiting time is less than delay time
    If dkPort.InBufferCount = 0 Then
      'MsgBox "Errors in the serial commnuncation line", MB_ICONSTOP, "DK.BAS"
      DKTimeout% = 128
    Else
      DKTimeout% = 0
    End If
  End If
End Function

Function DKType%(TypeCode%, dkPort As Control, Timeout%)
  MsgBox "Will be modified for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKUnits%(Units%, dkPort As Control, Timeout%)
  MsgBox "Will be removed for DK-Series Demo ", MB_ICONEXCLAMATION, "DK.BAS"
End Function

Function DKWaveQ%(DataL&, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Queries the monochromator for current wavelength.
'
' Command: To Instrument:   <29>
'          From Instrument: <29>
'                           <Data High Byte><Data Middle Byte><Data Low Byte>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort as Control.  DataL& is a LONG INTEGER.
'
' DataL& = (Data High Byte)*65536 + (Data Middle Byte)*256 + (Data Low Byte)
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  Dim High&, Middle&, Low&
  On Error GoTo DKWaveQErr
  Cmd% = 29
  ' Sending the Wave? command.
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKWaveQResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKWaveQErr
  
  'Get returned query data
  High& = Asc(dkPort.Input)         'Read the high byte.
  Middle& = Asc(dkPort.Input)       'Read the middle byte.
  Low& = Asc(dkPort.Input)          'Read the low byte.
  
  DataL& = High& * 65536 + Middle& * 256 + Low&

  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKWaveQResume:
  DKWaveQ% = ErrorStatus%
  Exit Function

DKWaveQErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKWaveQResume

End Function



Function DKZero%(TurretByte%, dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Ajusts the monochromator zero offset factors so the current position
' is defined as the zero order transmission wavelength (ie: 0 nm).
'
'
' Command: To Instrument:   <52>
'          From Instrument: <52>
'                           <TurretByte%>
'          From Instrument: <Status Byte><24>
'
' The valid values for <TurretByte%> are 0, 1, 2. One is for turret 1, 2 for
' turret 2, and zero for both.
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKZeroErr
  Cmd% = 52
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKZeroResume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKZeroErr
  ' Send out TurretByte%
  dkPort.Output = Chr$(TurretByte%)
  'Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKZeroResume:
  DKZero% = ErrorStatus%
  Exit Function

DKZeroErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKZeroResume

End Function



'***********************************************************************************
'Begin ~1e   (see modification history)

Function DKStepDnM1%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <61>
'          From Instrument: <61>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 61
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err

  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKStepDnM1% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

Function DKStepUpM1%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <67>
'          From Instrument: <67>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 67
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err

  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKStepUpM1% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

Function DKStepDnM2%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <62>
'          From Instrument: <62>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 62
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err

  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKStepDnM2% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

Function DKStepUpM2%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <68>
'          From Instrument: <68>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 68
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err

  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKStepUpM2% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

Function DKStepM1OrM2%(dkPort As Control, Timeout%)
' To disable Timeout% (in seconds), set Timeout% to 0
' Timeout% will be set to 1hr if >1hr.
'
' Decrements the grating angle by 2.5E-3 deg/step (half-step mode) and 2.5E-4 def/step (ustep mode)
' in the counter-clockwise direction for M1 (Entrance side grating turret
' in a DK242, or the only turret in a DK240.)
'
' Command: To Instrument:   <60>
'          From Instrument: <60>
'                           <Status Byte><24>
'
' This function's return value is an INTEGER.  A value of zero at bit 7
' (the MSB) indicates success.
'
' The passed parameter dkPort is a commnunication control.
'
' dkPort is the communications control assigned to the monochromator's
' COM port by the DKInitComPort%() function.
'
  On Error GoTo DKDecM1Err
  Cmd% = 60
  dkPort.Output = Chr$(Cmd%)
  ' Checking for echoed byte.
  If Timeout% > 0 Then
    ErrorStatus% = DKTimeout%(dkPort, Timeout%)
    If ErrorStatus% = 128 Then GoTo DKDecM1Resume
  End If
  Echoed% = Asc(dkPort.Input)       'Read the echoed byte
  If Echoed% <> Cmd% Then GoTo DKDecM1Err
  ' Get Status and Cancel Bytes
  ErrorStatus% = DKGetStatusCancel%(dkPort, Timeout%)

DKDecM1Resume:
  DKStepM1OrM2% = ErrorStatus%
  Exit Function

DKDecM1Err:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  ErrorStatus% = 128      'Error; set bit 7 of return value
  Resume DKDecM1Resume

End Function

' end ~1e  (see modification history)
'*******************************************************************************
