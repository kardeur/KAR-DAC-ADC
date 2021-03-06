# Kar-DAC-ADC

Installation du Hat Raspberry KAR-DAC/ADC

## Méthode d'installation classique - *Conventional installation method*

Ouvrez le fichier `/boot/config.txt` avec votre éditeur favori :

*- Open the file `/boot/config.txt` with your favorite editor :*

```bash
sudo nano /boot/config.txt
```

Commentez le paramètre `dtparam=audio=on` et ajoutez les lignes nécessaires à l'initialisation de KAR-DAC/ADC :

*- Comment the parameter `dtparam=audio=on` and add the necessary lines to initialize KAR-DAC/ADC :*

```bash
# Enable audio (loads snd_bcm2835)
#dtparam=audio=on

# KAR-DAC/ADC
dtparam=i2c_arm=on
dtparam=i2s=on
dtoverlay=i2s-mmap
dtoverlay=rpi-proto
```

Sauvegardez les modifications, et redémarrez votre système.
Activez la sortie son de votre KAR-DAC/ADC à l'aide de la commande suivante, et sauvegardez vos paramètres :

*- Save the changes, and restart your system.
Activate the sound output of your KAR-DAC/ADC with the following command, and save your settings:*

```bash
amixer set 'Output Mixer HiFi' unmute
sudo alsactl store
```


## Testez votre installation - *Test your installation*

Vous pouvez enfin tester votre carte son à l’aide de la commande suivante :

*- Finally, you can test your sound card with the following command:*

```bash
speaker-test -c2 -t wav
```

Si vous entendez quelque chose, tout est ok !

*- If you hear something, everything is ok!*






## Installation par EEPROM (Avancé) - *Installation by EEPROM (Expert)*

N'utilisez cette méthode que si vous disposez de connaissances avancées en systèmes Raspberry.
Cette méthode doit uniquement être utilisée si la méthode énoncée plus haut n'a pas été suivie.

*- Use this method only if you have advanced knowledge of Raspberry systems.
This method should only be used if the above method has not been followed.*

Ouvrez le fichier `/boot/config.txt` et ajoutez la ligne suivante :

*- Open the file `/boot/config.txt` and add the following line :*

```bash
dtparam=i2c_vc=on
```

Clonez le répertoire officiel d'EEPROM Raspberry :

*- Clone the official Raspberry EEPROM directory :*

```bash
sudo apt-get install git
git clone https://github.com/kardeur/KAR-DAC-ADC.git
cd KAR-DAC-ADC/
```

Clonez le répertoire EEPROM KAR-DAR/ADC :

*- Clone the KAR-DAR/ADC EEPROM directory :*

```bash
sudo apt-get install git
git clone https://github.com/raspberrypi/hats
cd hats/eepromutils
make
```

_Faites entrer votre module en mode configuration en connectant un jumper sur les pins prévues à cet effet._

*- _Bring your module into configuration mode by connecting a jumper to the pins provided for this purpose._*

Créez le fichier de configuration kardac-eeprom.eep :

*- Create the configuration file kardac-eeprom.eep*

```bash
./eepmake ../../KAR-DAC-ADC/kardac_eeprom.txt kardac_eeprom.eep /boot/overlays/rpi-proto.dtbo
```

Flashez votre système Raspberry à l'aide du fichier qui vient d'être configuré :

*- Flash your Raspberry system using the file that has just been configured*

```bash
sudo ./eepflash.sh -w -f=kardac_eeprom.eep -t=24c32
```



## En savoir plus

Découvrez plus de tutoriels sur [kardeur.io](https://kardeur.io/tutoriels/).
