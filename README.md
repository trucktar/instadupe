# instadupe
Instagram's website clone built with Bootstrap and Django. 

## Getting Started

These instructions will get you copy of this project up and running for local development and testing purposes.

### Requirements

- [Python](https://www.python.org/downloads/)
- [Pipenv](https://github.com/pypa/pipenv#installation)
  - `pip install pipenv`
- [Git](https://git-scm.com/downloads)
- [PostgreSQL](https://www.postgresql.org/download/)

### Setup and Installation

1. Clone this [repository](https://github.com/trucktar/instadupe.git) using `git clone`. Then, change your working directory to the repository.

   ```
   $ git clone https://github.com/trucktar/instadupe.git
   $ cd instadupe/
   ```

2. Install project and development dependencies.

   ```
   $ pipenv sync
   ```

3. Activate the project's virtualenv

   ```
   $ pipenv shell
   ```

### Database Configuration

Ensure you have PostgreSQL installed and running. Then,

1. Enter psql, a terminal-based front-end to PostgreSQL:

   ```
   $ psql -U postgres
   ```

2. Run the following queries to create the db role and database.

   ```
   postgres=# CREATE USER instadupe WITH CREATEDB;
   postgres=# CREATE DATABASE instadupe OWNER instadupe;
   ```

### Launching the application

1. Create a `.env` file and set the following env variables:

   ```
   DATABASE_URL=postgres://instadupe@localhost/instadupe
   SECRET_KEY=suitable-for-development-only
   ```

2. Run the following commands to create the database tables:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser account.

   ```
   python manage.py createsuperuser
   ```

4. Finally, fire up the server and navigate to http://127.0.0.1:8000/
   ```
   python manage.py runserver
   ```

## Built using

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Bootstrap](https://getbootstrap.com/) - The world’s most popular framework for building responsive, mobile-first sites.

## Credits

[Nyota Mwangi](https://github.com/trucktar/)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
