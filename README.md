# SipyMike

# Configuración de Sipy con Expansion Board 3.0
___
Detalles en [Pycom][Pycom]

## Configuración del hardware

1. Primero se debe actualizar la placa de expansión. Se debe instalar [el software](https://docs.pycom.io/pytrackpysense/installation/firmware.html) para actualizar el firmware.

2. Actualizar el firmware de la placa. Desde windows se debe tener el driver conectado al puerto COM e instalar [este software](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true). Desde Ubuntu se debe instalar [estos componentes](https://software.pycom.io/downloads/linux-1.15.1.html) y seguir las instrucciones de [esta página](https://docs.pycom.io/gettingstarted/installation/firmwaretool.html#second).

> IMPORTANTE: Es necesario tener conectada la antena externa para evitar quemar el dispositivo

3. Existen dos programas con plugins diseñados para subir código al dispositivo; [Atom](https://docs.pycom.io/pymakr/installation/atom.html) y [Visual Studio Code](https://docs.pycom.io/pymakr/installation/vscode.html). Para instalar los plugins de cada editor de código ingrese a los correspondientes enlaces.


> ```Ctrl-F``` performs a "safe-boot" of the device that prevents ```boot.py``` and ```main.py``` from executing


## Registro de dispositivos (Sigfox)
