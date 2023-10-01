# EventEmailSystem

The event email system will send emails on employee's birthday or work anniversary. This job is done automatically every day at 11am using cronjobs.

- Python, Django, rest framework, cron

## Step by step guide to run project

### Virtual environment
Run following command to install virtualenv.

`pip install virtualenv`

Create virtualenv

`virtualenv envname`

Activate environment

`source virtualenv_name/bin/activate`

### Install Packages
Install django

`pip install django`

Install requests

`pip install requests`

### Setup django project

Start django project

`django-admin startproject EventEmailSystem`

create django app

`django-admin startapp emailApp`

### Install requirements form requirements file

`pip install -r requirements.txt`


### Run django project

Go to project folder where manage.py file is present.
`python manage.py runserver`


