VERSION 5.00
Begin VB.Form setCal 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Calibrate Command"
   ClientHeight    =   1920
   ClientLeft      =   2835
   ClientTop       =   5175
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
   ScaleHeight     =   1920
   ScaleWidth      =   6015
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   4440
      MaskColor       =   &H00FF0000&
      TabIndex        =   10
      Top             =   1320
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   3240
      MaskColor       =   &H000000FF&
      TabIndex        =   9
      Top             =   1320
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlCmCal 
      Height          =   1935
      Left            =   0
      ScaleHeight     =   1875
      ScaleWidth      =   5955
      TabIndex        =   2
      Top             =   0
      Width           =   6015
      Begin VB.PictureBox pnlDesiredWave 
         Height          =   375
         Left            =   480
         ScaleHeight     =   315
         ScaleWidth      =   4875
         TabIndex        =   5
         Top             =   720
         Width           =   4935
         Begin VB.TextBox txtDesiredWave 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Left            =   1920
            MaxLength       =   8
            TabIndex        =   1
            Top             =   35
            Width           =   1335
         End
         Begin VB.Label lblUnitDesW 
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
            Left            =   3270
            TabIndex        =   8
            Top             =   45
            Width           =   1665
         End
         Begin VB.Label lblDesiredWave 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Desired Wavelength :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   6
            Top             =   75
            Width           =   1875
         End
      End
      Begin VB.PictureBox pnlOldWave 
         Height          =   375
         Left            =   480
         ScaleHeight     =   315
         ScaleWidth      =   4875
         TabIndex        =   3
         Top             =   240
         Width           =   4935
         Begin VB.TextBox txtOldWave 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Left            =   1920
            MaxLength       =   8
            TabIndex        =   0
            Top             =   35
            Width           =   1335
         End
         Begin VB.Label lblUnitOldW 
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
            Left            =   3270
            TabIndex        =   7
            Top             =   45
            Width           =   1665
         End
         Begin VB.Label lblOldWave 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Goto Wavelength :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   4
            Top             =   75
            Width           =   1875
         End
      End
   End
End
Attribute VB_Name = "setCal"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, GotoW&, DesiredW&
  On Error GoTo cmdCanOKErr
  GotoW& = txtOldWave.Text
  DesiredW& = txtDesiredWave.Text
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload setCal
    Case 1          ' 1 is OK button.
      warnMessg.Show MODAL
      If gblContinueCancel% = IDCONTINUE Then
        If GotoW& <> gblCurWL& Then
          Status% = DKGoto%(GotoW&, frmDK.comComm1, 300) '5: 5s Timeout%
        End If
        If Status% < 128 Then
          gblCurWL& = GotoW&
          frmDK.lblWLength.Caption = gblCurWL&
          Status% = DKCalibrate%(DesiredW&, frmDK.comComm1, 5) '5: 5s Timeout%
          If Status% < 128 Then
            gblOkCancel% = IDOK
            gblCurWL& = 10000
            frmDK.lblWLength.Caption = gblCurWL&
          Else
            MsgBox "An error has occurred !"
            gblOkCancel% = IDCANCEL
          End If
        End If
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
  Centerform setCal
  txtOldWave.Text = gblCurWL&
  txtDesiredWave.Text = gblCurWL&
  
End Sub

Private Sub txtDesiredWave_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13     ' 13 if ascii of CR

    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select

End Sub

Private Sub txtOldWave_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13     ' 13 if ascii of CR
      
    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select

End Sub

