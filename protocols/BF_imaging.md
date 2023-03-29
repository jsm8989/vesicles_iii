Notes from Jurij meeting 1/11/21:
- Turn on
- Choose objectives etc
- Run temika
- Channel 1 = fluoro, channel 0 = BF
- Focus sample
- Close aperture diaphragm, filter diaphragm
- Move condenser until filter diagram is in focus, centre it
- Open it just outside field of view
- Play with illumination/camera/display settings
- Adjust aperture diaphragm as necessary
- Same for fluoro; just be sure to pick correct filter cube and check illumination settings again.
The above needs to be done every time (who knows what the previous set up was). Also be careful not to break the objective (ie touch the sample) - especially, eg, with the autofocus features. 

In general temika is very powerful!


Running Temika as a basic user:
- After logging into the PC (note it is different to your BSS account), open a terminal (for example by typing it in the start menu)
- In the terminal type `temika` and hit Enter
- The main temika windows should open. From here the most relevant ones, which can all be found in "View", are: Display Settings, Camera Settings, Illumination
- Remember in "Display Settings" to click at the pixel range section near the bottom, to expand the window further, and tick the "Automatic" box
- You can load our default imaging parameters by choosing File > Load Script and load the script at home/Documents/vesicles_iii/bf_epi_optimal.xml
- Then to record epi/bf simultaneously, press "Enable" on Illumination > Sequence, and press a record button **on a different window to the illumination window**
  - Recording from the illumination window simply saves the .multiled illumination metadata
- The files are saved automatically to your chosen destination, but it is worth putting them on the network somewhere. When finished with imaging, close the main temika window (which should close them all) and then log out
- 
