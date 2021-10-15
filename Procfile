release: python ssp/manage.py migrate
worker: gunicorn -w 2 ssp.wsgi & celery --app  ssp worker
