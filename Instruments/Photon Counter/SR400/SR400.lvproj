<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="9008000">
	<Property Name="Instrument Driver" Type="Str">True</Property>
	<Property Name="NI.Project.Description" Type="Str">This project is used by developers to edit API and example files for LabVIEW Plug and Play instrument drivers.</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="CCSymbols" Type="Str">OS,Win;CPU,x86;</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="SR400.lvlib" Type="Library" URL="../SR400.lvlib"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Merge Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Merge Errors.vi"/>
			</Item>
			<Item Name="GPIB Numbers.vi" Type="VI" URL="../../../../Global/GPIB Numbers.vi"/>
			<Item Name="GPIB Type Def.ctl" Type="VI" URL="../../../../Global/GPIB Type Def.ctl"/>
			<Item Name="count time to cycles.vi" Type="VI" URL="../../count time to cycles.vi"/>
			<Item Name="RealNumberCompare.vi" Type="VI" URL="../../../../Math Operations/RealNumberCompare.vi"/>
			<Item Name="round to one sig fig.vi" Type="VI" URL="../../../../Math Operations/round to one sig fig.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
