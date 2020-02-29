1, get repo from: https://github.com/MarkDuLj/mcr
2, press "Clone or download" and copy link
3, in pycharm, press VCS->get from version control, paste the link
4, cd shutter_warranty project in your local machine in command center
5, "pip install requirements.txt "
6, "virtualenv env"
7, "source env/bin/activate"
8, "python manage.py runserver"
9, open a browser and type the server link "127.0.0.1:8000"
(need to check again)


superuser(this account only for debugging)
user name:mcr
email:ldu@shipperbee.com
password:mcr266588

common users:
Mark/Carol/Ruiying
password:test12345

Run server
in current project directory, command line, input"python manage.py runserver"

update database
 "python manage.py makemigrations"

update other files
in current project directory, command line, input"python manage.py migrate"

create date model
in models.py

step by step debug, check objects
use "python manage.py shell"