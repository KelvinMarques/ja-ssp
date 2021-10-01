worker: celery --app  ssp worker -l INFO -c 1 -p getvent
release: python ssp/manage.py migrate
web: cd ssp && gunicorn -w 2 ssp.wsgi
