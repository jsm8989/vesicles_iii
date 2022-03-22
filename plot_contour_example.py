import sys
sys.path.append("../python-temika-reader") # NB when doing this need to run the script from it's own dir
sys.path.append("../contour_analyzer")
from contour_fitter import load_contour_cpp
from pytmk import Movie
import matplotlib.pyplot as plt

m = Movie("../well_C5_cell_0000.movie") 
c = load_contour_cpp('../well_C5_cell_0000_contour_full.txt') 


def plot_contour(i):
	"""
	Plot entire contour over image
	"""
	plt.imshow(m.get_frame(i))
	if c[i][1] is not None:
		plt.plot(*c[i][1].T, c = 'r')



# eg 10th frame and contour 
plot_contour(10)
plt.show()

