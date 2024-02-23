VERSION 4.00
Begin VB.Form setUnit 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Units Command"
   ClientHeight    =   1920
   ClientLeft      =   1770
   ClientTop       =   3990
   ClientWidth     =   3375
   BeginProperty Font 
      name            =   "MS Sans Serif"
      charset         =   1
      weight          =   700
      size            =   8.25
      underline       =   0   'False
      italic          =   0   'False
      strikethrough   =   0   'False
   EndProperty
   ForeColor       =   &H80000008&
   Height          =   2325
   Left            =   1710
   LinkTopic       =   "Form2"
   MaxButton       =   0   'False
   ScaleHeight     =   1920
   ScaleWidth      =   3375
   Top             =   3645
   Width           =   3495
   Begin Threed.SSPanel pnlSetUnit 
      Height          =   1935
      Left            =   0
      TabIndex        =   2
      Top             =   0
      Width           =   3375
      _version        =   65536
      _extentx        =   5953
      _extenty        =   3413
      _stockprops     =   15
      backcolor       =   -2147483633
      bevelwidth      =   2
      borderwidth     =   0
      alignment       =   6
      Begin Threed.SSFrame fraUnit 
         Height          =   1335
         Left            =   240
         TabIndex        =   5
         Top             =   240
         Width           =   1695
         _version        =   65536
         _extentx        =   2990
         _extenty        =   2355
         _stockprops     =   14
         caption         =   "CM Units"
         Begin Threed.SSOption optUnit 
            Height          =   255
            Index           =   2
            Left            =   120
            TabIndex        =   3
            TabStop         =   0   'False
            Top             =   870
            Width           =   1335
            _version        =   65536
            _extentx        =   2355
            _extenty        =   450
            _stockprops     =   78
            caption         =   "Angstroms"
            BeginProperty font {FB8F0823-0164-101B-84ED-08002B2EC713} 
               name            =   "MS Sans Serif"
               charset         =   1
               weight          =   400
               size            =   8.25
               underline       =   0   'False
               italic          =   0   'False
               strikethrough   =   0   'False
            EndProperty
         End
         Begin Threed.SSOption optUnit 
            Height          =   255
            Index           =   0
            Left            =   120
            TabIndex        =   4
            Top             =   330
            Width           =   1335
            _version        =   65536
            _extentx        =   2355
            _extenty        =   450
            _stockprops     =   78
            caption         =   "centi-Microns"
            BeginProperty font {FB8F0823-0164-101B-84ED-08002B2EC713} 
               name            =   "MS Sans Serif"
               charset         =   1
               weight          =   400
               size            =   8.25
               underline       =   0   'False
               italic          =   0   'False
               strikethrough   =   0   'False
            EndProperty
            value           =   -1  'True
         End
         Begin Threed.SSOption optUnit 
            Height          =   255
            Index           =   1
            Left            =   120
            TabIndex        =   6
            TabStop         =   0   'False
            Top             =   600
            Width           =   1335
            _version        =   65536
            _extentx        =   2355
            _extenty        =   450
            _stockprops     =   78
            caption         =   "Nanometers"
            BeginProperty font {FB8F0823-0164-101B-84ED-08002B2EC713} 
               name            =   "MS Sans Serif"
               charset         =   1
               weight          =   400
               size            =   8.25
               underline       =   0   'False
               italic          =   0   'False
               strikethrough   =   0   'False
            EndProperty
         End
      End
      Begin Threed.SSCommand cmdCanOK 
         Height          =   315
         Index           =   0
         Left            =   2160
         TabIndex        =   0
         Top             =   840
         Width           =   975
         _version        =   65536
         _extentx        =   1720
         _extenty        =   556
         _stockprops     =   78
         caption         =   "Cancel"
         forecolor       =   255
      End
      Begin Threed.SSCommand cmdCanOK 
         Height          =   315
         Index           =   1
         Left            =   2160
         TabIndex        =   1
         Top             =   1200
         Width           =   975
         _version        =   65536
         _extentx        =   1720
         _extenty        =   556
         _stockprops     =   78
         caption         =   "OK"
         forecolor       =   16711680
      End
   End
End
Attribute VB_Name = "setUnit"
Attribute VB_Creatable = False
Attribute VB_Exposed = False
Option Explicit
Dim modUnitsN%

Private Sub cmdCanOK_Click(Index As Integer)
  Dim Status%
  On Error GoTo cmdCanOKErr
  Select Case Index
    Case 0          ' 0 is Cancel button.
      gblOkCancel% = IDCANCEL
      Unload setUnit
    Case 1          ' 1 is OK button.
      Status% = CMUnits%(modUnitsN%, frmCM11x.comComm1, 5) '5: 5s Timeout%
      If Status% < 128 Then
        Select Case modUnitsN%
          Case 0
            gblUnits$ = "centi-Microns"
            gblUnitToNm! = 10
          Case 1
            gblUnits$ = "Nanometers"
            gblUnitToNm! = 1
          Case 2
            gblUnits$ = "Angstroms"
            gblUnitToNm! = 0.1
        End Select
        
        gblUnitsN% = modUnitsN%
        gblCurWL& = 0
        gblOkCancel% = IDOK
        Unload setUnit
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
  Centerform setUnit
  setUnit.optUnit(gblUnitsN%) = True
End Sub

Private Sub optOrder_Click(Index As Integer, Value As Integer)
  modUnitsN% = Index
End Sub

Private Sub optUnit_Click(Index As Integer, Value As Integer)
  modUnitsN% = Index
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

