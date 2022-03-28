import sys
sys.path.append("../python-temika-reader") # NB when doing this need to run the script from it's own dir
sys.path.append("../contour_analyzer")
from contour_fitter import *
from pytmk import Movie
import matplotlib.pyplot as plt
import os

min_len = 200

m = Movie("../well_C5_cell_0000.movie") 
cf = '../well_C5_cell_0000_contour_full.txt'
c = load_contour_cpp(cf) 

contours = list(filter(lambda z: z[1] is not None and len(z[1]) > min_len, c))

fit_param = default_fit_parameters
fit_param['sub_radius'] = 'static_shape'
fit_param['vertical_radius'] = 1000.
fit_param['depth_of_focus'] = 0.0
fit_param['exposure_time'] = 0.1
#for dirs in next(os.walk(big_dirs))[1]:
if True == True:

	fit_param['contour_file'] = cf
	mf = cf.split("_contour_full.txt")[0] + ".movie"
	if os.path.isfile(mf):
		fit_param['movie_file'] = mf
		m = Movie(mf)
		header = m.header
		fit_param['extra_info'] = header
		if 'Temperature=' in header:
			temperature_celsius = float(header.split("Temperature=")[-1].split("\n")[0])
			fit_param['kT'] = celsius_to_kT(temperature_celsius)
	else:
		fit_param['movie_file'] = None





def plot_contour(i):
	"""
	Plot entire contour over image
	"""
	fit = fit_mps(contours, fit_param, plot = True, verbose = True) # plot the PS too

	plt.imshow(m.get_frame(i))
	if c[i][1] is not None:
		plt.plot(*c[i][1].T, c = 'r')

	


# eg 10th frame and contour 
plot_contour(10)
plt.show()

