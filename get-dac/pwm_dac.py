import RPi.GPIO as gpio
class PWM_DAC:
    def __init__(self,gpio_pin,pwm_frequency,dynamic_range,verbose=False):
        self.gpio_pin=gpio_pin
        self.pwm_frenquency=pwm_frequency
        self.dynamic_range=dynamic_range
        self.verbose=verbose

        gpio.setmode(gpio.BCM)
        gpio.setup(self.gpio_pin,gpio.OUT,initial=0)

        self.pwm=gpio.PWM(self.gpio_pin,pwm_frequency)
        self.pwm.start(0)

    def set_voltage(self,voltage):
        if voltage<0 or voltage>self.dynamic_range:
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.0-{self.dynamic_range:.2f}B)")
            duty_cycle=0
        else:
            duty_cycle=(voltage/self.dynamic_range)*100
        self.pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose and 0<=voltage<=self.dynamic_range:
            print(f"Коэффициент заполнения {duty_cycle:.2f}B")

    def deinit(self):
        self.pwm.stop()
        gpio.output(self.gpio_pin,0)
        gpio.cleanup()

if __name__=="__main__":
    try:
        dac=PWM_DAC(12,500,3.290,True)
        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах"))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте снова\n")
    finally:
        dac.deinit()