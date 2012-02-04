To collect temperature dependent impedance data, use ImpedanceDataCollection VI. Written by Brett Guisti combining cn8202temp_controller and HP4192A Example under one master VI, modified by Jon Cox. Changing the sub VIs inside the master library doesn't change the seperate cn8202temp_controller and HP4192A Example VIs on disk.

To collect temperature independent impedance data, use "Fastsweep."  Taken from National instruments website, modified by Brett Guisti, Jon Cox, and Brian Davis.


To control the furnace only, use cn8202temp_controller. written by Brett Guisti.


The ramptime VI plots Temp v. Time and Setpoint v. Time of temperature controller.  Used to trouble shoot controller when first built.  Written by Brett Guisti.


If you'd like to collect data in realtime (i.e., capacitance vs. time) then use the Realtime Data Gatherer, written by Brian Davis.