import mcp4725_driver as mcp4725
import signal_generator as sg
import time

amplitude = 3.0  
signal_frequency = 10  
sampling_frequency = 1000 

try:
    dac = mcp4725.MCP4725(dynamic_range=5.0, verbose=False)
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        
        signal_voltage = normalized_amplitude * amplitude
        dac.set_voltage(signal_voltage)
        
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()