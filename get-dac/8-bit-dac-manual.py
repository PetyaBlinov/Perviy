import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
leds=[22,27,17,26,25,21,20,16]
gpio.setup(leds,gpio.OUT)
dynamic_range={
    'min voltage':0.0,
    'max voltage':3.3,
    'resolution':8,
    'current value':0,
    'pins':leds,
    'voltage step':0.0129
}
def voltage_to_number(voltage):
    if not (0.0<=voltage<=dynamic_range['max voltage']):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0.0-{dynamic_range['max voltage']:.2f}B)")
        return 0
    return int(voltage/dynamic_range['max voltage']*255)
def number_to_dac(number):
    if number<0 or number>255:
        raise ValueError("число должно быть от 0 до 255")
    for i, pin in enumerate(leds):
        bit=(number>>i)&1
        gpio.output(pin,bit)
    bits=[(number>>i)&1 for i in range(8)]
    print(f"Число на ЦАП: {number}, биты:{bits}")
try:
    while True:
        try:
            voltage=float(input("Введите напряжение в вольтах"))
            number=voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")
finally:
    gpio.output(leds,0)
    gpio.cleanup()
