# todo
Todo app - REST


# environment
- python3
- django
- django-rest-framework
- django-filter


# how to run
 - ```git clone git@github.com:dhruvsingh/todo.git```
 - make a virtual environment (ensure it is python3)
 - activate virtual environment
 - ```$ cd todo```
 - ```$ pip install -r requirements.txt```
 - ```$ cd todo```
 - ```$ ./manage.py migrate```
 - ```$ ./manage.py runserver```
 - browse to http://127.0.0.1/api/task/ to view list of all tasks
 - the same can also be seen using the included bash script test.sh; run it using ```$ bash -v test.sh | python -m json.tool```
     - the bash script does the following:
         - adds a todo
         - lists all todos (Shows only one, since one is added)
         - updates the first todo as done
         - lists all todos (shows only one)
         - add another todo
         - list all todos
         - delete todo1
         - list all todos