from vesicles_iii.scripts.pytmk import Movie
from contour_analyzer.contour_fitter import (
    load_contour_cpp,
    default_fit_parameters,
    celsius_to_kT,
)
import matplotlib.pyplot as plt
import os
from pathlib import Path

min_len = 200
path = "\\\\sf3\\cicutagroup\\jsm89\\"
m = Movie(Path(path + "v8_BF_40x.12Apr2022_15.01.16.movie"))
cf = path + "v8_BF_40x.12Apr2022_15.01.16_contour_full.txt"

## should work, throws TypeError :()
# m = Movie("\\\\sf3\\cicutagroup\\jsm89\\v1_BF_40x.29Mar2022_10.37.27.movie")
# cf = '\\\\sf3\\cicutagroup\\jsm89\\v1_BF_40x.29Mar2022_10.37.27_contour_full.txt'


# m = Movie("../well_C5_cell_0000.movie")
# cf = "../well_C5_cell_0000_contour_full.txt"
c = load_contour_cpp(cf)

# returns a list of all "frames" in the text file which have length > min_len (ie before going to 0...)
contours = list(filter(lambda z: z[1] is not None and len(z[1]) > min_len, c))  #
with open("Z:\\code\\vesicles_iii\\contour_example.txt", "a") as f:
    # f.write("countours.shape = {}".format(contours.shape))
    f.write("len(contours) = {}".format(len(contours)))
    f.write(str(contours))


# probably need to change pixel resolution from default - TODO
fit_param = default_fit_parameters
fit_param["sub_radius"] = "static_shape"
fit_param["vertical_radius"] = 1000.0
fit_param["depth_of_focus"] = 0.0
fit_param["exposure_time"] = 0.1
# for dirs in next(os.walk(big_dirs))[1]:
if True == True:
    fit_param["contour_file"] = cf
    mf = cf.split("_contour_full.txt")[0] + ".movie"
    if os.path.isfile(mf):
        fit_param["movie_file"] = mf
        m = Movie(Path(mf))
        header = m.header
        fit_param["extra_info"] = header
        if "Temperature=" in header:
            temperature_celsius = float(header.split("Temperature=")[-1].split("\n")[0])
            fit_param["kT"] = celsius_to_kT(temperature_celsius)
    else:
        fit_param["movie_file"] = None


def plot_contour(i):
    """
    Plot entire contour over image
    """
    fit = fit_mps(
        contours, fit_param, plot=True, verbose=True
    )  # plot the PS too -- maybe save these somewhere with a nice naming system?

    plt.imshow(m.get_frame(i))
    if c[i][1] is not None:
        plt.plot(*c[i][1].T, c="r")


# eg 10th frame and contour
choice = 11
# for choice in range(110, 120):
plot_contour(choice)
plt.title(
    "{}th frame with superimposed contour. If blank, may be bad_frame".format(choice)
)
plt.show()
