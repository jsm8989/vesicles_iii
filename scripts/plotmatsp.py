import os
import scipy.io as sio
import sys
import matplotlib.pyplot as plt

# load .mat file from cicutagroup/jsm89
#filename = str((sys.argv[1]))


filename= 'BF_2.28Mar2022_15.42.44_8.20_forPython.mat'
data1 = sio.loadmat('Z:\code\jamie_matlab_scripts\\'+filename)

#print(data)

plt.plot(data1['q'][4:20], data1['ps'][4:20], label="data1") # q_min: q_max
plt.title("Raw PS for "+filename[:-14])
plt.xlabel("q (1/m)")
plt.ylabel("mean square amplitude (m^2)")
plt.show()