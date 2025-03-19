# Django Command List

A comprehensive list of useful Django commands for project setup, database management, testing, and more.

## 📌 Basic Project Setup & Management
```bash
django-admin startproject <project_name> .
```
_Create a new Django project._

```bash
python manage.py startapp <app_name>
```
_Create a new Django app inside the project._

```bash
python manage.py runserver
```
_Start the development server._

```bash
python manage.py runserver <port>
```
_Start the server on a specific port (e.g., `python manage.py runserver 8080`)._

## 📌 Database Management
```bash
python manage.py makemigrations
```
_Generate new migrations based on changes in models._

```bash
python manage.py migrate
```
_Apply migrations to the database._

```bash
python manage.py sqlmigrate <app_name> <migration_number>
```
_View the raw SQL for a migration._

```bash
python manage.py showmigrations
```
_List all migrations and their status._

```bash
python manage.py flush
```
_Reset the database (deletes all data but keeps tables)._

## 📌 User & Authentication Management
```bash
python manage.py createsuperuser
```
_Create a new superuser for Django admin._

```bash
python manage.py changepassword <username>
```
_Change a user's password._

## 📌 Shell & Data Management
```bash
python manage.py shell
```
_Open an interactive Django shell._

```bash
python manage.py dumpdata <app_name.ModelName>
```
_Export data from the database to a JSON file._

```bash
python manage.py loaddata <filename>
```
_Load data from a JSON file into the database._

## 📌 Testing & Debugging
```bash
python manage.py test
```
_Run all tests._

```bash
python manage.py test <app_name>
```
_Run tests for a specific app._

```bash
python manage.py check
```
_Check for any issues in the project._

## 📌 Static Files & Media
```bash
python manage.py collectstatic
```
_Collect static files for deployment._

```bash
python manage.py findstatic <file_name>
```
_Find the location of a static file._

## 📌 Custom Django Commands
```bash
python manage.py <custom_command>
```
_Run a custom command (if defined in the project)._

## 📌 Additional Commands
```bash
python manage.py diffsettings
```
_Show the difference between default settings and the project’s settings._

```bash
python manage.py dumpdata
```
_Dump data from the database._

```bash
python manage.py inspectdb
```
_Generate Django models based on an existing database._

```bash
python manage.py migrate --fake
```
_Mark migrations as applied without actually running them._

---

⚡ **Save this guide for quick reference!** 🚀  
🌟 Feel free to contribute and improve this list! 🔥
