VERSION 5.00
Begin VB.Form UWrToNov 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Write To Novram"
   ClientHeight    =   2160
   ClientLeft      =   1710
   ClientTop       =   4710
   ClientWidth     =   4455
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
   Icon            =   "UWRTONOV.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   2160
   ScaleWidth      =   4455
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
   Begin VB.PictureBox pnlWrToNov 
      Height          =   2175
      Left            =   0
      ScaleHeight     =   2115
      ScaleWidth      =   4395
      TabIndex        =   1
      Top             =   0
      Width           =   4455
      Begin VB.PictureBox pnlByte 
         Height          =   795
         Left            =   360
         ScaleHeight     =   735
         ScaleWidth      =   3555
         TabIndex        =   5
         Top             =   720
         Width           =   3615
         Begin VB.TextBox txtWrHex 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H00C0C0C0&
            Enabled         =   0   'False
            ForeColor       =   &H00FF0000&
            Height          =   345
            Left            =   2040
            MaxLength       =   5
            MultiLine       =   -1  'True
            TabIndex        =   7
            Text            =   "UWRTONOV.frx":030A
            Top             =   410
            Width           =   1335
         End
         Begin VB.TextBox txtWrByte 
            Alignment       =   2  'Center
            Appearance      =   0  'Flat
            BackColor       =   &H00FFFFFF&
            ForeColor       =   &H00FF0000&
            Height          =   345
            Left            =   2040
            MaxLength       =   5
            MultiLine       =   -1  'True
            TabIndex        =   4
            Text            =   "UWRTONOV.frx":030C
            Top             =   30
            Width           =   1335
         End
         Begin VB.Label Label1 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "In Hex :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   1200
            TabIndex        =   8
            Top             =   480
            Width           =   735
         End
         Begin VB.Label lblByte 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Word To Write :"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   480
            TabIndex        =   6
            Top             =   75
            Width           =   1515
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
            Left            =   2400
            MaxLength       =   3
            MultiLine       =   -1  'True
            TabIndex        =   0
            Text            =   "UWRTONOV.frx":030E
            Top             =   10
            Width           =   975
         End
         Begin VB.Label lblAddr 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Enter an Address (1-64):"
            ForeColor       =   &H80000008&
            Height          =   255
            Left            =   60
            TabIndex        =   3
            Top             =   75
            Width           =   2235
         End
      End
   End
End
Attribute VB_Name = "UWrToNov"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, Addr%, WordWr&
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Exit (Cancel) button.
      gblOkCancel% = IDCANCEL
      Unload UWrToNov
    Case 1          ' 1 is Read (OK) button.
      If Len(txtAddr) Then
        warnMessg.Show MODAL
        If gblContinueCancel% = IDCONTINUE Then
          Addr% = txtAddr.Text
          WordWr& = txtWrByte.Text
          Status% = DKNovramWrite%(Addr%, WordWr&, frmDK.comComm1, 2) '2: 2s Timeout%
          If Status% < 128 Then
            txtWrByte.Text = WordWr&
          Else
            txtWrByte.Text = "Error"
          End If
          gblOkCancel% = IDOK
          txtAddr.SetFocus
        End If
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
  Centerform UWrToNov
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

Private Sub txtWrByte_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    'Case 13                 ' 13 if ascii of CR
    Case Asc("0") To Asc("9")
    
    Case 8      ' 8 is ascii of BS
    
    Case Else
      KeyAscii = 0
  End Select
End Sub

Private Sub txtWrByte_KeyUp(KeyCode As Integer, Shift As Integer)
  txtWrHex.Text = Hex$(Val(txtWrByte.Text))
End Sub


