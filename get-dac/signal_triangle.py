import time as  t
def get_triangle_wave_amplitude(freq,t):
    period=1.0/freq
    phase=t%period
    normal_phase=phase/period
    if normal_phase<0.5:
        return normal_phase*4-1
    else:
        return 3-normal_phase*4
def wait_for_sampling_period(sampling_frequency): 
    sampling_period = 1 / sampling_frequency
    t.sleep(sampling_period)