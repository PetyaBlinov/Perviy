import r2r_dac as r2r
import signal_generator as sg 
import time

amplitude = 3.2
signal_frequency = 1  # Исправил опечатку
sampling_frequency = 100  # Исправил опечатку

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        norm_A = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        signal_value = norm_A * amplitude
        dac.set_voltage(signal_value)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()