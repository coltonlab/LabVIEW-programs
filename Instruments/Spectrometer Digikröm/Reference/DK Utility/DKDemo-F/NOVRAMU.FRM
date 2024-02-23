VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "comdlg32.ocx"
Object = "{5E9E78A0-531B-11CF-91F6-C2863C385E30}#1.0#0"; "MSFLXGRD.OCX"
Begin VB.Form NovramU 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Novram Utility"
   ClientHeight    =   5610
   ClientLeft      =   1305
   ClientTop       =   2550
   ClientWidth     =   8205
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
   ScaleHeight     =   5610
   ScaleWidth      =   8205
   Begin VB.PictureBox picGauge 
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0C0&
      FillColor       =   &H00FF0000&
      BeginProperty Font 
         Name            =   "MS Serif"
         Size            =   6
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   120
      ScaleHeight     =   345
      ScaleWidth      =   1185
      TabIndex        =   1
      Top             =   120
      Width           =   1215
   End
   Begin VB.PictureBox pnlNovramU 
      Height          =   6135
      Left            =   0
      ScaleHeight     =   6075
      ScaleWidth      =   7755
      TabIndex        =   0
      Top             =   0
      Width           =   7815
      Begin MSFlexGridLib.MSFlexGrid grdNovramU 
         Height          =   5295
         Left            =   1440
         TabIndex        =   2
         Top             =   0
         Width           =   5700
         _ExtentX        =   10054
         _ExtentY        =   9340
         _Version        =   393216
         Rows            =   50
         Cols            =   3
         BackColorBkg    =   16777215
      End
      Begin MSFlexGridLib.MSFlexGrid grdNovramU2 
         Height          =   615
         Left            =   1560
         TabIndex        =   3
         Top             =   0
         Width           =   1215
         _ExtentX        =   2143
         _ExtentY        =   1085
         _Version        =   393216
         BackColorBkg    =   16777215
      End
      Begin MSFlexGridLib.MSFlexGrid grdNovramU1 
         Height          =   495
         Left            =   1920
         TabIndex        =   4
         Top             =   120
         Width           =   1215
         _ExtentX        =   2143
         _ExtentY        =   873
         _Version        =   393216
         BackColorBkg    =   16777215
      End
   End
   Begin MSComDlg.CommonDialog dlgDialog 
      Left            =   0
      Top             =   5640
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.Menu ReadTop 
      Caption         =   "&Read"
      Begin VB.Menu mnuRead 
         Caption         =   "&Novram"
         Index           =   0
      End
      Begin VB.Menu mnuRead 
         Caption         =   "&File"
         Index           =   1
      End
      Begin VB.Menu mnuRead 
         Caption         =   "-"
         Index           =   2
      End
      Begin VB.Menu mnuRead 
         Caption         =   "&Print"
         Index           =   3
      End
      Begin VB.Menu mnuRead 
         Caption         =   "-"
         Index           =   4
      End
      Begin VB.Menu mnuRead 
         Caption         =   "&Exit"
         Index           =   5
      End
   End
   Begin VB.Menu WriteTop 
      Caption         =   "&Write"
      Begin VB.Menu mnuWrite 
         Caption         =   "&Novram"
         Index           =   0
      End
      Begin VB.Menu mnuWrite 
         Caption         =   "&File"
         Index           =   1
      End
   End
   Begin VB.Menu ContentsTop 
      Caption         =   "&Contents"
      Begin VB.Menu mnuContents 
         Caption         =   "&Novram Contents"
         Index           =   0
      End
      Begin VB.Menu mnuContents 
         Caption         =   "&Copy 11-33 to 42-64"
         Index           =   1
      End
      Begin VB.Menu mnuContents 
         Caption         =   "Co&py 42-64 to 11-33"
         Index           =   2
      End
   End
End
Attribute VB_Name = "NovramU"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim modNovContents&(65)
Dim modNovText$(21), modNovTextContents$(21)
Dim modCancel%
Dim modFileName$, modFilePath$
Dim modRows%, modCols%
Dim modGridHgt, modGridWid
Dim RdNovramIn%     'True/False
Dim modEnteredNunber&, modEnteredString$

Private Sub AddressDisplay()
  Dim Ret%, I%
  Ret% = NovramCaption%(1)  '0: name type, 1: address type

  For I% = 0 To 1
    grdNovramU1.FixedAlignment(I%) = 2 ' 2: Center for the fixed cells.
    grdNovramU2.FixedAlignment(I%) = 2 ' 2: Center for the fixed cells.
  Next I%
  
  grdNovramU1.ColAlignment(1) = 2 ' 2: center align.
  grdNovramU2.ColAlignment(1) = 2 ' 2: center align.

  For I% = 1 To 32               'modRows% - 1
    grdNovramU1.Col = 0
    grdNovramU2.Col = 0
    grdNovramU1.Row = I%
    grdNovramU2.Row = I%
    grdNovramU1.Text = I%      ' - 1    'The 0-63 grid
    grdNovramU2.Text = I% + 32    '63  'The 64-127 grid
    
    grdNovramU1.Col = 1
    grdNovramU2.Col = 1
    grdNovramU1.Text = modNovContents&(I% - 1)         '- 1)
    grdNovramU2.Text = modNovContents&(I% + 31)         '+ 63)
  Next I%
  
  'grdNovramU.HighLight = False
  'grdNovramU2.HighLight = False

End Sub

Private Sub Form_Load()
  Centerform Me
  ' Initialize variables for non-fixed height/width of grid less
  ' fixed row/column and grid border (30)
  modGridHgt = grdNovramU.Height - 30     '30
  modGridWid = grdNovramU.Width - 30

  grdNovramU.Visible = False
  grdNovramU1.Visible = False
  grdNovramU2.Visible = False
  picGauge.Visible = False

  mnuWrite(0).Enabled = False   'Novram
  mnuWrite(1).Enabled = False   'File
  mnuContents(0).Enabled = False   'Novram contents
  mnuContents(1).Enabled = False   'Copy 0-63 to 64-127
  mnuContents(2).Enabled = False   'Copy 64-127 to 0-63
  mnuRead(3).Enabled = False   'Print menu.

  RdNovramIn% = False

End Sub

Private Function GetGrooves%(GrooveIndex&)
  Select Case GrooveIndex&
    Case 7
      GetGrooves% = 75
    Case 6
      GetGrooves% = 150
    Case 5
      GetGrooves% = 300
    Case 4
      GetGrooves% = 600
    Case 3
      GetGrooves% = 1200
    Case 2
      GetGrooves% = 1800
    Case 1
      GetGrooves% = 2400
    Case 0
      GetGrooves% = 3600
    Case Else
      GetGrooves% = 0         ' error condition
  End Select

End Function

Private Function GetUnits$(UnitsIndex&)
  Select Case UnitsIndex&
    Case 1
      GetUnits$ = "centi-Microns"
    Case 2
      GetUnits$ = "Nanometers"
    Case Else       '4
      GetUnits$ = "Angstroms"
    'Case Else
      'GetUnits$ = "Error"         ' error condition
  End Select
  
End Function

Private Sub grdNovramU_Click()
  Dim I%, rowNum%, colNum%, RValS$, RValI%
  Dim MsgS$, Titles$, OldVal$, Passed%
  ReDim StrS$(2)  ' 3 variables
  Titles$ = "Novram NEW VALUE"
  rowNum% = grdNovramU.Row

  Select Case rowNum%
    Case 1  ' "Serial Number"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 99999, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 99999
        modNovContents&(1) = Int(modEnteredNunber&)
      End If
    Case 2  ' "IEEE-488 Address"
      ValueIn2Bytes 0, 32, rowNum% - 1
      If gblCancel% = False Then
        modNovContents&(6) = modNovContents&(6) And &HFF00
        modNovContents&(6) = modNovContents&(6) Or modEnteredNunber&
      End If
    Case 3  ' "Grating 1 type (g/mm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(30) = Int(modEnteredNunber&)
      End If
    Case 4  ' "Grating 2 type (g/mm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(31) = Int(modEnteredNunber&)
      End If
    Case 5  ' "Grating 3 type (g/mm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 1, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(32) = Int(modEnteredNunber&)
      End If
    Case 6  ' "Grating 1 Blaze (nm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 1, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(10) = Int(modEnteredNunber&)
      End If
    Case 7  ' "Grating 2 Blaze (nm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 1, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(11) = Int(modEnteredNunber&)
      End If
    Case 8  ' "Grating 3 Blaze (nm)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 1, 65535, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 65535
        modNovContents&(12) = Int(modEnteredNunber&)
      End If
    Case 9  ' "Number of Gratings"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 1, 3, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 3
        modNovContents&(28) = modNovContents&(28) And &HFF
        modNovContents&(28) = modNovContents&(28) Or (modEnteredNunber& * 256)
      End If
    Case 10 ' "MicroStep(1) or not(0)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 1, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 1
        If (modEnteredNunber&) Then
            modNovContents&(28) = modNovContents&(28) Or &H1
        Else
            modNovContents&(28) = modNovContents&(28) And &HFFFE
        End If
      End If
    Case 11 ' "Double(1) or not(0)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 1, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 1
        If (modEnteredNunber&) Then
            modNovContents&(28) = modNovContents&(28) Or &H2
        Else
            modNovContents&(28) = modNovContents&(28) And &HFFFD
        End If
      End If
    Case 12 ' " OMA(1) or not(0)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 1, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 1
        If (modEnteredNunber&) Then
            modNovContents&(28) = modNovContents&(28) Or &H4
        Else
            modNovContents&(28) = modNovContents&(28) And &HFFFB
        End If
      End If
    Case 13 ' " CSR(1) or not(0)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 1, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 1
        If (modEnteredNunber&) Then
            modNovContents&(28) = modNovContents&(28) Or &H8
        Else
            modNovContents&(28) = modNovContents&(28) And &HFFF7
        End If
      End If
    Case 14 ' " GPIB(1) or not(0)"
      'ValueIn2Bytes (MinVal&, MaxVal&, IndexVal%)
      ValueIn2Bytes 0, 1, rowNum% - 1
      If gblCancel% = False Then
        'modEnteredNunber& should be <= 1
        If (modEnteredNunber&) Then
            modNovContents&(28) = modNovContents&(28) Or &H10
        Else
            modNovContents&(28) = modNovContents&(28) And &HFFEF
        End If
      End If
    Case 15 ' "Marked as Programmed"
      'ValueInStrings (NumStr%, StrS$(), IndexVal%)
      StrS$(0) = "Yes"
      StrS$(1) = "No"
      ValueInStrings 1, StrS$(), rowNum% - 1    'NumStr%: 0, 1.
      If gblCancel% = False Then
        Select Case modEnteredString$
          Case "YES"
            modNovContents&(0) = 43690
          Case Else     ' "NO" and default case
            modNovContents&(0) = 65535
        End Select
      End If

    Case Else
      Beep
  End Select

End Sub

Private Sub grdNovramU_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13  ' Enter key
      grdNovramU_Click
    Case Else

  End Select
End Sub

Private Sub grdNovramU1_Click()
  gblOVal& = grdNovramU1.Text
  gblAddr% = (grdNovramU1.Row - 1)
  Novcontent.Show MODAL
  If gblOkCancel% = IDOK Then
    grdNovramU1.Text = gblNVal&
    modNovContents&(gblAddr%) = gblNVal&
  End If

End Sub

Private Sub grdNovramU1_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13  ' Enter key
      grdNovramU1_Click
    Case Else

  End Select

End Sub

Private Sub grdNovramU2_Click()
  gblOVal& = grdNovramU2.Text
  gblAddr% = (grdNovramU2.Row - 1)
  Novcontent.Show MODAL
  If gblOkCancel% = IDOK Then
    grdNovramU2.Text = gblNVal&
    modNovContents&(gblAddr% + 32) = gblNVal&
  End If

End Sub

Private Sub grdNovramU2_KeyPress(KeyAscii As Integer)
  Select Case KeyAscii
    Case 13  ' Enter key
      grdNovramU2_Click
    Case Else

  End Select

End Sub

Private Sub mnuContents_Click(Index As Integer)
  Dim Ret%, I%, Temp$
  Select Case Index
    Case 0  'Novram Contents
      ' Initialize the value of rows and columns for the grid.
      modRows% = 34     '65     'Count the title row.
      modCols% = 2      'Count the index column.
      grdNovramU.Visible = False
      Ret% = SizeCells%(1)   '0: address type
      AddressDisplay
      mnuContents(1).Enabled = True   'Copy 0-63 to 64-127
      mnuContents(2).Enabled = True   'Copy 64-127 to 0-63
    Case 1  'Copy 11-33 to 42-64    'Copy 0-63 to 64-127
      grdNovramU1.Col = 1
      grdNovramU2.Col = 1
      For I% = 11 To 32         '0 To 31      '63
        grdNovramU1.Row = I%        '+ 1
        grdNovramU2.Row = I% - 1      '+ 1

        grdNovramU2.Text = grdNovramU1.Text
        modNovContents&(I% + 31) = modNovContents&(I%)
      Next I%
        grdNovramU2.Row = 1        '+ 1
        Temp$ = grdNovramU2.Text
        grdNovramU2.Row = 32
        grdNovramU2.Text = Temp$
        modNovContents&(64) = modNovContents&(32)
        
    Case 2  'Copy 42-64 to 11-33 'Copy 64-127 to 0-63
      grdNovramU1.Col = 1
      grdNovramU2.Col = 1
      For I% = 10 To 31         '0 To 63
        grdNovramU1.Row = I% + 1
        grdNovramU2.Row = I%
        grdNovramU1.Text = grdNovramU2.Text
        'modNovContents&(I% + 1) = modNovContents&(I% + 31)
        modNovContents&(I%) = modNovContents&(I% + 31)
        
      Next I%
      
      grdNovramU2.Row = 32        '+ 1
      Temp$ = grdNovramU2.Text
      grdNovramU2.Row = 1
      grdNovramU2.Text = Temp$
      modNovContents&(32) = modNovContents&(63)
  
  End Select

End Sub

Private Sub mnuRead_Click(Index As Integer)
  Dim I%, Ret%, DataByte&, PerCentPtr%
  ' Initialize the value of rows and columns for the grid.
  modRows% = 16     'Count the title row.
  modCols% = 3      'Count the index column.
  
  If Index <> 3 Then    '3 is Print menu.
    grdNovramU.Visible = False
    grdNovramU1.Visible = False
    grdNovramU2.Visible = False
    mnuContents(1).Enabled = False   'Copy 0-63 to 64-127
    mnuContents(2).Enabled = False   'Copy 64-127 to 0-63
  End If
  
  Select Case Index
    Case 0  'Novram
      If gblInitCom% Then
        picGauge.Visible = True
        picGauge.Cls
        picGauge.CurrentX = (picGauge.ScaleWidth - picGauge.TextWidth("Reading")) \ 2
        picGauge.CurrentY = (picGauge.ScaleHeight - picGauge.TextHeight("Reading")) \ 2
        picGauge.Print "Reading"
        RdNovramIn% = True
      
        For I% = 1 To 64
          'Function DKNovramRead%(Address%, DataL&, dkPort As Control, Timeout%)
          Ret% = DKNovramRead%(I%, DataByte&, frmDK.comComm1, 5)
          If Ret% < 128 Then
            'modNovContents&(I% - 1) = DataByte&
            modNovContents&(I% - 1) = DataByte&
          Else
            RdNovramIn% = False
            MsgBox "An error has occurred. ", MB_ICONSTOP
            Exit For
          End If

          PerCentPtr% = I% * 100 / 64
          picGauge.Line (0, 0)-((PerCentPtr% * (picGauge.ScaleWidth / 100)), picGauge.ScaleHeight), QBColor(9), BF
     
        Next I%
        Ret% = SizeCells%(0)   '0: name type.
        NameDisplay
        picGauge.Visible = False
        grdNovramU.Visible = True
      Else
        MsgBox "Did you initialize a serial port ? "
      End If
    Case 1  'File
      Ret% = OpenFile()
      If Ret% <> 0 Then
       RdNovramIn% = False      ' error
      Else
       RdNovramIn% = True       ' No error.
      End If
      Ret% = SizeCells%(0)   '0: name type.

      NameDisplay
      grdNovramU.Visible = True
    Case 3  'Print
      Dim PMode%
      If grdNovramU.Visible = True Then
        'PMode% - 0: Text contents, 1: Address contents.
        PMode% = 0
      ElseIf grdNovramU1.Visible = True Then
        PMode% = 1
      End If
      PrintNovram PMode%
    Case 5  'Exit
      Unload Me
    Case Else
      Beep
  End Select

  If RdNovramIn% Then
    mnuWrite(0).Enabled = True   'Novram
    mnuWrite(1).Enabled = True   'File
    mnuContents(0).Enabled = True   'Novram contents
    mnuRead(3).Enabled = True   'Print menu.
  End If

End Sub

Private Sub mnuWrite_Click(Index As Integer)
  Dim I%, DataByte&, Ret%, PerCentPtr%
  Dim Pass%
  Select Case Index
    Case 0  'Novram
      If gblInitCom% Then
        warnMessg.Show MODAL
        If gblContinueCancel% = IDCONTINUE Then
          picGauge.Visible = True
          picGauge.Cls
          picGauge.CurrentX = (picGauge.ScaleWidth - picGauge.TextWidth("Writing")) \ 2
          picGauge.CurrentY = (picGauge.ScaleHeight - picGauge.TextHeight("Writing")) \ 2
          picGauge.Print "Writing"
          Pass% = True
          For I% = 1 To 64
            DataByte& = modNovContents&(I% - 1)
            'CMNovramWrite% (Address%, DataByte%, cmPort As Control, Timeout%)
            Ret% = DKNovramWrite%(I%, DataByte&, frmDK.comComm1, 5)
            If Ret% < 128 Then
              modNovContents&(I% - 1) = DataByte&
            Else
              Pass% = False
              MsgBox "An error has occurred at address " & I%, MB_ICONSTOP, "Write To Novram"
              Exit For
            End If
            PerCentPtr% = I% * 100 / 64
            picGauge.Line (0, 0)-((PerCentPtr% * (picGauge.ScaleWidth / 100)), picGauge.ScaleHeight), QBColor(9), BF
          Next I%
        
          picGauge.Visible = False
          If Pass% = True Then
            MsgBox "In order to use the new Novram values, you must turn the monochromator off and then on. You also need to reset this program."
          End If
        End If
      
      Else
        MsgBox "Did you initialize a serial port ? "
      End If
    Case 1  'File
      SaveAsFile
    Case Else   'Nothing
  
  End Select

End Sub

Private Sub NameDisplay()
  Dim I%, Ret%
  'Read the name of the novram's location into modNovText$(21)
  NovramTextRead
  ToAscArray modNovContents&()
  Ret% = NovramCaption%(0)  '0: name type, 1: address type

  For I% = 0 To 2
    grdNovramU.FixedAlignment(I%) = 2 ' 2: Center for the fixed cells.
  Next I%
  
  grdNovramU.ColAlignment(2) = 2 ' 2: center align.

  For I% = 1 To 15
    grdNovramU.Col = 0
    grdNovramU.Row = I%
    grdNovramU.Text = I%
    grdNovramU.Col = 1
    grdNovramU.Text = modNovText$(I% - 1)
    grdNovramU.Col = 2
    grdNovramU.Text = modNovTextContents$(I% - 1)
  Next I%
  
  'grdNovramU.HighLight = False
  
End Sub

Private Function NovramCaption%(GridType%)
' GridType% has two choices: 0 for name type and 1 for
' address type. If GridType% is out of range, the function
' will return 1 instead of 0 for no error.
  Select Case GridType%
    Case 0
      grdNovramU.Row = 0
      grdNovramU.Col = 0
      grdNovramU.Text = "ITEM"
      grdNovramU.Col = 1
      grdNovramU.Text = "NAME"
      grdNovramU.Col = 2
      grdNovramU.Text = "Value"

      NovramCaption% = 0    ' No error.
    Case 1
      grdNovramU1.Row = 0
      grdNovramU1.Col = 0
      grdNovramU1.Text = "Address"
      grdNovramU2.Row = 0
      grdNovramU2.Col = 0
      grdNovramU2.Text = "Address"
      
      grdNovramU1.Col = 1
      grdNovramU1.Text = "1-32 Contents"
      grdNovramU2.Col = 1
      grdNovramU2.Text = "33-64 Contents"

      NovramCaption% = 0    ' No error.
    Case Else
      NovramCaption% = 1    ' Indication of an error that has occurred.
  End Select


End Function

Private Sub NovramTextRead()
  'Read texts into modNovText$(21) array.
  modNovText$(0) = "Serial number"
  modNovText$(1) = "IEEE-488 Address"
  modNovText$(2) = "Grating 1 type (g/mm)"
  modNovText$(3) = "Grating 2 type (g/mm)"
  modNovText$(4) = "Grating 3 type (g/mm)"
  modNovText$(5) = "Grating 1 Blaze (nm)"
  modNovText$(6) = "Grating 2 Blaze (nm)"
  modNovText$(7) = "Grating 3 Blaze (nm)"
  modNovText$(8) = "Number of Gratings"
  modNovText$(9) = "MicroStep(1) or not(0)"
  modNovText$(10) = "Double(1) or Single(0)"
  modNovText$(11) = "OMA(1) or not(0)"
  modNovText$(12) = "CSR(1) or not(0)"
  modNovText$(13) = "GPIB(1) or not(0)"
  modNovText$(14) = "Marked as Programmed"

End Sub

Private Function OpenFile%()
' The function will return 0 if it has no error; otherwise,
' it will return <>0.
  Dim I%, FileNumber%, TempS$, TempI%
  Dim TempV As Variant
  On Error GoTo OpenFileErr
  modCancel% = False     'Initialize the default value.
  dlgDialog.InitDir = "*.*"
  ' Flags: Sets the options for the Open and Save As dialog boxes.
  ' OFN_FILEMUSTEXIST (&H1000&): Specifies that the user can enter only names of existing files
  ' in the File Name text box. If this flag is set and the user enters an invalid file name, a
  ' warning is displayed. This flag automatically sets the OFN_PATHMUSTEXIST flag.
  ' OFN_HIDEREADONLY (&H4&): Hides the Read Only checked box.
  dlgDialog.Flags = OFN_FILEMUSTEXIST + OFN_HIDEREADONLY
  dlgDialog.CancelError = True
  ' Does file exist?
  dlgDialog.Filter = "Novram Files (*.NOV)|*.NOV|Text Files (*.TXT)|*.TXT|All Files (*.*)|*.*"
  dlgDialog.Action = 1     ' 1: Open
  ' Display file name only.
  modFileName$ = dlgDialog.FileTitle
  ' Display file name with path
  modFilePath$ = dlgDialog.FileName
  FileNumber% = FreeFile
  Open modFilePath$ For Input As FileNumber%
  For I% = 0 To 63
    Input #FileNumber%, modNovContents&(I%)
 Next I%
  Close FileNumber%
  OpenFile% = 0     'No error
OpenFileResume:
  Exit Function

OpenFileErr:
  OpenFile% = 1     'An error
  Select Case Err
    Case 53
      MsgBox modFileName + Chr$(13) + "Cannot find this file" + Chr$(13) + "Please verify that the correct path and filename are given", 48
    Case 32755
      ' "Cancel was selected"
      modCancel% = True
      OpenFile% = 0     'No error
    Case Else
      MsgBox "Error code is : " & Err, 48
  End Select
  Resume OpenFileResume

End Function

Private Sub PrintNovram(PrtMode%)
'PrtMode% - 0: Text contents, 1: Address contents.
'Need to write an error trap routine.
  Dim I%, J%
  Dim DotS$, Line1S$, LineS$, CR_LF$
  Dim PrtW!, PrtH!
  On Error GoTo PrintNovramErr
  DotS$ = "..............."
  CR_LF$ = Chr$(13) + Chr$(10)
  ' PD_USEDEVMODECOPIES: &H40000&; setting this flag disables the copies edit control.
  ' PD_PRINTSETUP: &H40&; causes the system to display the Print Setup dialog box rather
  'than the Print dialog box.
  dlgDialog.Flags = &H40000 Or &H40&
  dlgDialog = 5     'Printer dialog box
  Printer.ScaleMode = 7 ' 5: in inches, 6: mm, 7: cm
  'Printer.Width & Height always return in twips
  '1cm = 567 twips
  PrtW! = Printer.Width / 567
  PrtH! = Printer.Height / 567

  
  Select Case PrtMode%
  Case 0
    LineS$ = " DK NOVRAM PARAMETERS"
    Printer.Print LineS$
    For I% = 0 To 14    'CVI
      Printer.CurrentY = I% / 2 + 1   ' Set coordinate Y.
      LineS$ = Left$((modNovText$(I%) & DotS$), 40) & "  " & LTrim$(modNovTextContents$(I%)) & CR_LF$
      Printer.Print LineS$
    Next I%
    Printer.EndDoc
  Case 1
    Printer.CurrentY = 0.5
    For I% = 0 To 3
      Printer.CurrentX = PrtW! * I / 4
      Printer.Print "Address" & " " & "Contents";
    Next I%
    For I% = 0 To 15  'Will change back to 31.
      Printer.CurrentY = I% / 2 + 1   ' Set coordinate Y.
      For J% = 0 To 3
        Printer.CurrentX = PrtW! * J% / 4 + 0.5
        'Line1S$ = Left$((Str$(I% + J% * 16) & Space(8)), 8)     '32
        Line1S$ = Left$((Str$(I% + 1 + J% * 16) & Space(8)), 8)   '32
        LineS$ = Line1S$ & Str$(modNovContents&(I% + J% * 16))  '32
        Printer.Print LineS$;
      Next J%
    Next I%
    Printer.EndDoc
  End Select

PrintNovramResume:
  Exit Sub

PrintNovramErr:
  Select Case Err
    Case 32755
      ' "Cancel was selected"
      modCancel% = True
    Case Else
      MsgBox "Error code is : " & Err, 48
  End Select
  Resume PrintNovramResume

End Sub

Private Sub PutGrooves(IndexVal%)
' IndexVal% starts from 0.
  Dim Titles$, MsgS$, OldVal$, RValS$, Passed%
  Titles$ = "Novram NEW VALUE"
  
  Do
    'MsgS$ = modNovText$(IndexVal%)
    MsgS$ = " Grooves/mm: 3600, 2400, 1800, 1200, 600, 300, 150, or 75"
    OldVal$ = modNovTextContents$(IndexVal%)
    RValS$ = InputBox$("Enter " & MsgS$, Titles$, OldVal$, Screen.Width / 4, 0)
    If RValS$ = "" Then
      gblCancel% = True     'Cancel hit.
      Passed% = True
    Else
      gblCancel% = False    'Cancel wasn't hit.
      Passed% = True
      Select Case Val(RValS$)
        'Case MinVal& To MaxVal&
        Case 3600
          modEnteredNunber& = 0
        Case 2400
          modEnteredNunber& = 1
        Case 1800
          modEnteredNunber& = 2
        Case 1200
          modEnteredNunber& = 3
        Case 600
          modEnteredNunber& = 4
        Case 300
          modEnteredNunber& = 5
        Case 150
          modEnteredNunber& = 6
        Case 75
          modEnteredNunber& = 7
        Case Else
          MsgBox "Entered value is out of range. Hit 'OK' to continue"
          Passed% = False
      End Select
    End If
  Loop While (Passed% = False)
          
  If Passed% = True And gblCancel% = False Then
    grdNovramU.Text = RValS$
    'modNovTextContents$(IndexVal%) = RValS$
  End If

End Sub

Private Sub SaveAsFile()
  Dim Temp$, CR$, I%
  Dim rsp%, FileNumber%
  On Error GoTo SaveAsFileErr
  dlgDialog.InitDir = "*.nov"
  ' Flags: Sets the options for the Open and Save As dialog boxes.
  ' OFN_OVERWRITEPROMPT(&H2&): Causes the Save As dialog box to generate a message box if the
  ' selected file alreadyexits
  ' OFN_HIDEREADONLY (&H4&): Hides the Read Only checked box.
  dlgDialog.Flags = OFN_OVERWRITEPROMPT + OFN_HIDEREADONLY
  dlgDialog.CancelError = True
  ' Does the file exist?
  dlgDialog.Filter = "Novram Files (*.NOV)|*.NOV|Text Files (*.TXT)|*.TXT|All Files (*.*)|*.*"
  dlgDialog.Action = 2     ' 2: Save As
  modFileName = dlgDialog.FileTitle
  modFilePath = dlgDialog.FileName
  
  FileNumber% = FreeFile
  Open modFilePath For Output As FileNumber%
  For I% = 0 To 63
    Temp$ = Format$(modNovContents&(I%), "@@@@@")
    Print #FileNumber%, Temp$
  Next I%
  Close FileNumber%
  ' MsgBox MessageInBox, TypeOfBox, TitleOfBox
  MsgBox modFilePath + " Saved", MB_ICONEXCLAMATION, "Save"


SaveAsFileResume:
  Exit Sub

SaveAsFileErr:
  Select Case Err
    Case 53
      MsgBox modFileName + Chr$(13) + "Cannot find this file" + Chr$(13) + "Please verify that the correct path and filename are given", 48
    Case 71
      rsp% = MsgBox("Disk not ready" + Chr$(13), MB_ICONEXCLAMATION + MB_RETRYCANCEL, "SaveAs: Error")
      If rsp% = IDRETRY Then
        Resume 0
      Else
        gblCancel% = True
      End If

    Case 32755
      ' "Cancel was selected"
      gblCancel% = True
    Case Else
      MsgBox "Error code is : " & Err, 48
  End Select
  Resume SaveAsFileResume

End Sub

Private Function SizeCells%(GridType%)
' GridType% has two choices: 0 for name type and 1 for
' address type. If GridType% is out of range, the function
' will return 1 instead of 0 for no error.
  ' Declare local variables
  Dim Count
  Dim ScrollHgt
  Dim ScrollWid
  ' Initialize variables for scroll bar height/width
  ScrollHgt = 255
  ScrollWid = 255
  ' Display both scroll bars
  grdNovramU.ScrollBars = 3     '3
  
  Select Case GridType%
    Case 0      ' 0: for name type.
      ' Set # of fixed and non-fixed rows/cols to default
      grdNovramU.Rows = modRows%
      grdNovramU.Cols = modCols%
      ' Set # of fixed rows/cols to default
      grdNovramU.FixedRows = 1
      grdNovramU.FixedCols = modCols% - 1
      ' Set row heights to evenly display 23 rows in grid height
      For Count = 0 To modRows% - 1
        grdNovramU.RowHeight(Count) = modGridHgt / 15   '22
      Next Count

      ' Set the width of grid
      grdNovramU.Width = modGridWid
      
      ' Set col widths to display 3 columns in non-fixed grid width.
      grdNovramU.ColWidth(0) = (modGridWid - ScrollWid) / 8
      grdNovramU.ColWidth(1) = (modGridWid - ScrollWid) * 5 / 8          '5 / 8
      grdNovramU.ColWidth(2) = (modGridWid - ScrollWid) * 2 / 8

      SizeCells% = 0    ' No error.
    Case 1      ' 1: for address type.
      ' Set # of fixed and non-fixed rows/cols to default
      grdNovramU1.Rows = modRows%
      grdNovramU1.Cols = modCols%
      grdNovramU2.Rows = modRows%
      grdNovramU2.Cols = modCols%
      
      ' Set # of fixed rows/cols to default
      grdNovramU1.FixedRows = 1
      grdNovramU1.FixedCols = 1
      grdNovramU2.FixedRows = 1
      grdNovramU2.FixedCols = 1
      ' Set row heights to evenly display 23 rows in grid height
      For Count = 0 To modRows% - 1
        grdNovramU1.RowHeight(Count) = modGridHgt / 22
        grdNovramU2.RowHeight(Count) = modGridHgt / 22
      Next Count
    
      grdNovramU1.Width = modGridWid / 2
      grdNovramU1.Height = modGridHgt
      '[object.]Move left[, top[, width[, height] ] ]
      grdNovramU2.Move grdNovramU1.Left + grdNovramU1.Width, grdNovramU1.Top, modGridWid / 2, modGridHgt

      
      ' Set col widths to display 3 columns in non-fixed grid width.
      grdNovramU1.ColWidth(0) = (modGridWid - ScrollWid) * 2 / 16
      grdNovramU1.ColWidth(1) = (modGridWid - ScrollWid) * 6 / 16
      
      grdNovramU2.ColWidth(0) = (modGridWid - ScrollWid) * 2 / 16
      grdNovramU2.ColWidth(1) = (modGridWid - ScrollWid) * 6 / 16

      grdNovramU1.Visible = True
      grdNovramU2.Visible = True
      SizeCells% = 0    ' No error.
    Case Else
      SizeCells% = 1    ' Indication of an error.
  End Select

End Function

Private Sub ToAscArray(Orig&())
  Dim TempL&, TemI%
  ' Baud rate
'  Select Case Orig&(0)
'    Case 0, 1, 2, 3, 4, 5, 6, 7
'      modNovTextContents$(0) = Str$(9600 / 2 ^ Orig&(0))
'    Case Else
'      modNovTextContents$(0) = Str$(0)  'error
'  End Select
  
  ' Serial Number
  modNovTextContents$(0) = Str$(Orig&(1))
  ' IEEE-488 Address
  modNovTextContents$(1) = Str$(Orig&(6) And &HFF)
  ' Grating 1 type
  modNovTextContents$(2) = Str$(Orig&(30))
  ' Grating 2 type
  modNovTextContents$(3) = Str$(Orig&(31))
  ' Grating 3 type
  modNovTextContents$(4) = Str$(Orig&(32))
  ' Grating 1 Blaze
  modNovTextContents$(5) = Str$(Orig&(10))
  ' Grating 2 Blaze
  modNovTextContents$(6) = Str$(Orig&(11))
  ' Grating 3 Blaze
  modNovTextContents$(7) = Str$(Orig&(12))
  ' Number of Gratings
  TemI% = Orig&(28) / 256
  modNovTextContents$(8) = Str$(TemI%)
  ' MicroStep(1) or not (0)
  TemI% = 0
  If (Orig&(28) And &H1) Then TemI% = 1
  modNovTextContents$(9) = TemI%
  ' Double(1) or not(0)
  TemI% = 0
  If (Orig&(28) And &H2) Then TemI% = 1
  modNovTextContents$(10) = TemI%
  ' OMA(1) or not(0)
  TemI% = 0
  If (Orig&(28) And &H4) Then TemI% = 1
  modNovTextContents$(11) = TemI%
  ' CSR(1) or not(0)
  TemI% = 0
  If (Orig&(28) And &H8) Then TemI% = 1
  modNovTextContents$(12) = TemI%
  ' GPIB(1) or not(0)
  TemI% = 0
  If (Orig&(28) And &H10) Then TemI% = 1
  modNovTextContents$(13) = TemI%
  ' Marked as programmed
  If Orig&(0) = 43690 Then
    modNovTextContents$(14) = "Yes"
  Else
    modNovTextContents$(14) = "No"
  End If

End Sub

Private Sub ValueIn2Bytes(MinVal&, MaxVal&, IndexVal%)
' This subroutine will prompt a dialog box and check the
' entered number in this box. It will wait until a user to
' enter a correct value or to hit cancel button.
' IndexVal% starts from 0.
  Dim Titles$, MsgS$, OldVal$, RValS$, Passed%
  Titles$ = "Novram NEW VALUE"
  Do
    MsgS$ = modNovText$(IndexVal%)
    OldVal$ = modNovTextContents$(IndexVal%)
    RValS$ = InputBox$("Enter " & MsgS$, Titles$, OldVal$, Screen.Width / 4, 0)
    If RValS$ = "" Then
      gblCancel% = True     'Cancel hit.
      Passed% = True
    ElseIf IsNumeric(RValS$) = False Then
      MsgBox "Entered value is not a number."
      Passed% = False
    Else
      Select Case Val(RValS$)
        Case MinVal& To MaxVal&
          gblCancel% = False    'Cancel wasn't hit.
          Passed% = True
        Case Else
          MsgBox "Entered value is out of range. Hit 'OK' to continue"
          Passed% = False
      End Select
    End If
  Loop While (Passed% = False)
          
  If Passed% = True And gblCancel% = False Then
    grdNovramU.Text = RValS$
    'modNovTextContents$(IndexVal%) = RValS$
    modEnteredNunber& = Val(RValS$)
  End If

End Sub

Private Sub ValueInStrings(NumStr%, StrS$(), IndexVal%)
' This routine will use NumStr% (from 0) as a number of string will
'be used in this sub. StrS$() is a string array to be
'compared with the entered strings. IndexVal% is the index
'of modNovText$() array.
  Dim Titles$, MsgS$, MsgT$, OldVal$, RValS$, Passed%
  Dim I%
  Titles$ = "Novram NEW VALUE"
  MsgS$ = modNovText$(IndexVal%) & " : "
  For I% = 0 To NumStr%
    If I% = NumStr% Then
      MsgT$ = StrS$(I%) & "."
    Else
      MsgT$ = StrS$(I%) & ", "
    End If
    MsgS$ = MsgS$ + MsgT$
  Next I%
  OldVal$ = modNovTextContents$(IndexVal%)

  Do
    RValS$ = InputBox$("Enter " & MsgS$, Titles$, OldVal$, Screen.Width / 4, 0)
    
    If RValS$ = "" Then
      gblCancel% = True     'Cancel hit.
      Passed% = True
    Else
      Passed% = False
      For I% = 0 To NumStr%
        If UCase$(RValS$) = UCase$(StrS$(I%)) Then
          RValS$ = StrS$(I%)
          gblCancel% = False    'Cancel  wasnot hit.
          Passed% = True
          Exit For
        End If
      Next I%
      If Passed = False Then
        MsgBox "Entered value is out of range. Hit 'OK' to continue"
      End If
    End If
  Loop While (Passed% = False)
          
  If Passed% = True And gblCancel% = False Then
    grdNovramU.Text = RValS$
    modEnteredString$ = UCase$(RValS$)
  End If

End Sub

