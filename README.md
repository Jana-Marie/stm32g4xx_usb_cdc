# stm32g4xx_usb_cdc

This repo contains a STM32G474 USB CDC example implementation, combined with [Jan Breuer's SCPI parser library v2](https://www.jaybee.cz/scpi-parser/) allowing you to build your own STM32G4xx based scientific instruments.

### Working example instruments

[NiklasFauth's Wireless Charging SMU](https://github.com/NiklasFauth/charge-hf)


[Jan--Henrik's Mini-TDR](https://github.com/Jan--Henrik/Mini-TDR)


### Folder structure

- **usb_cdc_g4/** : Universal CDC implementation for STM32G4xx, include this folder + changes to the Makefile
- **libscpi/** : [Jan Breuer's awesome SCPI parser library v2](https://www.jaybee.cz/scpi-parser/)
- **Inc/** : Contains the header files, please note `Inc/scpi-def.h`
- **Inc/** : Contains the source files, please note `Src/scpi-def.c` and `Src/scpi-com.c`
- **testscripts/** : Contains some python test scripts and example software
