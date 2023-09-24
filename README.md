One Form
=====

Django Form


Installation and usage
======================

Quick start
-----------

1. Add "form" to your INSTALLED_APPS setting like this::

   ``` python
        INSTALLED_APPS = [
            ...,
            "form",
        ]
    ```

2. In your project settings.py add the following::

   ``` python
        DJANGO_PAGINATION_LIMIT = 50
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": env("DJANGO_PAGINATION_LIMIT", default=50),
    ```

How to contribute
=================

Please make sure to update tests as appropriate.

Getting Started
---------------

1. Clone the repository

    ``` bash
        # Run the following command in your terminal
        pre-commit install
        git update-index --assume-unchanged .idea/runConfigurations/* .idea/riso.iml
    ```


2. Prepare the environment, Create a virtual environment with Python 3.11 or higher and activate it. Then install the
   dependencies using pip:

    ``` bash
        # Run the following command in your terminal
        cd riso
        pip install -r requirements.txt
    ```

3. Update following files

    ```
        # .envs/.local/.django
        # .envs/.local/.postgres
    ```

4. Then using pycharm runConfiguration to start coding

Useful commands
---------------

- Run test with coverage

    ``` bash
        docker-compose -f riso/local.yml run --rm django pytest --cov --cov-report term-missing --cov-report html
    ```

Other information
=================

What's in this project?
-----------------------

This project is a Django project with a single app called "form".
