#!/bin/python
import pyvisa as visa
import time

rm = visa.ResourceManager('@py')
smu = rm.open_resource("ASRL/dev/ttyACM1::INSTR")

print(smu.query("*IDN?"))

while True:
    starttime = time.time() * 1000
    for i in range(100):
        voltage = float(smu.query("MEAS:VOLT:DC:IN?"))
    print("Time for 100 queries: %ims" % (time.time() * 1000 - starttime))
