import numpy as np
import matplotlib.pyplot as plt

def plot_data(data, o_data, f_data, equalized, f, t):
    plt.figure(figsize=(10, 8))
    plt.subplot(2,1,1)
    plt.plot(t, data,'-r',label=r"$Original amplitude(t)$")
    plt.xlabel('time[s]')
    plt.plot(t, equalized,'-b',label=r"$Filtered amplitude(t)$")
    plt.xlabel('time[s]')
    plt.subplot(2,1,1)
    plt.legend()
    plt.grid()

    plt.subplot(2,1,2)
    plt.plot(f[:len(data)//2],np.abs(o_data[:len(data)//2]),'-r',label=r"$Original magnitude(f)$")
    plt.xlabel('f [Hz]')
    plt.xlim([0,5e3])
    plt.plot(f[:len(data)//2],np.abs(f_data[:len(data)//2]),'-b',label=r"$Filtered magnitude(f)$")
    plt.xlabel('f [Hz]')
    plt.xlim([0,5e3])
    plt.legend()
    plt.tight_layout()
    plt.grid()
    plt.show()