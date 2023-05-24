# Party-slasher
You have to kill someone and find your killer !

## Installation des bibliothèques requises
Ce guide explique comment installer les bibliothèques requises pour un projet à l'aide de pip, le gestionnaire de packages Python.

### Prérequis
Python (version 3.x recommandée) est installé sur votre système.
Assurez-vous de disposer de la version correcte en exécutant la commande suivante dans votre terminal :
```bash
python --version
```
### Instructions d'installation
1) Clonez ou téléchargez le dépôt du projet sur votre machine locale.
2) Ouvrez votre terminal et accédez au répertoire du projet.
3) Créez un environnement virtuel (facultatif, mais fortement recommandé) en exécutant la commande suivante :

```bash
python -m venv venv
```
Activez l'environnement virtuel. La commande varie selon le système d'exploitation :

Sur Windows :
```bash
venv\Scripts\activate
```
Sur macOS et Linux :
```bash
source venv/bin/activate
```

Une fois que votre environnement virtuel est actif, vous pouvez procéder à l'installation des bibliothèques requises.
Assurez-vous que vous êtes toujours dans le répertoire du projet.

Installez les bibliothèques requises en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```
Cette commande va lire le fichier requirements.txt présent dans le répertoire du projet et installer toutes les bibliothèques répertoriées avec leurs dépendances.
Attendez que pip télécharge et installe toutes les bibliothèques spécifiées.
Ce processus peut prendre un certain temps en fonction du nombre et de la taille des bibliothèques.
Une fois l'installation terminée, vous pouvez exécuter le projet avec toutes ses dépendances correctement installées.

### Configurer la partie
1) Ouvrez le fichier `config-email.json` avec votre éditeur de texte favori
2) Remplacez les valeurs des champs `email` et `password` par votre adresse email et votre mot de passe
   Attention, pour Google, pensez à [générer un mot de passe d'application](https://support.google.com/accounts/answer/185833?hl=fr).
   Si vous utilisez un autre fournisseur, veuillez modifier les champs `smtp_address` et `smtp_port` en fonction de votre fournisseur.
3) Enregistrez le fichier
4) Ouvrez le fichier `config.json` avec votre éditeur de texte favori
5) Définissez l'ensemble des paramètres de la partie (joueurs et joueuses, ainsi que leur mail -crucial pour qu'iels reçoivent les informations-)
6) Enregistrez le fichier

### Instructions d'exécution
1) À partir du terminal précédemment ouvert et configuré, exécutez la commande suivante :
```bash
python3 script.py
```
2) Demandez à vous ami·es de vérifier leurs mails et de suivre les instructions
3) Enjoy !

> Pensez à commenter l'ensemble des print() dans le code si vous ne voulez pas que les joueurs et joueuses voient les informations de debug (comme les mails des autres joueurs et joueuses ou encore les informations sur la partie)