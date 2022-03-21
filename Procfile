web: gunicorn django_project.wsgi:oc_lettings_site --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate