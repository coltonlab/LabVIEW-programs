VERSION 5.00
Begin VB.Form ctrSpeed 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Speed Command"
   ClientHeight    =   1320
   ClientLeft      =   1965
   ClientTop       =   5175
   ClientWidth     =   5655
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
   ScaleHeight     =   1320
   ScaleWidth      =   5655
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   4080
      MaskColor       =   &H00FF0000&
      TabIndex        =   2
      Top             =   840
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   3000
      MaskColor       =   &H000000FF&
      TabIndex        =   1
      Top             =   840
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlCtrSpeed 
      Height          =   1335
      Left            =   0
      ScaleHeight     =   1275
      ScaleWidth      =   5595
      TabIndex        =   3
      Top             =   0
      Width           =   5655
      Begin VB.PictureBox pnlNewSpeed 
         Height          =   375
         Left            =   480
         ScaleHeight     =   315
         ScaleWidth      =   4515
         TabIndex        =   4
         Top             =   240
         Width           =   4575
         Begin VB.TextBox txtSpeed 
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            Height          =   285
            Left            =   1920
            MaxLength       =   8
            TabIndex        =   0
            Top             =   30
            Width           =   1335
         End
         Begin VB.Label lblAperS 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "nm/min"
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
            Left            =   3360
            TabIndex        =   6
            Top             =   45
            Width           =   1095
         End
         Begin VB.Label lblNewSpeed 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Select New Speed :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   5
            Top             =   75
            Width           =   1755
         End
      End
   End
End
Attribute VB_Name = "ctrSpeed"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit



Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, SSpeed%
  On Error GoTo cmdCanOKErr
  SSpeed% = Val(txtSpeed.Text)
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload ctrSpeed
    Case 1          ' 1 is OK button.
      Status% = DKSpeed%(SSpeed%, frmDK.comComm1, 5) '5: 5s Timeout%
      If Status% < 128 Then gblSSpeed% = SSpeed%
      gblOkCancel% = IDOK
  End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  On Error GoTo ctrSpeedErr
  Centerform ctrSpeed
  txtSpeed.Text = gblSSpeed%
  txtSpeed.SelLength = Len(txtSpeed)

ctrSpeedResume:
  Exit Sub

ctrSpeedErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume ctrSpeedResume

End Sub

