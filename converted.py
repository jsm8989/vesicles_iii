# %%

import sys
sys.path.append("python-temika-reader")

from pytmk import Movie
from PIL import Image
#import IPython.display #import Image
import matplotlib.pyplot as plt
#matplotlib inline
import moviepy ### where is this?

# %%
m = Movie("well_C5_cell_0000.movie")

print(m.n_frames)

img = Image.fromarray(m.get_frame(10))

# %%
img.save("img1.png", "PNG")

# %%

for i in range(100):
    frame = m.get_frame(i)
    img = Image.fromarray(frame)
    img.save("img{}.png".format(i), "PNG")

# %%
#IPython.display.Image(m.get_frame(10))

# %%
from moviepy.editor import *




# %%
import glob
images = glob.glob('*.png')
images.sort()
print(images)

# %%
clip = moviepy.editor.ImageSequenceClip(images, fps = 4) 
clip.write_videofile("video.mp4", fps = 24)

# %%


# %%


# %%
### lattice simulations 
