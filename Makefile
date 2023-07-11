migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

runserver:
	./manage.py runserver

pre-commit-all:
	pre-commit run --all-files

.upgrade:
	./manage.py upgrade -vv
