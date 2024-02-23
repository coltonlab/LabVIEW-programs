VERSION 5.00
Begin VB.Form setSlits 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Slit Calibration Commands"
   ClientHeight    =   2295
   ClientLeft      =   1260
   ClientTop       =   5250
   ClientWidth     =   5895
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
   ScaleHeight     =   2295
   ScaleWidth      =   5895
   Begin VB.Frame fraSlits 
      Caption         =   "SLITS CAL"
      Height          =   1215
      Left            =   240
      TabIndex        =   15
      Top             =   340
      Width           =   1215
      Begin VB.OptionButton optSltAdj 
         Caption         =   "S1"
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
         Index           =   0
         Left            =   120
         TabIndex        =   18
         Top             =   360
         Width           =   855
      End
      Begin VB.OptionButton optSltAdj 
         Caption         =   "S2"
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
         Index           =   1
         Left            =   120
         TabIndex        =   17
         Top             =   600
         Width           =   855
      End
      Begin VB.OptionButton optSltAdj 
         Caption         =   "S3"
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
         Index           =   2
         Left            =   120
         TabIndex        =   16
         Top             =   840
         Width           =   855
      End
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   3240
      MaskColor       =   &H000000FF&
      TabIndex        =   14
      Top             =   1680
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   4440
      MaskColor       =   &H00FF0000&
      TabIndex        =   13
      Top             =   1680
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlSetSlits 
      Height          =   2295
      Left            =   0
      ScaleHeight     =   2235
      ScaleWidth      =   5835
      TabIndex        =   0
      Top             =   0
      Width           =   5895
      Begin VB.PictureBox pnlSW 
         Height          =   375
         Index           =   0
         Left            =   1800
         ScaleHeight     =   315
         ScaleWidth      =   3555
         TabIndex        =   1
         Top             =   360
         Width           =   3615
         Begin VB.TextBox txtSW 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Index           =   0
            Left            =   2280
            MaxLength       =   4
            TabIndex        =   2
            Text            =   "0"
            Top             =   45
            Width           =   855
         End
         Begin VB.Label lblUnitSW 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "um"
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
            Left            =   3120
            TabIndex        =   4
            Top             =   45
            Width           =   375
         End
         Begin VB.Label lblSW 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter Desired S1 Width:"
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   0
            Left            =   105
            TabIndex        =   3
            Top             =   75
            Width           =   2070
         End
      End
      Begin VB.PictureBox pnlSW 
         Height          =   375
         Index           =   1
         Left            =   1800
         ScaleHeight     =   315
         ScaleWidth      =   3555
         TabIndex        =   5
         Top             =   720
         Width           =   3615
         Begin VB.TextBox txtSW 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Index           =   1
            Left            =   2280
            MaxLength       =   4
            TabIndex        =   6
            Text            =   "0"
            Top             =   45
            Width           =   855
         End
         Begin VB.Label lblSW 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter Desired S2 Width:"
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   1
            Left            =   120
            TabIndex        =   8
            Top             =   75
            Width           =   2175
         End
         Begin VB.Label lblUnitSW 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "um"
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
            Left            =   3120
            TabIndex        =   7
            Top             =   45
            Width           =   375
         End
      End
      Begin VB.PictureBox pnlSW 
         Height          =   375
         Index           =   2
         Left            =   1800
         ScaleHeight     =   315
         ScaleWidth      =   3555
         TabIndex        =   9
         Top             =   1080
         Width           =   3615
         Begin VB.TextBox txtSW 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Index           =   2
            Left            =   2280
            MaxLength       =   4
            TabIndex        =   10
            Text            =   "0"
            Top             =   45
            Width           =   855
         End
         Begin VB.Label lblSW 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter Desired S3 Width:"
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   2
            Left            =   120
            TabIndex        =   12
            Top             =   75
            Width           =   2175
         End
         Begin VB.Label lblUnitSW 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "um"
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
            Index           =   2
            Left            =   3120
            TabIndex        =   11
            Top             =   45
            Width           =   375
         End
      End
   End
End
Attribute VB_Name = "setSlits"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim modSlitsN%

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, SlitByte%, SlitWidth%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload setSlits
    Case 1          ' 1 is OK button.
      Select Case modSlitsN%
        Case 0
          SlitByte% = 22  ' S1 adjustment.
        Case 1
          SlitByte% = 23  ' S2 adjustment.
        Case 2
          SlitByte% = 35  ' S3 adjustment.
      End Select
      SlitWidth% = txtSW(modSlitsN%).Text
      Status% = DKSltAdjCal%(SlitByte%, SlitWidth%, frmDK.comComm1, 5)
      If Status% > 127 Then GoTo cmdCanOKErr
      Select Case modSlitsN%
        Case 0      ' Slit 1 calibration.
          gblS1% = SlitWidth%  ' S1 calibration
          txtSW(0).Text = SlitWidth%
        Case 1      ' Slit 2 calibration
          gblS2% = SlitWidth%  ' S2 calibration.
          txtSW(1).Text = SlitWidth%
        Case 2
          gblS3% = SlitWidth%  ' S3 adjustment.
          txtSW(2).Text = SlitWidth%
      End Select
      gblOkCancel% = IDOK
  End Select
  
cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Centerform setSlits
  txtSW(0) = gblS1%     ' Entrance slit width.
  txtSW(1) = gblS2%     ' Entrance slit width.
  txtSW(2) = gblS3%     ' Entrance slit width.
  
  setSlits.optSltAdj(0) = True
    txtSW(1).Enabled = False
    txtSW(2).Enabled = False
  
  If (gblNovAdd29& And &H2) Then
    ' For DK242
    
  Else
    optSltAdj(2).Visible = False
    pnlSW(2).Visible = False
  End If
  
  
End Sub





Private Sub optSltAdj_Click(Index As Integer)
  Dim I%
  modSlitsN% = Index
  For I% = 0 To 2
    txtSW(I%).Enabled = False
  Next I
  txtSW(Index).Enabled = True
  
End Sub


Private Sub txtSW_KeyPress(Index As Integer, KeyAscii As Integer)
 Select Case KeyAscii
    Case 13     ' 13 if ascii of CR
      cmdCanOK_Click (1)      ' 1: is OK button
    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select
End Sub


