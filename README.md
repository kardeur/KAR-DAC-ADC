Téléchargez le fichier de configuration sur votre raspberry à l’aide de :

sudo apt-get install git
git clone https://github.com/kardeur/KAR-DAC-ADC.git
cd KAR-DAC-ADC/

Méthode d'installation classique : 


Faites entrer votre module en mode configuration en connectant un jumper sur les pins prévues à cet effet.

Une fois la manipulation effectuée, lancez le fichier de configuration.

sudo python3 install_dac_hat.py

Une confirmation vous sera demandé, indiquez simplement « yes ».

Vous pouvez enfin tester votre carte son à l’aide de la commande suivante :

speaker-test -c2 -t wav

Si vous entendez quelque chose, tout est ok !


Découvrez plus de tutoriels sur https://kardeur.io/tutoriels/
