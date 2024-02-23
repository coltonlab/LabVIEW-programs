VERSION 5.00
Begin VB.Form Form1 
   Appearance      =   0  'Flat
   BackColor       =   &H80000005&
   Caption         =   "Form1"
   ClientHeight    =   2715
   ClientLeft      =   1245
   ClientTop       =   1740
   ClientWidth     =   7365
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
   LinkTopic       =   "Form1"
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   2715
   ScaleWidth      =   7365
   Begin VB.CommandButton Command1 
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      Caption         =   "Command1"
      Default         =   -1  'True
      Height          =   495
      Left            =   3000
      TabIndex        =   0
      Top             =   1920
      Width           =   1215
   End
   Begin VB.PictureBox picStep 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Index           =   4
      Left            =   6120
      Picture         =   "FORM1.frx":0000
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   5
      Top             =   960
      Width           =   510
   End
   Begin VB.PictureBox picStep 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Index           =   3
      Left            =   5520
      Picture         =   "FORM1.frx":030A
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   4
      Top             =   960
      Width           =   510
   End
   Begin VB.PictureBox picStep 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Index           =   0
      Left            =   1800
      Picture         =   "FORM1.frx":0614
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   1
      Top             =   960
      Width           =   510
   End
   Begin VB.PictureBox picStep 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      ForeColor       =   &H80000008&
      Height          =   510
      Index           =   1
      Left            =   2400
      Picture         =   "FORM1.frx":091E
      ScaleHeight     =   480
      ScaleWidth      =   480
      TabIndex        =   2
      Top             =   960
      Width           =   510
   End
   Begin VB.PictureBox picStep 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0C0&
      ForeColor       =   &H80000008&
      Height          =   495
      Index           =   2
      Left            =   3000
      ScaleHeight     =   465
      ScaleWidth      =   2385
      TabIndex        =   6
      Top             =   960
      Width           =   2415
      Begin VB.PictureBox pnlWLength 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FF0000&
         Height          =   255
         Left            =   120
         ScaleHeight     =   195
         ScaleWidth      =   1035
         TabIndex        =   3
         Top             =   120
         Width           =   1095
      End
      Begin VB.Label lblUnits 
         Alignment       =   2  'Center
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Angstroms"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FF0000&
         Height          =   255
         Left            =   1320
         TabIndex        =   8
         Top             =   120
         Width           =   1005
      End
   End
   Begin VB.Label lblUnitDesW 
      Alignment       =   2  'Center
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Angstroms"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   255
      Index           =   0
      Left            =   960
      TabIndex        =   7
      Top             =   360
      Width           =   1005
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False

Private Sub Command1_Click()
  MsgBox "Command clicked"
End Sub

