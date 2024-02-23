VERSION 5.00
Begin VB.Form ctrStep 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Step Command"
   ClientHeight    =   1935
   ClientLeft      =   660
   ClientTop       =   4425
   ClientWidth     =   6015
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
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   1935
   ScaleWidth      =   6015
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "STEP"
      Height          =   315
      Index           =   1
      Left            =   4080
      MaskColor       =   &H00FF0000&
      TabIndex        =   1
      Top             =   1440
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   2880
      MaskColor       =   &H000000FF&
      TabIndex        =   0
      Top             =   1440
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlCtrStep 
      Height          =   1935
      Left            =   0
      ScaleHeight     =   1875
      ScaleWidth      =   5955
      TabIndex        =   4
      Top             =   0
      Width           =   6015
      Begin VB.PictureBox Panel3D1 
         Height          =   375
         Left            =   360
         ScaleHeight     =   315
         ScaleWidth      =   5235
         TabIndex        =   8
         Top             =   240
         Width           =   5295
         Begin VB.Label lblSize 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            Caption         =   "1"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   12
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00FF0000&
            Height          =   285
            Left            =   2160
            TabIndex        =   2
            Top             =   25
            Width           =   1335
         End
         Begin VB.Label Label2 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Current Size (+/-) :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   10
            Top             =   75
            Width           =   1995
         End
         Begin VB.Label lblUnitWL 
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
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   1
            Left            =   3600
            TabIndex        =   9
            Top             =   45
            Width           =   1605
         End
      End
      Begin VB.PictureBox pnlCurWave 
         Height          =   375
         Left            =   360
         ScaleHeight     =   315
         ScaleWidth      =   5235
         TabIndex        =   5
         Top             =   840
         Width           =   5295
         Begin VB.Label lblWave 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            Caption         =   "0"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   12
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H80000008&
            Height          =   285
            Left            =   2160
            TabIndex        =   3
            Top             =   25
            Width           =   1335
         End
         Begin VB.Label lblUnitWL 
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
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   0
            Left            =   3600
            TabIndex        =   7
            Top             =   45
            Width           =   1605
         End
         Begin VB.Label lblCurWave 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Current Wavelength :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   6
            Top             =   75
            Width           =   1995
         End
      End
   End
End
Attribute VB_Name = "ctrStep"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, WLength&, DataL&
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Exit (Cancel) button.
      gblOkCancel% = IDCANCEL
      Unload ctrStep
    Case 1          ' 1 is STEP (OK) button.
      Status% = DKStep%(frmDK.comComm1, 5) '5: 5s Timeout%
      If Status% < 128 Then
        ' Query current wavelength.
        Status% = DKQuery%(0, DataL&, frmDK.comComm1, 5) '5: 5s Timeout%
        gblCurWL& = DataL&
        lblWave.Caption = gblCurWL&
      Else
        MsgBox "An error has occurred !", MB_ICONSTOP
      End If
      gblOkCancel% = IDOK
  End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Dim Size%
  Centerform ctrStep
  If gblCurSize% >= 128 Then
    Size% = 128 - gblCurSize%
  Else
    Size% = gblCurSize%
  End If
  lblSize.Caption = Size%
  lblWave.Caption = gblCurWL&
 
End Sub

Private Sub lblSize_Click()
  Dim Size%
  ctrSize.Show MODAL
  If gblCurSize% >= 128 Then
    Size% = 128 - gblCurSize%
  Else
    Size% = gblCurSize%
  End If
  lblSize.Caption = Size%

End Sub

Private Sub txtWL_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13     ' 13 if ascii of CR
      cmdCanOK_Click (1)      ' 1: is OK button
    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select

End Sub

