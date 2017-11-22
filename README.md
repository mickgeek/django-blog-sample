# Django Blog Sample

This repository contains a simple web application built with the Django web framework.

The project has the next basic apps:
- Blog (with draft/publish/archive management of posts, pagination and tag filtering)
- Flatpages
- Contact

## Setting Up a Development Environment

1. Create a Python 3.6 virtual environment.
2. Install required dependencies:
```bash
pip install -r requirements.txt
```
3. Create a MySQL database:
```
mysql -u root -p
CREATE DATABASE djangoblogsample;
\q
```
4. Apply migrations to create database schema:
```bash
python manage.py migrate
```
5. Load sample data to the database:
```bash
python manage.py loaddata sample_db_data.json
```
6. Create a superuser that can log in to the admin panel:
```bash
python manage.py createsuperuser
```
7. Run the local server:
```bash
python manage.py runserver
```

And, enjoy it! :tada:
