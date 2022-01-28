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


### 28/1/22
- Got account on Fedora PC in Leica room, will need to get Guil/Jurij to show me how to change the cameras over (and what the benefit of doing this is, as Jurij seemed a little confused, but it made some sense when I said I was doing flickering experiments)
  - NB the leica can already do some kind of BF transmission
- Imaged Monday's samples (again 80/20 glucose/vesicles) on the Nikon to refamiliarise with Fedora.
- Notes on BF:
  - Write up Jurij's step-by-step protocol for optimum imaging, as not sure if I have got it here (although it ended up being pretty clear, and temika is quite intuitive I find)
  - Struggled to see anything on 40x mag but was clear on 20x and 10x
  - The vesicles were not very floppy at all, perhaps for similar reasons as mentioned yesterday
  - The temika z-drive controls are very delayed and it seems more useful to sue the focus knob on the scope (without leaning on the optical table ideally)
  - Curious whether "eye" option (either on temika or the physical button) actually allows you to see through the eyepieces, as this did not seem to be the case today
  - There appear to be a few "burst vesicles" or something similar at the bottom of the sample (maybe also remnant oil after using it on the wet objective yesterday - should really get different sample holders. Perhaps also a thicker optical slide will also allow use of the 40x objective as in the past we were definitely more zoomed in on inidividual vesicles)
  - Once again the majority of the vesicles were nicely at the bottom of the glucose - could be relevant to ESA project ie whether they need to be "trapped" at all?
  - I also need to play around with the camera settings, similarly with leica imaging, as I remember in the apst it was easy to capture fewer frames
  -
- Attempted fluorescence (ie channel 1 illumination - remember to (physically?) change the FL block)
  - Could not quite get this to work, will have to double check which filter block and which LED to illuminate with (see eg spectra and notes on door)
  - Maybe the vesicles had somehow lost their fluorescence (although they were fluorescing on the confocal yesterday...)
  - Also changed the BF significantly on returning to that
  - Time for lectures, will have another go later if possible (although I think the room is booked for CL3 work for the rest of the afternoon)
- saved af ew images locally in data/


- Software afternoon
  - Reorganised directory structure on local laptop, cloning Guil's relevant github repos so I can pull/push any edits from either side
  - Working out how to package them (adding __init__ and setup files to them) so I don't have to keep adding to path (inspired by discussion with Kieran yesterday who has done similar for a local conda package. Note he also wrote a bash script to keep reinstalling the package once it has been edited)
  - After a lot of time I realised (through talking to Sasha) that simply adding the relevant folders to path through sys.path.append() is a much quicker (if shorter-term) way of doing it, thanks Sasha!
  - I now have a nice way of testing Guil's programs locally, and it works perfectly for the example data (surprise surprise). Python script currently takes a txt file containing the contour as input, which itself comes from the c++ contour tracker (I believe). Gonna look into this now
  - Managed to save a text file of the "results" using Guil's sample contour, which concluded a bending modulus of (264.829902+-10.955818)pNnm, a tension of (0.001486+-0.000166)pN/nm and a radius of 4010.748218nm for that particular sample. Also gave a bunch of other information including many decay times and associated errors for ~15 different modes. Will need to dive into this to see what's relevant (and how to neaten up the output) but happy that could work.
  - I have created a "jamie" branch on Guil's contour_analyzer repo to keep track of my own changes/documentation (could also just fork it but may be nice to merge later on)
  - Next up: generating my own contour text file from the c++
- NB: Aske had Will sort a few things on the office PC including downloading Ilastik for all users, could be worth exploring although maybe it only deals with single frames and hecne not as useful for my purposes.
