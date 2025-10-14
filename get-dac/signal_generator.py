import numpy as np
import time

def get_sin_wave_amplitude(freq, t):  
    sin_value = np.sin(2 * np.pi * freq * t)
    normal_value = (sin_value + 1) / 2
    return normal_value

def wait_for_sampling_period(sampling_frequency): 
    sampling_period = 1 / sampling_frequency
    time.sleep(sampling_period)
