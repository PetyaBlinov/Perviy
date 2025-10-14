import mcp4725_driver as mcp4725
import signal_generator as sg
import time

amplitude = 3.0  # Амплитуда сигнала в вольтах
signal_frequency = 5  # Частота сигнала в Герцах  
sampling_frequency = 500  # Частота дискретизации в Герцах

try:
    dac = mcp4725.MCP4725(dynamic_range=5.0, verbose=False)
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        
        # Генерируем нормализованную амплитуду синусоиды
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        
        # Преобразуем в напряжение и подаем на выход 12-bit DAC
        signal_voltage = normalized_amplitude * amplitude
        dac.set_voltage(signal_voltage)
        
        # Ожидаем следующий период дискретизации
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()