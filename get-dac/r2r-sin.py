import r2r_dac as r2r
import signal_generator as sg 
import time

amplitude = 3
signal_frequency = 10 
sampling_frequency = 1000  

if __name__=="__main__":
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183,True)
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        norm_A = sg.get_sin_wave_amplitude(signal_frequency, time.time())
        signal_value = norm_A * amplitude
        dac.set_voltage(signal_value)
        sg.wait_for_sampling_period(sampling_frequency)
        print(f"Время:{current_time:.2f}, Напряжение:{signal_value:.2f}V")
