release: python ssp/manage.py migrate
worker: cd .\ssp\ & gunicorn -w 2 ssp.wsgi & celery --app  ssp worker -l INFO -c 1 -P gevent
