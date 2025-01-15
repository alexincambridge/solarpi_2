import time
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=1)

def read_mppt_data():
    if not client.connect():
        print("Error al conectar con el MPPT")
        return None

    try:
        result = client.read_input_registers(0x3100, 6, unit=1)
        if result.isError():
            print("Error al leer datos")
            return None

        voltage = result.registers[0] / 100.0
        current = result.registers[1] / 100.0
        soc = result.registers[4]
        return voltage, current, soc
    finally:
        client.close()

while True:
    data = read_mppt_data()
    if data:
        voltage, current, soc = data
        print(f"Tensión: {voltage:.2f} V | Corriente: {current:.2f} A | SOC: {soc}%")
    else:
        print("Error al obtener datos")
    time.sleep(2)

datos_cli.py (END)
