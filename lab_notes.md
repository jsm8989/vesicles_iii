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
- Note that running the analysis on the same contour multiple times gives the same results


### 31/1/22
- Continued with the c++, going down many rabbit holes but ultimately making some progress. No lectures today so spent most of 10am-17:30 on the screen.
- Pointers are confusing but at least I can now identify them and have a rough idea for how they're used.
- Forked Guil's code to my own branch and pulled locally, was a nice system and ended up compiling as required (can also use the makefile as I imagine it was intended)
- Spent a long time trying to change the header dependencies to tidy up the repo but got stuck and so had to revert back to an earlier commit and create a new branch
- Just need to set up the intitial contour now (as in track_contours.cpp) and it should work from there; have only been testing on Guil's sample data so far. Guil is happy to help so try not to go down too many more rabbit holes!


### 2/2/22
- Spoke to Rafia from the Rutherford Hub about Katie's refund request from September. Got to meet the team (incl Steve, Frank, ?Methia) and turns out they have an open door policy. Rafia has been there since October
- They found the request and apparently sorted it all out, but the "second approver" (who is someone else within the dept) never got round to approving it, hence no payment was ever made
- They have processed it again, usually such requests are bundled and sent off on Wednesdays (ie today) so this one will go out next Wednesday, and payment should be received between 11-14th of Feb.
- Now that we have done a trial run (hopefully successfully) we will process bigger claims in one go in the future, through the same expenses form as before.
- Microfluidics tomorrow, be in the lab for 9! (and then finish ~17, nicely in time for footy training)


### 3/2/22
- Microfluidics training with Dean and ?Chenyan (no Aske :( ). It can be quite difficult standing passively in that room for a few hours, but the next bit should be more interactive. It is very in-depth training (which is great) but I'm not yet sure if it really needs 2 full days!
- Notes:
  - SU8 is expensive (£600-1000 per 0.5L bottle)
  - But we may as well use it because it will degrade
  - Try and keep everything clean - always start with acetone, then eg IPA if appropriate
  - Didn't know we can do this on a glass slide, this is of course handy but then we don't get a nice "master" from which multiple devices can be produced
  - Laser writer levelling can be quite time-consuming, as can some of the baking steps (see the timings in the notes, when Dean sends them, which should hopefully be tomorrow)
  - SU8 20XX series has the notation that XX stands for the micron thickness for 3000rpm spin of duration (...), or something like that
  - Can see the 300micron "squares" which are the exposure units in the DLW, on the device, where it has been "stitched" together. In general, try to design devices so that fine structures can be contained within these. 
  - This morning we used spin process 7, although these are subject to editing by any user; SU8 prefers a two-spin process at low and then high speeds. Make sure the vaccum is greater than 25(au), otherwise it won't allow running!
  - First check coolant levels before opening DLW software
  - Can use in-house software for CAD style editing, it is more basic but make sure you save stuff if you do this (esp in case need to restart the software for whatever reason)
  - Ejecting/loading can be done either on the software or the hardware, software is probs better for logging, either way it gives a very Star-Trek vibe
  - Put the coated side of the substrate face down into the DLW
  - Don't put the spring side of the substrate holder down on a surface
  - Go slow when pipetting/pouring photoresist to prevent bubbles; will probably need to cut pipette tip (esp for more viscous ones)
  - Si wafers are in general better quality but much more expensive than glass slides. If we compared glass wafers and Si wafers, the Si ones are a similar price, despite being better quality, due to the electronics industry.
  -   Better = easier to see dust, less roughness (almost atomically smooth), can produce more things in one go (obviously)
  -   Similarities = both hard enough that cutting with razor is no problem, also defect size/overall quality both easily good enough for "microfluidics".
- Will try join the meeting this afternoon if I am not in the middle of something
- 
