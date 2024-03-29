import os
import scipy.io as sio
import matplotlib.pyplot as plt
from pathlib import Path

for file in os.listdir(Path("\\\\sf3\\cicutagroup\\jsm89\\")):
    if ("v3_BF_20x_shutter" in str(file)) and ("forPython" in str(file)):
        print(file)
        data1 = sio.loadmat(Path("\\\\sf3\\cicutagroup\\jsm89\\" + file))

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
