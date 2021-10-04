release: python ssp/manage.py migrate
worker: celery --app  ssp worker -l INFO -c 1 -p getvent
web: cd ssp && gunicorn -w 2 ssp.wsgi
