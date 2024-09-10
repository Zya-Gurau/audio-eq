import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from eq import *
from plot_data import *

GAINS = [-20,-20,-20,-20,-20,-20,-20,-20,-20,-20]

#takes a mono wav file
sample_rate, data = wav.read("sample.wav")
len_data = len(data)

f = sample_rate/len_data * np.arange(len_data)
t  = 1/sample_rate * np.arange(len_data) 

fourier_original_data = np.fft.fft(data)/len_data

equalized = eq_ten_band(data, sample_rate, GAINS)
wav.write("filtered_sample.wav", sample_rate, equalized.astype(np.int16))

fourier_filtered_data = np.fft.fft(equalized)/len_data

plot_data(data, fourier_original_data, fourier_filtered_data, equalized, f, t)
