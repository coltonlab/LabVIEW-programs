VERSION 5.00
Begin VB.Form SetCOM 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Initializing Serial Port"
   ClientHeight    =   1935
   ClientLeft      =   4260
   ClientTop       =   5520
   ClientWidth     =   3240
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
   Icon            =   "SETCOM.frx":0000
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   1935
   ScaleWidth      =   3240
   Begin VB.CommandButton cmdCanOK 
      Caption         =   "OK"
      Height          =   315
      Index           =   1
      Left            =   1920
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
      Left            =   1920
      MaskColor       =   &H000000FF&
      TabIndex        =   0
      Top             =   1080
      UseMaskColor    =   -1  'True
      Width           =   975
   End
   Begin VB.PictureBox Picture1 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Left            =   480
      Picture         =   "SETCOM.frx":030A
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   6
      Top             =   1200
      Width           =   510
   End
   Begin VB.PictureBox Picture2 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Left            =   960
      Picture         =   "SETCOM.frx":0614
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   5
      Top             =   1200
      Width           =   510
   End
   Begin VB.PictureBox pnlSetCOM 
      Height          =   1935
      Left            =   0
      ScaleHeight     =   1875
      ScaleWidth      =   3195
      TabIndex        =   2
      Top             =   0
      Width           =   3255
      Begin VB.ComboBox cboBaud 
         Appearance      =   0  'Flat
         BackColor       =   &H00C0C0C0&
         ForeColor       =   &H00404040&
         Height          =   300
         Left            =   1800
         Style           =   2  'Dropdown List
         TabIndex        =   3
         Top             =   600
         Width           =   1095
      End
      Begin VB.ComboBox cboCOM 
         Appearance      =   0  'Flat
         BackColor       =   &H00C0C0C0&
         ForeColor       =   &H00404040&
         Height          =   300
         Left            =   1800
         Style           =   2  'Dropdown List
         TabIndex        =   4
         Top             =   240
         Width           =   1095
      End
      Begin VB.Label Label1 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Baud rate"
         Height          =   285
         Left            =   360
         TabIndex        =   8
         Top             =   600
         Width           =   1215
      End
      Begin VB.Label lblPortNumber 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Port number"
         Height          =   285
         Left            =   360
         TabIndex        =   7
         Top             =   240
         Width           =   1215
      End
   End
End
Attribute VB_Name = "SetCOM"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim modPortNo%, modBaud%

Private Sub cboBaud_Click()
  modBaud% = cboBaud.ListIndex
End Sub

Private Sub cboCOM_Click()
  modPortNo% = cboCOM.ListIndex
End Sub

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Selection%, Ret%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload SetCOM
    Case 1          ' 1 is OK button.
      If COMInit%(modPortNo%, modBaud%) Then    'True if successful
        Picture1.Visible = False
        gblPortNo% = modPortNo%
        gblBaud% = modBaud%
        gblOkCancel% = IDOK
        Picture2.Visible = True
        'If Not gblIniExist% Then
          Selection% = MsgBox("Do you want to save the configurarion ?", MB_YESNO)
          If Selection% = IDYES Then
            If SaveCmInit%() Then gblIniExist% = True
          Else
            'If user selects No, then the program does nothing.
          End If
        'End If
        'Unload SetCOM
      Else
        frmComMsg.Show MODAL
      End If
  End Select
    
cmdCanOKResume:
  Exit Sub

cmdCanOKErr:
  MsgBox "Error code is : " & Err, MB_ICONEXCLAMATION
  Resume cmdCanOKResume

End Sub

Private Sub Form_Load()
  Dim I%, Baud$
  Centerform SetCOM
  For I% = 0 To 3
    cboCOM.AddItem "COM" & I% + 1
  Next I%
  cboCOM.ListIndex = gblPortNo%

  ' Valid baud rates for CM110/112 are 9600, 4800, 2400, 1200, 600, 300, 150 and 75,
  ' but valid baud rates for Visual Basic are 9600, 4800, 2400, 1200, 600, 300.
  For I% = 0 To 5
    Baud$ = Str$(9600 / (2 ^ I%))
    cboBaud.AddItem Baud$
  Next I%
  cboBaud.ListIndex = gblBaud%
  Picture1.Visible = True
  Picture2.Visible = False

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

