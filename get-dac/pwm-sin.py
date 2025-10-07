import pwm_dac as pdd
import signal_generator as sg
import time

ampl=3.2
freq_sign=10
freq_samp=1000
try:
    dac=pdd.PWM_DAC(12, 500, 3.290)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        norm_A=sg.get_sin_wave_amplitude(freq_sign, current_time)
        sign_val=norm_A*ampl
        dac.set_voltage(sign_val)
        sg.wait_for_sampling_period(freq_samp) 
finally:
    dac.deinit()