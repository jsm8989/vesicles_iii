import sys
sys.path.append("python-temika-reader")
sys.path.append("contour_analyzer")
sys.path.append("moviereader")

from read_cpp_contour import load_contour_cpp # in contour_analyzer
from pytmk import Movie # in python-temika-reader
import matplotlib.pyplot as plt
from PIL import Image
import contour_tracker # in moviereader
import numpy as np

m = Movie("well_C5_cell_0000.movie") # test data in any directory

# print(m.n_frames)

frame = m.get_frame(10)
shape = np.shape(frame)
print(shape)

img = Image.fromarray(frame)

img.show()


# # from plot_contour.py:
# #Define a function to plot the full contour over the image
# def plot_contour(i):
        # plt.imshow(m.get_frame(i))
        # if c[i][1] is not None:
                # plt.plot(*c[i][1].T, c = 'r')
# 
# 
# 
# #As an example, plot the 10th frame and contour together
# plot_contour(10)
# 
# plt.show()



# think of good way to get center, first point (+ what do they mean?)
first_point = [61,114] # for the example vesicle image
center = [0.5*shape[0],0.5*shape[1]] # should work generally for any image centred on the vesicle
contour1 = contour_tracker.get_contour(frame, first_point, center, verbose = True)
print("Result of get_contour: \n", contour1)


contours = contour_tracker.combo_tracker(m, first_point, center, verbose = True)


contour_tracker.save_contour("contour.txt",contours, start = 10, end = 100)
