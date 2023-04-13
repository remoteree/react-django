# Prerequisistes

# Startup Instructions
1. Activate a virtualenv using `source <your_virtual_env>/bin/activate`. To create a virtualenv using `python -m venv <your_virtual_env_name>`
2. Install dependencies by using `pip install -r requirements.txt`. If there are packages that are not included in the requirments.txt, just install them one at a time using `pip install <package_name>`
3. cd into to /backend and run the server using `python manage.py runserver`

# Development Instructions

## Frontend Instructions
1. Make use of the apiHelper.js module's makeCall to make calls to the server. The method takes a request body, request method, and a request url
2. I have imported and install Semantic UI's React library which gives you a lot of nice usable components out of the box for fast development. Check out the components available here: https://react.semantic-ui.com/

### Useful libraries for frontend libraries
* Front-end react routing: https://reactrouter.com/en/main

## Backend Instructions
1. Add your api end-points to backend/backend/backend_app/views.py. Feel free to include separate files as needed
2. Add your models to backend/backend/backend_app/models.py. 
3. Update `DATABASES` config in backend/backend/settings.py if you want to use a database other than mysql
