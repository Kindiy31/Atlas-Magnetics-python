import datetime
import serial
import time
import random
from threading import Thread
import numpy as np

status = True
NLPC = int(input("Введіть NLPC: "))
class emulator:
    def __init__(self):
        self.input = serial.Serial('COM1', 9600)
        self.output = serial.Serial('COM2', 9600)
        self.voltages = []
    def insert_voltage(self):
        while status:
            voltages = []
            for i in range(NLPC):
                voltage = random.randint(1, 3300)
                voltage = voltage / 1000
                voltages.append(voltage)
            voltage_with_nlpc = round(float(np.mean(voltages)), 2)
            self.input.write(str(voltage_with_nlpc).encode('utf-8') + b'\n')
            time.sleep(0.1)

    def read_voltage(self):
        while status:
            data = b''  # Пустий байтовий рядок для збереження даних
            while True:
                byte = self.output.read(1)  # Читання одного байта
                if byte == b'\n':  # Якщо це символ нового рядка
                    break  # Завершити читання
                data += byte  # Додати байт до рядка даних
            voltage = data.decode('utf-8')
            try:
                voltage = float(voltage)
            except:
                continue
            self.voltages.append(voltage)
        return self.voltages

if __name__ == '__main__':
    em = emulator()
    t1 = Thread(target=em.insert_voltage)
    t2 = Thread(target=em.read_voltage)
    start_time = datetime.datetime.now()
    t1.start()
    t2.start()
    input('Сервіс запущено, для зупинки натисніть ENTER\n')
    status = False
    end_time = datetime.datetime.now()
    voltages = em.voltages
    job_time = end_time - start_time
    job_time = job_time.seconds
    mean_voltages = round(float(np.mean(voltages)), 2)
    min_voltages = round(float(np.min(voltages)), 2)
    max_voltages = round(float(np.max(voltages)), 2)
    print(f"""Сервіс завершив свою роботу.

Час роботи: {job_time} секунд
NLPC: {NLPC}
Середній вольтаж: {mean_voltages}
Максимальний вольтаж: {max_voltages}
Мінімальний вольтаж: {min_voltages}
Отримано результатів: {len(voltages)}""")
