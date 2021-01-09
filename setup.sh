echo "collect static file ..."
python manage.py collectstatic

echo "run server ..."
uwsgi --ini uwsgi.ini

echo "supervisord ..."
supervisord -c supervisord.conf
