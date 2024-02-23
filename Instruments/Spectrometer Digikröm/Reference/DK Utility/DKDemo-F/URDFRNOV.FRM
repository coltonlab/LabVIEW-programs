VERSION 5.00
Begin VB.Form URdFrNov 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Read From Novram"
   ClientHeight    =   2295
   ClientLeft      =   1260
   ClientTop       =   3780
   ClientWidth     =   4320
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
   Icon            =   "URDFRNOV.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   2295
   ScaleWidth      =   4320
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   3000
      MaskColor       =   &H00FF0000&
      TabIndex        =   10
      Top             =   1680
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   1920
      MaskColor       =   &H000000FF&
      TabIndex        =   9
      Top             =   1680
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlRdFrNov 
      Height          =   2295
      Left            =   0
      ScaleHeight     =   2235
      ScaleWidth      =   4275
      TabIndex        =   1
      Top             =   0
      Width           =   4335
      Begin VB.PictureBox pnlByte 
         Height          =   735
         Left            =   360
         ScaleHeight     =   675
         ScaleWidth      =   3555
         TabIndex        =   5
         Top             =   720
         Width           =   3615
         Begin VB.Label Label1 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "In Hex :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   1560
            TabIndex        =   8
            Top             =   360
            Width           =   735
         End
         Begin VB.Label lblRdHex 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   9.75
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00808080&
            Height          =   285
            Left            =   2280
            TabIndex        =   7
            Top             =   360
            Width           =   975
         End
         Begin VB.Label lblRdByte 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BorderStyle     =   1  'Fixed Single
            Caption         =   "0"
            BeginProperty Font 
               Name            =   "MS Sans Serif"
               Size            =   9.75
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00808080&
            Height          =   285
            Left            =   2280
            TabIndex        =   4
            Top             =   45
            Width           =   975
         End
         Begin VB.Label lblByte 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Word Read from Novram :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   6
            Top             =   75
            Width           =   2235
         End
      End
      Begin VB.PictureBox pnlAddr 
         Height          =   390
         Left            =   360
         ScaleHeight     =   330
         ScaleWidth      =   3555
         TabIndex        =   2
         Top             =   240
         Width           =   3615
         Begin VB.TextBox txtAddr 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            ForeColor       =   &H00FF0000&
            Height          =   350
            Left            =   2280
            MaxLength       =   3
            MultiLine       =   -1  'True
            TabIndex        =   0
            Text            =   "URDFRNOV.frx":030A
            Top             =   15
            Width           =   975
         End
         Begin VB.Label lblAddr 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter an Address (1-64) :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   3
            Top             =   75
            Width           =   2115
         End
      End
   End
End
Attribute VB_Name = "URdFrNov"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, Addr%, WordRd&
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Exit (Cancel) button.
      gblOkCancel% = IDCANCEL
      Unload URdFrNov
    Case 1          ' 1 is Read (OK) button.
      If Len(txtAddr) <> 0 And Val(txtAddr) <> 0 Then
        Addr% = txtAddr.Text
        Status% = DKNovramRead%(Addr%, WordRd&, frmDK.comComm1, 2) '2: 2s Timeout%
        If Status% < 128 Then
          lblRdByte.Caption = WordRd&
          lblRdHex.Caption = Hex$(WordRd&)
        Else
          lblRdByte.Caption = "Error"
          lblRdHex.Caption = "$Error"
        End If
        gblOkCancel% = IDOK
        txtAddr.SetFocus
      Else
        MsgBox "The entered number is out of range", MB_ICONEXCLAMATION
        txtAddr.SetFocus
      End If
    End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION, "DK.BAS"
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Centerform URdFrNov
  txtAddr.SelLength = Len(txtAddr)
End Sub

Private Sub txtAddr_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    'Case 13                 ' 13 if ascii of CR
    Case Asc("0") To Asc("9")

    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select

End Sub

Private Sub txtWL_KeyPress(KeyAscii As Integer)
End Sub

