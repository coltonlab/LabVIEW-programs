VERSION 5.00
Begin VB.Form Novcontent 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Novram Content"
   ClientHeight    =   1935
   ClientLeft      =   1230
   ClientTop       =   1770
   ClientWidth     =   5010
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
   ScaleWidth      =   5010
   Begin VB.PictureBox pnlNovCont 
      Height          =   1935
      Left            =   0
      ScaleHeight     =   1875
      ScaleWidth      =   4935
      TabIndex        =   1
      Top             =   0
      Width           =   5000
      Begin VB.CommandButton cmdCanOK 
         Caption         =   "Exit"
         Height          =   315
         Index           =   0
         Left            =   2040
         MaskColor       =   &H000000FF&
         TabIndex        =   8
         Top             =   1440
         UseMaskColor    =   -1  'True
         Width           =   975
      End
      Begin VB.CommandButton cmdCanOK 
         Caption         =   "OK"
         Height          =   315
         Index           =   1
         Left            =   3240
         MaskColor       =   &H00FF0000&
         TabIndex        =   7
         Top             =   1440
         UseMaskColor    =   -1  'True
         Width           =   975
      End
      Begin VB.PictureBox pnlNovram 
         Height          =   375
         Index           =   1
         Left            =   480
         ScaleHeight     =   315
         ScaleWidth      =   4035
         TabIndex        =   6
         Top             =   720
         Width           =   4095
         Begin VB.TextBox txtVal 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            ForeColor       =   &H00FF0000&
            Height          =   285
            Left            =   2880
            MaxLength       =   5
            TabIndex        =   0
            Top             =   35
            Width           =   1095
         End
         Begin VB.Label lblAddr 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter New Value (0-65535):"
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   1
            Left            =   60
            TabIndex        =   3
            Top             =   75
            Width           =   2475
         End
      End
      Begin VB.PictureBox pnlNovram 
         Height          =   375
         Index           =   0
         Left            =   480
         ScaleHeight     =   315
         ScaleWidth      =   4035
         TabIndex        =   4
         Top             =   240
         Width           =   4095
         Begin VB.Label lblOVal 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BorderStyle     =   1  'Fixed Single
            ForeColor       =   &H80000008&
            Height          =   285
            Left            =   2880
            TabIndex        =   2
            Top             =   0
            Width           =   1095
         End
         Begin VB.Label lblAddr 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Content of address xxx"
            ForeColor       =   &H80000008&
            Height          =   255
            Index           =   0
            Left            =   60
            TabIndex        =   5
            Top             =   75
            Width           =   2475
         End
      End
   End
End
Attribute VB_Name = "Novcontent"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload Me
    Case 1          ' 1 is OK button.
      If Val(txtVal) > 65535 Then
        MsgBox "The entered value is out of range !"
        txtVal.SetFocus
      Else
        gblNVal& = Val(txtVal)
        gblOkCancel% = IDOK
        Unload Me
      End If
  End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Centerform Me
  'Content of xxx memory:
  lblAddr(0) = "Content of address " & gblAddr + 1 & " :"
  lblOVal.Caption = gblOVal&
  
End Sub

Private Sub txtVal_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13     ' 13 if ascii of CR
      cmdCanOK_Click (1)    '1: OK button.
    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select

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

