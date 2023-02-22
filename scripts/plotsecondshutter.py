import os
import scipy.io as sio
import sys
import matplotlib.pyplot as plt

# load .mat file from cicutagroup/jsm89
# filename = str((sys.argv[1]))


# filename= 'BF_2.28Mar2022_15.42.44_8.20_forPython.mat'

# fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
for file in os.listdir("Z:\code\jamie_matlab_scripts\\"):
    if "v3_BF_20x_shutter" in str(file):
        # print(file)
        data1 = sio.loadmat("Z:\code\jamie_matlab_scripts\\" + file)

        # print(data)
        # time = float(file[18:26])
        plt.plot(
            data1["q"][4:20],
            data1["ps"][4:20] * (10**18),
            label=str(file[18:26]) + "s",
        )  # q_min: q_max

        # plt.plot(data1['q'][4:20], data1['ps'][4:20], label=str(file[18:26])+"s") # q_min: q_max


plt.suptitle(
    "Raw PS for different shutter times for vesicle of radius 12um"
)  # +filename[:-14])
plt.xlabel("q (1/m)")
plt.ylabel(r"$\langle |u(q)|^2 \rangle$ (nm$^2$)")
plt.legend()

plt.show()
