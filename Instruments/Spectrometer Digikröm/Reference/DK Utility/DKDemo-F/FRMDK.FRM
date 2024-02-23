VERSION 5.00
Object = "{648A5603-2C6E-101B-82B6-000000000014}#1.1#0"; "mscomm32.ocx"
Begin VB.Form frmDK 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "DK-SERIES Demo"
   ClientHeight    =   3060
   ClientLeft      =   2670
   ClientTop       =   4080
   ClientWidth     =   8700
   BeginProperty Font 
      Name            =   "MS Sans Serif"
      Size            =   8.25
      Charset         =   0
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   ForeColor       =   &H80000008&
   Icon            =   "FRMDK.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   3060
   ScaleWidth      =   8700
   Begin VB.PictureBox pnlMainBG 
      Height          =   3015
      Left            =   5
      ScaleHeight     =   2955
      ScaleWidth      =   8595
      TabIndex        =   0
      Top             =   5
      Width           =   8655
      Begin VB.PictureBox Picture1 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H80000005&
         ForeColor       =   &H80000008&
         Height          =   840
         Left            =   720
         Picture         =   "FRMDK.frx":030A
         ScaleHeight     =   810
         ScaleWidth      =   1080
         TabIndex        =   3
         Top             =   1560
         Width           =   1110
      End
      Begin VB.PictureBox pnlBkGnd 
         BackColor       =   &H00C00000&
         Height          =   375
         Index           =   2
         Left            =   240
         ScaleHeight     =   315
         ScaleWidth      =   1515
         TabIndex        =   1
         Top             =   3480
         Width           =   1575
      End
      Begin VB.PictureBox pnlBkGnd 
         BackColor       =   &H00FFFF80&
         Height          =   2175
         Index           =   1
         Left            =   3000
         ScaleHeight     =   2115
         ScaleWidth      =   5355
         TabIndex        =   2
         Top             =   360
         Width           =   5415
         Begin VB.PictureBox picStep 
            Appearance      =   0  'Flat
            AutoSize        =   -1  'True
            BackColor       =   &H80000005&
            ForeColor       =   &H80000008&
            Height          =   510
            Index           =   4
            Left            =   4680
            Picture         =   "FRMDK.frx":167E
            ScaleHeight     =   480
            ScaleWidth      =   480
            TabIndex        =   4
            Top             =   1320
            Width           =   510
         End
         Begin VB.PictureBox picStep 
            Appearance      =   0  'Flat
            AutoSize        =   -1  'True
            BackColor       =   &H80000005&
            ForeColor       =   &H80000008&
            Height          =   510
            Index           =   3
            Left            =   4200
            Picture         =   "FRMDK.frx":1988
            ScaleHeight     =   480
            ScaleWidth      =   480
            TabIndex        =   9
            Top             =   1320
            Width           =   510
         End
         Begin VB.PictureBox picStep 
            Appearance      =   0  'Flat
            AutoSize        =   -1  'True
            BackColor       =   &H80000005&
            ForeColor       =   &H80000008&
            Height          =   510
            Index           =   0
            Left            =   360
            Picture         =   "FRMDK.frx":1C92
            ScaleHeight     =   480
            ScaleWidth      =   480
            TabIndex        =   8
            Top             =   1320
            Width           =   510
         End
         Begin VB.PictureBox picStep 
            Appearance      =   0  'Flat
            AutoSize        =   -1  'True
            BackColor       =   &H80000005&
            ForeColor       =   &H80000008&
            Height          =   510
            Index           =   1
            Left            =   840
            Picture         =   "FRMDK.frx":1F9C
            ScaleHeight     =   480
            ScaleWidth      =   480
            TabIndex        =   7
            Top             =   1320
            Width           =   510
         End
         Begin VB.PictureBox picStep 
            Appearance      =   0  'Flat
            AutoSize        =   -1  'True
            BackColor       =   &H00C0C0C0&
            ForeColor       =   &H80000008&
            Height          =   495
            Index           =   2
            Left            =   1320
            ScaleHeight     =   465
            ScaleWidth      =   2865
            TabIndex        =   5
            Top             =   1320
            Width           =   2895
            Begin VB.Label lblWLength 
               Alignment       =   2  'Center
               BorderStyle     =   1  'Fixed Single
               Caption         =   "0"
               BeginProperty Font 
                  Name            =   "MS Sans Serif"
                  Size            =   8.25
                  Charset         =   0
                  Weight          =   400
                  Underline       =   0   'False
                  Italic          =   0   'False
                  Strikethrough   =   0   'False
               EndProperty
               Height          =   255
               Left            =   120
               TabIndex        =   15
               Top             =   120
               Width           =   1095
            End
            Begin VB.Label lblUnits 
               Alignment       =   2  'Center
               Appearance      =   0  'Flat
               BackColor       =   &H80000005&
               BackStyle       =   0  'Transparent
               Caption         =   "tenths of Angstroms"
               BeginProperty Font 
                  Name            =   "MS Sans Serif"
                  Size            =   8.25
                  Charset         =   0
                  Weight          =   400
                  Underline       =   0   'False
                  Italic          =   0   'False
                  Strikethrough   =   0   'False
               EndProperty
               ForeColor       =   &H00FF0000&
               Height          =   255
               Left            =   1320
               TabIndex        =   6
               Top             =   120
               Width           =   1485
            End
         End
         Begin VB.Label lblGrtN 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "1"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   8.25
               Charset         =   0
               Weight          =   400
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00000000&
            Height          =   255
            Left            =   5040
            TabIndex        =   14
            Top             =   45
            Width           =   255
         End
         Begin VB.Label lblSerial 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "Serial : xxxxx"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   8.25
               Charset         =   0
               Weight          =   400
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00000000&
            Height          =   255
            Left            =   3720
            TabIndex        =   13
            Top             =   360
            Width           =   1575
         End
         Begin VB.Label lblBlaze 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "Blaze : xxxxx nm"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   8.25
               Charset         =   0
               Weight          =   400
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00FF0000&
            Height          =   255
            Left            =   240
            TabIndex        =   12
            Top             =   600
            Width           =   1815
         End
         Begin VB.Label lblGroove 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "Groove : xxxxx g/mm"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   8.25
               Charset         =   0
               Weight          =   400
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00FF0000&
            Height          =   255
            Left            =   240
            TabIndex        =   11
            Top             =   240
            Width           =   1815
         End
      End
      Begin VB.Label lblDKlabel 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "DK-Series Demo Software"
         BeginProperty Font 
            Name            =   "Roman"
            Size            =   18
            Charset         =   255
            Weight          =   700
            Underline       =   0   'False
            Italic          =   -1  'True
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FF0000&
         Height          =   975
         Left            =   240
         TabIndex        =   10
         Top             =   360
         Width           =   2535
      End
   End
   Begin MSCommLib.MSComm comComm1 
      Left            =   0
      Top             =   3960
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
      DTREnable       =   -1  'True
   End
   Begin VB.Menu topCommands 
      Caption         =   "&Commands"
      Begin VB.Menu topControl 
         Caption         =   "&Control"
         Begin VB.Menu mnuGoto 
            Caption         =   "&Goto"
         End
         Begin VB.Menu mnuScan 
            Caption         =   "&Scan"
         End
         Begin VB.Menu mnuSpeed 
            Caption         =   "S&peed"
         End
         Begin VB.Menu mnuSlits 
            Caption         =   "S&lits"
         End
         Begin VB.Menu mnuSlot 
            Caption         =   "Slot Wi&dth"
         End
         Begin VB.Menu mnuSize 
            Caption         =   "S&ize"
            Enabled         =   0   'False
            Visible         =   0   'False
         End
         Begin VB.Menu mnuSelect 
            Caption         =   "S&elect"
         End
         Begin VB.Menu mnuIncDec 
            Caption         =   "I&nc and Dec"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuIncDec2 
            Caption         =   "In&c and Dec M2"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuQuery 
            Caption         =   "&Query"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuEcho 
            Caption         =   "&Echo"
         End
         Begin VB.Menu mnuReset 
            Caption         =   "&Reset"
         End
         Begin VB.Menu mnuDivider3 
            Caption         =   "-"
         End
         Begin VB.Menu mnuFilter 
            Caption         =   "&Filter"
         End
      End
      Begin VB.Menu topSetup 
         Caption         =   "&Setup"
         Begin VB.Menu mnuCalibrate 
            Caption         =   "&Calibrate"
         End
         Begin VB.Menu mnuSlitCal 
            Caption         =   "&Slit Cal."
         End
         Begin VB.Menu mnuZero 
            Caption         =   "&Zero"
         End
         Begin VB.Menu mnuBaud 
            Caption         =   "&Baud"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuOrder 
            Caption         =   "&Order"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuUnits 
            Caption         =   "&Units"
            Visible         =   0   'False
         End
         Begin VB.Menu mnuType 
            Caption         =   "&Type"
            Visible         =   0   'False
         End
      End
      Begin VB.Menu topExit 
         Caption         =   "&Exit"
      End
   End
   Begin VB.Menu topNovram 
      Caption         =   "&Novram"
      Begin VB.Menu mnuRead 
         Caption         =   "Novram &Read"
      End
      Begin VB.Menu mnuWrite 
         Caption         =   "Novram &Write"
      End
      Begin VB.Menu mnuUtility 
         Caption         =   "Novram &Utility"
      End
   End
   Begin VB.Menu topCOM 
      Caption         =   "&COM Port"
      Begin VB.Menu mnuBaudFinding 
         Caption         =   "&Baud Finding"
      End
      Begin VB.Menu mnuLoopback 
         Caption         =   "&Loopback COM Test"
      End
      Begin VB.Menu mnuDivider1 
         Caption         =   "-"
      End
      Begin VB.Menu mnuRtsCtsStatus 
         Caption         =   "RTS, CTS &Status"
      End
      Begin VB.Menu mnuDivider2 
         Caption         =   "-"
      End
      Begin VB.Menu mnuInitCOM 
         Caption         =   "&Initialize COM Port"
      End
   End
   Begin VB.Menu topOption 
      Caption         =   "&Option"
      Begin VB.Menu mnuOption 
         Caption         =   "DOS &Baud Finding"
         Index           =   0
         Visible         =   0   'False
      End
      Begin VB.Menu mnuOption 
         Caption         =   "&Save Configuration"
         Index           =   1
      End
   End
   Begin VB.Menu topHelp 
      Caption         =   "&Help"
      Begin VB.Menu mnuHelp 
         Caption         =   "&Contents"
         Enabled         =   0   'False
         Index           =   0
      End
      Begin VB.Menu mnuHelp 
         Caption         =   "&Using Help"
         Index           =   1
      End
      Begin VB.Menu mnuHelp 
         Caption         =   "-"
         Index           =   2
      End
      Begin VB.Menu mnuHelp 
         Caption         =   "&About DK-Series"
         Index           =   3
      End
   End
End
Attribute VB_Name = "frmDK"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub AlignGotoBar()
  Dim LeftVar!, TopVar!, HeightVar!, WidthVar!
  Dim I%
  
  HeightVar! = picStep(0).Height
  TopVar! = picStep(0).Top
  
  For I% = 1 To 4
    WidthVar! = picStep(I%).Width
    LeftVar! = picStep(I% - 1).Left + picStep(I% - 1).Width
    picStep(I%).Move LeftVar!, TopVar!, WidthVar!, HeightVar!
  Next I%
  
End Sub

'
Private Sub Form_Load()
  Dim I%, Baud$
  On Error GoTo FormErr
  TopLeftform frmDK
  gblIniExist% = GetDkInit%()
  If gblIniExist% Then
    If COMInit%(gblPortNo%, gblBaud%) Then
      'Initializing dk successfully. Do nothing.
    Else
      SetCOM.Show MODAL
    End If
  Else
    SetCOM.Show MODAL
  End If
  If gblInitCom% Then
    'If CM110, gblType% = 0; if CM112, gblType%=1 or 254
    If gblType% = 0 Then    'if CM110
      mnuType.Enabled = False
      mnuIncDec2.Enabled = False
    Else
      mnuType.Enabled = True
      mnuIncDec2.Enabled = True
    End If
    gblFilter% = 1
    InitQueries
    UpdateScreen
  End If
  AlignGotoBar

FormResume:
  Exit Sub

FormErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume FormResume

End Sub

Private Sub Form_Unload(Cancel As Integer)
  End
End Sub

Private Sub mnuBaud_Click()
  ' Take out for DK-Series Demo
End Sub

Private Sub mnuBaudFinding_Click()
  baudSearching.Show MODAL
  If gblInitCom% Then
    InitQueries
    UpdateScreen
  End If

End Sub

Private Sub mnuCalibrate_Click()
  setCal.Show MODAL
  lblWLength.Caption = gblCurWL&
End Sub

Private Sub mnuEcho_Click()
  ctrEcho.Show MODELESS
End Sub

Private Sub mnuFilter_Click()
  If gblInitCom% Then
    ctrFilter.Show MODELESS
  Else
    MsgBox "Did you initialize a serial port ? "
  End If
End Sub

Private Sub mnuGoto_Click()
  ctrGoto.Show MODAL
  lblWLength.Caption = gblCurWL&

End Sub

Private Sub mnuHelp_Click(Index As Integer)
  Dim R&
  Dim Helptopic&
  Select Case Index
    Case 0  'Contents
      Helptopic& = 1
      R& = WinHelp(frmDK.hwnd, HelpFile, HELP_CONTENTS, Helptopic&)  'HELP_CONTENTS  HELP_CONTEXT
    Case 1  'Seach
      Helptopic& = 0
      R& = WinHelp(frmDK.hwnd, HelpFile, HELP_HELPONHELP, Helptopic&)
    Case 3  'About CM110/112
      About.Show MODAL
    Case Else
      MsgBox "An error has occurred !"
  End Select
End Sub

Private Sub mnuIncDec_Click()
  ctrIncDec.Show MODAL
End Sub

Private Sub mnuIncDec2_Click()
  ctrIncDecM2.Show MODAL
End Sub

Private Sub mnuInitCOM_Click()
  SetCOM.Show MODAL
  If gblOkCancel% = IDOK Then
    InitQueries
    UpdateScreen
  End If
  
End Sub

Private Sub mnuLoopback_Click()
  Loopback.Show MODAL
End Sub

Private Sub mnuOption_Click(Index As Integer)
  Dim Ret
  On Error GoTo mnuOptionErr
  Select Case Index
    Case 0  'DOS Baud Finding
      ' Take it out for DK-Series demo
    Case 1  'Save Configuration
      SaveConfig
  End Select

mnuOptionResume:
  Exit Sub

mnuOptionErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume mnuOptionResume

End Sub

Private Sub mnuOrder_Click()
  ' Take out for DK-Series Demo
End Sub

Private Sub mnuQuery_Click()
  ctrQuery.Show MODELESS
End Sub

Private Sub mnuRead_Click()
  URdFrNov.Show MODELESS
End Sub

Private Sub mnuReset_Click()
  If gblInitCom% Then
    ctrReset.Show MODELESS
  Else
    MsgBox "Did you initialize a serial port ? "
  End If

End Sub

Private Sub mnuRtsCtsStatus_Click()
  CtsRts.Show MODELESS
End Sub

Private Sub mnuScan_Click()
  ctrScan.Show MODAL
  lblWLength.Caption = gblCurWL&
End Sub

Private Sub mnuSelect_Click()
  ctrGrtsel.Show MODAL
  InitQueries
  UpdateScreen
End Sub

Private Sub mnuSize_Click()
  ctrSize.Show MODELESS
End Sub

Private Sub mnuSlitCal_Click()
  setSlits.Show MODAL
End Sub

Private Sub mnuSlits_Click()
  ctrSlits.Show MODAL
End Sub

Private Sub mnuSlot_Click()
    ctrSlotW.Show MODAL
End Sub

Private Sub mnuSpeed_Click()
  If gblInitCom% Then
    ctrSpeed.Show MODELESS
  Else
    MsgBox "Did you initialize a serial port ? "
  End If

End Sub

Private Sub mnuStep_Click()
  ctrStep.Show MODAL
  lblWLength.Caption = gblCurWL&
End Sub

Private Sub mnuType_Click()
  setType.Show MODAL
  lblWLength.Caption = gblCurWL&

End Sub

Private Sub mnuUtility_Click()
  NovramU.Show MODAL
End Sub

Private Sub mnuWrite_Click()
  UWrToNov.Show MODELESS
End Sub

Private Sub mnuZero_Click()
  If gblInitCom% Then
    SetZero.Show MODAL
    lblWLength.Caption = gblCurWL&
  Else
    MsgBox "Did you initialize a serial port ? "
  End If

End Sub


Private Sub picStep_Click(Index As Integer)
  Dim Status%, StpSize%, DataL&
  On Error GoTo picStepErr
  Select Case Index
    Case 2  'lblWLength box
    
    Case 0, 1, 3, 4
      Select Case Index
        Case 0  'Double arror left
          'StpSize% = -20
          Status% = DKScanDn%(frmDK.comComm1, 1, 5)  '5: 5s Timeout%
        Case 1  'Single arrow left
          'StpSize% = -1
          Status% = DKStepDn%(frmDK.comComm1, 5)  '5: 5s Timeout%
        Case 3  'Single arrow right
          'StpSize% = 1
          Status% = DKStepUp%(frmDK.comComm1, 5)  '5: 5s Timeout%
        Case 4  'Double arrow right
          'StpSize% = 20
          Status% = DKScanUp%(frmDK.comComm1, 1, 5)  '5: 5s Timeout%
      End Select
        'Set step size
        'Status% = DKSize%(StpSize%, frmDK.comComm1, 5)  '5: 5s Timeout%
        'Status% = DKStep%(frmDK.comComm1, 5)  '5: 5s Timeout%
       
        
        'Query current wavelength
        'Status% = DKQuery%(0, DataL&, frmDK.comComm1, 5) '5: 5s Timeout%
        Status% = DKWaveQ%(DataL&, frmDK.comComm1, 5)
        gblCurWL& = DataL&
        frmDK.lblWLength.Caption = gblCurWL&
    
    Case Else
  
  End Select

picStepResume:
  Exit Sub

picStepErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  Resume picStepResume

End Sub

Private Sub lblWLength_Click()
  ctrGoto.Show MODAL
  lblWLength.Caption = gblCurWL&
End Sub

Private Sub topExit_Click()
  End
End Sub

Private Sub UpdateScreen()
  lblWLength.Caption = gblCurWL&
  lblSerial.Caption = "Serial : " & gblSerial$
  lblGroove.Caption = "Groove : " & gblCurGr& & " g/mm"
  lblBlaze.Caption = "Blaze : " & gblCurBl& & " nm"
  lblGrtN.Caption = gblNGrtSelted&
End Sub

