<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="9008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="LabVIEW" Type="Folder" URL="..">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="Write To Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File.vi"/>
				<Item Name="Write To Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (DBL).vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="General Error Handler CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler CORE.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="Write To Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (I64).vi"/>
				<Item Name="Write To Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write To Spreadsheet File (string).vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Merge Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Merge Errors.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="DAQmx Read (Analog DBL 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog DBL 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read.vi"/>
				<Item Name="DAQmx Read (Analog 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Analog 1D DBL 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 1D DBL 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 2D Bool NChan 1Samp NLine).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 2D Bool NChan 1Samp NLine).vi"/>
				<Item Name="DAQmx Create Task.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/task.llb/DAQmx Create Task.vi"/>
				<Item Name="DAQmx Create Channel (AI-Voltage-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Voltage-Basic).vi"/>
				<Item Name="DAQmx Timing (Sample Clock).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Sample Clock).vi"/>
				<Item Name="DAQmx Create Virtual Channel.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Virtual Channel.vi"/>
				<Item Name="DAQmx Create Channel (AO-Voltage-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AO-Voltage-Basic).vi"/>
				<Item Name="DAQmx Create Channel (DI-Digital Input).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (DI-Digital Input).vi"/>
				<Item Name="DAQmx Create Channel (DO-Digital Output).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (DO-Digital Output).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Voltage-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Voltage-Basic).vi"/>
				<Item Name="DAQmx Timing.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing.vi"/>
				<Item Name="DAQmx Stop Task.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/task.llb/DAQmx Stop Task.vi"/>
				<Item Name="DAQmx Clear Task.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/task.llb/DAQmx Clear Task.vi"/>
				<Item Name="DAQmx Write (Digital Bool 1Line 1Point).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital Bool 1Line 1Point).vi"/>
				<Item Name="DAQmx Write.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write.vi"/>
				<Item Name="DAQmx Write (Analog DBL 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog DBL 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 1D Bool 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D Bool 1Chan 1Samp).vi"/>
				<Item Name="DTbl Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital Size.vi"/>
				<Item Name="DAQmx Write (Digital 2D Bool NChan 1Samp NLine).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 2D Bool NChan 1Samp NLine).vi"/>
				<Item Name="Obtain Semaphore Reference.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Obtain Semaphore Reference.vi"/>
				<Item Name="AddNamedSemaphorePrefix.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/AddNamedSemaphorePrefix.vi"/>
				<Item Name="GetNamedSemaphorePrefix.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/GetNamedSemaphorePrefix.vi"/>
				<Item Name="Validate Semaphore Size.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Validate Semaphore Size.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Semaphore RefNum" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Semaphore RefNum"/>
				<Item Name="Semaphore Refnum Core.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Semaphore Refnum Core.ctl"/>
				<Item Name="Acquire Semaphore.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Acquire Semaphore.vi"/>
				<Item Name="Release Semaphore.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Release Semaphore.vi"/>
				<Item Name="Not A Semaphore.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Not A Semaphore.vi"/>
				<Item Name="Release Semaphore Reference.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/Release Semaphore Reference.vi"/>
				<Item Name="RemoveNamedSemaphorePrefix.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/semaphor.llb/RemoveNamedSemaphorePrefix.vi"/>
				<Item Name="Get File Extension.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Get File Extension.vi"/>
				<Item Name="Serial Port Init.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/Serial Port Init.vi"/>
				<Item Name="Open Serial Driver.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_sersup.llb/Open Serial Driver.vi"/>
				<Item Name="serpConfig.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/serpConfig.vi"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="Bytes At Serial Port.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/Bytes At Serial Port.vi"/>
				<Item Name="Serial Port Read.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/Serial Port Read.vi"/>
				<Item Name="Serial Port Write.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/Serial Port Write.vi"/>
				<Item Name="Resize Panel.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Resize Panel.vi"/>
				<Item Name="Snd Play Wave File.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/Snd Play Wave File.vi"/>
				<Item Name="Snd Gen Error Call Chain.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/Snd Gen Error Call Chain.vi"/>
				<Item Name="Snd Read Wave File.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/Snd Read Wave File.vi"/>
				<Item Name="Sound Format.ctl" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/Sound Format.ctl"/>
				<Item Name="Snd Write Waveform.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/Snd Write Waveform.vi"/>
				<Item Name="SO Config.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/SO Config.vi"/>
				<Item Name="SO Write.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/SO Write.vi"/>
				<Item Name="SO Start.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/SO Start.vi"/>
				<Item Name="SO Wait.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/SO Wait.vi"/>
				<Item Name="SO Clear.vi" Type="VI" URL="/&lt;vilib&gt;/sound/lvsound.llb/SO Clear.vi"/>
				<Item Name="DAQmx Create Timing Source (Digital Edge using Counter).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Digital Edge using Counter).vi"/>
				<Item Name="DAQmx Create Timing Source.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source.vi"/>
				<Item Name="GPIB Status Boolean Array.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/GPIB Status Boolean Array.ctl"/>
				<Item Name="Write File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write File+ (string).vi"/>
				<Item Name="compatWriteText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatWriteText.vi"/>
				<Item Name="Read Characters From File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Characters From File.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="Write Characters To File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Characters To File.vi"/>
				<Item Name="Play Sound File.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Play Sound File.vi"/>
				<Item Name="_Get Sound Error From Return Value.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/_Get Sound Error From Return Value.vi"/>
				<Item Name="Sound Output Wait.vi" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Wait.vi"/>
				<Item Name="Sound Output Task ID.ctl" Type="VI" URL="/&lt;vilib&gt;/sound2/lvsound2.llb/Sound Output Task ID.ctl"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="DTbl Compress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Compress Digital.vi"/>
				<Item Name="Compress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Compress Digital.vi"/>
				<Item Name="DWDT Compress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Compress Digital.vi"/>
				<Item Name="compatOverwrite.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOverwrite.vi"/>
				<Item Name="DTbl Binary U8 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Binary U8 to Digital.vi"/>
				<Item Name="Binary to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Binary to Digital.vi"/>
				<Item Name="DWDT Binary U32 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Binary U32 to Digital.vi"/>
				<Item Name="DTbl Binary U32 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Binary U32 to Digital.vi"/>
				<Item Name="DWDT Binary U16 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Binary U16 to Digital.vi"/>
				<Item Name="DTbl Binary U16 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Binary U16 to Digital.vi"/>
				<Item Name="DWDT Binary U8 to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Binary U8 to Digital.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="VISA GPIB Control REN Mode.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA GPIB Control REN Mode.ctl"/>
				<Item Name="Timestamp Subtract.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/TSOps.llb/Timestamp Subtract.vi"/>
				<Item Name="DU64_U32SubtractWithBorrow.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/TSOps.llb/DU64_U32SubtractWithBorrow.vi"/>
				<Item Name="I128 Timestamp.ctl" Type="VI" URL="/&lt;vilib&gt;/Waveform/TSOps.llb/I128 Timestamp.ctl"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="subSigGeneratorBlock.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/subSigGeneratorBlock.vi"/>
				<Item Name="Nearest Frequency for Block.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalConfig.llb/Nearest Frequency for Block.vi"/>
				<Item Name="Nearest Freq in Int Cycles.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalConfig.llb/Nearest Freq in Int Cycles.vi"/>
				<Item Name="subInternalTiming.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/subInternalTiming.vi"/>
				<Item Name="subShouldUseDefSigName.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/subShouldUseDefSigName.vi"/>
				<Item Name="sub2ShouldUseDefSigName.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/sub2ShouldUseDefSigName.vi"/>
				<Item Name="subGetSignalName.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/subGetSignalName.vi"/>
				<Item Name="ex_GenAddAttribs.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/SimulateSignalBlock.llb/ex_GenAddAttribs.vi"/>
				<Item Name="ex_SetExpAttribsAndT0.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_SetExpAttribsAndT0.vi"/>
				<Item Name="Timestamp Add.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/TSOps.llb/Timestamp Add.vi"/>
				<Item Name="DU64_U32AddWithOverflow.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/TSOps.llb/DU64_U32AddWithOverflow.vi"/>
				<Item Name="ex_SetAllExpressAttribs.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_SetAllExpressAttribs.vi"/>
				<Item Name="ex_WaveformAttribs.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_WaveformAttribs.ctl"/>
				<Item Name="ex_WaveformAttribsPlus.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_WaveformAttribsPlus.ctl"/>
				<Item Name="Waveform Array To Dynamic.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Waveform Array To Dynamic.vi"/>
				<Item Name="Dynamic To Waveform Array.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Dynamic To Waveform Array.vi"/>
				<Item Name="Create ActiveX Event Queue.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Create ActiveX Event Queue.vi"/>
				<Item Name="Create Error Clust.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Create Error Clust.vi"/>
				<Item Name="Wait types.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Wait types.ctl"/>
				<Item Name="Wait On ActiveX Event.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/Wait On ActiveX Event.vi"/>
				<Item Name="EventData.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/EventData.ctl"/>
				<Item Name="OccFireType.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/ax-events.llb/OccFireType.ctl"/>
				<Item Name="Query Registry Key Info.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Query Registry Key Info.vi"/>
				<Item Name="Enum Registry Keys.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Enum Registry Keys.vi"/>
				<Item Name="Flatten Pixmap(6_1).vi" Type="VI" URL="/&lt;vilib&gt;/picture/pixmap.llb/Flatten Pixmap(6_1).vi"/>
				<Item Name="Flatten Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pixmap.llb/Flatten Pixmap.vi"/>
				<Item Name="imagedata.ctl" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/imagedata.ctl"/>
				<Item Name="Write BMP File(6_1).vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Write BMP File(6_1).vi"/>
				<Item Name="Write BMP File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Write BMP File.vi"/>
				<Item Name="Write BMP Data.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Write BMP Data.vi"/>
				<Item Name="Write BMP Data To Buffer.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Write BMP Data To Buffer.vi"/>
				<Item Name="Calc Long Word Padded Width.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Calc Long Word Padded Width.vi"/>
				<Item Name="Flip and Pad for Picture Control.vi" Type="VI" URL="/&lt;vilib&gt;/picture/bmp.llb/Flip and Pad for Picture Control.vi"/>
				<Item Name="Digital to Binary.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Digital to Binary.vi"/>
				<Item Name="DWDT Digital to Binary U32.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U32.vi"/>
				<Item Name="DTbl Digital to Binary U32.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U32.vi"/>
				<Item Name="Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Digital Size.vi"/>
				<Item Name="DWDT Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital Size.vi"/>
				<Item Name="DWDT Digital to Binary U16.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U16.vi"/>
				<Item Name="DTbl Digital to Binary U16.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U16.vi"/>
				<Item Name="DWDT Digital to Binary U8.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U8.vi"/>
				<Item Name="DTbl Digital to Binary U8.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U8.vi"/>
				<Item Name="Get LV Class Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/LVClass/Get LV Class Path.vi"/>
				<Item Name="VISA Lock Async.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Lock Async.vi"/>
				<Item Name="Dflt Data Dir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Dflt Data Dir.vi"/>
				<Item Name="Open Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Open Registry Key.vi"/>
				<Item Name="STR_ASCII-Unicode.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/STR_ASCII-Unicode.vi"/>
				<Item Name="Registry WinErr-LVErr.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry WinErr-LVErr.vi"/>
				<Item Name="Registry Handle Master.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Handle Master.vi"/>
				<Item Name="Registry refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry refnum.ctl"/>
				<Item Name="Registry SAM.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry SAM.ctl"/>
				<Item Name="Registry RtKey.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry RtKey.ctl"/>
				<Item Name="Read Registry Value Simple STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple STR.vi"/>
				<Item Name="Read Registry Value STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value STR.vi"/>
				<Item Name="Registry Simplify Data Type.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Simplify Data Type.vi"/>
				<Item Name="Read Registry Value.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value.vi"/>
				<Item Name="Read Registry Value DWORD.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value DWORD.vi"/>
				<Item Name="Read Registry Value Simple.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple.vi"/>
				<Item Name="Read Registry Value Simple U32.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple U32.vi"/>
				<Item Name="Write to XML File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File.vi"/>
				<Item Name="Write to XML File(string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File(string).vi"/>
				<Item Name="Write to XML File(array).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File(array).vi"/>
				<Item Name="Read From XML File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File.vi"/>
				<Item Name="Read From XML File(array).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File(array).vi"/>
				<Item Name="ParseXMLFragments.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/ParseXMLFragments.vi"/>
				<Item Name="FindFirstTag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindFirstTag.vi"/>
				<Item Name="FindEmptyElement.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindEmptyElement.vi"/>
				<Item Name="FindElement.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindElement.vi"/>
				<Item Name="FindMatchingCloseTag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindMatchingCloseTag.vi"/>
				<Item Name="FindCloseTagByName.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindCloseTagByName.vi"/>
				<Item Name="FindElementStartByName.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindElementStartByName.vi"/>
				<Item Name="Read From XML File(string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File(string).vi"/>
				<Item Name="NI_Gmath.lvlib" Type="Library" URL="/&lt;vilib&gt;/gmath/NI_Gmath.lvlib"/>
				<Item Name="Path To Command Line String.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Path To Command Line String.vi"/>
				<Item Name="PathToUNIXPathString.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/CFURL.llb/PathToUNIXPathString.vi"/>
				<Item Name="Registry View.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry View.ctl"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="Close Serial Driver.vi" Type="VI" URL="/&lt;vilib&gt;/Instr/serial.llb/Close Serial Driver.vi"/>
				<Item Name="Release Instrument.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Release Instrument.vi"/>
				<Item Name="viRef buffer.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/viRef buffer.vi"/>
				<Item Name="Preload Instrument.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Preload Instrument.vi"/>
				<Item Name="Run Instrument.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Run Instrument.vi"/>
				<Item Name="Call Instrument.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Call Instrument.vi"/>
				<Item Name="VIParam.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/VIParam.ctl"/>
				<Item Name="Convert Type Descriptor and Flat Data.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/victl.llb/Convert Type Descriptor and Flat Data.vi"/>
				<Item Name="NI_MABase.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MABase.lvlib"/>
				<Item Name="DAQmx Write (Analog 1D DBL 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 1D DBL 1Chan NSamp).vi"/>
				<Item Name="DAQmx Fill In Error Info.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/miscellaneous.llb/DAQmx Fill In Error Info.vi"/>
				<Item Name="DAQmx Write (Analog 1D DBL NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 1D DBL NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Analog 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Analog 2D DBL NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 2D DBL NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Analog Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Analog Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 2D U32 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 2D U32 NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 2D U8 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 2D U8 NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U32 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U32 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U8 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U8 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital Wfm 1Chan NSamp).vi"/>
				<Item Name="DWDT Uncompress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Uncompress Digital.vi"/>
				<Item Name="DTbl Uncompress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Uncompress Digital.vi"/>
				<Item Name="DAQmx Write (Raw 1D I16).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D I16).vi"/>
				<Item Name="DAQmx Write (Raw 1D I32).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D I32).vi"/>
				<Item Name="DAQmx Write (Raw 1D I8).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D I8).vi"/>
				<Item Name="DAQmx Write (Raw 1D U16).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D U16).vi"/>
				<Item Name="DAQmx Write (Raw 1D U32).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D U32).vi"/>
				<Item Name="DAQmx Write (Raw 1D U8).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Raw 1D U8).vi"/>
				<Item Name="DAQmx Write (Digital 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Analog 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital U8 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital U8 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital U32 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital U32 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U32 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U32 NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U8 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U8 NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 1D Bool NChan 1Samp 1Line).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D Bool NChan 1Samp 1Line).vi"/>
				<Item Name="DAQmx Write (Analog 2D I16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 2D I16 NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Analog 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Counter Frequency 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter Frequency 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Counter Ticks 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter Ticks 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Counter Time 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter Time 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Counter 1D Frequency NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1D Frequency NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Counter 1D Time NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1D Time NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Counter 1DTicks NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1DTicks NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Analog 2D I32 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Analog 2D I32 NChan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital U16 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital U16 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U16 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U16 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Digital 1D U16 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 1D U16 NChan 1Samp).vi"/>
				<Item Name="DAQmx Write (Digital 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Digital 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQmx Rollback Channel If Error.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Rollback Channel If Error.vi"/>
				<Item Name="DAQmx Create AI Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create AI Channel (sub).vi"/>
				<Item Name="DAQmx Create Channel (AI-Voltage-Custom with Excitation).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Voltage-Custom with Excitation).vi"/>
				<Item Name="DAQmx Create Channel (AI-Resistance).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Resistance).vi"/>
				<Item Name="DAQmx Create Channel (AI-Temperature-Thermocouple).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Temperature-Thermocouple).vi"/>
				<Item Name="DAQmx Set CJC Parameters (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Set CJC Parameters (sub).vi"/>
				<Item Name="DAQmx Create Channel (AI-Temperature-RTD).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Temperature-RTD).vi"/>
				<Item Name="DAQmx Create Channel (AI-Temperature-Thermistor-Iex).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Temperature-Thermistor-Iex).vi"/>
				<Item Name="DAQmx Create Channel (AI-Temperature-Thermistor-Vex).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Temperature-Thermistor-Vex).vi"/>
				<Item Name="DAQmx Create AO Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create AO Channel (sub).vi"/>
				<Item Name="DAQmx Create Channel (AO-FuncGen).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AO-FuncGen).vi"/>
				<Item Name="DAQmx Create DI Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create DI Channel (sub).vi"/>
				<Item Name="DAQmx Create DO Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create DO Channel (sub).vi"/>
				<Item Name="DAQmx Create Channel (CI-Frequency).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Frequency).vi"/>
				<Item Name="DAQmx Create CI Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create CI Channel (sub).vi"/>
				<Item Name="DAQmx Create Channel (CI-Period).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Period).vi"/>
				<Item Name="DAQmx Create Channel (CI-Count Edges).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Count Edges).vi"/>
				<Item Name="DAQmx Create Channel (CI-Pulse Width).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Pulse Width).vi"/>
				<Item Name="DAQmx Create Channel (CI-Semi Period).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Semi Period).vi"/>
				<Item Name="DAQmx Create Channel (AI-Current-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Current-Basic).vi"/>
				<Item Name="DAQmx Create Channel (AI-Strain-Strain Gage).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Strain-Strain Gage).vi"/>
				<Item Name="DAQmx Create Channel (AI-Temperature-Built-in Sensor).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Temperature-Built-in Sensor).vi"/>
				<Item Name="DAQmx Create Channel (AI-Frequency-Voltage).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Frequency-Voltage).vi"/>
				<Item Name="DAQmx Create Channel (CO-Pulse Generation-Frequency).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CO-Pulse Generation-Frequency).vi"/>
				<Item Name="DAQmx Create CO Channel (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create CO Channel (sub).vi"/>
				<Item Name="DAQmx Create Channel (CO-Pulse Generation-Time).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CO-Pulse Generation-Time).vi"/>
				<Item Name="DAQmx Create Channel (CO-Pulse Generation-Ticks).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CO-Pulse Generation-Ticks).vi"/>
				<Item Name="DAQmx Create Channel (AI-Position-LVDT).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Position-LVDT).vi"/>
				<Item Name="DAQmx Create Channel (AI-Position-RVDT).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Position-RVDT).vi"/>
				<Item Name="DAQmx Create Channel (CI-Two Edge Separation).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Two Edge Separation).vi"/>
				<Item Name="DAQmx Create Channel (AI-Acceleration-Accelerometer).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Acceleration-Accelerometer).vi"/>
				<Item Name="DAQmx Create Channel (CI-Position-Angular Encoder).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Position-Angular Encoder).vi"/>
				<Item Name="DAQmx Create Channel (CI-Position-Linear Encoder).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Position-Linear Encoder).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Acceleration-Accelerometer).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Acceleration-Accelerometer).vi"/>
				<Item Name="DAQmx Create AI Channel TEDS(sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create AI Channel TEDS(sub).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Current-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Current-Basic).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Position-LVDT).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Position-LVDT).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Position-RVDT).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Position-RVDT).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Resistance).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Resistance).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Strain-Strain Gage).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Strain-Strain Gage).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Temperature-RTD).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Temperature-RTD).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Temperature-Thermistor-Iex).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Temperature-Thermistor-Iex).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Temperature-Thermistor-Vex).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Temperature-Thermistor-Vex).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Voltage-Custom with Excitation).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Voltage-Custom with Excitation).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Temperature-Thermocouple).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Temperature-Thermocouple).vi"/>
				<Item Name="DAQmx Create Channel (AI-Sound Pressure-Microphone).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Sound Pressure-Microphone).vi"/>
				<Item Name="DAQmx Create Channel (TEDS-AI-Sound Pressure-Microphone).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (TEDS-AI-Sound Pressure-Microphone).vi"/>
				<Item Name="DAQmx Create Channel (CI-GPS Timestamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-GPS Timestamp).vi"/>
				<Item Name="DAQmx Create Channel (AO-Current-Basic).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AO-Current-Basic).vi"/>
				<Item Name="DAQmx Create Channel (AI-Voltage-RMS).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Voltage-RMS).vi"/>
				<Item Name="DAQmx Create Channel (AI-Current-RMS).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Current-RMS).vi"/>
				<Item Name="DAQmx Create Channel (AI-Position-EddyCurrentProxProbe).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (AI-Position-EddyCurrentProxProbe).vi"/>
				<Item Name="DAQmx Read (Analog 1D DBL NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 1D DBL NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Analog 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Analog 2D DBL NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 2D DBL NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Analog Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Analog Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 1D Bool 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D Bool 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U32 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U32 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U8 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U8 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 2D U32 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 2D U32 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 2D U8 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 2D U8 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital Bool 1Line 1Point).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital Bool 1Line 1Point).vi"/>
				<Item Name="DAQmx Read (Digital Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Raw 1D I16).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D I16).vi"/>
				<Item Name="DAQmx Read (Raw 1D I32).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D I32).vi"/>
				<Item Name="DAQmx Read (Raw 1D I8).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D I8).vi"/>
				<Item Name="DAQmx Read (Raw 1D U16).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D U16).vi"/>
				<Item Name="DAQmx Read (Raw 1D U32).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D U32).vi"/>
				<Item Name="DAQmx Read (Raw 1D U8).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Raw 1D U8).vi"/>
				<Item Name="DAQmx Read (Digital 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Counter 1D DBL 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter 1D DBL 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Counter DBL 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter DBL 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Counter U32 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter U32 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Counter 1D U32 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter 1D U32 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U8 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U8 NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U32 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U32 NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital U8 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital U8 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital U32 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital U32 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 1D Bool NChan 1Samp 1Line).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D Bool NChan 1Samp 1Line).vi"/>
				<Item Name="DAQmx Read (Analog 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Analog 2D I16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 2D I16 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Analog 2D I32 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 2D I32 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Analog 2D U32 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Analog 2D U32 NChan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital U16 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital U16 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U16 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U16 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Digital 1D U16 NChan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 1D U16 NChan 1Samp).vi"/>
				<Item Name="DAQmx Read (Digital 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Digital 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQmx Timing (Handshaking).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Handshaking).vi"/>
				<Item Name="DAQmx Timing (Implicit).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Implicit).vi"/>
				<Item Name="DAQmx Timing (Use Waveform).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Use Waveform).vi"/>
				<Item Name="DAQmx Timing (Change Detection).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Change Detection).vi"/>
				<Item Name="DAQmx Timing (Burst Import Clock).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Burst Import Clock).vi"/>
				<Item Name="DAQmx Timing (Burst Export Clock).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Burst Export Clock).vi"/>
				<Item Name="DAQmx Timing (Pipelined Sample Clock).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/timing.llb/DAQmx Timing (Pipelined Sample Clock).vi"/>
				<Item Name="DAQmx Create Timing Source (Frequency).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Frequency).vi"/>
				<Item Name="DAQmx Create Timing Source (Frequency_sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Frequency_sub).vi"/>
				<Item Name="DAQmx Create Timing Source (sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (sub).vi"/>
				<Item Name="DAQmx Create Timing Source (Digital Edge using Counter_sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Digital Edge using Counter_sub).vi"/>
				<Item Name="DAQmx Create Timing Source (Signal From Task).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Signal From Task).vi"/>
				<Item Name="DAQmx Create Timing Source (SignalFromTask_sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (SignalFromTask_sub).vi"/>
				<Item Name="DAQmx Create Timing Source (Digital Change Detection).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Digital Change Detection).vi"/>
				<Item Name="DAQmx Create Timing Source (Digital Change Detection_sub).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Digital Change Detection_sub).vi"/>
				<Item Name="DAQmx Create Timing Source (Control Loop From Task).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (Control Loop From Task).vi"/>
				<Item Name="DAQmx Create Timing Source (sub2).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/timing.llb/DAQmx Create Timing Source (sub2).vi"/>
				<Item Name="NI_Matrix.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/Matrix/NI_Matrix.lvlib"/>
				<Item Name="DAQmx Read (Counter 1D Pulse Freq 1 Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter 1D Pulse Freq 1 Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Counter 1D Pulse Ticks 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter 1D Pulse Ticks 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Counter 1D Pulse Time 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter 1D Pulse Time 1Chan NSamp).vi"/>
				<Item Name="DAQmx Read (Counter Pulse Freq 1 Chan 1 Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter Pulse Freq 1 Chan 1 Samp).vi"/>
				<Item Name="DAQmx Read (Counter Pulse Ticks 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter Pulse Ticks 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Read (Counter Pulse Time 1Chan 1Samp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/read.llb/DAQmx Read (Counter Pulse Time 1Chan 1Samp).vi"/>
				<Item Name="DAQmx Create Channel (CI-Pulse Freq).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Pulse Freq).vi"/>
				<Item Name="DAQmx Create Channel (CI-Pulse Time).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Pulse Time).vi"/>
				<Item Name="DAQmx Create Channel (CI-Pulse Ticks).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/create/channels.llb/DAQmx Create Channel (CI-Pulse Ticks).vi"/>
				<Item Name="Read From Spreadsheet File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File.vi"/>
				<Item Name="Read From Spreadsheet File (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (DBL).vi"/>
				<Item Name="Read Lines From File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File.vi"/>
				<Item Name="Read From Spreadsheet File (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (I64).vi"/>
				<Item Name="Read From Spreadsheet File (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read From Spreadsheet File (string).vi"/>
				<Item Name="DAQmx Write (Counter 1D Frequency 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1D Frequency 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Counter 1D Ticks 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1D Ticks 1Chan NSamp).vi"/>
				<Item Name="DAQmx Write (Counter 1D Time 1Chan NSamp).vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/write.llb/DAQmx Write (Counter 1D Time 1Chan NSamp).vi"/>
				<Item Name="Get Project Library Version.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/Get Project Library Version.vi"/>
				<Item Name="ex_Modify Signal Name.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_Modify Signal Name.vi"/>
				<Item Name="math.ctl" Type="VI" URL="/&lt;vilib&gt;/express/express shared/math.ctl"/>
				<Item Name="ex_Math.vi" Type="VI" URL="/&lt;vilib&gt;/express/express arith-compare/TimeDomainMathBlock.llb/ex_Math.vi"/>
				<Item Name="DAQmx Control Task.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/configure/task.llb/DAQmx Control Task.vi"/>
				<Item Name="sub Waveform Array To Dynamic.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/miscellaneous.llb/sub Waveform Array To Dynamic.vi"/>
				<Item Name="Convert 1DWfm to DDT.vi" Type="VI" URL="/&lt;vilib&gt;/DAQmx/miscellaneous.llb/Convert 1DWfm to DDT.vi"/>
				<Item Name="subBuildXYGraph.vi" Type="VI" URL="/&lt;vilib&gt;/express/express controls/BuildXYGraphBlock.llb/subBuildXYGraph.vi"/>
				<Item Name="NI_MAPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/measure/NI_MAPro.lvlib"/>
				<Item Name="ex_GetAllExpressAttribs.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/ex_GetAllExpressAttribs.vi"/>
				<Item Name="Express Waveform Components.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Express Waveform Components.vi"/>
				<Item Name="ex_SmoothingDesign.vi" Type="VI" URL="/&lt;vilib&gt;/express/express analysis/FilterBlock.llb/ex_SmoothingDesign.vi"/>
				<Item Name="Check for Equality.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/WDTOps.llb/Check for Equality.vi"/>
				<Item Name="ex_Modify Signals Names.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_Modify Signals Names.vi"/>
				<Item Name="subFilter.vi" Type="VI" URL="/&lt;vilib&gt;/express/express analysis/FilterBlock.llb/subFilter.vi"/>
				<Item Name="NI_XML.lvlib" Type="Library" URL="/&lt;vilib&gt;/xml/NI_XML.lvlib"/>
				<Item Name="NIMS_And Generic Elements.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_And Generic Elements.vi"/>
				<Item Name="NIMS_Check Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_Check Index.vi"/>
				<Item Name="NIMS_Grow Vector.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Grow Vector.vi"/>
				<Item Name="NIMS_Replace - Get Dims Poly.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims Poly.vi"/>
				<Item Name="NIMS_Get Elements - RV(_).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - RV(_).vi"/>
				<Item Name="NIMS_num_to_str.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str.vi"/>
			</Item>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nilvaiu.dll" Type="Document" URL="nilvaiu.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 2009/resource/lvanlys.dll"/>
			<Item Name="lvsound.dll" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 2009/resource/lvsound.dll"/>
			<Item Name="lvsound2.dll" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 2009/resource/lvsound2.dll"/>
			<Item Name="wlmData.dll" Type="Document" URL="../../WINDOWS/system32/wlmData.dll"/>
			<Item Name="DOMUserDefRef.dll" Type="Document" URL="DOMUserDefRef.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="wlmData.dll" Type="Document" URL="../../Program Files/HighFinesse/Wavelength Meter WS5 399/Com-Test/wlmData.dll"/>
			<Item Name="visarc" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 2009/resource/visarc"/>
			<Item Name="lvanlys.dll" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 6.1/resource/lvanlys.dll"/>
			<Item Name="HP4192A Measure.vi" Type="VI" URL="../Instruments/HP4192A Impedance Analyzer/Program Archive/ImpedanceDataCollection.llb/HP4192A Measure.vi"/>
			<Item Name="HP4192A Sweep.vi" Type="VI" URL="../Instruments/HP4192A Impedance Analyzer/Program Archive/ImpedanceDataCollection.llb/HP4192A Sweep.vi"/>
			<Item Name="cn8202temp_controller.vi" Type="VI" URL="../Instruments/HP4192A Impedance Analyzer/ImpedanceDataCollection.llb/cn8202temp_controller.vi"/>
			<Item Name="read gain subvi (used in CP).vi" Type="VI" URL="../Instruments/Microwave Amplifier/Original VIs/read gain subvi (used in CP).vi"/>
			<Item Name="set gain button.vi" Type="VI" URL="../Instruments/Microwave Amplifier/Original VIs/set gain button.vi"/>
			<Item Name="NIMS_Get Row Vector - Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_Get Row Vector - Matrix.vi"/>
			<Item Name="error.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Functions/Error Handling/error.ctl"/>
			<Item Name="Translate Error.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Functions/Error Handling/Translate Error.vi"/>
			<Item Name="NIMS_Already Translated.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ErrorHandling/NIMS_Already Translated.vi"/>
			<Item Name="Create Error.vi" Type="VI" URL="/&lt;vilib&gt;/imathl/engines/lvmath/Functions/Error Handling/Create Error.vi"/>
			<Item Name="NIMS_Is Row Vector - Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_Is Row Vector - Matrix.vi"/>
			<Item Name="NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466.lvgen/NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466_000.vi"/>
			<Item Name="NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D.lvgen/NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D_000.vi"/>
			<Item Name="NIMS_Get Row Vector_w Error - Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_Get Row Vector_w Error - Matrix.vi"/>
			<Item Name="NIMS_string_Format Under No Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under No Specifier.vi"/>
			<Item Name="NIMS_string_Pad Zero Ahead Under Precision.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Pad Zero Ahead Under Precision.vi"/>
			<Item Name="NIMS_string_Convert Decimal Symbol.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Convert Decimal Symbol.vi"/>
			<Item Name="NIMS_string_Convert Exp String.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Convert Exp String.vi"/>
			<Item Name="NIMS_string_Truncate String to Fit Width.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Truncate String to Fit Width.vi"/>
			<Item Name="NIMS_string_Pad Decimal Point.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Pad Decimal Point.vi"/>
			<Item Name="NIMS_string_Format Under Exp Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Exp Specifier.vi"/>
			<Item Name="NIMS_string_Format Under Decimal Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Decimal Specifier.vi"/>
			<Item Name="NIMS_string_Pad Zero Ahead Under Sharp Flag.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Pad Zero Ahead Under Sharp Flag.vi"/>
			<Item Name="NIMS_string_Format Under Hex Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Hex Specifier.vi"/>
			<Item Name="NIMS_string_Format Under Unsigned Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Unsigned Specifier.vi"/>
			<Item Name="NIMS_string_Format Under String Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under String Specifier.vi"/>
			<Item Name="NIMS_string_Format Under Octal Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Octal Specifier.vi"/>
			<Item Name="NIMS_string_Format Under G Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under G Specifier.vi"/>
			<Item Name="NIMS_string_Format Under Char Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Under Char Specifier.vi"/>
			<Item Name="NIMS_string_Format Into String (1D-DBL).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Format Into String (1D-DBL).vi"/>
			<Item Name="NIMS_string_Extract Conversion Specifier.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Extract Conversion Specifier.vi"/>
			<Item Name="NIMS_string_Validate Specifier String.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Validate Specifier String.vi"/>
			<Item Name="NIMS_string_Convert Specifier String.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Convert Specifier String.vi"/>
			<Item Name="NIMS_string_Split Format String.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Split Format String.vi"/>
			<Item Name="NIMS_string_Write Formatted Data to String (1D-DBL).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Write Formatted Data to String (1D-DBL).vi"/>
			<Item Name="NIMS_sprintf(Str,RM).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/sprintf/NIMS_sprintf(Str,RM).vi"/>
			<Item Name="NIMS_Range_Compute_Iterations.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/RangeToken/NIMS_Range_Compute_Iterations.vi"/>
			<Item Name="NIMS_Replace - Range3.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/RangeToken/NIMS_Replace - Range3.ctl"/>
			<Item Name="NIMS_Range_Compute_Iterations_E8D80E2E2826472C92413183A93F3170_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Range_Compute_Iterations_E8D80E2E2826472C92413183A93F3170.lvgen/NIMS_Range_Compute_Iterations_E8D80E2E2826472C92413183A93F3170_000.vi"/>
			<Item Name="NIMS_M_Check_R3_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_M_Check_R3_Index.vi"/>
			<Item Name="NIMS_Replace - Range2.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/RangeToken/NIMS_Replace - Range2.ctl"/>
			<Item Name="NIMS_M_Check_R2_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_M_Check_R2_Index.vi"/>
			<Item Name="NIMS_V_Check_R3_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_V_Check_R3_Index.vi"/>
			<Item Name="NIMS_S_Check_R2_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_S_Check_R2_Index.vi"/>
			<Item Name="NIMS_S_Check_R3_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_S_Check_R3_Index.vi"/>
			<Item Name="NIMS_V_Check_R2_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_V_Check_R2_Index.vi"/>
			<Item Name="NIMS_S_Check_S_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_S_Check_S_Index.vi"/>
			<Item Name="NIMS_And Array Elements.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_And Array Elements.vi"/>
			<Item Name="NIMS_And Scalar Element.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_And Scalar Element.vi"/>
			<Item Name="NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819.lvgen/NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819_000.vi"/>
			<Item Name="NIMS_S_Check_VorM_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_S_Check_VorM_Index.vi"/>
			<Item Name="NIMS_V_Check_VorM_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_V_Check_VorM_Index.vi"/>
			<Item Name="NIMS_V_Check_S_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_V_Check_S_Index.vi"/>
			<Item Name="NIMS_M_Check_S_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_M_Check_S_Index.vi"/>
			<Item Name="NIMS_M_Check_VorM_Index.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Support/NIMS_M_Check_VorM_Index.vi"/>
			<Item Name="NIMS_M_Check_R3_Index_C9D4ADDBEED646AD8F1420F6AAAE4825_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_M_Check_R3_Index_C9D4ADDBEED646AD8F1420F6AAAE4825.lvgen/NIMS_M_Check_R3_Index_C9D4ADDBEED646AD8F1420F6AAAE4825_000.vi"/>
			<Item Name="NIMS_V_Check_R3_Index_3E100C0EDAA048D9B6E5EFFA67F36675_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_R3_Index_3E100C0EDAA048D9B6E5EFFA67F36675.lvgen/NIMS_V_Check_R3_Index_3E100C0EDAA048D9B6E5EFFA67F36675_000.vi"/>
			<Item Name="NIMS_M_Check_R2_Index_CB9C43F9BFC542B1A90793FD40220440_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_M_Check_R2_Index_CB9C43F9BFC542B1A90793FD40220440.lvgen/NIMS_M_Check_R2_Index_CB9C43F9BFC542B1A90793FD40220440_000.vi"/>
			<Item Name="NIMS_V_Check_VorM_Index_47BC16D128454DE8AE963953E2F83B3C_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_VorM_Index_47BC16D128454DE8AE963953E2F83B3C.lvgen/NIMS_V_Check_VorM_Index_47BC16D128454DE8AE963953E2F83B3C_000.vi"/>
			<Item Name="NIMS_V_Check_R2_Index_4B057989E21146F8B4BAB42F0D4DD1C6_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_R2_Index_4B057989E21146F8B4BAB42F0D4DD1C6.lvgen/NIMS_V_Check_R2_Index_4B057989E21146F8B4BAB42F0D4DD1C6_000.vi"/>
			<Item Name="NIMS_S_Check_R2_Index_1B5EC3458F474AA885F742AD621A4611_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_S_Check_R2_Index_1B5EC3458F474AA885F742AD621A4611.lvgen/NIMS_S_Check_R2_Index_1B5EC3458F474AA885F742AD621A4611_000.vi"/>
			<Item Name="NIMS_S_Check_R3_Index_E0F81B0D72364FE4BD8F3EA4C5F4523B_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_S_Check_R3_Index_E0F81B0D72364FE4BD8F3EA4C5F4523B.lvgen/NIMS_S_Check_R3_Index_E0F81B0D72364FE4BD8F3EA4C5F4523B_000.vi"/>
			<Item Name="NIMS_M_Check_VorM_Index_9C21C756A8C3411E921ADF397DBF7353_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_M_Check_VorM_Index_9C21C756A8C3411E921ADF397DBF7353.lvgen/NIMS_M_Check_VorM_Index_9C21C756A8C3411E921ADF397DBF7353_000.vi"/>
			<Item Name="NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763.lvgen/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_000.vi"/>
			<Item Name="NIMS_S_Check_VorM_Index_4CB38BA0E4B64BF395B80E6DF542F7A5_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_S_Check_VorM_Index_4CB38BA0E4B64BF395B80E6DF542F7A5.lvgen/NIMS_S_Check_VorM_Index_4CB38BA0E4B64BF395B80E6DF542F7A5_000.vi"/>
			<Item Name="NIMS_S_Check_S_Index_C71F322822DA45E5B6D556F1CF9C33A7_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_S_Check_S_Index_C71F322822DA45E5B6D556F1CF9C33A7.lvgen/NIMS_S_Check_S_Index_C71F322822DA45E5B6D556F1CF9C33A7_000.vi"/>
			<Item Name="NIMS_M_Check_S_Index_3BA02B2341064375AA8B00597C30672A_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_M_Check_S_Index_3BA02B2341064375AA8B00597C30672A.lvgen/NIMS_M_Check_S_Index_3BA02B2341064375AA8B00597C30672A_000.vi"/>
			<Item Name="NIMS_Replace - Check Linear.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Check Linear.vi"/>
			<Item Name="NIMS_Grow Vector - Vector.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Grow Vector - Vector.vi"/>
			<Item Name="NIMS_Grow Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Grow Matrix.vi"/>
			<Item Name="NIMS_Grow Matrix_50E491F312E64D308CF036A0202C8DE5_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Grow Matrix_50E491F312E64D308CF036A0202C8DE5.lvgen/NIMS_Grow Matrix_50E491F312E64D308CF036A0202C8DE5_000.vi"/>
			<Item Name="NIMS_Grow Vector - Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Grow Vector - Matrix.vi"/>
			<Item Name="NIMS_Grow Vector - Matrix_44476DC76A734164A055A2C9BF8D19D8_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Grow Vector - Matrix_44476DC76A734164A055A2C9BF8D19D8.lvgen/NIMS_Grow Vector - Matrix_44476DC76A734164A055A2C9BF8D19D8_000.vi"/>
			<Item Name="NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B.lvgen/NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B_000.vi"/>
			<Item Name="NIMS_Replace - Get Dims R3.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims R3.vi"/>
			<Item Name="NIMS_Replace - Get Dims R2.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims R2.vi"/>
			<Item Name="NIMS_Replace - Get Dims Scalar.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims Scalar.vi"/>
			<Item Name="NIMS_Replace - Get Dims Matrix.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims Matrix.vi"/>
			<Item Name="NIMS_Replace - Get Dims Vector.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Get Dims Vector.vi"/>
			<Item Name="NIMS_Replace - Get Dims Scalar_41576B403CBD4961B191FEEAB55E3777_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Get Dims Scalar_41576B403CBD4961B191FEEAB55E3777.lvgen/NIMS_Replace - Get Dims Scalar_41576B403CBD4961B191FEEAB55E3777_000.vi"/>
			<Item Name="NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC.lvgen/NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC_000.vi"/>
			<Item Name="NIMS_Replace - Get Dims Matrix_8A2A58E1ACB84C40AD7808B8A16677F5_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Get Dims Matrix_8A2A58E1ACB84C40AD7808B8A16677F5.lvgen/NIMS_Replace - Get Dims Matrix_8A2A58E1ACB84C40AD7808B8A16677F5_000.vi"/>
			<Item Name="NIMS_Replace - Resize Needed 1D.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Resize Needed 1D.vi"/>
			<Item Name="NIMS_Replace - Assignment Format.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Assignment Format.ctl"/>
			<Item Name="NIMS_Replace - Size Check _(_)=S.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - Size Check _(_)=S.vi"/>
			<Item Name="NIMS_Replace - V(S)=S.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ReplaceToken/NIMS_Replace - V(S)=S.vi"/>
			<Item Name="NIMS_Get Elements - V(R2).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - V(R2).vi"/>
			<Item Name="NIMS_Get Elements - V(S).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - V(S).vi"/>
			<Item Name="NIMS_Get Elements - V(V).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - V(V).vi"/>
			<Item Name="NIMS_Get Elements - RV(M).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - RV(M).vi"/>
			<Item Name="NIMS_Get Elements - V(R2)_6908C3CBC145405FBDD78690B7F1945D_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - V(R2)_6908C3CBC145405FBDD78690B7F1945D.lvgen/NIMS_Get Elements - V(R2)_6908C3CBC145405FBDD78690B7F1945D_000.vi"/>
			<Item Name="NIMS_Get Elements - RV(M)_26B0FF57CBD149438820B5A2EA9835D0_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - RV(M)_26B0FF57CBD149438820B5A2EA9835D0.lvgen/NIMS_Get Elements - RV(M)_26B0FF57CBD149438820B5A2EA9835D0_000.vi"/>
			<Item Name="NIMS_Get Elements - V(V)_D802331D13C1477FBB264FA67E6BC4E8_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - V(V)_D802331D13C1477FBB264FA67E6BC4E8.lvgen/NIMS_Get Elements - V(V)_D802331D13C1477FBB264FA67E6BC4E8_000.vi"/>
			<Item Name="NIMS_Get Elements - V(S)_C99A26467DB24FA3A79619D034B25FD8_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - V(S)_C99A26467DB24FA3A79619D034B25FD8.lvgen/NIMS_Get Elements - V(S)_C99A26467DB24FA3A79619D034B25FD8_000.vi"/>
			<Item Name="NIMS_Get Elements - RV(_) - Check.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/VariableToken/Read/NIMS_Get Elements - RV(_) - Check.vi"/>
			<Item Name="MC_CommandStatement_break.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/CommandStatement/MC_CommandStatement_break.vi"/>
			<Item Name="NIMS_Range_R2 - Integer.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/RangeToken/NIMS_Range_R2 - Integer.vi"/>
			<Item Name="NIMS_num_to_str_Left Trim String Array.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str_Left Trim String Array.vi"/>
			<Item Name="NIMS_num_to_str_Number to String Conversion (Format 2D-DBL).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str_Number to String Conversion (Format 2D-DBL).vi"/>
			<Item Name="NIMS_num_to_str_Number to String Conversion (Precision 2D-DBL).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str_Number to String Conversion (Precision 2D-DBL).vi"/>
			<Item Name="NIMS_string_Output Image Part.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctionSupport/string/NIMS_string_Output Image Part.vi"/>
			<Item Name="NIMS_num_to_str_Number to String Conversion (Precision 2D-CDB).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str_Number to String Conversion (Precision 2D-CDB).vi"/>
			<Item Name="MC_Global_Global.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Constants/MC_Global_Global.vi"/>
			<Item Name="NIMS_Complex Is Real.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeSupport/NIMS_Complex Is Real.vi"/>
			<Item Name="NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819.lvgen/NIMS_And Array Elements_631861BECDC54B97B1BA31611A562819_001.vi"/>
			<Item Name="NIMS_Complex Is Real_BFF64F03737C4AE8B5ABA3DF8972BF83_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Complex Is Real_BFF64F03737C4AE8B5ABA3DF8972BF83.lvgen/NIMS_Complex Is Real_BFF64F03737C4AE8B5ABA3DF8972BF83_000.vi"/>
			<Item Name="NIMS_num_to_str(GM,I32).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str(GM,I32).vi"/>
			<Item Name="NIMS_num_to_str(GM,I32)_5CE35A3ADCD84855A536B72EFB4499BC_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_num_to_str(GM,I32)_5CE35A3ADCD84855A536B72EFB4499BC.lvgen/NIMS_num_to_str(GM,I32)_5CE35A3ADCD84855A536B72EFB4499BC_000.vi"/>
			<Item Name="NIMS_num_to_str(GRowV,I32).vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/num_to_str/NIMS_num_to_str(GRowV,I32).vi"/>
			<Item Name="NIMS_CH_character datatype.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Plug In/_Char/NIMS_CH_character datatype.ctl"/>
			<Item Name="NIMS_CH_String to Character Array.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Plug In/_Char/NIMS_CH_String to Character Array.vi"/>
			<Item Name="NIMS_CH_Character 2D to String 1D.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Plug In/_Char/NIMS_CH_Character 2D to String 1D.vi"/>
			<Item Name="NIMS_strconcat.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/BuiltInFunctions/strconcat/NIMS_strconcat.vi"/>
			<Item Name="NIMS_CH_String CV to Character 2D.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Plug In/_Char/NIMS_CH_String CV to Character 2D.vi"/>
			<Item Name="MC_Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Functions/Error Handling/MC_Error Cluster From Error Code.vi"/>
			<Item Name="MergeErrorsWrapper.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Functions/Error Handling/MergeErrorsWrapper.vi"/>
			<Item Name="NIMS_CH_Character RV to String.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Plug In/_Char/NIMS_CH_Character RV to String.vi"/>
			<Item Name="NIMS_NodeEndStatement_Output.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/NodeEndStatement/NIMS_NodeEndStatement_Output.vi"/>
			<Item Name="MC_Version.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Parser/MC_Version.vi"/>
			<Item Name="MC_GlobalManager_Actions.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalManager/MC_GlobalManager_Actions.ctl"/>
			<Item Name="MC_Global_NamesAndDefaultValues.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Constants/MC_Global_NamesAndDefaultValues.vi"/>
			<Item Name="MC_Registration_Global.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Registration_Global.vi"/>
			<Item Name="MC_Registered_VIs_Global.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Registered_VIs_Global.vi"/>
			<Item Name="MC_Close_All_Registered_SubVI.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Close_All_Registered_SubVI.vi"/>
			<Item Name="MC_Register_Notification_Command.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Register_Notification_Command.ctl"/>
			<Item Name="MC_Register_Notification_Type.ctl" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Register_Notification_Type.ctl"/>
			<Item Name="MC_Get_Notification_Event.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Get_Notification_Event.vi"/>
			<Item Name="MC_Registered_VIs.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Registered_VIs.vi"/>
			<Item Name="MC_Register_VI_In_Memory.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalRegistration/MC_Register_VI_In_Memory.vi"/>
			<Item Name="MC_GlobalManager.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/Managers/GlobalManager/MC_GlobalManager.vi"/>
			<Item Name="Untranslate Error.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath/Functions/Error Handling/Untranslate Error.vi"/>
			<Item Name="NIMS_Finalize Error.vi" Type="VI" URL="/&lt;vilib&gt;/imath/engines/lvmath2/RunTimeEngine/ErrorHandling/NIMS_Finalize Error.vi"/>
			<Item Name="NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466.lvgen/NIMS_Get Row Vector - Matrix_73C62E6A23B74A87BA790FCBD9952466_001.vi"/>
			<Item Name="NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D.lvgen/NIMS_Is Row Vector - Matrix_4F6842B7C8CD4B4582A38F7F5CF8F00D_001.vi"/>
			<Item Name="NIMS_Get Row Vector_w Error - Matrix_31409C6EFA9547E0948162E6772A2E51_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Row Vector_w Error - Matrix_31409C6EFA9547E0948162E6772A2E51.lvgen/NIMS_Get Row Vector_w Error - Matrix_31409C6EFA9547E0948162E6772A2E51_000.vi"/>
			<Item Name="NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB.lvgen/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_000.vi"/>
			<Item Name="NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7.lvgen/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_000.vi"/>
			<Item Name="NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660.lvgen/NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660_000.vi"/>
			<Item Name="NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763.lvgen/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_001.vi"/>
			<Item Name="NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB.lvgen/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_001.vi"/>
			<Item Name="NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B.lvgen/NIMS_Grow Vector - Vector_0F7B9864027A49AB8CF222BDCEF5509B_001.vi"/>
			<Item Name="NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC.lvgen/NIMS_Replace - Get Dims Vector_0148CEE0D65143AD8EFB93349F5363FC_001.vi"/>
			<Item Name="NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7.lvgen/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_001.vi"/>
			<Item Name="NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_002.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763.lvgen/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_002.vi"/>
			<Item Name="NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_002.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB.lvgen/NIMS_Replace - Check Linear_3F5099154F904E698C6642037B8E50AB_002.vi"/>
			<Item Name="NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_002.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7.lvgen/NIMS_Replace - Size Check _(_)=S_C93E24300E2D4FA1B1057E3B3E42F8F7_002.vi"/>
			<Item Name="NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660.lvgen/NIMS_Replace - V(S)=S_1F711D65782C407D901BB57589CB2660_001.vi"/>
			<Item Name="NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC.lvgen/NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC_000.vi"/>
			<Item Name="NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_003.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763.lvgen/NIMS_V_Check_S_Index_9D00806FB30D483D9348023134CBD763_003.vi"/>
			<Item Name="NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC_001.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC.lvgen/NIMS_Get Elements - RV(_) - Check_30A5434E2C4242B098C990FE3FB371BC_001.vi"/>
			<Item Name="NIMS_Range_R2 - Integer_0F76E486ADCC4BDD96F616E7B4D02525_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_Range_R2 - Integer_0F76E486ADCC4BDD96F616E7B4D02525.lvgen/NIMS_Range_R2 - Integer_0F76E486ADCC4BDD96F616E7B4D02525_000.vi"/>
			<Item Name="NIMS_num_to_str(GRowV,I32)_52FF5984ECAE430BAA47FE5E9FC630B0_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_num_to_str(GRowV,I32)_52FF5984ECAE430BAA47FE5E9FC630B0.lvgen/NIMS_num_to_str(GRowV,I32)_52FF5984ECAE430BAA47FE5E9FC630B0_000.vi"/>
			<Item Name="NIMS_CH_String CV to Character 2D_A8457589C506491A87E921C75CEE07B3_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_CH_String CV to Character 2D_A8457589C506491A87E921C75CEE07B3.lvgen/NIMS_CH_String CV to Character 2D_A8457589C506491A87E921C75CEE07B3_000.vi"/>
			<Item Name="NIMS_NodeEndStatement_Output_53EC0D466D134D7ABD903AC30B43404B_000.vi" Type="VI" URL="/&lt;instcachedir&gt;/0/NIMS_NodeEndStatement_Output_53EC0D466D134D7ABD903AC30B43404B.lvgen/NIMS_NodeEndStatement_Output_53EC0D466D134D7ABD903AC30B43404B_000.vi"/>
			<Item Name="daqmx.rc" Type="Document" URL="../../Program Files/National Instruments/LabVIEW 2009/resource/objmgr/daqmx.rc"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Driver" Type="EXE">
				<Property Name="App_applicationGUID" Type="Str"></Property>
				<Property Name="App_applicationName" Type="Str">Driver.exe</Property>
				<Property Name="App_fileDescription" Type="Str">Driver</Property>
				<Property Name="App_INI_aliasGUID" Type="Str"></Property>
				<Property Name="App_INI_GUID" Type="Str"></Property>
				<Property Name="App_internalName" Type="Str">Driver</Property>
				<Property Name="App_productName" Type="Str">Driver</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Driver</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeTypedefs" Type="Bool">true</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Destination[0].destName" Type="Str">Driver.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Driver/Driver.exe</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Driver/data</Property>
				<Property Name="Destination[2].destName" Type="Str">Other stuff</Property>
				<Property Name="Destination[2].path" Type="Path">../builds/NI_AB_PROJECTNAME/Driver/Other stuff</Property>
				<Property Name="Destination[2].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="DestinationCount" Type="Int">3</Property>
				<Property Name="Source[0].itemID" Type="Str">{F4F1E64E-0ED7-4F97-82BE-EA4149CA8152}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/LabVIEW/Main/Driver.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
			</Item>
		</Item>
	</Item>
</Project>
