import sys
sys.path.append("python-temika-reader")
sys.path.append("contour_analyzer")
#This is a simple script to open the movie, load the full contour, and plot the contour overlayed on the image.

from read_cpp_contour import load_contour_cpp
from pytmk import Movie
import matplotlib.pyplot as plt

m = Movie("well_C5_cell_0000.movie") #Loads the movie
c = load_contour_cpp('well_C5_cell_0000_contour_full.txt') #Loads the full contour

#Define a function to plot the full contour over the image
def plot_contour(i):
	plt.imshow(m.get_frame(i))
	if c[i][1] is not None:
		plt.plot(*c[i][1].T, c = 'r')



#As an example, plot the 10th frame and contour together
plot_contour(10)

plt.show()
