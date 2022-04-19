"""
Good for showing expected behaviour, regions of parameter space + justification (this is original), etc if the data doesn't work out
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def amplitudes2d(q_x, q_y, KbT=1, sigma = 1, kappa=1):
    return (KbT)/(sigma*(q_x**2 + q_y**2)+ kappa*(q_x**2 + q_y**2)**2)

amplitudes2d=np.vectorize(amplitudes2d)

def amplitudes1d(q_x, KbT=1, sigma=1, kappa=1):
    return (KbT/2*sigma)*(1/q_x - 1/np.sqrt(sigma/kappa + q_x**2) )

amplitudes1d=np.vectorize(amplitudes1d)

q_x = np.outer(np.linspace(-0.1,0.1, 100), np.ones(100))
q_y=q_x.copy().T

fig=plt.figure(figsize=plt.figaspect(2.))

#
ax=fig.add_subplot(2,1,1)
q_x_1d = np.linspace(-2,2,100)
ax.plot(q_x_1d,amplitudes1d(q_x_1d))

#
ax=fig.add_subplot(2,1,2,projection="3d")
surf = ax.plot_surface(q_x,q_y,amplitudes2d(q_x,q_y), edgecolor = "green")



plt.show()