# Mini-Galerie d'Images Django

## Installation
1. Installez les dépendances : `pip install -r requirements.txt`
2. Configurez Redis : `sudo service redis-server start`
3. Lancez le serveur Django : `python manage.py runserver`
4. Lancez le worker Celery : `celery -A MiniGalerie worker -l info`

## Lancer les Tests
```bash
python manage.py test
