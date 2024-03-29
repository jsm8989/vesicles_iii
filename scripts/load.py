from moviereader import contour_tracker
from contour_analyzer.contour_fitter import load_contour_cpp  # in contour_analyzer
from vesicles_iii.scripts.pytmk import Movie
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


m = Movie(Path("../well_C5_cell_0000.movie"))  # test data

print("There are {} frames in this movie".format(m.n_frames))

frame = m.get_frame(10)  # arbitrary frame choice
shape = np.shape(frame)
# print(shape)

img = Image.fromarray(frame)

# img.show() # image without contour


# think of good way to get center, first point
first_point = [155, 112]  # for the example vesicle image
center = [112, 112]  # should work generally for any image centred on the vesicle
contour1 = contour_tracker.get_contour(frame, first_point, center, verbose=True)
print("Result of get_contour: \n", contour1)


# contours = contour_tracker.combo_tracker(m, first_point, center, verbose = True, start=10, end=100)


contour_tracker.save_contour("contour.txt", contour1)
