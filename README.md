# Mess Website - Website for Dining Facility at IIT Indore
A Django-based software project that simplifies the process of applying for rebates by students.

## Features
- Automated rebate rule checks
- Student information access
- Admin allocation
- Email notifications
- Billing automation

Ongoing development of additional features ...

## Note to Developers

### Setup
- Clone the repository
    ```shell
    $ git clone https://github.com/DaemonLab/Mess-Website.git
    ```
- Install Python 3.10 Or Higher
- Install Django 
    ```shell
    $ pip install django
    ```
- Install all dependencies
    ```shell
    $ pip install –-user -r requirements.txt
    ```
- Create a superuser
    ```shell
    $ python manage.py createsuperuser
    ```
- Migrate the database
    ```shell
    $ python manage.py migrate
    ```
- Copy the environment
    ```shell
    $ cp .env.example .env
    ```
- Edit the environment variables in `.env` file
- Finally run
    ```shell
    $ python manage.py runserver
    ```
_Note:_ SQLite is as the default database
