#  Silsolver

This is a project that contains **Django, Django-Rest, PostgreSQL, pgAdmin, and Docker.**

**Description**

This project is a basic Django web application that uses PostgreSQL as the database and pgAdmin for database management. The project can be easily set up and run using Docker Compose.

Installation

Clone the repository:
`git clone https://github.com/avdevssolutions/silsolver.git`
Navigate to the project directory:
`cd silsolver`
Build and start the containers:
`docker-compose up --build -d`
Access the web application at http://localhost:8000
Access pgAdmin at http://localhost:8080 and log in using the credentials specified in the docker-compose.yml file.

**Usage**

After installation, the web application will be available at http://localhost:8000.
The application can be customized by modifying the Django project files located in the app directory.

The PostgreSQL database can be accessed and managed using pgAdmin.
To log in to pgAdmin, open http://localhost:8080 in a web browser and enter the username and password specified in the docker-compose.yml file.

**Configuration**

The following environment variables can be set to configure the project:

DB_NAME: The name of the PostgreSQL database (default: devdb).

DB_USER: The username for the PostgreSQL database (default: devuser).

DB_PASSWORD: The password for the PostgreSQL database (default: changeme).

DB_HOST: The hostname for the PostgreSQL database (default: db).

DB_PORT: The port for the PostgreSQL database (default: 5432).

PGADMIN_DEFAULT_EMAIL: The email address for the default pgAdmin user (default: admin@avdevs.com).

PGADMIN_DEFAULT_PASSWORD: The password for the default pgAdmin user (default: Avdevs@123).

These environment variables can be set in the docker-compose.yml file.

**Repo Handler**

[**Kushal Dulani**](https://www.linkedin.com/in/kushaldulani/)
**[AV DEVS SOLUTIONS](https://www.linkedin.com/company/avdevs/)**
