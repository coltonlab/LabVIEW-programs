VERSION 5.00
Begin VB.Form warnMessg 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   BorderStyle     =   0  'None
   Caption         =   "Warning Message"
   ClientHeight    =   1440
   ClientLeft      =   1440
   ClientTop       =   2310
   ClientWidth     =   3615
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
   ScaleHeight     =   1440
   ScaleWidth      =   3615
   Begin VB.PictureBox pnlwarning 
      BackColor       =   &H80000018&
      Height          =   1455
      Left            =   0
      ScaleHeight     =   1395
      ScaleWidth      =   3555
      TabIndex        =   0
      Top             =   0
      Width           =   3615
      Begin VB.CommandButton cmdCanCONT 
         Caption         =   "Cancel"
         Height          =   315
         Index           =   0
         Left            =   960
         MaskColor       =   &H000000FF&
         TabIndex        =   3
         Top             =   960
         UseMaskColor    =   -1  'True
         Width           =   975
      End
      Begin VB.CommandButton cmdCanCONT 
         Caption         =   "CONTINUE"
         Height          =   315
         Index           =   1
         Left            =   2040
         MaskColor       =   &H00FF0000&
         TabIndex        =   2
         Top             =   960
         UseMaskColor    =   -1  'True
         Width           =   1215
      End
      Begin VB.Label lblLBmessg 
         Alignment       =   2  'Center
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Using this command will change factory settings"
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
         Height          =   615
         Index           =   1
         Left            =   360
         TabIndex        =   1
         Top             =   240
         Width           =   2895
      End
   End
End
Attribute VB_Name = "warnMessg"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Private Sub cmdCanCONT_Click(Index As Integer)
  Select Case Index
    Case 0  '0: Cancel button
      gblContinueCancel% = IDCANCEL
    Case 1  '1: CONTINUE button
      gblContinueCancel% = IDCONTINUE
  End Select
  Unload warnMessg

End Sub

Private Sub Form_Activate()
  'Dim Minutes%, DelayTime%, Timeout%
  'Timeout% = 3    'in seconds
  'Minutes% = Minute(Time$)
  'DelayTime% = Second(Time$) + Timeout%     'Timeout% in seconds
  'DoEvents
  'While ((Minute(Time$) - Minutes%) * 60 + Second(Time$) < DelayTime%)
  'Wend    'Wait until character present or waiting time is less than delay time
  'Unload warnMessg

End Sub

Private Sub Form_Load()
  Centerform Me
End Sub

