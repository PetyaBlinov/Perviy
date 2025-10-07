import RPi.GPIO as gpio
class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose=False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_range
        self.verbose=verbose

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self.gpio_bits,gpio.OUT,initial=0)
    def set_number(self,number):
        if number<0 or number>255:
            raise ValueError("число должно быть от 0 до 255")
        for i, pin in enumerate(self.gpio_bits):
            bit=(number>>i)&1
            gpio.output(pin,bit)
        if self.verbose:
            bits=[(number>>i)&1 for i in range(8)]
            print(f"Число на ЦАП: {number}, биты:{bits}")
    def set_voltage(self,voltage):
        if voltage<0 or voltage>self.dynamic_range:
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.0-{dynamic_range:.2f}B)")

            number=0
        else:
            max_value=(1<<len(self.gpio_bits))-1
            number=int(voltage/self.dynamic_range*max_value)
        self.set_number(number)
    def deinit(self):
        gpio.output(self.gpio_bits,0)
        gpio.cleanup()

if __name__=="__main__":
    try:
        dac=R2R_DAC([16,20,21,25,26,17,27,22], 3.183, True)

        while True:
            try:
                voltage=float(input("Введите напряжение в Вольтах:  "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    
    finally:
        dac.deinit()
