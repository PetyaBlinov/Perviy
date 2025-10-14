import r2r_dac as r2r
import time

amplitude = 3.2  
signal_frequency = 10 
sampling_frequency = 1000  

def get_triangle_wave_amplitude(freq, t):

    period = 1.0 / freq
    phase = t % period
    normalized_phase = phase / period
    

    if normalized_phase < 0.5:

        return normalized_phase * 2
    else:

        return (1 - normalized_phase) * 2

def wait_for_sampling_period(sampling_freq):

    sampling_period = 1.0 / sampling_freq
    time.sleep(sampling_period)

try:

    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, verbose=False)
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        
        normalized_amplitude = get_triangle_wave_amplitude(signal_frequency, current_time)
        
        signal_voltage = normalized_amplitude * amplitude
        dac.set_voltage(signal_voltage)
        
        wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()