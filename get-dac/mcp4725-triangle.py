import mcp4725_driver as mcp
import signal_generator as sg 
import time

amplitude=3.0
signal_frequency=10
sampling_frequency=1000

def get_triange_wave_amplitude(freq,t):
    period=1.0/freq
    phase=t%period
    normal_phase=phase/period
    if normal_phase<0.5:
        return normal_phase*2
    else:
        return (1-normal_phase)*2

try:
    dac=mcp.MCP4725(dynamic_range=5.0,verbose=False)
    start_time=time.time()

    while True:
        current_time=time.time()-start_time
        normal_amp=get_triange_wave_amplitude(signal_frequency, current_time)

        signal_voltage=normal_amp*amplitude
        dac.set_voltage(signal_voltage)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
