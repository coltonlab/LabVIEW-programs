VERSION 5.00
Begin VB.Form Loopback 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   Caption         =   "Loopback COM Test"
   ClientHeight    =   1710
   ClientLeft      =   2235
   ClientTop       =   1650
   ClientWidth     =   4215
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
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   1710
   ScaleWidth      =   4215
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   2760
      MaskColor       =   &H00FF0000&
      TabIndex        =   2
      Top             =   1200
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "Exit"
      Height          =   315
      Index           =   0
      Left            =   1560
      MaskColor       =   &H000000FF&
      TabIndex        =   1
      Top             =   1200
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox pnlLoopback 
      Height          =   1695
      Left            =   0
      ScaleHeight     =   1635
      ScaleWidth      =   4155
      TabIndex        =   0
      Top             =   0
      Width           =   4215
      Begin VB.Label lblLBmessg 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Loopback communications test FAILED"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   9.75
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H000000FF&
         Height          =   735
         Index           =   1
         Left            =   360
         TabIndex        =   5
         Top             =   2760
         Width           =   3495
      End
      Begin VB.Label lblLBmessg 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Loopback communications test PASSED"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   9.75
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FF0000&
         Height          =   735
         Index           =   2
         Left            =   360
         TabIndex        =   4
         Top             =   2280
         Width           =   3495
      End
      Begin VB.Label lblLBmessg 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Disconnect the serial cable at DK end, and install a jumper between  pins 2 and 3."
         Height          =   735
         Index           =   0
         Left            =   360
         TabIndex        =   3
         Top             =   360
         Width           =   3495
      End
   End
End
Attribute VB_Name = "Loopback"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%, EchoB$, Byte1$   '~2CM
  Dim PortNo%, Baudrate%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Exit (Cancel) button.
      gblOkCancel% = IDCANCEL
      Unload Loopback
    Case 1          ' 1 is OK button.
      If gblInitCom% = False Then
        PortNo% = gblPortNo% + 1
        Baudrate% = 9600 / 2 ^ gblBaud%
        Status% = DKInitComPort%(PortNo%, Baudrate%, frmDK.comComm1)
      Else
        Status% = 0     'No error
      End If
      
      If Status% < 128 Then
        lblLBmessg(0).Visible = False
        gblOkCancel% = IDOK
        frmDK.comComm1.Output = Chr$(55)
        Status% = DKTimeout%(frmDK.comComm1, 1)
        If Status% = 128 Then     'Failed
          lblLBmessg(2).Move 360, 2760  'Passed message.
          lblLBmessg(1).Move 360, 360   'Failed message.
          gblInitCom% = True
        Else
          Byte1$ = frmDK.comComm1.Input  ' ~2CM
          If Asc(Byte1$) = 55 Then
            lblLBmessg(1).Move 360, 2760    'Failed message
            lblLBmessg(2).Move 360, 360     'Passed message
            gblInitCom% = True
          Else
            lblLBmessg(2).Move 360, 2760    'Passed message
            lblLBmessg(1).Move 360, 360     'Failed message
            gblInitCom% = False
          End If
        End If
      Else
        MsgBox " An error has occurred "
      End If
  End Select

cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Centerform Loopback
  lblLBmessg(0).Visible = True

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

