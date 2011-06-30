<?xml version='1.0' encoding='UTF-8'?>
<Library LVVersion="9008000">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Lib.Description" Type="Str">Digikröm
DK 240 ¼ Meter
DK 242 Double ¼ Meter
DK 480 ½ Meter
Monochromator / Spectrograph


Spectral Products
200 Dorado Place SE Albuquerque, NM 87123
Phone (877) 208-0245 Fax (505) 298-9908</Property>
	<Property Name="NI.Lib.HelpPath" Type="Str"></Property>
	<Property Name="NI.Lib.Icon" Type="Bin">#1#!!!!!!!)!"1!&amp;!!!-!%!!!@````]!!!!"!!%!!!+!!!!*Q(C=\&gt;1^&lt;NN!%)&lt;BTY',J&amp;38)E7A%RC9+[BRG9*!$#4N8%'NCR4+%?9+KGB$H1SY3D?.#Z?[AK\!P&amp;QN;3?B&lt;3"+E1!BN2,V\&gt;`$Z9*3/6Z,J_J?/D&lt;0(N10T7L4LFZUB]`$XT%?+Q\B$`5083@LRS'[K@[$9"DJZ`EH&lt;G:S`-@"F']TX/WP`MUY^20X@[CJ`K@7LRN`8V\`9Q]^?RT:`@`R$RS8RW_C9`@#3&gt;FJF+1%R3GG@MAOS:-]S:-]S:-]S)-]S)-]S)0=S:X=S:X=S:X=S)X=S)X=S)W]H/1C&amp;\H))374*R-FAS9$*)WB+0F+0)EH]31?`CLR**\%EXA3$UW5?"*0YEE]C9&gt;O3DS**`%EHM4$5%73Z34(EXA98I%H]!3?Q".YG&amp;+"*Q!%EQ5$"Y0!5&amp;!:8!3?Q".YO&amp;4A#4S"*`!%(KI6?!*0Y!E]A9=O:67C;0K4(!`$S0%Y(M@D?"Q01]PR/"\(YXA=$^0*]4A?"_&amp;-[!Q/15YHJY(TR`%Y(H\E?"S0YX%]DI?K]I3]L%SP[5^S0)&lt;(]"A?QW.Y'%+'R`!9(M.D?"B7BM@Q'"\$9XC93I&lt;(]"A?!W*-SP1S"D-['IW-Q0$Q+&lt;P&amp;SF/+)L&amp;S3H8TKGZ+V=WGOIF5.Y@K1V&gt;^G+I0388R62&gt;6&gt;&lt;&amp;5&amp;U(VZF42KBD6361\^QWVZXN(W6,7F"6F37EI#]K=-OO\`O''_`V?O^V/W_V7[`6;K^6+S_634&gt;.IM6BI0J^L.JO.LY(XH/-,Y@"?OO4[^OTD?&gt;N_O7_PXD4N^?S_P8FXXN\IJ,V_?^&amp;?H8ZLW[`5@\C\0@PUO7]`P)_'[^^`,`U.\U;^UO0_L.&amp;X^!\OEQ!!!!!</Property>
	<Property Name="NI.Lib.Version" Type="Str">1.0.0.0</Property>
	<Item Name="Public" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">1</Property>
		<Item Name="Action-Status" Type="Folder">
			<Item Name="Query" Type="Folder">
				<Item Name="Query Filter.vi" Type="VI" URL="../Public/Action-Status/Query/Query Filter.vi"/>
				<Item Name="Query Wavelength.vi" Type="VI" URL="../Public/Action-Status/Query/Query Wavelength.vi"/>
				<Item Name="Query Grating.vi" Type="VI" URL="../Public/Action-Status/Query/Query Grating.vi"/>
				<Item Name="Query Scan Speed.vi" Type="VI" URL="../Public/Action-Status/Query/Query Scan Speed.vi"/>
				<Item Name="Query Slits.vi" Type="VI" URL="../Public/Action-Status/Query/Query Slits.vi"/>
			</Item>
			<Item Name="Action-Status.mnu" Type="Document" URL="/&lt;instrlib&gt;/Digikrom DK24x/Public/Action-Status/Action-Status.mnu"/>
			<Item Name="Goto Wavelength.vi" Type="VI" URL="../Public/Action-Status/Goto Wavelength.vi"/>
			<Item Name="Scan.vi" Type="VI" URL="../Public/Action-Status/Scan.vi"/>
			<Item Name="Scan (To).vi" Type="VI" URL="../Public/Action-Status/Scan (To).vi"/>
			<Item Name="Scan (Up).vi" Type="VI" URL="../Public/Action-Status/Scan (Up).vi"/>
			<Item Name="Scan (Down).vi" Type="VI" URL="../Public/Action-Status/Scan (Down).vi"/>
			<Item Name="Scan (Slew Up).vi" Type="VI" URL="../Public/Action-Status/Scan (Slew Up).vi"/>
			<Item Name="Scan (Slew Down).vi" Type="VI" URL="../Public/Action-Status/Scan (Slew Down).vi"/>
			<Item Name="Step Up.vi" Type="VI" URL="../Public/Action-Status/Step Up.vi"/>
			<Item Name="Step Down.vi" Type="VI" URL="../Public/Action-Status/Step Down.vi"/>
		</Item>
		<Item Name="Configure" Type="Folder">
			<Item Name="Configure.mnu" Type="Document" URL="/&lt;instrlib&gt;/Digikrom DK24x/Public/Configure/Configure.mnu"/>
			<Item Name="Set Filter.vi" Type="VI" URL="../Public/Configure/Set Filter.vi"/>
			<Item Name="Set Grating.vi" Type="VI" URL="../Public/Configure/Set Grating.vi"/>
			<Item Name="Set Scan Speed.vi" Type="VI" URL="../Public/Configure/Set Scan Speed.vi"/>
			<Item Name="Adjust Slit.vi" Type="VI" URL="../Public/Configure/Adjust Slit.vi"/>
			<Item Name="Adjust Slit (1).vi" Type="VI" URL="../Public/Configure/Adjust Slit (1).vi"/>
			<Item Name="Adjust Slit (2).vi" Type="VI" URL="../Public/Configure/Adjust Slit (2).vi"/>
			<Item Name="Adjust Slit (3).vi" Type="VI" URL="../Public/Configure/Adjust Slit (3).vi"/>
			<Item Name="Reset Grating.vi" Type="VI" URL="../Public/Configure/Reset Grating.vi"/>
			<Item Name="Reset Slit.vi" Type="VI" URL="../Public/Configure/Reset Slit.vi"/>
		</Item>
		<Item Name="Utility" Type="Folder">
			<Item Name="Calibration" Type="Folder">
				<Item Name="NovRAM Read.vi" Type="VI" URL="../Public/Utility/Calibration/NovRAM Read.vi"/>
				<Item Name="NovRAM Write.vi" Type="VI" URL="../Public/Utility/Calibration/NovRAM Write.vi"/>
				<Item Name="Calibrate Grating.vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Grating.vi"/>
				<Item Name="NovRAM Dump.vi" Type="VI" URL="../Public/Utility/Calibration/NovRAM Dump.vi"/>
				<Item Name="Calibrate Slit.vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Slit.vi"/>
				<Item Name="Calibrate Slit (1).vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Slit (1).vi"/>
				<Item Name="Calibrate Slit (2).vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Slit (2).vi"/>
				<Item Name="Calibrate Slit (3).vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Slit (3).vi"/>
				<Item Name="Calibrate Zero.vi" Type="VI" URL="../Public/Utility/Calibration/Calibrate Zero.vi"/>
			</Item>
			<Item Name="Utility.mnu" Type="Document" URL="/&lt;instrlib&gt;/Digikrom DK24x/Public/Utility/Utility.mnu"/>
			<Item Name="Model Query.vi" Type="VI" URL="../Public/Utility/Model Query.vi"/>
			<Item Name="Self-Test.vi" Type="VI" URL="../Public/Utility/Self-Test.vi"/>
			<Item Name="Serial Query.vi" Type="VI" URL="../Public/Utility/Serial Query.vi"/>
			<Item Name="Echo.vi" Type="VI" URL="../Public/Utility/Echo.vi"/>
			<Item Name="Revision Query.vi" Type="VI" URL="../Public/Utility/Revision Query.vi"/>
			<Item Name="Set CSR Mode.vi" Type="VI" URL="../Public/Utility/Set CSR Mode.vi"/>
			<Item Name="Clear.vi" Type="VI" URL="../Public/Utility/Clear.vi"/>
		</Item>
		<Item Name="VI Tree.vi" Type="VI" URL="../Public/VI Tree.vi"/>
		<Item Name="Initialize.vi" Type="VI" URL="../Public/Initialize.vi"/>
		<Item Name="Close.vi" Type="VI" URL="../Public/Close.vi"/>
		<Item Name="Example - Manual Control.vi" Type="VI" URL="../Public/Example - Manual Control.vi"/>
	</Item>
	<Item Name="Private" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">2</Property>
		<Item Name="Write.vi" Type="VI" URL="../Private/Write.vi"/>
		<Item Name="Read.vi" Type="VI" URL="../Private/Read.vi"/>
		<Item Name="Decode Error.vi" Type="VI" URL="../Private/Decode Error.vi"/>
		<Item Name="Check Error.vi" Type="VI" URL="../Private/Check Error.vi"/>
		<Item Name="Send Command.vi" Type="VI" URL="../Private/Send Command.vi"/>
		<Item Name="Scan Abort.vi" Type="VI" URL="../Private/Scan Abort.vi"/>
		<Item Name="Filter State.vi" Type="VI" URL="../Private/Filter State.vi"/>
		<Item Name="Flush.vi" Type="VI" URL="../Private/Flush.vi"/>
		<Item Name="Debug Log.vi" Type="VI" URL="../Private/Debug Log.vi"/>
		<Item Name="Default Instrument Setup.vi" Type="VI" URL="../Private/Default Instrument Setup.vi"/>
		<Item Name="Reset Wait.vi" Type="VI" URL="../Private/Reset Wait.vi"/>
		<Item Name="Unlock.vi" Type="VI" URL="../Private/Unlock.vi"/>
		<Item Name="Command.ctl" Type="VI" URL="../Private/Command.ctl"/>
	</Item>
</Library>
