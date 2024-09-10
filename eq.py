from scipy import signal
from scipy.signal import butter, lfilter
import itertools


BANDS = [(20,39),(40,79),(80,159),(160,299),(300,599),
         (600,1199),(1200,2399),(2400,4999),(5000,9999),(10000,20000)]
ORDER = [2,3,3,3,3,3,3,3,3,3]

def bandpass_filter(data, lowcut, highcut, sr, order=5):
    nyq = 0.5 * sr
    low = lowcut / nyq
    high = min(highcut / nyq, 0.99999999999999)
    b, a = butter(order, [low, high], btype='bandpass')
    filtered = lfilter(b, a, data)
    return filtered

def eq_ten_band(data, sr, gains):
    r_data = []
    for i in range(10):
        filtered_band = bandpass_filter(data, BANDS[i][0], BANDS[i][1], sr, order = ORDER[i]) * 10**(gains[i]/20)
        if len(r_data) <1:
            r_data=filtered_band
        else:
            r_data+=filtered_band
    return r_data

    