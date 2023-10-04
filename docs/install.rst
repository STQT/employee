Quick start
======================================================================

How to start project
----------------------------------------------------------------------



To build use the commands::

    docker-compose -f local.yml up -d --build

To create superuser use the commands::

    docker-compose -f local.yml run django python manage.py createsuperuser

To create employees (more 50000) use the commands::

    docker-compose -f local.yml run django python manage.py create_employees

Changes to files in `src/` will be picked up and reloaded automatically.


Code manipulating
----------------------------------------------------------------------

To create migration files:
    ::

        docker-compose -f local.yml run django python manage.py makemigrations


To using shell:
    ::

        docker-compose -f local.yml run django python manage.py shell_plus

To using shell:
    ::

        docker-compose -f local.yml run django python manage.py shell_plus

