VERSION 5.00
Begin VB.Form CtsRts 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "CTS and RTS Status"
   ClientHeight    =   2415
   ClientLeft      =   2310
   ClientTop       =   2835
   ClientWidth     =   3735
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
   ScaleHeight     =   2415
   ScaleWidth      =   3735
   Begin VB.Frame fraOrder 
      Caption         =   "Pc input:CTS"
      Height          =   975
      Left            =   240
      TabIndex        =   6
      Top             =   1200
      Width           =   1695
      Begin VB.OptionButton optCts 
         Caption         =   "True (Enabled)"
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
         TabIndex        =   8
         Top             =   360
         Width           =   1345
      End
      Begin VB.OptionButton optCts 
         Caption         =   "False (Disabled)"
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
         TabIndex        =   7
         Top             =   600
         Width           =   1455
      End
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   2280
      MaskColor       =   &H000000FF&
      TabIndex        =   0
      Top             =   1440
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   2280
      MaskColor       =   &H00FF0000&
      TabIndex        =   1
      Top             =   1800
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlCtsRts 
      Height          =   2415
      Left            =   0
      ScaleHeight     =   2355
      ScaleWidth      =   3675
      TabIndex        =   2
      Top             =   0
      Width           =   3735
      Begin VB.Frame Frame1 
         Caption         =   "Pc output: RTS"
         Height          =   975
         Left            =   240
         TabIndex        =   3
         Top             =   120
         Width           =   1695
         Begin VB.OptionButton optRTS 
            Caption         =   "False (Disabled)"
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
            Width           =   1455
         End
         Begin VB.OptionButton optRTS 
            Caption         =   "True (Enabled)"
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
            Top             =   360
            Width           =   1345
         End
      End
   End
End
Attribute VB_Name = "CtsRts"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, Cts%, Rts%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload CtsRts
    Case 1          ' 1 is OK button.
      Status% = DKRtsCts%(frmDK.comComm1, Rts%, Cts%)
      If Status% < 128 Then
        If Rts% = True Then
          optRTS(1) = False
          optRTS(0) = True
        Else
          optRTS(0) = False
          optRTS(1) = True
        End If

        If Cts% = True Then
          optCts(1) = False
          optCts(0) = True
        Else
          optCts(0) = False
          optCts(1) = True
        End If

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
  Centerform CtsRts
End Sub

Private Sub optCts_MouseUp(Index As Integer, Button As Integer, Shift As Integer, X As Single, Y As Single)
  optCts(Index) = False
End Sub

Private Sub optRTS_MouseUp(Index As Integer, Button As Integer, Shift As Integer, X As Single, Y As Single)
  optRTS(Index) = False
End Sub

