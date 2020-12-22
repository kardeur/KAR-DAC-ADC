#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#filename            : install_dac_hat.py.py
#description    : Fichier d'installation de la carte d'extension de Kardeur.io (ADC / DAC)
#author              : David Minard
#email               : david@kardeur.io
#date                : 2020/12/15
#version             : 0.0.1
#usage               : $ python install_dac_hat.py.py
#notes               : 
#license             : GPL-3.0 or any later version
#python_version      : 2.7.16
#==============================================================================

import subprocess
import fileinput
# CHECK IF CARD IS ALREADY INSTALLED

aplay_output = subprocess.check_output(['aplay', '-l'])

if "sndrpiproto" in aplay_output :
    print ("\n")
    print (" - La carte d'extension DAC/ADC de Karden.io est déjà configurée - ")
    print (" - Karden.io's DAC/ADC expansion card is already configured - ")
    print ("\n")
    exit()
else :
    subprocess.call(["sudo", "apt-get", "install", "git", "-y"])
    subprocess.call(["git", "clone", "https://github.com/raspberrypi/hats"])
    subprocess.call(["git", "clone", "https://github.com/skiselev/i2s_audio_phat"])
    subprocess.call(['./hats/eepromutils/eepmake i2s_audio_phat/eeprom_settings_i2s_audio_phat.txt i2s_audio_phat.eep /boot/overlays/rpi-proto.dtbo'], shell=True)
    subprocess.call(['sudo ./hats/eepromutils/eepflash.sh -w -f=i2s_audio_phat.eep -t=24c32'], shell=True)
    with open('/boot/config.txt', 'r') as file :
        filedata = file.read()
    filedata = filedata.replace('dtparam=audio=on', '#dtparam=audio=on')
    with open('/boot/config.txt', 'w') as file:
        file.write(filedata)
    file.close()
# EST-CE QUON DOIT REBOOT ???? A TEST
    subprocess.call(["amixer", "set", "'Master'", "100", "unmute")]
    subprocess.call(["amixer", "set", "'Output Mixer HiFi'", "unmute")]
    subprocess.call(["sudo", "alsactl", "store")]
    exit()
