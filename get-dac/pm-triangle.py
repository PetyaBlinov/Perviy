import pwm_dac as pdd
import signal_triangle as st
import time

ampl=3.2
freq_sign=1
freq_samp=100
try:
    dac=pdd.PWM_DAC(12, 500, 3.290)
    start_time=time.time()
    while True:
        current_time=time.time()-start_time
        norm_A=st.get_triangle_wave_amplitude(freq_sign, current_time)
        sign_val=(norm_A+1)/2*ampl
        dac.set_voltage(sign_val)
        st.wait_for_sampling_period(freq_samp) 
finally:
    dac.deinit()