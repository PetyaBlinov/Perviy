import mcp4725_driver as mcp4725
import signal_generator as sg
import time


try: 
    amplitude = 2
    signal_frequency = 10
    sampling_frequency = 500
    mcp = mcp4725.MCP4725(5.0, 0x61, True)
    start_time=time.time()
    while True:
        try:
            current_time = time.time()-start_time
            voltage = sg.get_triangle_amplitude(signal_frequency, current_time)
            mcp.set_voltage(voltage*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally: 
    mcp.deinit()