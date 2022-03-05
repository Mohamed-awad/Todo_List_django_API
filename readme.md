# Todo List Api Application

This is a TODO-list module task to help the backend users to create tasks for the end-users developed using Django, as backend code for a mobile application, using docker.

## you can do 
    * Signup for normal user from api end point
    * Login for normal user from api end point
    * Logout for normal user from api end point
    * List your tasks from api end point
    * List your tasks from api end point filtered by finished or unfinished ones. 
    * Complete A task from api end point
    * Admin Can Create tasks for end user from Admin Panel 
    * Admin Can Add due date for each task from Admin Panel 
    * Admin Can Filter Tasks by finished, pending and overdue for each user.   

## Install

* you need to install Web Browser 
* you need to install docker and docker-engin
* you need to install postman

## Run the project

* Clone the project 
* open the project in terminal by press `Ctrl-Alt+T`
* Build Docker Image `docker build --tag todo_list:latest .` 
* Run Docker Image `docker run  -p 8000:8000 todo_list:latest`
* open another terminal window `Ctrl-Alt+T`
* list docker containers `docker container ps`
* get CONTAINER ID from previous command 
* Create superuser `docker exec -it <container_id> python manage.py createsuperuser`
* enter superuser credentials
* open your browser on (http://localhost:8000/admin/)
* login with superuser credentials to admin panel
* to consume todo list apis use this api postman collection (https://www.getpostman.com/collections/5f72f865a808936e0fd2)
* you can find api docs in this link (http://localhost:8000/api/docs/)



## Important Notes
    * for use any end point in the system except (signup & login)
        1. you need to send in headers Authurization token
        2. you can get it from login end point /api/users/login/
 
