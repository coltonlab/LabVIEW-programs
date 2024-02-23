VERSION 5.00
Begin VB.Form SetZeroX 
   Caption         =   "Zero Command (Indipendent)"
   ClientHeight    =   2475
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   4380
   LinkTopic       =   "Form2"
   ScaleHeight     =   2475
   ScaleWidth      =   4380
   StartUpPosition =   3  'Windows Default
   Begin VB.PictureBox pnlBkGnd 
      BackColor       =   &H00FFFF80&
      Height          =   975
      Index           =   0
      Left            =   120
      ScaleHeight     =   915
      ScaleWidth      =   4035
      TabIndex        =   10
      Top             =   120
      Width           =   4095
      Begin VB.PictureBox picStepM1 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H80000005&
         ForeColor       =   &H80000008&
         Height          =   510
         Index           =   1
         Left            =   3360
         Picture         =   "SETZEROX.frx":0000
         ScaleHeight     =   480
         ScaleWidth      =   480
         TabIndex        =   15
         Top             =   240
         Width           =   510
      End
      Begin VB.PictureBox picStep 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H00C0C0C0&
         ForeColor       =   &H80000008&
         Height          =   495
         Index           =   0
         Left            =   720
         ScaleHeight     =   465
         ScaleWidth      =   2625
         TabIndex        =   12
         Top             =   240
         Width           =   2655
         Begin VB.Label lblStepM1 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            Height          =   255
            Left            =   120
            TabIndex        =   14
            Top             =   120
            Width           =   975
         End
         Begin VB.Label lblOffsetM1 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            Height          =   255
            Left            =   1440
            TabIndex        =   13
            Top             =   120
            Width           =   975
         End
      End
      Begin VB.PictureBox picStepM1 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H80000005&
         ForeColor       =   &H80000008&
         Height          =   510
         Index           =   0
         Left            =   240
         Picture         =   "SETZEROX.frx":030A
         ScaleHeight     =   480
         ScaleWidth      =   480
         TabIndex        =   11
         Top             =   240
         Width           =   510
      End
      Begin VB.Label lblZeroM1 
         Alignment       =   2  'Center
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Step from 0"
         ForeColor       =   &H00FF0000&
         Height          =   255
         Index           =   0
         Left            =   840
         TabIndex        =   17
         Top             =   0
         Width           =   1005
      End
      Begin VB.Label lblZeroM1 
         Alignment       =   2  'Center
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Zero Offset"
         ForeColor       =   &H00FF0000&
         Height          =   255
         Index           =   1
         Left            =   2160
         TabIndex        =   16
         Top             =   0
         Width           =   1005
      End
   End
   Begin VB.PictureBox pnlBkGnd 
      BackColor       =   &H00FFFF80&
      Height          =   855
      Index           =   1
      Left            =   120
      ScaleHeight     =   795
      ScaleWidth      =   4035
      TabIndex        =   2
      Top             =   1080
      Width           =   4095
      Begin VB.PictureBox picStepM2 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H80000005&
         ForeColor       =   &H80000008&
         Height          =   510
         Index           =   0
         Left            =   240
         Picture         =   "SETZEROX.frx":0614
         ScaleHeight     =   480
         ScaleWidth      =   480
         TabIndex        =   7
         Top             =   240
         Width           =   510
      End
      Begin VB.PictureBox picStep 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H00C0C0C0&
         ForeColor       =   &H80000008&
         Height          =   495
         Index           =   1
         Left            =   720
         ScaleHeight     =   465
         ScaleWidth      =   2625
         TabIndex        =   4
         Top             =   240
         Width           =   2655
         Begin VB.Label lblStepM2 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            Height          =   255
            Left            =   120
            TabIndex        =   6
            Top             =   120
            Width           =   975
         End
         Begin VB.Label lblOffsetM2 
            Alignment       =   2  'Center
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            Height          =   255
            Left            =   1440
            TabIndex        =   5
            Top             =   120
            Width           =   975
         End
      End
      Begin VB.PictureBox picStepM2 
         Appearance      =   0  'Flat
         AutoSize        =   -1  'True
         BackColor       =   &H80000005&
         ForeColor       =   &H80000008&
         Height          =   510
         Index           =   1
         Left            =   3360
         Picture         =   "SETZEROX.frx":091E
         ScaleHeight     =   480
         ScaleWidth      =   480
         TabIndex        =   3
         Top             =   240
         Width           =   510
      End
      Begin VB.Label lblZeroM2 
         Alignment       =   2  'Center
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Step M2 from 0"
         ForeColor       =   &H00FF0000&
         Height          =   255
         Index           =   0
         Left            =   720
         TabIndex        =   9
         Top             =   0
         Width           =   1215
      End
      Begin VB.Label lblZeroM2 
         Alignment       =   2  'Center
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Zero Offset M2"
         ForeColor       =   &H00FF0000&
         Height          =   255
         Index           =   1
         Left            =   2160
         TabIndex        =   8
         Top             =   0
         Width           =   1215
      End
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "ZERO"
      Height          =   315
      Index           =   1
      Left            =   3240
      MaskColor       =   &H00FF0000&
      TabIndex        =   1
      Top             =   2040
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   2040
      MaskColor       =   &H000000FF&
      TabIndex        =   0
      Top             =   2040
      UseMaskColor    =   -1  'True
      Width           =   975
   End
End
Attribute VB_Name = "SetZeroX"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim modStepFrom0M1%, modStepFrom0M2%
Dim modOffsetM1&, modOffsetM2&

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, TurretByte%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Exit (Cancel) button.
      If modStepFrom0M1% Or modStepFrom0M2% Then
        Status% = DKGoto%(0, frmDK.comComm1, 5) '5: 5s Timeout%
      End If
      gblOkCancel% = IDCANCEL
      Unload SetZeroX
    Case 1          ' 1 is Zero (OK) button.
      warnMessg.Show MODAL
      If gblContinueCancel% = IDCONTINUE Then
        If (gblNovAdd29& And &H2) Then
          TurretByte% = 1     ' For turret 1.
          If lblStepM2.Caption <> 0 Then TurretByte% = 0    ' For both turrets
        Else
          TurretByte% = 1     ' For turret 1.
        End If
        Status% = DKZero%(TurretByte%, frmDK.comComm1, 5) '5: 5s Timeout%
        gblOkCancel% = IDOK
        RefreshIndicators
      Else
        'Do nothing
      End If
  End Select
    
cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Dim Status%
  Centerform Me
  '0: single, 1: Additive dispersion, 254: Subtractive dps.
  If (gblNovAdd29& And &H2) Then
    pnlBkGnd(1).Visible = True
  Else
    pnlBkGnd(1).Visible = False
  End If
  ' Check to see if gblCurWL& <> 0
  If gblCurWL& Then
    Status% = DKGoto%(0, frmDK.comComm1, 25) '25s Timeout%
    If Status% < 128 Then
      gblCurWL& = 0
      frmDK.lblWLength = gblCurWL&
    End If
  End If
  
  RefreshIndicators
  
 'go into independent drive for M1 or M2  ~NCT
  Status% = DKStepM1OrM2(frmDK.comComm1, 2) '2 second timeout

End Sub

Private Sub picStep_Click(Index As Integer)
  Dim Status%
  Status% = DKIncM1%(frmDK.comComm1, 2) '2: 2s Timeout%

End Sub

Private Sub picStepM1_Click(Index As Integer)
  Dim Status%
  Select Case Index
    Case 0  'Left arrow
      Status% = DKStepDnM1%(frmDK.comComm1, 2) '2: 2s Timeout%
      If Status% < 128 Then
        modStepFrom0M1% = modStepFrom0M1% - 1
      End If
    Case 1  'Right arrow
      Status% = DKStepUpM1%(frmDK.comComm1, 2) '2: 2s Timeout%
      If Status% < 128 Then
        modStepFrom0M1% = modStepFrom0M1% + 1
      End If
  End Select
  lblStepM1.Caption = modStepFrom0M1%

End Sub

Private Sub picStepM2_Click(Index As Integer)
  Dim Status%
  Select Case Index
    Case 0  'Left arrow
      Status% = DKStepDnM2%(frmDK.comComm1, 2) '2: 2s Timeout%
      If Status% < 128 Then
        modStepFrom0M2% = modStepFrom0M2% - 1
      End If
    Case 1  'Right arrow
      Status% = DKStepUpM2%(frmDK.comComm1, 2) '2: 2s Timeout%
      If Status% < 128 Then
        modStepFrom0M2% = modStepFrom0M2% + 1
      End If
  End Select
  lblStepM2.Caption = modStepFrom0M2%
 
End Sub

Private Sub RefreshIndicators()
  Dim MIndex%, DataL&, Status%
  'The index of current grating select.
  MIndex% = gblNGrtSelted& - 1
  ' Query the current zero offset of machine 1.
  Status% = DKNovramRead%(14 + MIndex%, DataL&, frmDK.comComm1, 5) '5: 5s Timeout%
  modOffsetM1& = DataL&
  ' Query the current zero offset of machine 2.
  Status% = DKNovramRead%(17 + MIndex%, DataL&, frmDK.comComm1, 5) '5: 5s Timeout%
  modOffsetM2& = DataL&
  lblOffsetM1.Caption = modOffsetM1&
  lblOffsetM2.Caption = modOffsetM2&
  'Zero out the steps from zero.
  modStepFrom0M1% = 0
  modStepFrom0M2% = 0

  lblStepM1.Caption = modStepFrom0M1%
  lblStepM2.Caption = modStepFrom0M2%

End Sub



