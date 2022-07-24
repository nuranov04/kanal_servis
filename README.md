Для запуска проекта вам необходимо ввести команды:

git clone https://github.com/nuranov04/kanal_servis.git

cd kanal_servis

python3 manage.py migrate

python3 manage.py runserver

открыть новый терминал и ввести команду для начало работы celery
"celery -A test_for_company_kanalservise worker -l info"

открыть новый терминал и ввести команду для начало работы celery-beat
'celery -A test_for_company_kanalservise beat -l info'

и довольствуйтесь проектом)
