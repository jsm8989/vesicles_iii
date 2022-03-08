A general space for writing about things in the lab. Will likely be messy. Some (not super standard) abbreviations: MF = microfluidic, BF = bright field. Notes from Michaelmas were much less frequent.

### 27/10/21
- Had initial meeting with Pietro and Guil
- Pipetted 5uL of Texas Red of unknown concentration (due to evaporation) into remaining DOPC/Chloroform solution 
- Precision not needed here yet
- It turns out there was no remaining solution…
- Added 171uL of DOPC at 25mgmL (from freezer 04), although lost one drop while pipetting, into the same “jar” containing the new TR
- Added 892uL of chloroform (inside the foom hood) to it, vortexed, proceeded as usual. Will be interesting to see what the fluoro looks like (on pipetting, it does not look very pink…)
- Usual dessicator isn’t free! Used greasy one on top shelf.
Done for today; to do at some point:
- Get on the github, review project meeting just now
- Make up sucrose/glucose
- Get on the Nikons
- Pester Morten (DLW is a mess)
- Order TR, DOPC? For the more precise stuff
- Clean up my old stuff, review notes, set up lab notebook

### 1/11/21
- Microscope training with Jurij
- See BF_imaging protocol for notes

### 11/11/21
Chat with Guil about software he could send me, and how it works 
- Can add contours on movie files in either c++ (cpp-contour-tracker/track_movie.cpp) or python (moviereader/contour_tracker.py)
- Used to need a starting contour (which Guil has own temika script for - this is what generated that nice .txt file in his great example dataset), but should be able to get started by specifying own centre and first_point on the boundary
- In the c++ version the relevant part is around line 96; might be able to avoid some of the bs before by just inputting the right thing at the right time
- Can go through it together next week if struggling
- In the python version (probably in c++ too) the combo_tracker function should be able to track the vesicle as it moves throughout the movie file (essentially recentering it)
- Once have the contours, extracting the parameters should be easy
- Maybe go over some C++!

### 9/12/21
Chat with Guil about simulating the fluctuations
- First
- 	Can get shapes either by putting them in or by inputting tension, bending modulus etc
- 	Currently no time evolution - should be easy enough to put in through Langevin
- 	Inverse FT, superposing modes q>=2, 
- Optics - more mature
- 	Black box in extracting contours through the optics
- In guil’s (local) dirs: 
- 	Bead_optics/
- 	Battle_of_fitters/make_fake_cell_lib.py


### 14/12/21
- For the past week (since 6/12) I have been in the office every afternoon, working on simulations and analysis software and reading some good papers which I hadn’t come across before
- Today, obtained CAD files from viola (which are on the DLW computer anyway). These chips are to trap RBCs so would need scaling up for vesicles. This may save significant time and/or the need to contact other researchers with similar designs (which will inevitably be much slower)
- Another possibility for immobilisng vesicles is the surface biotin-avidin treatment - worth looking into if microfluidic trapping remains unavailable/obtainable, this can probably be done in a very simple serpentine channel with the required number of in/outlets
- Viola mentioned the need to passivate the channel before flushing other stuff down to avoid this annoying surface tension effects, even then I’m not sure how useful “my design” is. 
- I spent a while trying to find BSA, and not many people knew; Michal was able to help me with some crystals, so I made up a 1% BSA solution in DI water, although noted after that people also make it up in eg PBS or other neutral buffers. Turns out BSA solution is very foamy… unless I did something wrong
- I used this to try to passivate my old chip, but perhaps it was already too dirty for this to be successful, also the flow of fluids is still sub-optimal. Maybe should split up the channels going into the main array region as in Viola’s/Emma’s recent design
- Also tried to passivate other chips including serpentine channels, but these clearly had not been very well bonded/inlet holes punched too large/other related problems, which was frustrating
- So I cut some new ones (one inlet/outlet each, from a previous PDMS pour I had) and bonded them onto the same slide after cleaning the slide and PDMS surfaces with IPA. Sadly, the bonding did not work, despite using the same procedure as always (I don’t think anyone had changed the power setting but I’m not entirely sure what it is usually set on).
- This could be linked to the discussion overheard by Anna a few weeks ago regarding replacing the plasma bonder
Thoughts:
- Shame not to have done more chip experimentation last week, I did not think to ask around beyond Morten, who was the designated microfluidics person and was ill, hence I stayed in Cambridge an extra few days (planning to leave tomorrow)
- Quite tired now and even though end of term has been quite relaxed, I didn’t make as much project progress (at least not ESA wise) as I hoped
- Currently planning to return on the 10th of January, apparently by then a new microfluidics expert is joining the (group? Department? building?). Maybe I should come back a few days earlier to try hard to get this working prototype ready for 21st Jan (as requested by ESA).
- Exams ahh! 
Questions:
- What to do with old PDMS?
- How best to passivate and clean microfluidic channels?
- Is it worth emailing authors of vesicle-trapping papers to see if they can send any resources? (NB: check SI of good papers)
Other plans for holiday:
- Ensure lab notes are compiled and nicely documented (although not too nice)
- Continue to read papers in detail, alongside revision
- Get fluctuation analysis set up
- Get simulation software done
- Try to simulate microfluidic geometries
- Sort arduino syringe pump control



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
- [meeting cancelled]


### 4/2/22
- Did PDMS, bonding and testing of new device between 11-15:30. Rate-limiting step was the 2 hour bake @60 degrees C.
- Mostly as before, with emphasis on cleaning around plasma bonding area, which I had not been too careful with previously
- My device was slightly leaky, we are unsure why. The 100um channels were also much easier to get flow through than the smaller ones, although it turned out the tubing and hole punch did not quite work.
I sadly also broke the plunger on the punching machine by pushing it down too fr, and this led to ~an hour delay (sorry Dean). Remember to always look perpendicular to the punching plane to avoid parallax! And the surfaces are not as hard as previous things I have punched on!!



### 7/2/22
- Did a lot of ESA electronics work yesterday, to show Nigel and co. our progress in a tangible manner.
- Katie has ordered reagents and is in charge of testing the reaction - I am really relying on her for this
- Wrote a simple script which could analyse sigmoidal curves by returning the gradient as a function of time, giving the initial and max rates. 
- Also currently deciding how best to characterise the saturation time - will talk to Pietro about this
- Plan for lab today: have booked DLW from 13:00-16:00, planning to print one of the Gennaio_attachment files that Viola sent me.
	- Also want to compare these to other works to show it's a better idea
	- Need to measure size (either post-production using profilometer or on software)
	- Expect ~100um channels, of a reasonable (50um?) depth, and smaller traps. Although this may be problematic for larger vesicle samples - reduce growth phase time?
	- For today only worth doing this on a single glass slide, as we are not yet interested in large scale production, and this may be more of a recall/test run for me
- At some point need to return to the EVOS with Timo, who I haven't spoken to for a while. Would be good to see what kind of scripting/remote control is possible with it



Tomorrow/later in the week:
- make some new vesicles, get some confocal/Temika time, and get more data
- continue c++ contour analysis
- spend more time on simulation code, should really have this done soon (and "out of the way")



Afternoon in the lab:
- All the phd students seem to have covid, office will be quiet for a while :( hopefully they can still make it to the dinner on the weekend!
- Forgot USB at home so could not smoothly transfer desired dxf from my laptop to DLW, and sadly I also could not find Viola's copy on the PC, so modified Dean's training one to include some traps. This ended up being a useful experience to get grips with the software (which is also faster than doing in on my laptop anyways).
- Cleaned the glass slide and did the SU8 spinning as best as I could remember, but I worry I got the heating/baking bits wrong.
-   I got a fresh slide, cleaned it with acetone and IPA, then left it at 65deg for a few mins. I then did the SU8 spin (program 7, hadn't been changed) and put the slide on at 200 for 10 mins, during which time I cleaned the spinner and turned off the vacuum etc. I also prepared the CAD during this time
-   Preparing the CAD took a little longer than 10mins so the slide with SU8 was left in the air for a while, at least the light was off.
-   Loaded, went through the calibration and sample prepation (which took me a few attempts but I reckon I've got the idea now), but could not "send to laser", I thought this was to do with the blocks that had been defined but eventually I found Dean who pointed out that I hadn't set the attributes (for future ref: chosoe "coarse" and set the second value to 800)
-   It then worked fine (and btw, the DLW does not expose any blocks that are empty)
- Now I am eating lunch and writing this. Will likely develop shortly and get the PDMS ready, then leave baking overnight? 
- Sadly the developmment did not work. I spoke to Peter while collecting a petri dish, and brought him down to show the idea of lithography/microfluidics (since he was waiting around for a while anyway). I didn't notice anything particularly unusual, but after the PGMEA dip, the IPA seemed to "congeal" the remaining photoresist off the substrate and it formed a weird substance in the dish. This continued when I tried to further develop it. My guess is that the pre-exposure baking steps did not work (which, on reflection the next day, I realised I had missed a longer water-desorption baking step after intial cleaning). 
- Either way, this was frustrating, but would give me an opportunity to go through it all again the next day, especially now that Dean had sent me the (draft) notes.

ESA meeting in the evening:
- More productive than expected, it was good to talk through why I had made certain decisions and whether alternatives were reasonable. 
- Progress has been made, and in theory with a good MF device and some good reaction tests from Katie we are almost good to go.
- Annoyingly campaign dates have changed againi and are currently pencilled in for 4-6th May. 
- Good, but mildly stressful, day (not sustainable)


### 8/2/22
- In the MF room at 08:30, quick clean and software ready after a good start to the morning. Was able to finish DLW exposure and clean ITO slides for electroformation pre 10am lecture. 
- After lecture, removed exposed slide and carried out development as detailed in protocol. Maybe a glass petri dish made a difference (yesterday I used a plastic one...)?
- Finished the final post-development bake slightly early (supposed to be 10 min at 200, I did more like 7.5 as I had overrun my booking slot slightly).
- Poured PDMS as in protocol, put in oven and ended up leaving it there for 2.5 hrs over lunch and QI lecture (should idaelly have been 2hrs but I don't think it is too important here). 
- Also did some electroformation during this time, ready by 15:10, with Roger wanting to do it after
- Cut and bonded new chip post-lecture and now writing this. On inspection it seems to have worked well; I don't have any tubing with me (or a huge amount of energy) and so will see whether I can trap the vesicles tomorrow morning, especially as the fluorescent Nikon is more available at that time. 
- NB when punching holes, I planned to use the mechanical device, but could not find the alan key needed to lower it towards the stage. Some of these logistic things would be nice to have in the drawers of the respective rooms.
- NBB left labcoat on hanger in Biochemistry lab when walking to waiting area, and will likely leave it there overnight. 


### 9/2/22
- Tested out new MF device using microscope in MF room. Worked well from a fluid flow point of view. Some of the trap squares have not come out quite right, but I realise that I should try passivating this structure before passing liquid through it as I am getting the same problems with the surface tension as in the last desing. Should also try make Vioa's design with the curved traps to see if that makes any difference.
- Tried to image vesicles in same scope but couldn't see anything (either the recently made ones or those from 2 weeks ago)


### 10/2/22
- Got in early on the Nikon microscope, I should still write up those notes as I spent a lot of time messing around with the hardware side of the illumination settings. Also I have yet to see a fluorescent signal for vesicles by myself - either this is a vesicles issue or an issue with my usage of the microscope
- To be fair, I could not clearly see vesicles in BF. I initally tried in a simple well (although without glucose) but I really think that cleaning the bottom of the glass slide or similar would be a good thing before next imaging attempt.
- I then viewed the MF channels, which at least gave me something to aim for, and they were easy to image (although still couldn't remove diffraction effects - see test images)
- I tried to inject some vesicles into the channels but this did not work from an imaging point of view (also directly from the syringe is perhaps not useful as may widen the inlet, and also seemed to give many bubbles, although this may also have been to do with the fact that there was stuf fin there from before. Need to work out best way to "clean" it)
- I also (still) do not seem to be able to control the z drive/focus by any means other than the actual buttons on the scope. 
- May try print new chip tomorrow, since the training lot will be mostly in the mechanics lab (although will maybe check this with Dean first)
- Also checked other computer and remembered that I forgot the capitals when setting my pw for it, tried to change it but the pw is too simple. Either way would be interesting to use the optical tweezers at some point (mainly for my own experience and interest, would be cool to see what they can do). It seems temika works in exactly the same way as on the Nikon computer.
- Also, tomorrow is Mattia's last day!
- NLO supo shortly (fisrt one of term)


### 11/2/22
- Continued coding, kept getting memory allocation issues and hence "segmentation fault (core dumped)"
- Found the source of the errors but not entirely sure what to do about it - given that this part of the code just needs to generate a text file with the initial contour, I could possibly do it a different way (eg in python) and then just `track_movie` with the movie file and the initial contour
- Left early (~14:30) to go and watch Lucien Hardy's QI seminar, then continued coding at home with Kieran but did not manage to pass any significant milestones


### 14/2/22
![Handwritten lab notes for this day](images/lab_notes_14_feb.jpg "Text to show on mouseover")


### 15/2/22
- Big tidy up of my digital records, have migrated all notes from the drive to Github
- Set up, modified and tested python scripts locally in order to generate an initial contour txt file; there are multiple examples of plotting contours which work so this should not be too hard, also much easier to work with both locally (at home) and at the office
- Spoke to Roger about locating DOPC and TR, these can both be found in Rini's box at the bottom of the freezer
- Made some (non-fluoro) vesicles with new sucrose solution made yesterday, cleaned vessel for making a new fluorescent lipid solution - Roger pointed out that the excat ratios are important for this work and that it would not be sensible to just add an arbitrary amount of TR into my (depleted) older lipid mixture
- Started playing around with lif files on ImageJ as I realie this is a whole different step to the movie file analysis which I been spending significant time on
- Tomorrow: 
- 	Make up lipid mixture
- 	Image this set of vesicles
- 	Make up BSA solution using Michal's stock
- 	Passivate MF
- 	Bring in electronics to discuss with Shash
- 	Ask Guil if he has any routines for analysing lif files


### 16/2/22
- Successful imaging on Nikon after finding notes from Jurij meeting - able to get it very clear
- 	 one thing to check is how to centre the filter at the top when you want to focus it on a certain part of your sample
- Now need to rememberhow to send the data to the Z drive from here; could write a script for it. 
- Also need to ask Guil what osmolarities we used in the past to get nice floppy stuff. These were not fluorescent so not too important for today anyway
- Also need to find corerct tubing size if I'm gonna have any chance of trapping the vesicles in the MF device, as injecting them in via syringe tubing today just led to leakage (mostly)


- Success in terms of remote connection from Nikon computers: you can run `ssh jsm89@sf1.bss.phy.private.cam.ac.uk` and get straight into the Z:/jsm89 directory
- Could create a local bash script which copies all movie files from a given date (eg using `scp *16Feb2022* jsm89@sf1.bss.phy.private.cam.ac.uk:~/data_remote/`) 
- Note the bigger files take a while, as expected!


### 21/2/22
- Made up fluorescent lipid solution and prepared slides for electroforming tomorrow
- Will try image on Nikon and maybe confocal if its free
- Get solution ratios from Guil! (I seem to remember 300/400mM being ok, but hasn't appeared so recently)


### 22/2/22
- nice palindrome date!
- made new glucose solution at 400mM
- successful fluoro (and BF) imaging of vesicles made with 300mM sucrose, put in imaging vessel with 1:9 ratio initially
- most of them were quite taught so I added 30uL of DI water to try and match the osmolarities slightly better (in the paper they used 197/200 sucrose/glucose, also in 1:9 imaging ratio)
- Nice to see the re-equilibration on adding the water
- Have also booked confocal but unless I get some nice floppy ones there's not much point (no reason I can't just persevere for floppy ones though)
- lots of brownian motion, fission products visible, good to know the fluoresence has worked
- NB on the EF today there were in the growth stage for 2h20 rather than the usual 2h, as the timings didn't quite work out with my lecture


- tbh the 1:9 ratio is still too densely packed for clear, individual imaging
- some were more floppy - have tried to give clear temika names to the files 
- definitely worth having a look through them and seeing if we can run any contour analysis
- also 40x objective seems like a good default, need to play around with camera mode each time (incl diff between fluoro and BF) but this will become more intuitive


### 23/2/22
Rough notes made while setting up new desktop environment in the office. Don't know why I didn't do this earlier... much nicer to work with than my laptop!
- It works! I compiled track_movie and it actually tracked something...
- Although it didn't seem to do the ending output I was expecting, and hasn't actually given me anything (isn't this where the text file is supposed to come from?)
- Update: it looks like it has updated the contour text file... maybe should compare this one to the previous one!
- Although it, and the movie it took as input, were in the directory above it; worth noting (probably to do with how I copied the file into the argument of the .exe)
- The two files are defo not identical, as one contained way more lines than the other. Not sure why, or how important this is...
- Got python files to run too and can now analyze_all for all movie files, with associated contour files, in a specified directory (basically as Guil had it - still need to initialise new contours to get those txt files!). Analysis working smoothly, will have to double check what kind of data we want for all of that.
- On local desktop VSCode setup I am gonna diverge from the likely git branch, since it works differently to how I expect from Linux, and reduce the number of files needed to clean it up. Can always upload to a separate git branch later.
- all the fns in have moved into `contour_fitter.py`
- have updated central repo README with new tasks

Also
- Spoke to Guil who provided me with the following extract from his lab book dated june 23rd 2021:
	- Imaged just after preparing. 10uL of 20mM sucrose vesicles + 210uL of 22mM glucose. Added glucose to chamber, then added vesicles to chamber, rather than pre-mixing. 
	- Floppiness and concentration were "perfect"
	- Same day we did 305mM glucose and 300mM sucrose, in same ratio. All extremely taut


### 24/2/22
Coding day, meeting with Pietro in the afternoon, after Rayleigh library book giveaway at 11am. See handwritten notes, Pietro meeting was very useful. 
Will aim to meet at least weekly for the next few weeks
![Pietro meeting 1](images/16457896175288136800017126300239.jpg "Text")
![Pietro meeting 2](images/16457896414346541402660351332016.jpg "Text")
![Pietro meeting 3](images/1645789655104821810061106393033.jpg "Text")

### 25/2/22
- Finished biochemistry rota for the week, on it again next week (then likely never again)
- Made 20mM sucrose and 22mM glucose solutions from my stock for floppy vesicles next week
- Smeared lipids on slide for dessication over the weekend, ready to EF on monday
- Got Will to enable remote access to office desktop (PC1) but sadly it didn't seem to work from my laptop (some kind fo kerbolos authentication issue...). Will have to survive without the new setup for the weekend (which will mostly be reading and lecture work anyway!)

### 28/2/22
- EF of new, hopefully floppier vesicles
- sadly no microscopes were free so gonna come back tomorrow morning for get them on the confocal, trying a different laser.
- See Pietro's images!
- Also managed to get remote connection to PC1 over the weekend
- Quite tired, did some QS and QI, and watched the office handstand session!

### 1/3/22
- Big confocal morning, from 8:30-12:30 with an hour break for a lecture
- Defo feel more confident about it now; got much clearer images and the new vesicles from yesterday were good
- Auto gain is useful
- Tried different lasers (633 and 594), didn't seem to have a huge impact
- Tried HyD detector which gave the blue Pietro had, generally less noisy and easier to control too (took some images with both that and PMT active)
- Haven't worked out how to add BF channel at the same time (which I should be able to get "for free")
- Also noticed that zooming was useful in taking these images, as long as the vesicles are sufficiently stationary. Did then give the impression that they were much larger than they actually were though
- Need to get flickering analysis ready to go, then get a time where I can image on Leica and BF on the same day. Or get Guil etc to change the camera around for me
- See notes from Pietro meeting for what kind of data I should get (and label it as clearly as possible, at least write in here what happened on each day)
- Also plasma bonded a multi well onto a coverslip for more imaging opps



### 7/3/22
Presentation with other part IIIs and part IIs, see Pietro feedback (TODO)

### 8/3/22
Finally noting down the fluorescence settings that work (not sure why I haven't before)
![image](https://user-images.githubusercontent.com/69422343/157300061-033df188-ee93-4bfa-a380-5a03890d53e2.png)
(see screenshot of temika settings)
Made a few wells. 22mM glucose volume:
- 150
- 30
- 20
Currently imaging 2uL of vesicles in the 30uL glucose - far too dense (and maybe why the image was initially so saturated)
Some very nice floppy vesicles though, would be great to have these on all scopes
Objective: 40x (light blue)
Filter cube 6 (can be seen on microscope view)
