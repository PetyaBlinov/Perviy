import r2r_adc as adc
import adc_plot as plot
import time 

ADC = adc.R2R_ADC(3.2, False)
voltages = []
times = []
duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time < duration):
        times.append(time.time()-start_time)
        voltages.append(ADC.get_sc_voltage())
        
    plot.plot_voltage_vs_time(times, voltages, ADC.dynamic_range)
finally:
    ADC.deinit()