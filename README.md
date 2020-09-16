# MLLWebsite
The Machine Learning Lab Website.

# Initial Setup
Install required packages:
```bash
# activate your virtual env
pip install poetry
poetry install
```

Apply initial database migrations.

```bash
python manage.py migrate
```

and then create superuser:
```bash
python manage.py createsuperuser
```

Now, the server can be run with following command:
```bash
python manage.py runserver
```
