# Mini-Galerie d’Images

## Description
Ce projet est une mini-galerie d'images développée avec Django, qui permet de télécharger, afficher, et trier des images par date de téléchargement. Elle inclut également une génération asynchrone de miniatures pour optimiser la navigation dans la galerie.

## Fonctionnalités
- Téléchargement d'images avec des informations (titre, date de téléchargement).
- Consultation et tri des images par date ou par titre.
- Génération asynchrone de miniatures pour chaque image.
- Accès aux miniatures et gestion optimisée des fichiers médias.

## Prérequis
- Python 3.8 ou supérieur
- Redis (pour la gestion des tâches asynchrones)
- Un environnement virtuel Python est recommandé pour isoler les dépendances du projet.

## Installation

1. **Clonez le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/mini-galerie.git
   cd mini-galerie
## Installez les dépendances :

  ```bash
pip install -r requirements.txt
  ```

## Configurez la base de données :

Dans settings.py, configurez la base de données (SQLite par défaut ou MySQL si nécessaire).
Créez les tables de base de données :
  ```bash
python manage.py makemigrations
python manage.py migrate
  ```

## Lancez le serveur de développement :

  ```bash
python manage.py runserver
```

## Démarrez le worker Celery :
Démarrez le worker Celery :

``` bash
celery -A MiniGalerie worker -l info
```

## Utilisation de l'API


### Téléchargement d'une Image
```URL : /api/images/upload/
Méthode : POST
Données attendues :
file : fichier de l'image (obligatoire)
title : titre de l'image (facultatif)
Liste des Images
```
```
URL : /api/images/
Méthode : GET
Paramètres de requête :
title : filtre par titre d'image
date_uploaded : filtre par date d'upload
Détail d'une Image
```
```
URL : /api/images/<int:id>/
Méthode : GET
Suppression d'une Image
```
```
URL : /api/images/<int:id>/delete/
Méthode : DELETE
Accès aux Miniatures
Les miniatures sont accessibles à l'URL : /uploads/<str:filename>
```
```
Tests
Pour lancer les tests unitaires :
```
```bash
python manage.py test
```

## Structure des Fichiers
- MiniGalerie/ : Le projet Django principal.

- galerie/ : L'application de gestion d'images.

- uploads/ : Répertoire où sont stockées les images téléchargées et leurs miniatures.

- requirements.txt : Liste des dépendances du projet.


