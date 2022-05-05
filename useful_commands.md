## Command pile
###### Installs
```
sudo apt-get install python3-pip
sudo pip3 install openpyxl
sudo apt-get install nsnake
sudo apt-get install greed
sudo apt-get install htop
```
###### SSH key
PowerShell: ```ssh-keygen -t ed25519```
Linux: ```cd /mnt/c/users/szala/.ssh```  ```ssh-copy-id -i id_ed25519.pub pi@192.168.1.4```
###### Others
```
sudo shutdown -h now
sudo raspi-config
pwd
scp pi@192.168.1.4:/home/pi/documents/cpu_temp.xlsx "C:\Users\szala\Desktop"
#!/usr/bin/env python
python 3 send_data.py
ipconfig
.\nmap -sn 192.168.1.0/24
ps -aef | grep python3
git config credential.helper store
fswebcam --fps 15 -S 8 -r 640x480 %Y-%m-%d_%H:%M:%S.jpg
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
nohup ./log_bme680.py &
```
## Links
- [GitHub: Temperature log](https://github.com/raspberrypilearning/temperature-log/blob/master/worksheet.md)
- [GitHub: BME680 python codes](https://github.com/pimoroni/bme680-python/tree/master/examples)
- [Raspberry Pi OS Documentation](https://www.raspberrypi.com/documentation/computers/os.html)
- [Raspberry Pi Configuration Documentation](https://www.raspberrypi.com/documentation/computers/configuration.html)
- [Adafruit BME680 overview and Arduino setup](https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/)
- [BME680 vs CCS811 vs SGP30](https://www.jaredwolff.com/finding-the-best-tvoc-sensor-ccs811-vs-bme680-vs-sgp30/)
- [External power supply forum discussion](https://forums.raspberrypi.com/viewtopic.php?t=288581)
- [Remote SSH with VSCODE](https://code.visualstudio.com/docs/remote/ssh)
- [Prettify Raspberry Pi shell with oh my zsh](https://www.seeedstudio.com/blog/2020/03/06/prettify-raspberry-pi-shell-with-oh-my-zsh/)
- [GitHub: ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)
- [GitHub: ohmyzsh themes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#agnoster)
- [Password-less SSH on Raspberry Pi](https://levelup.gitconnected.com/password-less-ssh-on-raspberry-pi-9295136afb32)
- [Raspberry Pi NoIR Camera Modul v2](https://www.rpibolt.hu/Raspberry_Pi_NoIR_Camera_Module_v2_-_8_megapixel_Sony_szenzor)
- [Cloning SD card](https://beebom.com/how-clone-raspberry-pi-sd-card-windows-linux-macos/)
###### BME680
- [Raspberry: Getting started with BME680](https://learn.pimoroni.com/article/getting-started-with-bme680-breakout)
- https://github.com/BoschSensortec/BME680_driver
- https://github.com/timothybrown/BSEC-Conduit
- https://github.com/rstoermer/bsec_bme680_python/
- https://github.com/twartzek/bme680-raspberry
- https://github.com/BoschSensortec/BME68x-Sensor-API
