run:
	python manage.py runserver


migrate:
	python manage.py makemigrations
	python manage.py migrate


prepare:
	make migrate
	mkdir static
	python manage.py collectstatic


heroku-local:
	heroku local


heroku-prod:
	heroku create
