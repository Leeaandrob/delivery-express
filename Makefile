clean:
		find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python manage.py runserver
shell: clean
	python manage.py shell

tests:
	python manage.py test --settings=delivery.settings_all_tests
migrations: clean
	python manage.py makemigrations

migrate: clean
	python manage.py migrate
