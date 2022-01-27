A general space for writing about things in the lab. Will likely be messy.

### 24/1/22
- Made vesicle sample to get back into it after the new year. Forgot to check which side of ITO conductive so dessicated the wrong side for an hour; decided the sample was not a particularly important one anyway and so smeared the other side and kept going. Convenient as only suitable confocal time is this afternoon and I want to go over it with Guil again.
- Have booked confocal 15:00-17:00, will make some notes on key things to do/look out for, hoping for good fluorescence but not necessarily getting data today (also need to check vesicle floppiness - get this from Guil's notes when we did this before)
- Ideally need to get some DLW time early this week to have a working prototype lab-on-a-chip for friday
- See handwritten page of notes for confocal time and usage. Will be useful as a reference for next time. Maybe ask Pietro for the matlab script for analysing confocal contours (different to BF ones)
- 


### 25/1/22
- Spent some time coding and thinking about ESA diffusion project alongside first day of lectures (which was fairly full)
- Spoke to Dean about training on the new microfluidics setup, should be able to do so next week


### 27/1/22
- Group meeting this afternoon. Aske presentation on post-transcriptional regulation in sRNA. Questions for Pietro:
  - MATLAB routine for confocal contour processing? Is this different to fluoro ones (and why? - check with Guil) >> Guil has the most recent ones
  - Are there any other BF/fluoro microscopes to check samples when tweezers room is in use/CL3? >> 0.34 or something (another Temika - ask Guil) and in the Tissue Culture room.
  - What is the plan with the Olympus?
- Have booked confocal for 16:30-17:30, post engineer service
- Plasma bonded PDMS cutout to cover slip for confocal imaging this afternoon, will use vesicle sample from monday, using 80uL of 400mM glucose and 20uL of vesicles produced with 300mM sucrose. 
- Confocal notes:
  - Managed to get it working after forgetting to turn on "visible" and wasting some time
  - Very noisy! Have I picked the correct laser?
  - Found that they are much more clearly visible when increasing the pinhole size
  - Also those at the "bottom" (which seems to be identifiable by some kind of dirt - see pictures) are much less mobile; I added some more in and noticed that these were moving quite rapidly, presumably down the density gradient until becoming stationary
  - Will have to play around with the detector settings on the right screen to reduce noise. At this level, it is difficult to tell how floppy the vesicles are; similarly they were made a few days ago and perhaps the glucose is a little old too and so the concentration imbalance might not be what I think it is
  - Scope sometimes has trouble resolving circular srtructures which I would have thought would be easily resolvable. Maybe this is a noise/intesity thing and the fact that they are simply smaller (paying with the zoom factor helped somewhat but this also meant they would move out of the frame more quickly)
  - xyt scan seems to work fine, will at some point need to work out how many frames I should scan over to get nice uncorrelated fluctuations
  - Required a phase correction of ~1.43 to avoid double images on the bidirectional scan (and it is unclear whether this made much qualitative difference to the images)
  - Changing input laser power didn't do much, nor did changing the PMT range (it seems as long as the peak and a decent bit up to FWHM is covered that will do)
  - took ~0.5GB data (most of which will not be useful), saved in D: and E: under "jsm89_temp_for_transfer" (can only save locally today as IT needs to reconnect it to the network)
- Also considered imaging in BF. Need to ask Jurij for account on that computer. Also need to go through changing the cameras with Guil (and why we have to do this...)
