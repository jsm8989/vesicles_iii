import os
import scipy.io as sio
import matplotlib.pyplot as plt
from pathlib import Path

filename = "v0_.29March2022_20x_weird_8.20_forPython.mat"

# print(file)
data1 = sio.loadmat(Path("\\\\sf3\\cicutagroup\\jsm89\\" + filename))

# print(data)
# time = float(file[18:26])
plt.plot(
    data1["q"][3:], data1["ps"][3:] * (10**18), label=str(filename[18:26]) + "s"
)  # q_min: q_max


# plt.plot(data1['q'][4:20], data1['ps'][4:20], label=str(file[18:26])+"s") # q_min: q_max


plt.suptitle("Raw PS for " + filename[:-14])
plt.xlabel("q (1/m)")
plt.ylabel(r"$\langle |u(q)|^2 \rangle$ (nm$^2$)")
# plt.legend()

plt.show()
