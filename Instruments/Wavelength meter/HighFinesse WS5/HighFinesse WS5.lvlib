<?xml version='1.0' encoding='UTF-8'?>
<Library LVVersion="23008000">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Lib.Description" Type="Str">LabVIEW Plug and Play instrument driver for the HighFinesse WS5 wavelength meter; depends on a DLL shipped with the wavelength meter to function.  (The proprietary software that ships with it must be installed.)</Property>
	<Property Name="NI.Lib.HelpPath" Type="Str"></Property>
	<Property Name="NI.Lib.Icon" Type="Bin">)Q#!!!!!!!)!"1!&amp;!!!-!%!!!@````]!!!!"!!%!!!*G!!!*Q(C=\:1R&lt;BN"$%7`AA"+KRM%;N/*F3IDA+[A'RAMNEMFJ)J+O5L.*A@1&amp;81&amp;8E%)@!&amp;&gt;9@/'/T9=Q)[;'("BTF,3@H,)NT/DF=I_32]V8L.BPJK4P(L?C+`8YM,,BC;WK]WN_+!"UXS9\$(_-(_IS"=^C&lt;?J.&lt;XC:&lt;&gt;;6@3:_:.J;P.C`&amp;&lt;L6PT&amp;/!G;5PZ_0PX4XO0P]&lt;=&gt;PW,E\+]GP&lt;**MS,&amp;%Q`==;OH'R-^U2-^U2-^U1-^U!-^U!-^U"X&gt;U2X&gt;U2X&gt;U1X&gt;U!X&gt;U!X&gt;U'OA#VXI1G&gt;6EO:*I[2I5C"*"E8*2]+4]#1]#1_X3HA3HI1HY5FY3&amp;(#E`!E0!F0QM-U*4Q*4]+4]#1]F#K3L)%/4]*$?15]!5`!%`!%0,25Q"-!"-W#QE%2-"1%AR]"4]!4]0"4!5`!%`!%0!%0915]!5`!%`!%0%SJ69GC;1-&gt;(ML)Y8&amp;Y("[(R_'BN"Q?B]@B=8A=(NL*Y8&amp;Y(!CHI6-="$G4H!4HRO&amp;R?0C3Q_0Q/$Q/D].$K(&lt;);W5;42PI]"A]"I`"9`!90*31Q70Q'$Q'D]&amp;$72E]"I`"9`!90,33Q70Q'$Q'C.'5^D++'2/.*%-Q?,DKN&amp;DN5B3*V?B`T?GAKB^!^9/F@G$5$Y,["KNPH0K'K#_U_A+K,YT[![M`C$KA?G0VAOK*OP"ZRE`Y%4`A/XS,&lt;`!FPGB4`X0CZ8,2_8T7[843]8D5Y8$1&lt;L@4&gt;LP6:L02=LH59L&amp;Y@&amp;N^:EQW?XAPX9`\7@[Y_`\\ZO\L?00TW`C,\_;*X_^H?X*@Q[@XUFNY._K$RC?P?&gt;&lt;I$Z$K6H1!!!!!</Property>
	<Property Name="NI.Lib.SourceVersion" Type="Int">587235328</Property>
	<Property Name="NI.Lib.Version" Type="Str">1.0.0.0</Property>
	<Property Name="NI.SortType" Type="Int">3</Property>
	<Item Name="Examples" Type="Folder">
		<Item Name="Example - setup and read wavelength.vi" Type="VI" URL="../Examples/Example - setup and read wavelength.vi"/>
	</Item>
	<Item Name="Public" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">1</Property>
		<Item Name="Action-Status" Type="Folder">
			<Item Name="Check for Server.vi" Type="VI" URL="../Public/Action-Status/Check for Server.vi"/>
			<Item Name="Check for &apos;Set&apos; Errors.vi" Type="VI" URL="../Public/Action-Status/Check for &apos;Set&apos; Errors.vi"/>
			<Item Name="Check for &apos;wait&apos; errors.vi" Type="VI" URL="../Public/Action-Status/Check for &apos;wait&apos; errors.vi"/>
			<Item Name="Check for Wavelength or Frequency Errors.vi" Type="VI" URL="../Public/Action-Status/Check for Wavelength or Frequency Errors.vi"/>
		</Item>
		<Item Name="Configure" Type="Folder">
			<Item Name="Operation.vi" Type="VI" URL="../Public/Configure/Operation.vi"/>
			<Item Name="Set exposure mode.vi" Type="VI" URL="../Public/Configure/Set exposure mode.vi"/>
			<Item Name="Set pulse mode.vi" Type="VI" URL="../Public/Configure/Set pulse mode.vi"/>
		</Item>
		<Item Name="Data" Type="Folder">
			<Item Name="Get Wavelength or Frequency.vi" Type="VI" URL="../Public/Data/Get Wavelength or Frequency.vi"/>
		</Item>
		<Item Name="Utility" Type="Folder">
			<Item Name="Convert Unit.vi" Type="VI" URL="../Public/Utility/Convert Unit.vi"/>
			<Item Name="Revision Query.vi" Type="VI" URL="../Public/Utility/Revision Query.vi"/>
		</Item>
		<Item Name="Close.vi" Type="VI" URL="../Public/Close.vi"/>
		<Item Name="Initialize.vi" Type="VI" URL="../Public/Initialize.vi"/>
		<Item Name="VI Tree.vi" Type="VI" URL="../Public/VI Tree.vi"/>
	</Item>
	<Item Name="Private" Type="Folder">
		<Property Name="NI.LibItem.Scope" Type="Int">2</Property>
		<Item Name="Control.vi" Type="VI" URL="../Private/Control.vi"/>
		<Item Name="Read C declarations into text ring.vi" Type="VI" URL="../Private/Read C declarations into text ring.vi"/>
		<Item Name="Start and wait.vi" Type="VI" URL="../Public/Start and wait.vi"/>
		<Item Name="Wait event.vi" Type="VI" URL="../Private/Wait event.vi"/>
		<Item Name="Wait for server.vi" Type="VI" URL="../Private/Wait for server.vi"/>
	</Item>
	<Item Name="Variable typedefs" Type="Folder">
		<Item Name="Amplitude.ctl" Type="VI" URL="../Variable typedefs.llb/Amplitude.ctl"/>
		<Item Name="CMI.ctl" Type="VI" URL="../Variable typedefs.llb/CMI.ctl"/>
		<Item Name="Exposure range.ctl" Type="VI" URL="../Variable typedefs.llb/Exposure range.ctl"/>
		<Item Name="Exposure Mode.ctl" Type="VI" URL="../Variable Typedefs.llb/Exposure Mode.ctl"/>
		<Item Name="Get errors.ctl" Type="VI" URL="../Variable typedefs.llb/Get errors.ctl"/>
		<Item Name="Measurement control mode.ctl" Type="VI" URL="../Variable typedefs.llb/Measurement control mode.ctl"/>
		<Item Name="Measurement range.ctl" Type="VI" URL="../Variable typedefs.llb/Measurement range.ctl"/>
		<Item Name="Measurement triggering.ctl" Type="VI" URL="../Variable typedefs.llb/Measurement triggering.ctl"/>
		<Item Name="Mode.ctl" Type="VI" URL="../Variable typedefs.llb/Mode.ctl"/>
		<Item Name="Pattern and analysis.ctl" Type="VI" URL="../Variable typedefs.llb/Pattern and analysis.ctl"/>
		<Item Name="RFC.ctl" Type="VI" URL="../Variable typedefs.llb/RFC.ctl"/>
		<Item Name="Set errors.ctl" Type="VI" URL="../Variable typedefs.llb/Set errors.ctl"/>
		<Item Name="Source type.ctl" Type="VI" URL="../Variable typedefs.llb/Source type.ctl"/>
		<Item Name="Unit.ctl" Type="VI" URL="../Variable Typedefs.llb/Unit.ctl"/>
		<Item Name="WLM control mode.ctl" Type="VI" URL="../Variable Typedefs.llb/WLM control mode.ctl"/>
	</Item>
	<Item Name="Control typedefs" Type="Folder">
		<Item Name="Pulse Mode.ctl" Type="VI" URL="../Control typedefs.llb/Pulse Mode.ctl"/>
		<Item Name="Wait Return Values.ctl" Type="VI" URL="../Control typedefs.llb/Wait Return Values.ctl"/>
		<Item Name="Wait Event.ctl" Type="VI" URL="../Control typedefs.llb/Wait Event.ctl"/>
		<Item Name="Measurement Mode.ctl" Type="VI" URL="../Control typedefs.llb/Measurement Mode.ctl"/>
	</Item>
	<Item Name="HighFinesse WS5 Readme.html" Type="Document" URL="../HighFinesse WS5 Readme.html"/>
	<Item Name="Wait for WLM Event.vi" Type="VI" URL="../Private/Wait for WLM Event.vi">
		<Property Name="NI.LibItem.Scope" Type="Int">2</Property>
	</Item>
</Library>
