# N5 Python Challenge

### Introduction:
    - Description: Small django application to register traffic infractions. 
    - Technologies: Django-rest-framework, PostgreSQL


## Local deployment:

### Requirements:

- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/desktop/)

### Run application (without docker)

```
$ git clone git@github.com:Abrunacci/n5_challenge.git
$ cd n5_challenge/
$ poetry install
$ poetry shell
$ cd traffic_infraction_register
$ ./manage.py seed
$ ./manage.py runserver
```

###  Run application (with docker)



## Application usage:

#### API Login:

```
curl -X POST localhost:8000/api/token/ -H "Content-Type: Application/json" -d '{"username":"321321", "password":"123456"}'
```

#### Save traffic infraction:

```
curl -X POST localhost:8000/api/save_infractions/ -d '{"date":"2024-08-01", "description":"cant park there", "type":"parking", "vehicle": "AB123CD", "amount":"231242.12"}' -H "Content-Type: Application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMzkyNzMxLCJpYXQiOjE3MjMzOTI0MzEsImp0aSI6IjJmZTg4MTYxMzM3OTQxOTlhMjAzNDJiYmExYjQ1YjQwIiwidXNlcl9pZCI6Mn0.vjZ-3Avo84q2cjdVPh4Qz2fsW3EXjVWTW1Lw5n4zI2A"
```

#### GET report

```
curl -X GET http://127.0.0.1:8000/api/generate_report/ -d "email=elcantante@mail.com"
```