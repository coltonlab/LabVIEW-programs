VERSION 5.00
Begin VB.Form setType 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Type Command"
   ClientHeight    =   1935
   ClientLeft      =   4410
   ClientTop       =   5775
   ClientWidth     =   4470
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
   ScaleWidth      =   4470
   Begin VB.PictureBox pnlSetType 
      Height          =   1935
      Left            =   360
      ScaleHeight     =   1875
      ScaleWidth      =   3795
      TabIndex        =   2
      Top             =   -120
      Width           =   3855
      Begin VB.CommandButton cmdCanOK 
         Caption         =   "OK"
         Height          =   315
         Index           =   1
         Left            =   2640
         MaskColor       =   &H00FF0000&
         TabIndex        =   1
         Top             =   1200
         UseMaskColor    =   -1  'True
         Width           =   975
      End
      Begin VB.CommandButton cmdCanOK 
         Caption         =   "Exit"
         Height          =   315
         Index           =   0
         Left            =   2640
         MaskColor       =   &H000000FF&
         TabIndex        =   0
         Top             =   840
         UseMaskColor    =   -1  'True
         Width           =   975
      End
      Begin VB.Frame fraType 
         Caption         =   "CM Type"
         Height          =   1335
         Left            =   240
         TabIndex        =   3
         Top             =   240
         Width           =   2175
         Begin VB.OptionButton optType 
            Caption         =   "Subtractive Dispersion"
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
            TabIndex        =   6
            Top             =   870
            Width           =   1935
         End
         Begin VB.OptionButton optType 
            Caption         =   "Additive Dispersion"
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
            TabIndex        =   5
            Top             =   600
            Width           =   1692
         End
         Begin VB.OptionButton optType 
            Caption         =   "Single Turret"
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
            TabIndex        =   4
            Top             =   330
            Value           =   -1  'True
            Width           =   1335
         End
      End
   End
End
Attribute VB_Name = "setType"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim modType%

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, TypeCode%
  On Error GoTo cmdCanOKErr
  If modType% = 2 Then modType% = 254
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload setType
    Case 1          ' 1 is OK button.
      Status% = DKType%(TypeCode%, frmDK.comComm1, 5) '5: 5s Timeout%
      If Status% < 128 Then
        gblType% = modType%
        gblCurWL& = 0
        gblOkCancel% = IDOK
        'Unload setType
      Else
        gblOkCancel% = IDCANCEL
      End If
  End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume
    
End Sub

Private Sub Form_Load()
  Dim typeIndex%
  Centerform setType
  Select Case gblType%
    Case 0, 1
      typeIndex% = gblType%
    Case 254
      typeIndex% = 2
    Case Else
      MsgBox " An error has occurred "
  End Select
  setType.optType(typeIndex%) = True
End Sub


Private Sub optType_Click(Index As Integer)
    modType% = Index
End Sub
