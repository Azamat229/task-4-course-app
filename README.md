# Course Application
It is simple API wich allows to users views a list of courses, create a new course, view a course detail by specifying its id and allows delete caused by specifying id.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Setup the virtual environment, and activate it
```bash
python -m venv env
env\Scripts\activate
```

### Installing
1. Assuming you have Python setup, run the following commands

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


2. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
3. Create a few test objects of each type.
4. Open tab to `http://127.0.0.1:8000/courses` to see the list of couses, with your new objects.

### Documentation


### Running the tests
There are no tests yet.

### Built With

### Authors
