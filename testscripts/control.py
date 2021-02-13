#!/bin/python
import pyvisa as visa

rm = visa.ResourceManager('@py')
smu = rm.open_resource("ASRL/dev/ttyACM0::INSTR")

print(smu.query("*IDN?"))

voltage = float(smu.query("MEAS:VOLT:DC:IN?"))
print(voltage)
