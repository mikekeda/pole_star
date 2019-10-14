# Pole Star

Python Software Engineer Assignment.

### Running

```
docker-compose up
```

This command will build code container and download postgres container, start them, run tests,
collect static, run migrations (create 2 tables and load initial data from positions.csv file) and start server.

After this app will be acceptable on http://localhost:8000

Create a superuser to check admin page:
```
python manage.py createsuperuser
```

## Running the tests

```
python manage.py
```


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [GeoDjango](https://docs.djangoproject.com/en/2.2/ref/contrib/gis/) - The geographic Web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - REST framework used
* [PostgreSQL](https://www.postgresql.org/) - Database used
* [PostGIS](https://postgis.net/) - Spatial database extender for PostgreSQL
* [Docker](https://docs.docker.com/compose/) - Container Platform used
* [Docker Compose](https://docs.docker.com/compose/) - Used for orchestrating docker containers

## Authors

* **Mykhailo Keda** - *Initial work* - [mikekeda](https://github.com/mikekeda)
