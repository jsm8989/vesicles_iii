import sys
sys.path.append("python-temika-reader")
sys.path.append("contour_analyzer")
sys.path.append("moviereader")

#from read_cpp_contour import load_contour_cpp
from pytmk import Movie
#import matplotlib.pyplot as plt
from PIL import Image


m = Movie("movies/data_remote/floppy.11Nov2021_11.21.55.movie")

n_frames = str(m.n_frames)
print("There are " + n_frames + " frames in this movie")

frame_choice = int(input("Which frame do you want? (int < n_frames) "))

frame = m.get_frame(frame_choice)
img = Image.fromarray(frame)

img.show()
response = input("Do you want to save this image? (y/n) ")
if response == "y":
	img.save("image.png") # should give a more meaningful name based on the file input and frame...
else: 
	pass

