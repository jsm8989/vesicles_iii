import sys

sys.path.append("../../python-temika-reader")
sys.path.append("../../contour_analyzer")
sys.path.append("../../moviereader")


# from read_cpp_contour import load_contour_cpp
from pytmk import Movie

# import matplotlib.pyplot as plt
from PIL import Image


"""
Current files in data_remote as of 24/2/22 (for easy changing):
                                                  Experiment.lif
-a----        22/02/2022     13:30       16508419 Experiment3.lif
-a----        11/11/2021     11:18        5234136 floppy.11Nov2021_11.18.08.movie ## good fluctuations
-a----        11/11/2021     11:18        3694696 floppy.11Nov2021_11.18.23.movie ## ok fluctuations, less sharp
-a----        11/11/2021     11:18          16084 floppy.11Nov2021_11.18.51.movie
-a----        11/11/2021     11:18        1123120 floppy.11Nov2021_11.18.52.movie
-a----        11/11/2021     11:20       11762940 floppy.11Nov2021_11.20.50.movie
-a----        11/11/2021     11:21        2794352 floppy.11Nov2021_11.21.55.movie
-a----        11/11/2021     11:23       31964296 floppy.11Nov2021_11.23.37.movie
-a----        16/02/2022     15:19       78338964 interface.16Feb2022_15.01.49.movie
-a----        16/02/2022     15:19       59906276 interface.16Feb2022_15.02.29.movie
-a----        16/02/2022     15:19       36865416 interface.16Feb2022_15.02.45.movie
-a----        13/05/2021     04:05       21060440 test.13May2021_11.05.04.movie
-a----        13/05/2021     04:05       15374132 test.13May2021_11.05.34.movie
-a----        13/05/2021     04:06       17058964 test.13May2021_11.06.22.movie
-a----        16/02/2022     15:19        9216384 test.16Feb2022_14.58.32.movie
"""


filename = sys.argv[1]
m = Movie(filename)
n_frames = str(m.n_frames)
print("There are " + n_frames + " frames in this movie")

frame_choice = int(
    input('Which frame do you want? (int < n_frames, choose -1 for "all") ')
)  # should add a range option (although don't spend too much time on this)
if frame_choice == -1:  # show all frames. NB this is long!
    frames = []
    imgs = []
    for i in range(int(n_frames)):
        frames.append(m.get_frame(i))
        imgs.append(Image.fromarray(frames[i]))
        imgs[i].show()
else:
    frame = m.get_frame(frame_choice)
    img = Image.fromarray(frame)
    # img.show()
    print("Image metadata:\n{}".format(m.header))
    response = input("Do you want to save this image? (y/N) ")
    if response == "y":
        img.save(
            "image.png"
        )  # should give a more meaningful name based on the file input and frame...
    else:
        pass
