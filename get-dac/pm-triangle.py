import pwm_dac as pdd
import signal_generator as sg
import time

# Параметры генерируемого сигнала
amplitude = 3.2  # Амплитуда сигнала в вольтах
signal_frequency = 2  # Частота сигнала в Герцах
sampling_frequency = 300  # Частота дискретизации в Герцах

def get_triangle_wave_amplitude(freq, t):
    """
    Генерирует треугольный сигнал с амплитудой от 0 до 1
    """
    period = 1.0 / freq
    phase = t % period
    normalized_phase = phase / period
    
    # Треугольный сигнал: подъем от 0 до 1 за половину периода, затем спуск
    if normalized_phase < 0.5:
        # Поднимаемся от 0 до 1
        return normalized_phase * 2
    else:
        # Спускаемся от 1 до 0  
        return (1 - normalized_phase) * 2

try:
    # Создаем объект для управления PWM DAC
    dac = pdd.PWM_DAC(12, 2000, 3.290, verbose=False)
    start_time = time.time()
    
    # Бесконечный цикл генерации сигнала
    while True:
        current_time = time.time() - start_time
        
        # Генерируем нормализованную амплитуду треугольного сигнала
        normalized_amplitude = get_triangle_wave_amplitude(signal_frequency, current_time)
        
        # Преобразуем в напряжение и подаем на выход PWM DAC
        signal_voltage = normalized_amplitude * amplitude
        dac.set_voltage(signal_voltage)
        
        # Ожидаем следующий период дискретизации (используем готовую функцию)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    # Корректно завершаем работу с PWM DAC
    dac.deinit()