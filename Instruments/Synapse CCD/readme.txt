Jobin Yvon LABVIEW Drivers for Symphony detectors

******************
version	0.9.4.0   
These drivers are compatible with labview version 7.0 and higher.
Corrected Base Units Setup on Init

version	0.9.2.0   
These drivers are compatible with labview version 6.0.2 and higher.


The labview drivers use two different librairies :
-global_lib.llb
-user _lib.llb

The high level programs are in the user_lib librairie. It shows how to use each sub command of the instrument.
Each low level command can be found in the global_lib librairie.



history :
version 0.9.2.0
-Add the Multi Accumulation mode in the spectral acquisition.

version 0.9.1.0
-Add the Trigger In options in both acquisition mode.

version 0.9.0.2
-Change the HORIBA Jobin Yvon logo

version 0.9.0.1
-Add the reading of the gain and the ADC for the corresponding Detector. These parameters can now be selected correctly.
-Correct minor bugs with Image areas.
-Add the Acquisition time information.

version 0.8.2.5
-correct problem with image mode with new version of JY COM.

version 0.8.2.3
-correct the Y number of pixels
-chang the uniqueID selection.

version 0.8.2.2
-Fixe some language error in VI's.
-Remove acquisire.vi chich was not used.


version 0.8.1
-Fixe some problem with the readout of the registry, of the uniqueID ....
-The Y pixel is still not well read , but it has now the acces in the front windows to correct this value to the correct number of pixels.

version 0.8
-correct the readout of the image mode.
-correct bugs when after stopping the VIs.

version 0.7
-add the image mode. 
-correct some bug with the spectrale mode

version 0.5
-first version of the drivers labview. 
-only spectral mode are supported.
