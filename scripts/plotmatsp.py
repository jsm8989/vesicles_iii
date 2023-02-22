import os
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pathlib import Path

# filename= 'BF_2.28Mar2022_15.42.44_8.20_forPython.mat'
q_max = -1
x_values = []
y_values10 = []
y_values5 = []
y_values15 = []
fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
for file in os.listdir(Path("\\\\sf3\\cicutagroup\\jsm89\\")):
    if ("v1_BF_20x_shutter" in str(file)) and ("forPython" in str(file)):
        # print(file)
        data1 = sio.loadmat(Path("\\\\sf3\\cicutagroup\\jsm89\\" + file))

        time = float(file[18:26])
        if time < 0.001:
            ax1.plot(
                data1["q"][4:q_max],
                data1["ps"][4:q_max] * (10**18),
                label=str(file[18:26]) + "s",
            )  # q_min: q_max
        else:
            ax2.plot(
                data1["q"][4:q_max],
                data1["ps"][4:q_max] * (10**18),
                label=str(file[18:26]) + "s",
            )  # q_min: q_max

        cross_sec_q = 10
        x_values.append(float(str(file[18:26])))
        y_values10.append(data1["ps"][cross_sec_q])

        cross_sec_q = 5
        y_values5.append(data1["ps"][cross_sec_q])

        cross_sec_q = 15
        y_values15.append(data1["ps"][cross_sec_q])

        # plt.plot(data1['q'][4:20], data1['ps'][4:20], label=str(file[18:26])+"s") # q_min: q_max


plt.suptitle(
    "Raw PS for different shutter times for vesicle of radius 12um"
)  # +filename[:-14])
plt.xlabel("q (1/m)")
# plt.ylabel("mean square amplitude (m^2)")
ax1.set(ylabel=r"$\langle |u(q)|^2 \rangle$ (nm$^2$)")
ax2.set(ylabel=r"$\langle |u(q)|^2 \rangle$ (nm$^2$)")
ax1.legend()
ax2.legend()
plt.show()


####
# plot a cross-section to visualise the trends better (as the current data is unclear)
def fit_func(x, a, b):
    return a * x + b


alpha5, beta5 = curve_fit(fit_func, x_values, y_values5)
print(alpha5)
print(beta5)

plt.plot(x_values, y_values5, ".b", label="5th detected mode")
plt.plot(x_values, fit_func(x_values, alpha5, beta5), "b")
plt.plot(x_values, y_values10, ".r", label="10th detected mode")
plt.plot(x_values, y_values15, ".g", label="15th detected mode")
plt.title(
    "Cross-section of PS showing amplitude against shutter time for the {}th detected mode".format(
        cross_sec_q
    )
)
plt.xlabel("shutter time / s")
plt.ylabel(r"$\langle |u(q)|^2 \rangle$ (nm$^2$)")
plt.legend()
plt.show()
