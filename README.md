# Simple Invoice generating API 

## Requirements
- Python 3.10.1
- Django 4.0
- Django REST Framework
- Postgresql

## Installation
 create a virtual environment
```
python -m venv env
```
activate the virtual environment

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
### Create .venv file inside the root project folder
```
DATABASE_NAME=<database name>
DATABASE_USER=<username>
DATABASE_PASS=<password>
HOST=<host>
PORT=<port>
```
###Migrate
```commandline
python manage.py migrate
```
###Run
Run api at port : 9000

```commandline
python manage.py runserver 9000
```


## Structure

Endpoint |HTTP Method | API Method 
-- | -- |-- 
`register/` | POST | Create a user
`login/` | POST | Login
`api/token/refresh/` | GET | Get Refresh Token
`notes/` | GET | Get all notes
`notes/:id` | GET,PUT,DELETE |  Get/Update/Delete a single item
`delete_image/:id/`| GET | Delete image
`upload_image/:note_id/`| POST | Upload image for notes
