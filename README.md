"#multi_related_forms" 

This is a simple example which shows us how to develop a survery form which has multi pages with photo uploading, and the form will be finished once press 'submit' button in the last one page.
this django app fits phone and computer's screen.
I used the seesion to control each tables and at the end to delete them. if you have any good suggestion, please don't hesitant to commit it here. thanks


how to install(below steps runs on windows):

1. Download Python 3.5 from official website. it will help us install like pip, easy_install, etc.

2. pip install virtualenv to install virtualenv tool which is very useful for multi django projects on your local develpment computer.

3. go to a folder whatever you want. and use command 'virtualenv djang_env' to create a python virtual environment. we will see it will use python 3.5 which you installed on your comptuer to install the new virtual enviroment. that means if you want to install a virtualenv which depends on python 2.7, you need to install python 2.7, and install the virtualenv on your python2.7/lib/site-pacakges, and at the same time, the command of virtualenv cames from python2.7. you must change the path system variables.

4. go to the virtualenv folder, you will see the several folder here. input the command: 'Scripts\activate', it will activate the virtualenv.

5. use command: 'pip install django', it will install the newest version of django for you. if you want to install like django 1.9, use 'pip install django==1.9'

6. pip install django-bootstrap3

7. pip install xlsxwriter

8. django-admin createproject xxx

9. copy the survery_form app to your django project.

10. add the survery_form to your settings/INSTALLED_APPS.

11. go to the django project folder, and command 'python manage.py makemigrations'.

12. python manage.py migrate.

13. python manage.py runserver.

14. Done


good luck.
