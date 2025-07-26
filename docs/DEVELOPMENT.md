# Get Started 🐋⚡🚀

🐋 To start the application, run the following command in the project root directory:

```bash
docker-compose up --build -d
```

⚡ To stop the application, run:

```bash
docker-compose down
```

🚀 Migrate database the Django development server in debug mode:

```bash
docker-compose exec <service_name_django> python manage.py makemigrations

docker-compose exec <service_name_django> python manage.py migrate
```

🍂 Seed fake data

```bash
docker-compose exec <service_name_django> python manage.py populate --amount 10
```

🦭 Search index Elasticsearch document

```bash
docker-compose exec <service_name_django> python manage.py search_index --rebuild
```

Unit test and test coverage

```bash
docker-compose exec <service_name_django> pytest
```

```bash
docker-compose exec <service_name_django> pytest --cov --cov-report=xml
```
