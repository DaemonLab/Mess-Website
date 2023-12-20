<a name="readme-top"></a>

# Mess Website - Website for Central Dining Facility at IIT Indore
A Django-based software project that automates and digitalises the complete dining system of IIT Indore.

## Features
- Automated rebate rule checks
- Student information access
- Automated allocation of caterers
- Email notifications
- Billing automation

Ongoing development of additional features ...

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About the Project

The Mess Website is a Django-based software project that automates and digitalises the complete dining system of IIT Indore. It is a web application that provides a platform for students to fill short and long rebates, caterer allocation forms, access their dining bills and other information. It also provides a platform for the institute's administrations to manage the dining system and the students of IIT Indore.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Django][Django]][Django-url]
* [![SQlite][SQlite]][SQlite-url]
* [![Bootstrap][Bootstrap]][Bootstrap-url]
* [![python][python]][python-url]
* [![Docker][Docker]][Docker-url]
* [![Gunicorn][Gunicorn]][Gunicorn-url]
* [![Nginx][Nginx]][Nginx-url]

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 +

### Installation

1. Clone the repository

    ```shell
     git clone https://github.com/DaemonLab/Mess-Website.git
    ```
2. Navigate to the project directory:

    ```shell
    cd team_22
    ```
3. Install all dependencies

    ```shell
    pip install –-user -r requirements.txt
    ```
4. Create a superuser

    ```shell
    python manage.py createsuperuser
    ```
5. Migrate the database

    ```shell    
    python manage.py migrate
    ```
6. Copy the environment
    ```shell
    cp .env.example .env
    ```
7. Edit the environment variables in `.env` file
8. Finally run
    ```shell
    $ python manage.py runserver
    ```
_Note:_ SQLite is as the default database

## Roadmap

- [x] Student Information Access
- [x] Short Rebate Form
- [x] Long Rebate Form
- [x] Caterer Allocation Form
- [x] Billing System - for both students and caterers
- [x] Email Notifications
- [ ] Scan QR Code feature

<p align="right">(<a href="#readme-top">back to top</a>)</p

## Contact

- [Ishaan Mittal](me210003039@iiti.ac.in)

Project Link: [https://github.com/DaemonLab/Mess-Website](https://github.com/DaemonLab/Mess-Website)


[Django]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[SQlite]: https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQlite-url]: https://www.sqlite.org/index.html
[Bootstrap]: https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/
[python]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[Docker]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Gunicorn]: https://img.shields.io/badge/gunicorn-37474F?style=for-the-badge&logo=gunicorn&logoColor=white
[Gunicorn-url]: https://gunicorn.org/
[Nginx]: https://img.shields.io/badge/nginx-269539?style=for-the-badge&logo=nginx&logoColor=white
[Nginx-url]: https://www.nginx.com/