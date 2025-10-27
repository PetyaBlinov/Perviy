import numpy as np
import time

def get_sin_wave_amplitude(freq, t):  
    sin_value = np.sin(2 * np.pi * freq * t)
    normal_value = (sin_value + 1) / 2
    return normal_value

def get_triangle_amplitude(freq, t):
    tri_value = 1/freq
    x = t%tri_value
    if x<=tri_value/2:
        return (2/tri_value)*x
    return 1-(2/tri_value)*(x-tri_value/2)


def wait_for_sampling_period(sampling_frequency): 
    sampling_period = 1 / sampling_frequency
    time.sleep(sampling_period)
